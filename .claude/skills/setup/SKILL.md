---
name: setup
description: First-time setup for the AI Web Design & Dev starter kit. Checks the member's machine (Node, git, GitHub CLI login, a Chrome-family browser), installs the taste-skill and impeccable design plugins from their official marketplaces, and verifies both loaded. Use when the member types /setup, says "set me up", "install the skills", "get started", or when taste-skill or impeccable is missing.
user-invocable: true
---

# Setup

You're setting up a course member's machine. They are probably not technical. Work through the steps in order, one at a time. Before running anything that installs or changes something, say what it does in one sentence and ask. Only report a step as done when a command's output proves it.

Keep a short checklist on screen and update it as you go:

```
[ ] 1. Node 22+
[ ] 2. git
[ ] 3. GitHub CLI, logged in
[ ] 4. A Chrome-family browser
[ ] 5. taste-skill installed
[ ] 6. impeccable installed
[ ] 7. Skills loaded
```

## 1. Node 22 or newer

Run `node --version`. Both design skills need Node 22+.

- Missing or older: send them to https://nodejs.org and the **LTS** installer for their system, then ask them to close and reopen the terminal and start Claude Code again in this folder.

## 2. git

Run `git --version`.

- Missing on Windows: https://git-scm.com/download/win (default options are fine).
- Missing on Mac: `xcode-select --install`, or https://git-scm.com/download/mac.

## 3. GitHub CLI, logged in

Run `gh auth status`.

- `gh` missing: https://cli.github.com.
- Not logged in: the login is interactive, so ask them to type `! gh auth login` in the Claude Code prompt and pick **GitHub.com → HTTPS → Login with a web browser**.

They need a free GitHub account. If they don't have one: https://github.com/signup.

## 4. A Chrome-family browser

taste-skill checks pages in a real browser. Look for Chrome, Edge or Chromium:

- Mac: `ls /Applications | grep -i -E "chrome|edge|chromium"`
- Windows (PowerShell or Git Bash): check `C:\Program Files\Google\Chrome\Application\chrome.exe` and `C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe`
- Linux: `command -v google-chrome chromium chromium-browser microsoft-edge`

Edge on Windows counts. If none is found, suggest installing Chrome. If a browser is installed somewhere unusual, they can set `CHROME_PATH` to its full path.

## 5. Install taste-skill

Ask first, then run:

```bash
claude plugin marketplace add Leonxlnx/taste-skill
claude plugin install taste-skill@taste-skill
```

If it says it's already installed, run `claude plugin update taste-skill@taste-skill` instead.

## 6. Install impeccable

Ask first, then run:

```bash
claude plugin marketplace add pbakaus/impeccable
claude plugin install impeccable@impeccable
```

If it's already installed, run `claude plugin update impeccable@impeccable`.

## 7. Check both loaded

Run `claude plugin list` and confirm both show **enabled**. If a plugin installed but its skills don't show up in this session, ask them to run `/reload-skills`, or quit Claude Code and start it again in this folder.

## Finish

Show the completed checklist and give one next step: open the course and start the next lesson. If any step failed, show the exact error, what it means in plain English, and the one thing to try next. Don't continue past a failed step.

## Rules

- Never install anything without asking.
- Never ask them to paste a password, token or API key into the chat.
- Don't edit their shell profile, PATH or global git config unless they ask.
- If something fails twice, stop and suggest they post the error in the AI Web Design & Dev channel in The Vibe Marketing Lab.
