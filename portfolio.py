"""Content helpers shared by the app and the pre-submission check."""

import json
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parent
PROFILE_PATH = ROOT / "data" / "profile.json"


def load_profile(path=PROFILE_PATH):
    return json.loads(Path(path).read_text(encoding="utf-8"))


def safe_url(value):
    """Only render explicit HTTP(S) links from the content file."""
    parsed = urlparse(value or "")
    return value if parsed.scheme in {"http", "https"} and parsed.netloc else ""


def content_gaps(profile):
    missing = []
    for field in ("name", "program", "year", "section", "short_bio"):
        if not str(profile.get(field, "")).strip():
            missing.append(field.replace("_", " "))
    story = profile.get("autobiography", {})
    for field in ("background", "education", "interests", "milestones"):
        if not story.get(field):
            missing.append("autobiography: " + field)
    skills = profile.get("skills", [])
    if not skills:
        missing.append("your skills and personal 1–5 ratings")
    for skill in skills:
        score = skill.get("rating")
        if not skill.get("name"):
            missing.append("a skill name")
        if type(score) not in (int, float) or not 1 <= score <= 5:
            missing.append(f"your 1–5 rating for {skill.get('name') or 'an unnamed skill'}")
    projects = profile.get("projects", [])
    if len(projects) < 3:
        missing.append(f"at least three projects ({len(projects)} supplied)")
    for index, project in enumerate(projects, 1):
        for field in ("title", "role", "tools"):
            if not project.get(field):
                missing.append(f"project {index}: {field}")
        if not project.get("outcome") and not safe_url(project.get("url")):
            missing.append(f"project {index}: outcome or valid link")
    return missing


def filtered_projects(projects, query="", tools=(), order="Featured order"):
    query = query.casefold().strip()
    selected = [
        project for project in projects
        if (not query or query in " ".join([
            project.get("title", ""), project.get("description", ""),
            project.get("role", ""), project.get("outcome", ""),
            " ".join(project.get("tools", [])),
        ]).casefold())
        and set(tools).issubset(project.get("tools", []))
    ]
    if order == "Title A–Z":
        selected.sort(key=lambda project: project["title"].casefold())
    return selected


def portfolio_markdown(profile):
    lines = [f"# {profile.get('name') or 'My portfolio'}", "",
             " · ".join(str(profile.get(key, "")) for key in ("program", "year", "section")),
             "", profile.get("short_bio", ""), "", "## My story"]
    story = profile.get("autobiography", {})
    for field in ("background", "education", "interests"):
        lines.extend(["", f"### {field.title()}", story.get(field, "")])
    lines.extend(["", "### Milestones"])
    for item in story.get("milestones", []):
        lines.append(f"- {item.get('date', '')}: {item.get('title', '')}. {item.get('description', '')}")
    lines.extend(["", "## Skills"])
    for item in profile.get("skills", []):
        score = item.get("rating")
        rating = f"{score}/5" if type(score) in (int, float) and 1 <= score <= 5 else "Rating pending"
        lines.append(f"- {item['name']}: {rating}")
    lines.extend(["", "## Projects"])
    for project in profile.get("projects", []):
        lines.extend(["", f"### {project['title']}", project.get("description", ""),
                      *([f"Focus: {project['category']}"] if project.get("category") else []),
                      f"Role: {project.get('role', '')}",
                      "Tools: " + ", ".join(project.get("tools", [])),
                      f"Outcome: {project.get('outcome', '')}", project.get("url", "")])
        if project.get("repository_private"):
            lines.append("Source repository is private; access is required.")
    return "\n".join(lines).strip() + "\n"
