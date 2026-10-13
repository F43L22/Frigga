"""Frigga's checks. Always run from main's copy, never from a pull request's.

  frigga.py validate <repo_dir>       Thread files have the required fields
  frigga.py gate <changed.txt>        PR is sponsored (if Urd) and the vote passed
  frigga.py sponsor <changed.txt>     commenter may sponsor this PR
"""
import os
import sys
from pathlib import Path

import yaml

REQUIRED = ["title", "knot", "status", "needs"]
STATUSES = {"idea", "active", "paused", "done"}
RE_KNOT = "reverse-engineered-library"
RE_REQUIRED = ["type", "platform", "legal"]
RE_TYPES = {"decomp", "recomp", "emulator", "source-release", "spec"}


def fail(msg):
    print(f"::error::{msg}")
    sys.exit(1)


def frontmatter(path):
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---"):
        return None
    try:
        return yaml.safe_load(text.split("---", 2)[1]) or {}
    except yaml.YAMLError:
        return None


def validate(repo):
    errors = []
    for path in sorted(Path(repo, "knots").glob("*/threads/*.md")):
        if path.name.startswith("_"):
            continue
        rel = path.relative_to(repo).as_posix()
        meta = frontmatter(path)
        if meta is None:
            errors.append(f"{rel}: missing or broken frontmatter")
            continue
        knot = path.parent.parent.name
        required = REQUIRED + (RE_REQUIRED if knot == RE_KNOT else [])
        errors += [f"{rel}: missing `{k}`" for k in required if meta.get(k) in (None, "")]
        if meta.get("knot") not in (None, knot):
            errors.append(f"{rel}: knot is `{meta['knot']}` but file is in `{knot}`")
        if meta.get("status") and meta["status"] not in STATUSES:
            errors.append(f"{rel}: status must be one of {sorted(STATUSES)}")
        if knot == RE_KNOT and meta.get("type") and meta["type"] not in RE_TYPES:
            errors.append(f"{rel}: type must be one of {sorted(RE_TYPES)}")
    if errors:
        fail("Thread check failed:\n" + "\n".join(errors))
    print("Threads OK")


def touched_knots(changed_file):
    knots = set()
    for line in Path(changed_file).read_text().splitlines():
        parts = line.strip().split("/")
        if len(parts) > 2 and parts[0] == "knots" and parts[1] != "_template":
            knots.add(parts[1])
        elif line.strip():
            knots.add("wyrd")  # everything outside knots/ belongs to the Wyrd Knot
    return knots or {"wyrd"}


def is_verdandi_plus(user, knot, norns):
    ranks = norns.get(knot) or {}
    members = (ranks.get("verdandi") or []) + (ranks.get("skuld") or [])
    return user.lower() in {m.lower() for m in members}


def load_norns():
    return yaml.safe_load(Path("norns.yml").read_text(encoding="utf-8")) or {}


def gate(changed_file):
    norns = load_norns()
    author = os.environ["PR_AUTHOR"]
    labels = {l for l in os.environ.get("LABELS", "").split(",") if l}
    knots = touched_knots(changed_file)
    urd_in = sorted(k for k in knots if not is_verdandi_plus(author, k, norns))
    if urd_in and "sponsored" not in labels:
        fail(f"{author} is Urd in {urd_in}: needs a Verdandi+ to comment /sponsor")
    if "vote-passed" not in labels:
        fail("Waiting for the vote (label: vote-passed)")
    print(f"Vote passed for {sorted(knots)}")


def sponsor(changed_file):
    norns = load_norns()
    user = os.environ["COMMENTER"]
    if user.lower() == os.environ.get("PR_AUTHOR", "").lower():
        fail("You can't sponsor your own pull request")
    knots = touched_knots(changed_file)
    missing = sorted(k for k in knots if not is_verdandi_plus(user, k, norns))
    if missing:
        fail(f"{user} must be Verdandi+ in {missing} to sponsor this")
    print(f"{user} sponsors this in {sorted(knots)}")


if __name__ == "__main__":
    if len(sys.argv) != 3 or sys.argv[1] not in {"validate", "gate", "sponsor"}:
        fail(__doc__)
    {"validate": validate, "gate": gate, "sponsor": sponsor}[sys.argv[1]](sys.argv[2])
