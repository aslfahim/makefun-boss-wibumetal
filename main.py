"""One Word for the Boss — entry writer.

Writes exactly one word describing a boss to /output/entry.txt.
The word is the whole entry: no spaces, no punctuation, no newline.
"""

import os
import sys


# The single word this entry submits. Chosen because every boss,
# in every industry, is the person you can never quite reach:
# the calendar is full, the door is closed, the reply never comes.
WORD = "Unreachable"

MAX_CHARS = 30


def _check(word):
    """Return a list of problems with `word`, empty when it is valid."""
    problems = []
    if not word:
        problems.append("word is empty")
    if len(word) > MAX_CHARS:
        problems.append("word is longer than %d characters" % MAX_CHARS)
    if word != word.strip():
        problems.append("word has leading or trailing whitespace")
    if any(ch.isspace() for ch in word):
        problems.append("word contains whitespace")
    if any(not ch.isalpha() for ch in word):
        problems.append("word contains a non-letter character")
    return problems


def _target_path():
    out_dir = os.environ.get("OUTPUT_DIR") or "/output"
    return os.path.join(out_dir, "entry.txt")


def main():
    problems = _check(WORD)
    if problems:
        for problem in problems:
            print("invalid word: %s" % problem, file=sys.stderr)
        return 1

    path = _target_path()
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(WORD)

    # Read the file back and confirm byte-for-byte what landed on disk,
    # then decode it and re-check the character count (1-30 chars).
    with open(path, "rb") as handle:
        raw = handle.read()
    if raw != WORD.encode("utf-8"):
        print("verification failed: disk holds %r" % raw, file=sys.stderr)
        return 1
    landed = raw.decode("utf-8")
    if not 1 <= len(landed) <= MAX_CHARS:
        print("verification failed: %d chars on disk" % len(landed),
              file=sys.stderr)
        return 1

    print("wrote %r (%d bytes) to %s" % (WORD, len(raw), path))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
