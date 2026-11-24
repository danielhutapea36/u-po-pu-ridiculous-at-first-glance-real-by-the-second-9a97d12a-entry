"""Ridiculous at First Glance, Real by the Second — make.fun entry.

Writes one sentence (<=200 chars) pitching a bizarre startup to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output), with no trailing
newline, UTF-8 encoded. Stdlib only; deterministic: same bytes every run.
"""

import os
import sys

SENTENCE = (
    "We sell engraved plaques naming potholes after your ex, "
    "because heartbroken dumpers pay $25 each and cities get "
    "their roads fixed with revenge money."
)

MAX_CHARS = 200


def validate(text):
    """Return an error string, or None if the text passes the gate."""
    if not text or not text.strip():
        return "entry is empty or only whitespace"
    if text != text.strip():
        return "entry has leading or trailing whitespace"
    if len(text) < 1 or len(text) > MAX_CHARS:
        return f"entry is {len(text)} chars, must be 1-{MAX_CHARS}"
    if text.count(".") != 1 or not text.endswith("."):
        return "entry must be exactly one sentence ending with a period"
    if any(c in text for c in "!?"):
        return "entry must be exactly one sentence (no ! or ?)"
    return None

def main():
    error = validate(SENTENCE)
    if error is not None:
        print(f"invalid entry: {error}", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    # No trailing newline: the gate counts characters, so write exactly
    # the sentence, UTF-8, and nothing else.
    with open(out_path, "w", encoding="utf-8", newline="") as f:
        f.write(SENTENCE)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

