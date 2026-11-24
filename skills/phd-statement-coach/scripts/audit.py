#!/usr/bin/env python3
"""Mechanical checks for an SOP draft in Markdown.

Usage: audit.py draft.md [--profile sop-profile.md]
Exit code 1 if anything blocks submission (placeholders, forbidden terms, em dashes).
"""
import re
import sys

ADJECTIVES = ["passionate", "fascinated", "journey", "robust", "cutting-edge", "deeply",
              "eager", "thrilled", "excited", "seamless", "leverage", "utilize", "delve",
              "tapestry", "pivotal", "invaluable", "unwavering", "instantly", "exactly"]


def forbidden_terms(profile_path):
    terms, on = [], False
    for line in open(profile_path, encoding="utf-8"):
        if line.startswith("## "):
            on = line.strip().lower() == "## never mention"
        elif on and line.strip().startswith("-") and line.strip("-").strip():
            terms.append(line.strip("-").strip())
    return terms


def audit(text, terms=()):
    body = re.sub(r"<!--.*?-->", "", text, flags=re.S)
    words = len(re.sub(r"[#*`>]", " ", body).split())
    problems = {
        "placeholders": re.findall(r"\[(?:TODO|OPTIONAL|CONFIRM|confirm)[^\]]*\]", body),
        "em_dashes": body.count("—"),
        "forbidden": [t for t in terms if re.search(re.escape(t), body, re.I)],
    }
    adjectives = {w: len(re.findall(rf"\b{w}\b", body, re.I)) for w in ADJECTIVES}
    return words, problems, {w: n for w, n in adjectives.items() if n}


def main():
    args = sys.argv[1:]
    if not args:
        sys.exit(__doc__)
    terms = forbidden_terms(args[args.index("--profile") + 1]) if "--profile" in args else []
    words, problems, adjectives = audit(open(args[0], encoding="utf-8").read(), terms)
    print(f"words: {words}")
    for k, v in problems.items():
        print(f"{k}: {v}")
    print(f"watch-list adjectives: {adjectives or 'none'}")
    blocked = problems["placeholders"] or problems["forbidden"] or problems["em_dashes"]
    print("RESULT:", "FIX BEFORE SUBMITTING" if blocked else "clean")
    sys.exit(1 if blocked else 0)


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--selftest":
        w, p, a = audit("A robust plan [TODO: role] for Acme College — done.", ["Acme College"])
        assert p["placeholders"] and p["forbidden"] == ["Acme College"] and p["em_dashes"] == 1 and a == {"robust": 1}
        w, p, a = audit("<!-- [TODO: hidden] --> Plain text.", ["Acme College"])
        assert not p["placeholders"] and not p["forbidden"] and w == 2
        print("selftest ok")
    else:
        main()
