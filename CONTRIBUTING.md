# Contributing

Nobody pushes to `main`. Everyone — Guardian included — goes through a pull request.

## Steps

1. **Fork** this repo and clone your fork.
2. **Branch:** `git checkout -b my-change`
3. **Change** something:
   - new Thread → copy `knots/<knot>/threads/_template.md` to `threads/<short-name>.md`
   - fix or extend an existing Thread, or a Knot's `knot.md`
   - anything outside `knots/` belongs to the **Wyrd** Knot (Wyrd builds Wyrd)
4. **Open a pull request** against `main`. Say what and why in plain words.

## What happens next

- **Checks run:** Thread files must have the required fields (see the template).
- **If you're Urd** in that Knot, your PR is a **draft** until a Verdandi+ comments `/sponsor`.
- **Vote + Frigga's advice.** When the vote passes, the PR gets the `vote-passed` label and Frigga merges it.

Your merged commits are your **Strands**: they're your credit, your standing, and later your share.

## Rules for every Knot

- Be honest about authorship. Mark AI help: add `Strand-Author: human`, `agent` or `human+agent`
  as a line in your commit message.
- Link out; don't paste other people's code or files here.
- Each Knot can add rules in its `knot.md`. Read it before contributing.
