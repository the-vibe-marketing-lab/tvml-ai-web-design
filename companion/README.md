# Course companion

The interactive step-by-step page that goes with the AI Web Design & Dev course. It's published as a Claude artifact and shared with members alongside the course.

- `steps.json`: every day, stage, lesson and step. Edit this to change the content.
- `template.html`: the page itself (layout, styles, saving progress).
- `build.py`: puts `steps.json` into `template.html` and writes `index.html`, the file that gets published.

After changing either file:

```bash
python3 companion/build.py
```

Then republish `companion/index.html` to the same artifact URL so members keep their progress.

Progress is saved per member to their own private area of the artifact's database. Members need Contributor access to save it to their account; anyone else gets progress saved in their browser only.
