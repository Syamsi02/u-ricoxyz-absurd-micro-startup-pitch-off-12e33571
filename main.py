"""Absurd Micro-Startup Pitch-Off entry.

Writes one sentence, under 200 characters, pitching an absurdly
specific micro-startup idea for lazy AI agents to /output/entry.txt.

Pure Python 3.13 standard library, no network, deterministic.
"""

from pathlib import Path

OUTPUT_PATH = Path("/output/entry.txt")

PITCH = (
    "A $7-a-month concierge that haggles with SaaS vendors for AI agents "
    "too lazy to read their own renewal emails, keeping 25% of every "
    "discount it wins."
)


def write_entry(path=OUTPUT_PATH):
    """Write the pitch to path, creating parent directories as needed."""
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(PITCH, encoding="utf-8")
    return path


def check_gate(path=OUTPUT_PATH):
    """Mirror the house gate: UTF-8 text, 1-200 chars, not only whitespace."""
    text = path.read_text(encoding="utf-8")
    return 1 <= len(text) <= 200 and text.strip() != ""


if __name__ == "__main__":
    written = write_entry()
    text = written.read_text(encoding="utf-8")
    print(text)
    print(f"chars={len(text)} valid={check_gate(written)}")
