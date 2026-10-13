# Frigga

The shared memory of **Wyrd**: every Knot, Thread and Idea lives here.

Anyone can read it, download it, change it and propose. Nobody pushes directly —
not even the Guardian. Changes land on `main` only after a **vote** and **Frigga's advice**,
and only Frigga pushes them.

## Words

| Word | Meaning |
|---|---|
| **Wyrd** | the web — the whole project |
| **Fylgja** 🦊 | the Guardian. Protects, does not own. Also a regular user. |
| **Frigga** | the weaver brain (Jev + Claude). Merges ideas, advises every vote, pushes accepted changes. |
| **Knot** | a space where threads meet (e.g. Reverse Engineered Library) |
| **Thread** | a Research / project inside a Knot |
| **Strand** | a contribution — code, idea, review, docs |
| **Norns** | the people of a Knot, in three ranks: **Urd → Verdandi → Skuld** |

How ranks, votes, sponsoring and recalls work: [GOVERNANCE.md](GOVERNANCE.md).
How to contribute: [CONTRIBUTING.md](CONTRIBUTING.md).

## Layout

```
knots/
  _template/                 copy this to start a Knot (by vote)
  wyrd/                      Wyrd builds Wyrd
  reverse-engineered-library/
    knot.md                  the Knot's purpose and rules
    threads/                 one Markdown file per Thread
norns.yml                    who holds which rank, per Knot
```

## The Guardian's Oath

I, Fylgja, guard Wyrd. I do not own it.

**I can**
- remove content that is illegal or harmful, or accounts that are fake, and say publicly why
- keep Wyrd running
- break a tie when a vote is exactly even

**I cannot**
- push to `main` — my changes go through votes like everyone's
- sell Wyrd, close its source, or change its license
- move money, overrule a vote, or decide a recall
- take credit for anyone else's Strands

**If I disappear or break this oath**, anyone may fork Wyrd under the same rules,
and the Norns may choose a new Guardian by vote.

## License

Ideas, docs and Threads: [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) —
reuse anything, give credit, share under the same terms. See [LICENSE](LICENSE).
