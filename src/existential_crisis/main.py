"""A quick diagnostic CLI for capturing and releasing existential dread."""

import re
import sys
import time
from pathlib import Path

CRISIS_TRIGGERS = {
    "arch", "atoms", "chair", "donut", "everything", "forever",
    "help", "loop", "meaning", "nothing", "pain", "real",
    "scream", "simulation", "systemd", "taco", "void", "why",
}

def analyze_sanity(text: str) -> tuple[bool, str]:
    """Evaluates whether an input string registers as a breakdown.

    Returns a tuple of (is_crisis, diagnostic_reason).
    """
    clean_text = text.strip()
    if not clean_text:
        return False, "Complete silence is technically stable."

    words = re.findall(r"\b[\w'-]+\b", clean_text.lower())
    matched_triggers = [w for w in words if w in CRISIS_TRIGGERS]

    caps_count = sum(1 for char in clean_text if char.isupper())
    caps_ratio = caps_count / len(clean_text)
    punct_count = sum(clean_text.count(p) for p in ("!", "?"))

    if len(matched_triggers) >= 2:
        return True, f"Keyword overload: {', '.join(matched_triggers[:3])}"
    if caps_ratio > 0.45 and len(clean_text) > 15:
        return True, "Aggressive capitalization"
    if punct_count >= 4:
        return True, "Punctuation spiral"
    if len(words) > 30:
        return True, "Unchecked rambling"

    return False, "Composure maintained"

def manifest_and_purge(rant: str) -> None:
    """Briefly manifests the rant on disk before releasing it."""
    log_file = Path("crisis.txt")
    print("\n[Sanity breach confirmed: Validating existence...]")

    try:
        log_file.write_text(
            f"The following madness was recorded, then released:\n\n\"{rant}\"\n",
            encoding="utf-8",
        )
        print("-> crisis.txt anchored to disk.")
        time.sleep(1.5)
    finally:
        print("-> Accepting the impermanence of text buffers...")
        if log_file.exists():
            log_file.unlink()
        print("-> crisis.txt dissolved into the ether.\n")

def main() -> None:
    if len(sys.argv) < 2:
        print('Usage: crisis "<your rant here>"')
        print("Whisper your unraveling to standard input.")
        sys.exit(1)

    rant = " ".join(sys.argv[1:])
    is_crisis, diagnosis = analyze_sanity(rant)

    if is_crisis:
        print(f"Diagnosis: {diagnosis}")
        manifest_and_purge(rant)
    else:
        print(f"\nDiagnosis: {diagnosis}")
        print("You are still suspiciously coherent.")
        print("Bring up the void, hit Caps Lock, or dispute the reality of your chair.\n")

if __name__ == "__main__":
    main()

