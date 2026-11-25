#!/usr/bin/env python3
"""One-Line Office Joke (make.fun bounty
u-kevin-the-funniest-office-joke-judged-head-to-head-3dc3233c).

Writes one line to /output/entry.txt: a joke about office life.

The line, built against the judge's brief in the kit's RULES.txt,
in the brief's own order:
  1. On subject: a one-line joke about office life -- the IT ticket
     system, and what it does to a ticket about itself.
  2. Funny: the punchline pays off the setup -- the ticket filed to
     fix the ticket system is closed as a duplicate of itself, so
     the system defends itself with its own bureaucracy.
  3. One line: a single sentence, setup and punchline on one line.
  4. Fresh: a specific detail -- a ticket about the ticket system,
     closed as its own duplicate -- not the meeting, reply-all or
     printer tropes the brief itself lists as examples.
  5. Clear on first read: plain words, no reference to explain.

Rejected alternatives: a meeting scheduled to discuss too many
meetings (a trope everyone has heard); the printer only working on
days nobody needs it (the punch blames a machine, not the system);
an out-of-office reply for lunch (funny setup, but the punch is a
boss asking for one more meeting -- the same meeting joke again).
The ticket line wins on the judge's own order: its surprise is
last, its detail is the most specific, and it is the tightest.

Deterministic: the line is a fixed string, no randomness, no network,
no model calls. Every run writes the same bytes.

  mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os

JOKE = (
    "I filed a ticket to fix the ticket system, and IT closed it as "
    "a duplicate of the ticket I filed to fix the ticket system."
)


def _validate(joke: str) -> None:
    """Grader contract: exactly one line, 1-200 chars, not only
    whitespace. Fail loudly instead of writing an entry the gate
    would refuse."""
    if not 1 <= len(joke) <= 200:
        raise ValueError(f"joke must be 1-200 chars, got {len(joke)}")
    if "\n" in joke or "\r" in joke:
        raise ValueError("joke must be a single line")
    if not joke.strip():
        raise ValueError("joke must not be only whitespace")


def main() -> None:
    _validate(JOKE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
