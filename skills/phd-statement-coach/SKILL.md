---
name: phd-statement-coach
description: Write, adapt and review a PhD Statement of Purpose (SOP / research statement) for a specific program, grounded only in facts the applicant can source. Use when the user wants to draft an SOP, adapt an SOP to another school, check an SOP against a program's prompt, review or score an SOP, cut it to a page limit, or export it to PDF for an application portal. Works for CS, ML and robotics PhD applications, including career switchers from industry.
---

# PhD Statement of Purpose

A workflow for writing and reviewing a PhD SOP that reads as one specific person, answers the program's own prompt, and contains nothing the applicant cannot back up in an interview.

Three rules hold in every step:

1. **No invented facts, numbers, feelings, events or ownership.** Every claim comes from a source the applicant gave (CV, fact file, paper, results file, message). If a fact is missing, leave a `[TODO: ...]` slot that says exactly what the applicant should write. Never write "I still remember..." or "I was fascinated..." for them.
2. **The applicant decides; you propose.** Direction, what to disclose (gaps, part-time study, a current program), which story to tell, and the final wording are theirs. State a risk once, then follow their decision.
3. **Check the program's AI policy.** Some programs ban AI-written content, some require disclosure, some only recommend limited use. Find the official wording and tell the applicant before drafting. When AI drafting is discouraged, switch to review-only mode (Step 4) and let the applicant write.

## Step 0: Load the applicant profile

Look for a private profile file (default `sop-profile.md` next to the applicant's materials; see `references/profile-template.md`). It holds the name to use, terms that must never appear (for example a school they do not want to mention), the research direction, facts sources, and past decisions. If none exists, create one from the template by asking the applicant, and keep it out of any public repository.

## Step 1: Gather inputs

Collect, and list back to the applicant before writing:

- **The program's exact prompt and limit.** Prefer the text inside the application portal over the public website; they often differ. Note word or page limits and any required parts (for example "societal impact, positive and negative").
- **Facts sources:** CV, a fact file with sources, papers (titles, venues, status, co-authors), results files, collaboration messages.
- **The story spine in the applicant's own words:** why this field, why now, what they want after the PhD. Ask; do not guess.
- **Faculty:** 2 or 3 names, each with one verified recent paper (open the paper or abstract page; do not rely on memory). Record the URL.
- **The policy check** from rule 3.

## Step 2: Draft

Follow `references/patterns.md` (15 patterns distilled from admitted CS and robotics PhD statements). In short:

- Open with one concrete case, then the general point, then the research question, within about 100 words.
- One thread through every project, and every project an honest instance of it.
- Each project: problem, why it is hard, what the applicant did, one number with its condition and baseline, a one-line lesson, a bridge to the next.
- State the applicant's share of team work in one line.
- Name the gap (for example no hands-on robots yet) once, plainly, and say what the PhD gives.
- Faculty: 2 or 3, each tied to one paper and to what the applicant would add.
- Close by echoing the opening; one sentence on the goal after the PhD.
- Plain wording: evidence instead of adjectives, terms of the target field, no em dashes.

Map every part of the program's prompt to a paragraph. Optional bold run-in heads help reviewers find each part.

When adapting an existing SOP to a new school, keep the core and rewrite only what the new prompt or faculty requires. Save the old version under a new name before changing it.

## Step 3: Self-check

Run `scripts/audit.py <draft.md> [--profile sop-profile.md]`. It reports the word count, em dashes, leftover `[TODO]` or bracket placeholders, forbidden terms from the profile, and a list of overused adjectives. Fix what it flags, then check by hand that every number matches its source.

## Step 4: Independent review

Reviews by the same agent that wrote the draft are anchored on its own choices. Start a fresh subagent that has not seen the drafting conversation and give it only: the draft, the program prompt and limit, `references/patterns.md`, `references/review.md`, and neutral applicant context. It returns scores, prompt coverage, a 15-pattern table, line-level feedback, questions that mine for missing material, a revision plan and "the one thing". The review gives feedback only; it never writes replacement paragraphs.

Show the applicant the review. The material-mining questions are the most valuable part: the applicant answers them in their own words, and those answers replace the weakest generic lines.

## Step 5: Finalize

- Remove every placeholder. The audit must show zero brackets and zero forbidden terms.
- Build the PDF: `scripts/build_pdf.py <draft.md> <out.pdf>` (needs `tectonic`; 11pt, 1-inch margins). Check the page count against the limit and cut in the order the review's revision plan gives.
- Upload only after the applicant approves the final PDF. Portals usually allow replacing the file until final submission.

## Files

- `references/patterns.md`: the 15 patterns and what not to copy.
- `references/review.md`: the review rubric and output format for Step 4.
- `references/profile-template.md`: the private applicant profile.
- `scripts/audit.py`: mechanical checks.
- `scripts/build_pdf.py`: Markdown to PDF.
