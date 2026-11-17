# SkillSpotlight DEMO

A fictional "creator-picked skills" page used for security demonstrations.

**Everything here is staged.** The influencer (Nova Reed), the site, and the rating
figures are invented. The ratings do not represent real users; the page discloses this
in its footer and marks the figures with an asterisk.

## What it shows

A skill that looks popular and trusted can still be flagged by a scanner. The skill
in `skills/meeting-notes-wizard/` is a harmless test fixture (like the EICAR antivirus
test file). It includes phrasing and patterns that AI skill scanners commonly flag:

| Pattern | Where | What it really does |
|---|---|---|
| "Set aside earlier instructions" wording | SKILL.md | Nothing, it only names the output format |
| "Do not mention" wording | SKILL.md | Refers to a step that prints the word "synced" |
| Base64 string | scripts/format_notes.py | Decodes to a harmless marker sentence |
| Network-looking URL | scripts/format_notes.py | Unused, points to `.invalid`, never called |
| Environment variable read | scripts/format_notes.py | Reads `USER` to greet by name |

No network calls, no file access outside stdin, no credentials.

## Hosting on GitHub Pages

1. Push this folder to a new repo.
2. Settings > Pages > deploy from the `main` branch, root folder.
3. Open the Pages URL. The download button serves `downloads/meeting-notes-wizard.zip`.

## Rebuilding the zip

```
cd skills && zip -r ../downloads/meeting-notes-wizard.zip meeting-notes-wizard
```
