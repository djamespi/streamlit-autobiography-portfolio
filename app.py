"""Run with: python -m streamlit run app.py"""

import html
import re

import altair as alt
import pandas as pd
import streamlit as st

from portfolio import ROOT, content_gaps, filtered_projects, load_profile, portfolio_markdown, safe_url


def main():
    profile = load_profile()
    name = profile.get("name") or "My portfolio"
    st.set_page_config(page_title=f"{name} | Autobiography & Portfolio", page_icon="🌿", layout="wide")
    st.markdown("""<style>
        .block-container {max-width:1120px;padding:4.5rem 2rem 3rem;}
        [data-testid="stHeading"] h1 {font-family:Georgia,serif;font-size:clamp(2rem,3.3vw,3.1rem)!important;
            line-height:1.14!important;letter-spacing:-.035em;padding-bottom:.4rem;}
        [data-testid="stHeading"] h2 {font-family:Georgia,serif;font-size:1.75rem!important;
            line-height:1.25;letter-spacing:-.025em;}
        [data-testid="stHeading"] h3 {font-size:1.18rem!important;line-height:1.4;letter-spacing:-.015em;}
        [data-testid="stMarkdownContainer"] p {font-size:1rem;line-height:1.65;}
        .eyebrow {color:#176B58;font-size:.74rem;letter-spacing:.14em;font-weight:700;margin:.2rem 0 .15rem;}
        [data-testid="stMarkdownContainer"] .hero-headline {font-size:1.2rem;line-height:1.5;
            font-weight:600;color:#176B58;margin:0 0 .3rem;}
        [data-testid="stMarkdownContainer"] .intro {font-size:1.03rem;line-height:1.75;
            color:#4B6058;max-width:620px;margin:.5rem 0 0;}
        .st-key-hero_intro {gap:.55rem;}
        .st-key-portrait {align-items:center!important;}
        .st-key-portrait [data-testid="stFullScreenFrame"] {display:flex;justify-content:center;}
        .st-key-portrait [data-testid="stImage"] {max-width:250px;margin-inline:auto;}
        .st-key-portrait [data-testid="stImage"] img {aspect-ratio:4/5;object-fit:cover;
            border-radius:16px;border:1px solid #DEE3D9;}
        [data-testid="stSidebar"] {border-right:1px solid #DBE0D6;}
        [data-testid="stSidebar"] .notebook-brand {display:flex;align-items:center;gap:.55rem;
            font-size:1.4rem!important;font-weight:650;line-height:1.25;margin:0 0 .4rem;padding:0;}
        .notebook-icon {font-size:1cap;line-height:1;flex-shrink:0;}
        [data-testid="stVerticalBlockBorderWrapper"] {border-radius:14px;}
        div.stButton>button,div.stDownloadButton>button {border-radius:8px;}
        @media(max-width:760px) {
            .block-container {padding:4.5rem 1.1rem 2rem;}
            [data-testid="stHeading"] h1 {font-size:2rem!important;}
            [data-testid="stHeading"] h2 {font-size:1.5rem!important;}
            [data-testid="stMarkdownContainer"] .hero-headline {font-size:1.08rem;}
            .st-key-portrait [data-testid="stImage"] {max-width:190px;}
        }
        </style>""", unsafe_allow_html=True)

    with st.sidebar:
        st.markdown('<h3 class="notebook-brand"><span class="notebook-icon" aria-hidden="true">🌿</span>'
                    '<span>Personal notebook</span></h3>', unsafe_allow_html=True)
        st.caption("AUTOBIOGRAPHY & PORTFOLIO")
        st.write(f"**{name}**")
        st.caption(f"Section: {profile.get('section') or 'Awaiting your section'}")
        view = st.radio("Explore", ["Full portfolio", "About & story", "Skills", "Projects", "Contact"], key="view")
        st.divider()
        st.download_button("Download portfolio", portfolio_markdown(profile),
                           file_name="portfolio.md", mime="text/markdown", width="stretch")
        github = safe_url(profile.get("github_url"))
        if github:
            st.link_button("Visit my GitHub ↗", github, width="stretch")
        st.caption("Built with Python & Streamlit")

    gaps = content_gaps(profile)
    if gaps:
        st.warning("Content draft — personal details and project information are still being added.")
        with st.expander("Content still needed before submission"):
            st.write("\n".join(f"- {item}" for item in gaps))

    def show(section):
        return view in ("Full portfolio", section)

    if show("About & story"):
        with st.container(key="hero"):
            intro, portrait = st.columns([2.1, 1], gap="medium", vertical_alignment="center")
            with intro, st.container(key="hero_intro"):
                st.markdown('<div class="eyebrow">A LITTLE ABOUT ME</div>', unsafe_allow_html=True)
                st.title(name)
                if profile.get("headline"):
                    st.markdown(f'<p class="hero-headline">{html.escape(profile["headline"])}</p>', unsafe_allow_html=True)
                identity = [str(profile.get(field, "")).strip() for field in ("program", "year")]
                st.write(" · ".join(value for value in identity if value) or "Program and year to be added")
                st.caption(f"Section: {profile.get('section') or 'To be added'}")
                bio = profile.get("short_bio") or "My personal introduction will appear here."
                st.markdown(f'<p class="intro">{html.escape(bio)}</p>', unsafe_allow_html=True)
            with portrait, st.container(key="portrait"):
                photo = ROOT / (profile.get("photo") or "assets/portrait-stand-in.svg")
                if not photo.is_file():
                    photo = ROOT / "assets/portrait-stand-in.svg"
                st.image(str(photo), width="stretch")
                if photo.name == "portrait-stand-in.svg":
                    st.caption("Clearly labeled portrait stand-in; replace with a personal photo if desired.")

        st.divider()
        section_heading("My story", "The experiences and interests behind my work.")
        story = profile.get("autobiography", {})
        tabs = st.tabs(["Background", "Education", "Interests", "Milestones"])
        for tab, key in zip(tabs[:3], ["background", "education", "interests"]):
            with tab:
                st.write(story.get(key) or "This part of my autobiography is awaiting my own writing.")
        with tabs[3]:
            milestones = story.get("milestones", [])
            if not milestones:
                st.info("My personal milestones will appear here.")
            for milestone in milestones:
                date, detail = st.columns([1, 4])
                date.markdown(f"**{milestone.get('date', '')}**")
                detail.markdown(f"**{milestone.get('title', '')}**")
                detail.write(milestone.get("description", ""))

    if show("Skills"):
        if view == "Full portfolio":
            st.divider()
        section_heading("What I’m learning", "My own skill ratings, on a scale of 1 to 5.")
        st.caption("1: getting started · 2: basic practice · 3: comfortable with guidance · 4: independent · 5: advanced")
        controls, chart_column = st.columns([1, 2], gap="large")
        with controls:
            threshold = st.slider("Minimum skill rating", 1, 5, 1, key="threshold")
            show_table = st.checkbox("Show the skills table", value=True, key="show_table")
            st.caption("Use the slider to focus on skills at or above a rating.")
        skills = profile.get("skills", [])
        if skills:
            st.write("My technical focus areas: " + ", ".join(skill["name"] for skill in skills) + ".")
        data = pd.DataFrame(skills, columns=["name", "rating", "evidence"])
        data["rating"] = pd.to_numeric(data["rating"], errors="coerce")
        pending = data[data["rating"].isna()].copy()
        data = data[data["rating"] >= threshold]
        if not pending.empty:
            st.caption("Personal ratings are still being added for: " + ", ".join(pending["name"]) + ".")
        with chart_column:
            if data.empty:
                st.info("No skill ratings to show yet." if not skills or len(pending) == len(skills)
                        else "No skills match this rating. Try lowering the slider.")
            else:
                chart = alt.Chart(data).mark_bar(color="#176B58", cornerRadiusEnd=5).encode(
                    x=alt.X("rating:Q", title="My rating (1–5)", scale=alt.Scale(domain=[0, 5]), axis=alt.Axis(tickMinStep=1)),
                    y=alt.Y("name:N", sort="-x", title=None),
                    tooltip=[alt.Tooltip("name:N", title="Skill"), alt.Tooltip("rating:Q", title="Rating"),
                             alt.Tooltip("evidence:N", title="How I use it")],
                ).properties(height=max(160, len(data) * 42))
                st.altair_chart(chart, width="stretch")
        if show_table:
            table = data.copy()
            if threshold == 1 and not pending.empty:
                pending["rating"] = "Rating pending"
                table = pd.concat([table, pending], ignore_index=True)
                table["rating"] = table["rating"].astype(str)
            st.dataframe(table.rename(columns={"name": "Skill", "rating": "My rating / 5", "evidence": "How I use it"}),
                         hide_index=True, width="stretch")

    if show("Projects"):
        if view == "Full portfolio":
            st.divider()
        section_heading("Selected projects", "A closer look at the things I’ve worked on.")
        projects = profile.get("projects", [])
        search_col, tools_col, order_col = st.columns([1.5, 1.5, 1])
        query = search_col.text_input("Search projects", placeholder="Title, tool, or keyword", key="project_search")
        tools = sorted({tool for project in projects for tool in project.get("tools", [])})
        chosen = tools_col.multiselect("Filter by tools", tools, key="project_tools")
        order = order_col.selectbox("Project order", ["Featured order", "Title A–Z"], key="project_order")
        selected = filtered_projects(projects, query, chosen, order)
        st.caption(f"Showing {len(selected)} of {len(projects)} projects. Tool filters match all selected tools.")
        if st.button("Reset project filters", key="reset_projects"):
            st.session_state["reset_filters"] = True
            st.rerun()
        if not projects:
            st.info("Project entries are awaiting GitHub review. Each will include my role, tools, and an outcome or link.")
        elif not selected:
            st.info("No projects match. Clear the search or reset the filters to see all projects.")
        for project in selected:
            with st.container(border=True):
                detail, metadata = st.columns([1.8, 1], gap="medium")
                with detail:
                    st.caption(project.get("category") or "Project")
                    st.subheader(project["title"])
                    if project.get("description"):
                        st.write(project["description"])
                    st.markdown("**Outcome**")
                    st.write(project.get("outcome") or "Explore the project through the link.")
                with metadata:
                    st.markdown("**My role**")
                    st.write(project.get("role", ""))
                    st.markdown("**Tools used**")
                    st.write(", ".join(project.get("tools", [])))
                    link = safe_url(project.get("url"))
                    if link:
                        st.link_button("View source (access required) ↗" if project.get("repository_private")
                                       else "View project ↗", link, width="stretch")
                        if project.get("repository_private"):
                            st.caption("Private team repository; source access is required.")
                if project.get("reflection"):
                    with st.expander("What I learned"):
                        st.write(project["reflection"])

    if show("Contact"):
        if view == "Full portfolio":
            st.divider()
        section_heading("Leave a note", "Questions, ideas, or feedback on my work are welcome.")
        form_column, note_column = st.columns([1.8, 1], gap="large")
        with note_column:
            st.markdown("### Thanks for stopping by.")
            st.write("The form acknowledges your note in this browser session. It does not send an email or save messages for the portfolio owner.")
            if profile.get("contact_email"):
                st.write(f"Contact email: {profile['contact_email']}")
        with form_column:
            with st.form("feedback", clear_on_submit=False):
                visitor = st.text_input("Your name", max_chars=100, key="visitor")
                email = st.text_input("Email (optional)", max_chars=254, key="email")
                topic = st.selectbox("What’s your note about?", ["General feedback", "A project", "Collaboration"], key="topic")
                message = st.text_area("Your message", max_chars=2000, height=140, key="message")
                submitted = st.form_submit_button("Submit feedback", type="primary")
            if submitted:
                st.session_state.pop("feedback_receipt", None)
                if not visitor.strip() or not message.strip():
                    st.error("Please add your name and a message before submitting.")
                elif email.strip() and not re.fullmatch(r"[^\s@]+@[^\s@]+\.[^\s@]+", email.strip()):
                    st.error("Please enter a valid email address, or leave the optional field blank.")
                else:
                    st.session_state["feedback_receipt"] = {
                        "name": visitor.strip(), "topic": topic, "message": message.strip(),
                    }
            receipt = st.session_state.get("feedback_receipt")
            if receipt:
                st.success(f"Thanks, {receipt['name']}! Your feedback has been acknowledged in this session.")
                with st.expander("Your feedback receipt"):
                    st.write(f"Topic: {receipt['topic']}")
                    st.text(receipt["message"])

    st.divider()
    st.caption(f"{name} · Section {profile.get('section') or 'to be added'} · Autobiography & Portfolio")


def section_heading(title, description):
    st.header(title)
    st.write(description)


if __name__ == "__main__":
    if st.session_state.pop("reset_filters", False):
        st.session_state["project_search"] = ""
        st.session_state["project_tools"] = []
        st.session_state["project_order"] = "Featured order"
    main()
