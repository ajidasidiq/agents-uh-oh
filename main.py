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


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
