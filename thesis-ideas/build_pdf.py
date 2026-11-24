"""Build Thesis_Ideas_Nini_Rizhamadze.pdf from thesis-ideas.md.

Requirements: pip install markdown weasyprint
Usage: python3 build_pdf.py
"""

from pathlib import Path

import markdown
from markdown.extensions.toc import TocExtension
from weasyprint import HTML

HERE = Path(__file__).parent
SOURCE = HERE / "thesis-ideas.md"
OUTPUT = HERE / "Thesis_Ideas_Nini_Rizhamadze.pdf"

TITLE_PAGE = """
<section class="title-page">
  <p class="kicker">Master's Thesis Planning</p>
  <h1 class="title">Thesis Ideas</h1>
  <p class="subtitle">Candidate topics, proposals and next steps</p>
  <div class="meta">
    <p><strong>Nini Rizhamadze</strong></p>
    <p>MSc in Data Science and Statistics (LM-82/LM-DATA)</p>
    <p>University of Palermo</p>
    <p>November 2026</p>
  </div>
</section>
"""

CSS = """
@page {
  size: A4;
  margin: 22mm 20mm 22mm 20mm;
  @bottom-center { content: counter(page); font-size: 9pt; color: #666; }
}
@page :first { @bottom-center { content: none; } }

body { font-family: "DejaVu Sans", Arial, sans-serif; font-size: 10pt; line-height: 1.45; color: #222; }

.title-page { page-break-after: always; padding-top: 70mm; }
.kicker { text-transform: uppercase; letter-spacing: 2px; color: #8a1c2b; font-size: 10pt; margin: 0; }
.title { font-size: 34pt; margin: 6px 0 4px 0; color: #1d2b44; border: none; }
.subtitle { font-size: 14pt; color: #555; margin: 0 0 60mm 0; }
.meta p { margin: 2px 0; font-size: 11pt; }

nav.toc { page-break-after: always; }
nav.toc h1 { border: none; }
nav.toc ul { list-style: none; padding-left: 0; margin: 0; }
nav.toc ul ul { padding-left: 16px; }
nav.toc li { margin: 3px 0; }
nav.toc > ul > li { margin-top: 9px; font-weight: bold; }
nav.toc > ul > li li { font-weight: normal; }
nav.toc a { color: #222; text-decoration: none; }
nav.toc a::after { content: leader('.') target-counter(attr(href), page); }

h1 { font-size: 18pt; color: #1d2b44; border-bottom: 2px solid #8a1c2b; padding-bottom: 4px; margin-top: 0; page-break-before: always; }
nav.toc h1, .title-page h1 { page-break-before: avoid; }
h2 { font-size: 13pt; color: #1d2b44; margin-top: 16px; page-break-after: avoid; }
h3 { font-size: 11pt; page-break-after: avoid; }

table { border-collapse: collapse; width: 100%; margin: 8px 0 12px 0; font-size: 9pt; page-break-inside: auto; }
tr { page-break-inside: avoid; }
th { background: #1d2b44; color: white; text-align: left; padding: 5px 6px; }
td { border-bottom: 1px solid #ddd; padding: 5px 6px; vertical-align: top; }
tr:nth-child(even) td { background: #f5f6f8; }

ul, ol { margin-top: 4px; }
li { margin-bottom: 3px; }
a { color: #1d4f91; }
code { font-size: 9pt; background: #f0f0f0; padding: 0 3px; }
"""


def main() -> None:
    md = markdown.Markdown(
        extensions=["tables", TocExtension(toc_depth="1-2")]
    )
    body = md.convert(SOURCE.read_text(encoding="utf-8"))
    toc = md.toc.replace('<div class="toc">', '<nav class="toc"><h1>Table of Contents</h1>', 1)
    toc = toc[: toc.rfind("</div>")] + "</nav>"
    html = f"<html><head><meta charset='utf-8'><style>{CSS}</style></head><body>{TITLE_PAGE}{toc}{body}</body></html>"
    HTML(string=html, base_url=str(HERE)).write_pdf(OUTPUT)
    print(f"Wrote {OUTPUT}")


if __name__ == "__main__":
    main()
