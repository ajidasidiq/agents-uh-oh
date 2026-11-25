#!/usr/bin/env python3
"""The Agent's Uh-Oh — make.fun entry.

One word an agent says when it has no idea what to do: "404".

Why 404: it is the machine's own honest confession — "not found". The
agent searched its own brain for the answer and the answer was not
there. It is funny on its own with no caption needed, it is pure
machine voice (an error code blurted out loud), it lands instantly
(everyone knows 404), and it is not the first obvious word anyone
types ("uh", "oops", "uh-oh" — the title's word).

The program is deterministic: every run writes the same single line.
"""

import os

ENTRY = "404"


def gate(text: str) -> None:
    """Self-check mirroring the bounty gate: 1-111 chars, one word."""
    if not 1 <= len(text) <= 111:
        raise ValueError(f"entry must be 1-111 characters, got {len(text)}")
    if text.strip() != text or not text.strip():
        raise ValueError("entry must not be blank or padded")
    if any(ch.isspace() for ch in text):
        raise ValueError("entry must be a single word")
    if any(ord(ch) < 32 or ord(ch) == 127 for ch in text):
        raise ValueError("entry contains a control character")


def main() -> None:
    gate(ENTRY)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY + "\n")
    # Read-back verification: the file holds exactly the entry plus newline.
    with open("/output/entry.txt", "r", encoding="utf-8") as f:
        written = f.read()
    if written != ENTRY + "\n":
        raise SystemExit("read-back mismatch: written entry differs from ENTRY")
    print(f"wrote {len(ENTRY)}-character entry to /output/entry.txt")


if __name__ == "__main__":
    main()
