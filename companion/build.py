"""Build the course companion page.

Injects steps.json into template.html and writes index.html, the file that
gets published as the Claude artifact.

    python3 companion/build.py
"""
import json
import pathlib
import sys

here = pathlib.Path(__file__).parent
steps = json.loads((here / "steps.json").read_text(encoding="utf-8"))

# A day with no lesson of its own (Day 7) carries its steps directly.
# Wrap them as one lesson-shaped block so the page renders every day the same way.
for day in steps["days"]:
    if not day["lessons"] and day.get("steps"):
        sources = ", ".join(n.rstrip(".") for n in day.get("source_lessons", []))
        day["lessons"] = [{
            "number": f"Day {day['day']}",
            "tracker_title": day["title"],
            "page_title": day["title"],
            "minutes": None,
            "skool_url": None,
            "no_video": True,
            "idea": day.get("note", ""),
            "steps": day["steps"],
            "done_when": f"You've used every page on your phone and logged what needs fixing. Draws on lessons {sources}.",
        }]

ids = [s["id"] for g in steps["days"] + steps["stages"] for l in g["lessons"] for s in l["steps"]]
if len(ids) != len(set(ids)):
    sys.exit("Duplicate step ids in steps.json")
if len(steps["days"]) != 7:
    sys.exit("steps.json must have exactly 7 days")

template = (here / "template.html").read_text(encoding="utf-8")
marker = "/*__DATA__*/null"
if template.count(marker) != 1:
    sys.exit("Data marker missing from template.html")

# Escape "</" so a prompt can never close the script tag early.
data = json.dumps(steps, ensure_ascii=False).replace("</", "<\\/")
(here / "index.html").write_text(template.replace(marker, data), encoding="utf-8")
print(f"Built index.html: {len(ids)} steps, {sum(len(g['lessons']) for g in steps['days'] + steps['stages'])} lessons")
