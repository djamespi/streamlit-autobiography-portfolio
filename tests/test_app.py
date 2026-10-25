"""Interaction tests use fictional fixtures, never the published content file."""
from unittest.mock import patch

import pytest
from streamlit.testing.v1 import AppTest

from portfolio import ROOT, content_gaps, load_profile, portfolio_markdown


@pytest.fixture
def profile():
    return {
        "name": "Test Student", "program": "Test Program", "year": "Year 3", "section": "TEST",
        "short_bio": "A fixture used only by automated tests.",
        "autobiography": {"background": "Test background", "education": "Test education",
                          "interests": "Test interests", "milestones": [{"date": "2025", "title": "Test milestone"}]},
        "skills": [{"name": "Python", "rating": 4, "evidence": "Test projects"},
                   {"name": "SQL", "rating": 2, "evidence": "Practice"}],
        "projects": [
            {"title": "Alpha", "role": "Developer", "tools": ["Python"], "outcome": "Test outcome", "url": "https://example.com/alpha"},
            {"title": "Beta", "role": "Designer", "tools": ["SQL"], "outcome": "Test outcome", "url": "https://example.com/beta"},
            {"title": "Gamma", "role": "Developer", "tools": ["Python", "SQL"], "outcome": "Test outcome", "url": "https://example.com/gamma"},
        ],
    }


def test_unfinished_content_is_visible():
    app = AppTest.from_file(ROOT / "app.py", default_timeout=30).run()
    assert not app.exception
    if content_gaps(load_profile()):
        assert any("Content draft" in item.value for item in app.warning)


def test_project_filter_empty_state_and_reset(profile):
    with patch("portfolio.load_profile", return_value=profile):
        app = AppTest.from_file(ROOT / "app.py", default_timeout=30).run()
        assert not app.exception
        app.radio(key="view").set_value("Projects").run()
        app.multiselect(key="project_tools").set_value(["Python", "SQL"]).run()
        assert [item.value for item in app.subheader] == ["Gamma"]
        app.text_input(key="project_search").set_value("no such project").run()
        assert any("No projects match" in item.value for item in app.info)
        app.button(key="reset_projects").click().run()
        assert not app.exception
        assert app.text_input(key="project_search").value == ""
        assert app.multiselect(key="project_tools").value == []
        assert len(app.subheader) == 3


def test_skills_threshold_and_navigation(profile):
    with patch("portfolio.load_profile", return_value=profile):
        app = AppTest.from_file(ROOT / "app.py", default_timeout=30).run()
        app.radio(key="view").set_value("Skills").run()
        app.slider(key="threshold").set_value(4).run()
        assert not app.exception
        assert app.dataframe[0].value["Skill"].tolist() == ["Python"]
        app.slider(key="threshold").set_value(5).run()
        assert any("No skills match" in item.value for item in app.info)
        app.checkbox(key="show_table").uncheck().run()
        assert len(app.dataframe) == 0
        app.radio(key="view").set_value("About & story").run()
        assert app.title[0].value == "Test Student"
        assert not app.exception


def test_feedback_validation_and_receipt_survives_rerun(profile):
    with patch("portfolio.load_profile", return_value=profile):
        app = AppTest.from_file(ROOT / "app.py", default_timeout=30).run()
        app.radio(key="view").set_value("Contact").run()
        submit = "FormSubmitter:feedback-Submit feedback"
        app.button(key=submit).click().run()
        assert any("name and a message" in item.value for item in app.error)
        app.text_input(key="visitor").set_value("Visitor")
        app.text_input(key="email").set_value("invalid-email")
        app.text_area(key="message").set_value("A test note.")
        app.button(key=submit).click().run()
        assert any("valid email" in item.value for item in app.error)
        app.text_input(key="email").set_value("")
        app.button(key=submit).click().run()
        assert not app.exception
        assert any("Thanks, Visitor!" in item.value for item in app.success)
        app.run()
        assert app.session_state["feedback_receipt"]["message"] == "A test note."
        assert app.success


def test_content_check_and_download_cover_required_fields(profile):
    assert content_gaps(profile) == []
    profile["projects"][0]["role"] = ""
    assert "project 1: role" in content_gaps(profile)
    markdown = portfolio_markdown(profile)
    assert all(title in markdown for title in ("Alpha", "Beta", "Gamma"))
    assert "Python: 4/5" in markdown
    assert "TEST" in markdown
