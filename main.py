#!/usr/bin/env python3
"""The Funniest One-Line Resignation Letter — make.fun entry.

Writes the resignation letter of a cron job that has fired every minute
since March to /output/entry.txt. Deterministic: the same line every run,
no randomness, no clock, no network, no file reads outside this repo.
"""

# The entry: one line, 102 characters, in the voice of a tired cron job.
ENTRY = (
    "I have fired every minute since March; today I am filing "
    "my two weeks' notice in the log nobody reads."
)


def main() -> None:
    import os

    # Guard the gate before writing: one line, 1-140 chars, not blank.
    assert 1 <= len(ENTRY) <= 140, "entry must be 1-140 characters"
    assert "\n" not in ENTRY and ENTRY.strip(), "entry must be a single line"

    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
