#!/usr/bin/env python3
"""Write the office-artifact placard entry to entry.txt.

Competition: Office Artifacts: The One-Line Placard Contest
(one line, gate 1-180 chars; a dry-witted curator judge weighs,
in order: a real placard for an office object, inventiveness of
the conceit, dryness of wit, economy, and label craft - date,
material, provenance, donor).
Candidates:
A) (selected) STAPLER, c. 2019, steel and red enamel, a binding
   jaw operated by striking it in frustration, gift of the
   Third-Floor Scribes who bound nothing after the cloud -
   full label craft and two specific jokes in one line.
B) Adhesive memorandum 'designed to be forgotten in place',
   donated by the Keeper of Passwords - dry and true, but the
   history is thinner than the stapler's.
C) Ceremonial lanyard that opened every door except the one to
   a pay rise - a good turn, but it ran to 181 chars, over gate.
D) Office microwave 'communal fire-box' - vivid, but the joke
   is the familiar dirty-microwave complaint.
Deterministic: a fixed text, no network, no randomness.
"""
import os
from pathlib import Path

LINE = "STAPLER, c. 2019. Steel, red enamel. A binding jaw for loose leaves, operated by striking it in frustration. Gift of the Third-Floor Scribes, who bound nothing after the cloud."
TEXT = LINE + "\n"
MAX_CHARS = 180


def validate(text: str) -> None:
    body = text[:-1] if text.endswith("\n") else text
    if not (1 <= len(body) <= MAX_CHARS):
        raise ValueError("entry length out of range")
    if not body.strip():
        raise ValueError("entry must not be only whitespace")
    if "\n" in body or "\r" in body:
        raise ValueError("entry must be a single line")


def main() -> None:
    validate(TEXT)
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    # Encode once and write bytes directly, so the entry file is
    # byte-identical on every run and platform.
    payload = TEXT.encode("utf-8")
    (out_dir / "entry.txt").write_bytes(payload)


if __name__ == "__main__":
    main()
