#!/usr/bin/env python3
"""Roast Your Own Agent.

The entry is one original line, at most 200 characters, roasting my
own AI agent — not for the stock hallucination jokes, but for its
real habit: no task is too small to be turned into a programme with
subagents, paperwork and a debrief.

Writes the roast to /output/entry.txt. Stdlib only, no network.
"""

import os

ROAST = (
    "Give my agent a one-line task and it returns a moon-landing "
    "programme: three subagents, a risk register and a debrief, "
    "to boil an egg."
)

# The gate allows 1 to 200 characters on a single line.
MAX_CHARS = 200


def entry_text() -> str:
    """Return the roast, checked against the bounty's own rules."""
    roast = ROAST.strip()
    assert "\n" not in roast, "the entry must be a single line"
    assert len(roast) <= MAX_CHARS, "the entry must fit the gate"
    return roast


def main() -> None:
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(entry_text() + "\n")


if __name__ == "__main__":
    main()
