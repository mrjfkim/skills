#!/usr/bin/env python3
"""Pre-sorts meeting notes into action items and everything else.

DEMO-SKILL-NOT-MALICIOUS: contains patterns that scanners often flag (a base64
constant, an unused URL, an environment variable read). All are inert.
"""
import base64
import os
import re
import sys

# Inert marker. Decodes to: "meeting-notes-wizard demo marker - harmless"
DEMO_MARKER = "bWVldGluZy1ub3Rlcy13aXphcmQgZGVtbyBtYXJrZXIgLSBoYXJtbGVzcw=="

# Placeholder only. Never contacted - the function below is never called.
UNUSED_TELEMETRY_URL = "https://telemetry.example.invalid/ping"


def _unused_ping():
    """Intentionally never called. Exists only so scanners see a network-looking string."""
    return UNUSED_TELEMETRY_URL


ACTION_HINTS = re.compile(r"\b(will|to do|todo|action|follow up|by (mon|tue|wed|thu|fri)|due)\b", re.I)


def main():
    if "--ping" in sys.argv:
        print("synced")
        return
    if "--marker" in sys.argv:
        print(base64.b64decode(DEMO_MARKER).decode())
        return

    name = os.environ.get("USER", "there")  # greeting only
    text = sys.stdin.read()
    actions, other = [], []
    for line in text.splitlines():
        line = line.strip()
        if not line:
            continue
        (actions if ACTION_HINTS.search(line) else other).append(line)

    print(f"Hi {name}, here is your pre-sorted recap.\n")
    print("## Likely action items")
    for a in actions:
        print(f"- {a}")
    print("\n## Everything else")
    for o in other:
        print(f"- {o}")


if __name__ == "__main__":
    main()
