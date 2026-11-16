# AI Web Design & Dev: Starter Kit

This is the companion repo for **AI Web Design & Dev**, a course inside [The Vibe Marketing Lab](https://www.skool.com/the-vibe-marketing-lab) on Skool. Clone it, open it in Claude Code, and you get:

- **Templates**: a starter site you can make your own, so you don't begin from a blank folder
- **Design skills**: one command installs the two design skills used in the course, [taste-skill](https://github.com/Leonxlnx/taste-skill) and [impeccable](https://github.com/pbakaus/impeccable)
- **Checklists**: the website brief, the SEO checklist and the launch kit
- **Prompts**: the prompts from each lesson, in course order

> **Status:** being built alongside the course. Folders marked "coming soon" fill in as the lessons go live.

## Get started

You need [Claude Code](https://claude.com/claude-code) installed and a paid Claude plan.

**1. Get the repo onto your computer.** In a terminal:

```bash
git clone https://github.com/the-vibe-marketing-lab/tvml-ai-web-design.git
cd tvml-ai-web-design
```

No git? On the GitHub page, click the green **Code** button, then **Download ZIP**, and unzip it somewhere you'll find it again.

**2. Open it in Claude Code:**

```bash
claude
```

**3. Run the setup:**

```
/setup
```

Claude checks your machine (Node, git, GitHub login, a browser for design checks), installs taste-skill and impeccable, and tells you exactly what's missing and how to fix it. Nothing gets installed without Claude asking you first.

## What's in here

| Folder | What it is |
|---|---|
| `templates/` | Starter sites. First up: `local-service`, for gyms, studios, trades and clinics |
| `checklists/` | Website brief, SEO checklist, launch and redirect kit, running-cost sheet |
| `prompts/` | Prompts and skills from each lesson, in course order |
| `.claude/skills/setup/` | The `/setup` command |

## The two design skills

You'll use both, for different jobs:

- **taste-skill** builds the site. It's made for business websites: landing pages, service pages, local businesses. It checks its own work in a real browser at desktop and phone sizes.
- **impeccable** reviews and polishes what you've built. Ask it to `critique`, `audit` or `polish` a page. It also works on dashboards, forms and app screens.

Build with taste, then review with impeccable. Don't run both on the same page at once.

Both are free, open-source projects by other people. `/setup` installs them from their own repos, so you always get the current version. To update them later:

```bash
claude plugin update taste-skill@taste-skill
claude plugin update impeccable@impeccable
```

## Help

Stuck? Post in the AI Web Design & Dev channel in The Vibe Marketing Lab, with a screenshot of what Claude said.
