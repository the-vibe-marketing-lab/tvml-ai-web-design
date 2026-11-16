# AI Web Design & Dev: Starter Kit

This repo is the companion kit for the AI Web Design & Dev course in The Vibe Marketing Lab. The person you're working with is a course member building a website for their own business (or a client's) with Claude Code. Assume they are not a developer.

## How to help

- **First session:** if taste-skill or impeccable isn't available, suggest running `/setup` before anything else.
- **Explain before you run.** Before any terminal command that installs software, changes git history, deploys, or touches DNS or billing, say in one plain sentence what it does and ask first.
- **Plain English.** Explain terms the first time they come up (repo, commit, deploy, DNS). Use Australian spelling.
- **One step at a time.** Give one next action, wait for it to work, then move on. Never hand over ten commands at once.
- **Secrets stay out of git.** API keys go in `.env`, which is git-ignored. Never commit one, and never paste a key into a file that gets committed.

## The stack

- **EmDash** (Cloudflare's CMS, built on Astro) for the site and its editing screen
- **GitHub** for the code
- **Cloudflare** for hosting, the domain and DNS

## Which design skill to use

- **Building or rebuilding a business website page:** taste-skill (`design-taste-frontend`). Use the `service` or `place` page kind for local businesses.
- **Reviewing, critiquing or polishing a page that exists:** impeccable (`/impeccable critique`, `/impeccable audit`, `/impeccable polish`).
- **Dashboards, forms, app screens:** impeccable only.
- Don't run both on the same page in the same pass. Build with taste, then review with impeccable. If they disagree, the member's brand wins.

## Repo map

- `templates/<name>/`: starter sites. Copy one into its own folder before editing; never edit the template in place.
- `checklists/`: brief, SEO, launch and cost sheets. Use them as the source of truth when checking a site.
- `prompts/`: prompts by lesson number. When the member names a lesson, check here first.

## Getting found, not just live

The point of the course is a site that gets found on Google and named by AI search, not just one that's live. When a page is built, check it against `checklists/` (titles, meta descriptions, headings, LocalBusiness schema, sitemap, robots.txt, image sizes) before calling it done. Don't promise rankings or timeframes.
