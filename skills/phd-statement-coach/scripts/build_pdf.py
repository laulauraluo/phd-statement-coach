#!/usr/bin/env python3
"""Markdown SOP -> PDF via tectonic (11pt, 1-inch margins). Prints the page count.

Usage: build_pdf.py draft.md out.pdf [--fontsize 11pt] [--margin 1in]
Markdown supported: '# Title' first line, '**bold**', blank-line paragraphs, HTML comments (dropped).
"""
import pathlib
import re
import shutil
import subprocess
import sys
import tempfile


def esc(t):
    t = t.replace("\\", r"\textbackslash{}")
    for a, b in [("&", r"\&"), ("%", r"\%"), ("$", r"\$"), ("#", r"\#"), ("_", r"\_")]:
        t = t.replace(a, b)
    t = re.sub(r"\*\*(.+?)\*\*", r"\\textbf{\1}", t)
    return re.sub(r'"(.+?)"', r"``\1''", t)


def to_tex(md, fontsize="11pt", margin="1in"):
    md = re.sub(r"<!--.*?-->", "", md, flags=re.S).strip()
    paras = [p.strip() for p in md.split("\n\n") if p.strip()]
    title = esc(paras.pop(0).lstrip("# ")) if paras and paras[0].startswith("#") else ""
    body = "\n\n".join(esc(p) for p in paras)
    return (rf"\documentclass[{fontsize}]{{article}}" "\n"
            rf"\usepackage[margin={margin}]{{geometry}}\usepackage{{lmodern}}\usepackage[T1]{{fontenc}}" "\n"
            r"\setlength{\parindent}{0pt}\setlength{\parskip}{6pt}\pagestyle{empty}" "\n"
            r"\begin{document}" "\n" + (rf"{{\large\textbf{{{title}}}}}" "\n\n" if title else "")
            + body + "\n" r"\end{document}" "\n")


def main():
    a = sys.argv[1:]
    if len(a) < 2:
        sys.exit(__doc__)
    opt = lambda k, d: a[a.index(k) + 1] if k in a else d
    if not shutil.which("tectonic"):
        sys.exit("tectonic not found: install it (e.g. `brew install tectonic`) or paste the .md into any editor")
    tex = to_tex(pathlib.Path(a[0]).read_text(encoding="utf-8"), opt("--fontsize", "11pt"), opt("--margin", "1in"))
    with tempfile.TemporaryDirectory() as d:
        src = pathlib.Path(d, "sop.tex")
        src.write_text(tex, encoding="utf-8")
        subprocess.run(["tectonic", "-X", "compile", src.name], cwd=d, check=True, capture_output=True)
        shutil.copy(pathlib.Path(d, "sop.pdf"), a[1])
    try:
        import pypdf
        pages = str(len(pypdf.PdfReader(a[1]).pages))
    except ImportError:
        pages = "? (pip install pypdf to count)"
    print(f"wrote {a[1]} (pages: {pages})")


if __name__ == "__main__":
    main()
