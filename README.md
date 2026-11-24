# phd-sop

A Claude Code skill for writing, adapting and reviewing a PhD Statement of Purpose, built while applying to CS and robotics PhD programs.

What it does differently from "write my SOP" prompts:

- **Nothing invented.** Every fact, number and feeling must come from a source you provide; gaps become `[TODO: ...]` slots that tell you what to write.
- **The program's own prompt drives the structure,** read from the application portal, and each program's AI-use policy is checked before drafting.
- **15 patterns from admitted statements** (`skills/phd-sop/references/patterns.md`), distilled from public admitted CS and robotics SOPs and published advice.
- **Independent review:** a fresh subagent that never saw the drafting scores the essay, quotes generic lines, and asks the questions that surface your real material. It gives feedback only and never writes paragraphs for you.
- **Mechanical checks and PDF export:** `audit.py` (placeholders, forbidden terms, em dashes, overused adjectives) and `build_pdf.py` (11pt, 1-inch margins, page count).

## Install

```bash
git clone https://github.com/laulauraluo/phd-sop.git
cp -r phd-sop/skills/phd-sop ~/.claude/skills/
```

Then ask Claude Code to "draft my SOP for <program>" or "review my SOP".

PDF export needs [tectonic](https://tectonic-typesetting.github.io/) and, for the page count, `pip install pypdf`.

## Your private profile

Copy `skills/phd-sop/references/profile-template.md` to a `sop-profile.md` next to your own materials. It holds your name, terms that must never appear, your direction in your own words, and decisions you have made. Keep it out of any public repository (`.gitignore` already excludes `sop-profile.md`).

## Credits

- Review framework adapted from the MIT-licensed `statement-coach` skill in [mohitagw15856/pm-claude-skills](https://github.com/mohitagw15856/pm-claude-skills).
- Patterns paraphrased from the admitted statements at [cs-sop.notion.site](https://cs-sop.notion.site) and advice by CMU's Student Academic Success Center, Mor Harchol-Balter, Andy Pavlo, the MIT EECS Communication Lab, Noah Smith, Nelson Liu et al., Maria Antoniak and Saujas Vaduguru. No text from those statements is reproduced.

## License

MIT
