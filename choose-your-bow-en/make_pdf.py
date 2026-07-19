#!/usr/bin/env python3
import re, subprocess, sys, pathlib, markdown

SRC = "ChooseYourBow_EN_Script_and_Shotlist.md"
HTML = "ChooseYourBow_EN_Script.html"
PDF  = "ChooseYourBow_EN_Script.pdf"
CHROME = "/opt/pw-browsers/chromium-1194/chrome-linux/chrome"

md_text = pathlib.Path(SRC).read_text()

body = markdown.markdown(md_text, extensions=["extra", "sane_lists", "nl2br"])

# color-code the beat rows
def add_li_class(html, keyword, cls):
    pat = re.compile(r'<li>(\s*(?:<strong>)?' + re.escape(keyword) + r'.*?)</li>', re.S)
    return pat.sub(lambda m: f'<li class="{cls}">{m.group(1)}</li>', html)

body = add_li_class(body, "ON SCREEN", "onscreen")
body = add_li_class(body, "SAY:", "say")
body = add_li_class(body, "B-ROLL:", "broll")

# slide/beat header paragraphs (contain "[Slide")
body = re.sub(r'<p>(<strong>\[Slide.*?)</p>', r'<div class="beat">\1</div>', body, flags=re.S)

css = """
@page { size: Letter; margin: 16mm 15mm 14mm 15mm; }
* { -webkit-print-color-adjust: exact; print-color-adjust: exact; box-sizing: border-box; }
body { font-family: Georgia, 'Times New Roman', serif; color:#1e2e22; background:#faf9f5;
       font-size: 11.5pt; line-height: 1.5; margin:0; }
h1 { font-size: 26pt; color:#2f5a3f; margin:0 0 2pt; letter-spacing:.5px; }
h1 + h3 { color:#c1683f; font-family:Arial,Helvetica,sans-serif; font-weight:700;
          font-size:11pt; letter-spacing:2px; text-transform:uppercase; margin:0 0 14pt; border:0; }
h2 { font-size:16pt; color:#faf9f5; background:#2f5a3f; padding:7pt 12pt; border-radius:6px;
     margin:22pt 0 10pt; page-break-after:avoid; page-break-before:auto; }
h3 { font-size:12.5pt; color:#2f5a3f; font-family:Arial,Helvetica,sans-serif;
     border-bottom:2px solid #c1683f; padding-bottom:3pt; margin:18pt 0 8pt; }
p { margin:6pt 0; }
strong { color:#2f5a3f; }
em { color:#3a3a3a; }
.beat { background:#f6f1e3; border-left:5px solid #c1683f; padding:6pt 10pt; margin:14pt 0 4pt;
        border-radius:0 6px 6px 0; page-break-inside:avoid; page-break-after:avoid; font-size:11pt; }
.beat strong { color:#c1683f; font-family:Arial,Helvetica,sans-serif; letter-spacing:.3px; }
.beat em { color:#2f5a3f; font-style:italic; }
ul { list-style:none; padding-left:0; margin:2pt 0 10pt; }
li { margin:4pt 0; padding:6pt 10pt 6pt 12pt; border-radius:0 5px 5px 0; page-break-inside:avoid;
     font-size:10.8pt; }
li strong { font-family:Arial,Helvetica,sans-serif; letter-spacing:.3px; }
li.onscreen { background:#eef1ea; border-left:4px solid #7d8f77; }
li.onscreen em { color:#2f5a3f; font-weight:bold; font-style:normal; }
li.say { background:#eaf1ec; border-left:4px solid #2f5a3f; font-size:11.4pt; line-height:1.55; }
li.say strong { color:#2f5a3f; }
li.broll { background:#f6efe9; border-left:4px solid #c1683f; color:#5a463c; }
li.broll strong { color:#c1683f; }
hr { border:0; border-top:1px dashed #c9beac; margin:16pt 0; }
/* intro + checklist generic bullets */
li:not(.onscreen):not(.say):not(.broll){ background:transparent; border-left:3px solid #d8cfbe;
     padding:3pt 8pt; }
"""

html = f"""<!doctype html><html><head><meta charset="utf-8"><style>{css}</style></head>
<body>{body}</body></html>"""
pathlib.Path(HTML).write_text(html)

r = subprocess.run([CHROME, "--headless=new", "--no-sandbox", "--disable-gpu",
    "--no-pdf-header-footer", f"--print-to-pdf={PDF}", pathlib.Path(HTML).resolve().as_uri()],
    capture_output=True, text=True, timeout=120)
print("chrome rc:", r.returncode)
sys.stderr.write(r.stderr[-800:] if r.stderr else "")
print("exists:", pathlib.Path(PDF).exists(), "size:", pathlib.Path(PDF).stat().st_size if pathlib.Path(PDF).exists() else 0)
