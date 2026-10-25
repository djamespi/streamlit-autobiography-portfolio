# Autobiography & Portfolio

A Streamlit app for Dexter James D. Benitez, a third-year BS Computer Science student at CIT-University, section F1. The autobiography and milestones use Dexter's supplied writing. His self-ratings are Backend Development 4/5, Quality Assurance / Testing 3/5, and AI Development 3/5. The portfolio features CITUClinicSystem for technical work, tinHealth for backend development, and Parola for AI development.

Repository: https://github.com/djamespi/streamlit-autobiography-portfolio

## Run locally

Use Python 3.12. From this directory on Windows:

```powershell
py -3.12 -m venv .venv-app
py -3.12 -m pip --python .venv-app\Scripts\python.exe install -r requirements.txt
.\.venv-app\Scripts\python.exe -m streamlit run app.py
```

If the provided environment already exists, run only the last command. Open http://localhost:8501.

## Add personal content

Edit `data/profile.json`. Keep autobiography wording your own. Supply:

- `name`, `program`, `year`, `section`, `short_bio`, and optionally `headline`.
- `autobiography.background`, `education`, `interests`, and `milestones`.
- `skills`: objects with `name`, your numeric `rating` from 1 to 5, and `evidence` explaining how you use the skill.
- `projects`: at least three objects, each with `title`, `role`, `tools` (a list), and `outcome` or `url`. Optional fields are `description` and `reflection`.
- Each milestone has `date`, `title`, and optionally `description`.
- Optionally set `github_url`, `contact_email`, and `photo` (a repository-relative asset path).

The default illustration is explicitly labeled as a portrait stand-in. Replace it with your own photo by adding the image to `assets/` and setting `photo` to its path.

The project selection and focus areas come from Dexter. tinHealth's README explicitly credits his backend, database, and some frontend work. Feature descriptions reflect inspected repository files; no claims are made about deployment, user counts, measured accuracy, or individual ownership of every feature. Parola's source repository is private and its link is labeled as requiring access. The portfolio only describes the project and does not include its source code, data, or credentials. See `docs/project-sources.md` for evidence. No GitHub token is required at runtime.

Check completeness:

```powershell
.\.venv-app\Scripts\python.exe check_content.py
```

This check verifies field coverage, not authorship or factual accuracy.

## Deploy to Streamlit Community Cloud

1. Review the autobiography, skill ratings, and three linked projects.
2. The app files are published at `djamespi/streamlit-autobiography-portfolio`. Future updates must include `app.py`, `portfolio.py`, `data/`, `assets/`, `requirements.txt`, and `.streamlit/config.toml` together; `app.py` alone is insufficient. Do not upload virtual environments or secrets.
3. Sign in at https://share.streamlit.io and select **Create app**. Choose repository `djamespi/streamlit-autobiography-portfolio`, branch `main`, and `app.py` as the main file.
4. In **Advanced settings**, select Python 3.12. This app needs no API keys or secrets.
5. Deploy. Verify the resulting public `https://….streamlit.app` URL in a signed-out or private browser window. Open the app and test project filters and feedback submission.
6. Copy the actual deployed URL to the assignment tab in Teams. Include your name and section in the submission comment. This project does not submit to Teams automatically.

Official deployment instructions: https://docs.streamlit.io/deploy/streamlit-community-cloud/deploy-your-app/deploy

## Feedback behavior

The form validates the name, optional email, and message. Successful submissions show an acknowledgment and keep a receipt in Streamlit session state. No email is sent and no messages are stored for the owner. The receipt disappears when the session ends. This behavior is stated beside the form.

## Checks

```powershell
py -3.12 -m pip --python .venv-app\Scripts\python.exe install -r requirements-dev.txt
.\.venv-app\Scripts\python.exe -m pytest -q
```

The tests use fictional fixtures isolated from `data/profile.json` to exercise three-project filtering, reset behavior, skill filtering, navigation, form validation, and session receipts.
