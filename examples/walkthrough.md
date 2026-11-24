# Walkthrough: one SOP from inputs to PDF

An **invented** applicant, so every name, number and paper below is made up. The point is the shape of each step, not the content.

**Alex**: five years as a backend engineer at a warehouse-automation company, one workshop paper, applying to robotics PhD programs. Prompt to the agent:

```text
Draft my SOP for the Robotics PhD at Example University. My CV and fact file are in ./materials.
```

## Step 0 · Profile

No `sop-profile.md` exists, so the agent asks five questions and writes one from [the template](../skills/phd-statement-coach/references/profile-template.md):

```markdown
## Never mention
- Old Employer Inc
## Direction
- Research direction in one sentence (your words): robots that notice when a shelf no longer looks like the map
```

From now on `audit.py --profile` fails any draft that contains "Old Employer Inc".

## Step 1 · Inputs, listed back before any writing

```text
Prompt (from the portal, not the website): 2 pages max. Answer: research goals,
  why this program, one challenge you overcame, societal impact (positive AND negative).
AI policy: "Applicants may use AI tools if they disclose how" (admissions FAQ, link)
  → drafting is allowed; you will need one disclosure sentence in the form.
Facts: CV (12 lines), facts.md (9 claims, each with a source), workshop paper (PDF)
Faculty: Prof. A, "Planning Under Map Drift" (2025): abstract page opened, URL saved
         Prof. B: no paper verified yet → [TODO]
Missing: why now; goal after the PhD. I will not guess these.
```

Alex answers the two missing questions in their own words.

## Step 2 · Draft

The agent maps each prompt part to a paragraph and writes only from the sources. Where it has nothing, it leaves a slot:

```markdown
**A challenge.** [TODO: one scene where something you built failed in a way you did
not expect. What did you see, what did you do the next day? 3–4 sentences, your words.]
```

## Step 3 · Audit

```text
$ python3 scripts/audit.py sop.md --profile sop-profile.md
words: 1142
placeholders: ['[TODO: one scene where ...]', '[TODO: Prof. B paper]']
em_dashes: 2
forbidden: []
watch-list adjectives: {'robust': 2, 'passionate': 1}
RESULT: FIX BEFORE SUBMITTING
```

## Step 4 · Independent review

A fresh subagent that never saw the drafting gets the draft, the prompt and the two reference files. An excerpt of its report:

```markdown
Scores: Specificity 6 · Trajectory 7 · Fit 4 · Voice 6

Prompt coverage: research goals ✓ · why program partial · challenge missing · societal impact partial (no negative)

Line-level
- "Example University's world-class faculty make it the ideal environment": any applicant could write this. Cut.
- "improved accuracy significantly": which accuracy, from what to what, under which condition?

Questions for you (answer in your own words)
1. The night-shift mis-pick problem in your CV: what did the failures look like on the floor?
2. What in Prof. A's paper made you think your question starts where it stops?

The one thing: replace the fit paragraph with one sentence per professor tied to one paper.
```

Alex answers question 1 in four rough sentences. Those sentences, lightly edited, fill the challenge slot. The review never writes them.

## Step 5 · Finalize

```text
$ python3 scripts/audit.py sop.md --profile sop-profile.md
...
RESULT: clean
$ python3 scripts/build_pdf.py sop.md Alex_SOP.pdf
wrote Alex_SOP.pdf (pages: 2)
```

Alex reads the PDF, approves it, and uploads it to the portal.
