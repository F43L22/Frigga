# Governance

Every number marked *(start)* is a starting value. The Norns can change it by vote.

## Roles

- **Fylgja** 🦊 — the Guardian. See the Oath in [README](README.md). Protects; never decides.
- **Frigga** — Jev + Claude. Merges duplicate Ideas, advises every vote publicly, pushes accepted changes.
  Frigga **advises but never votes**.
- **Norns** — everyone in a Knot. Ranks are **per Knot**: you can be Skuld in one and Urd in another.

## Ranks

Higher ranks can do everything lower ranks can.

| Rank | | Can |
|---|---|---|
| **0 · Urd** | *what was* — newcomer, learning the Knot | read · search · comment · vote · draft (needs a sponsor) |
| **1 · Verdandi** | *what is* — builder | + contribute Strands · review · **open votes** · **sponsor** Urds |
| **2 · Skuld** | *what shall be* — direction | + propose the future: roadmap, spending, promotions |

Anyone not listed in [`norns.yml`](norns.yml) for a Knot is **Urd** there.

### Origin seats

Whoever's Idea started a Knot starts as **Skuld** and never drops below **Verdandi**.
If Frigga merged several Ideas into one Knot, each of their authors gets an origin seat.

## Standing

```
standing = Σ (accepted Strands × how much each mattered)
         × relevance   — Jev: how well your proven skills fit this Knot
         − slow decay  — inactivity makes room for others
```

Relevance comes from **proven** work (Strands in related Knots, public history, endorsements
from qualified Norns), not from self-description. Qualification makes you rise **faster**;
it never lets you skip the work.

## Sponsoring

Urds cannot open votes. A Verdandi or Skuld can **sponsor** an Urd's draft:

1. Urd posts a draft (Idea, code, fix, concern) as a pull request.
2. A Verdandi+ of that Knot comments `/sponsor`.
3. It enters the normal vote. If accepted, the **Strand is credited to the Urd**; the sponsor is noted.

- Accepted sponsored work gives the sponsor a little standing; spam or legally rejected work costs some.
- Each Verdandi holds at most **3** open sponsorships *(start)*.
- Drafts unsponsored for **7 days** *(start)* are surfaced by Frigga to the best-fit Verdandis.

## Ranking up

- **Urd → Verdandi:** **3** accepted sponsored Strands, sponsored by at least **2** different people *(start)*.
  Strong relevance to the Knot can lower the count.
- **Verdandi → Skuld:** qualified standing + confirmation vote by the Knot's Skulds.
- **Moving down:** long inactivity, or a recall.

## Voting

Every decision follows the same path:

```
proposal (opened by Verdandi+, sources untouched)
  → Frigga's advice, posted publicly
  → vote
  → passed → Frigga pushes / executes
```

**Weight** = rank weight × standing.

| Rank | Weight *(start)* |
|---|---|
| Urd | 1 |
| Verdandi | 3 |
| Skuld | 5 |

- **Skuld cap:** all Skulds together hold at most **50%** of the weight in any vote.
- **Urd votes count** after **14 days** in the Knot and at least one comment or draft *(start)* —
  so fake accounts can't flood a vote.
- **Quorum and threshold** *(start)*: Strands — simple majority; roadmap and promotions — 60%;
  spending and recalls — 2/3, with a minimum turnout.

## Recall (taking down a Skuld)

1. A **Verdandi** opens the recall, with **3** co-signers *(start)*. Urds can raise it through sponsoring.
2. Frigga posts advice: evidence, the Skuld's record, and any signs of brigading (new accounts, coordinated timing).
3. The Skuld replies publicly.
4. **Only Urd and Verdandi vote.** The recalled Skuld and the other Skulds do not.
5. Passes with **2/3** of the weighted vote plus quorum → the Skuld becomes **Verdandi** and keeps all credit.

A failed recall can't be retried against the same person for **30 days** *(start)*.
Origin Skulds can be recalled too; they drop to Verdandi, their floor.
Fylgja does not decide recalls, but can remove fake accounts Frigga flags.

## Funding *(future)*

Each Thread will have a treasury. Two kinds of votes, same path as everything else:

- **Distribution** — how incoming money is split (e.g. contributors vs. spending), fixed by vote.
- **Spending** — what money is used for. A Skuld proposes: what, amount, recipient, milestones.
  Frigga advises (is the cost reasonable? history? red flags?). 2/3 + quorum.

Rules:
- Funds are released **by milestone**, never as a lump sum.
- Every movement is **public**: what came in, what went out, the vote, and Frigga's advice.
- **No one** moves money alone — not Frigga, not Fylgja.
- Contributor payouts follow the recorded Strands.

## Merging Ideas

When a new Idea arrives, Frigga checks it against existing Threads:

| Jev: P(same project) | Result |
|---|---|
| ≥ 0.85 | joined to the existing Thread |
| 0.5 – 0.85 | author chooses: join or stay separate |
| < 0.5 | new Thread |

The Idea is never lost: it joins as the author's own Strand. Any merge can be undone.
