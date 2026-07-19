#!/usr/bin/env python3
import re, subprocess, sys, pathlib, markdown
SRC, PDF = sys.argv[1], sys.argv[2]
HTML = SRC.replace(".md",".html")
CHROME="/opt/pw-browsers/chromium-1194/chrome-linux/chrome"
body = markdown.markdown(pathlib.Path(SRC).read_text(encoding="utf-8"), extensions=["extra","sane_lists","nl2br"])
def cls(html,kw,c):
    return re.compile(r'<li>(\s*(?:<strong>)?'+re.escape(kw)+r'.*?)</li>', re.S).sub(lambda m:f'<li class="{c}">{m.group(1)}</li>', html)
for kw,c in [("EN PANTALLA","onscreen"),("ON SCREEN","onscreen"),("DI:","say"),("SAY:","say"),("B-ROLL","broll")]:
    body=cls(body,kw,c)
body=re.sub(r'<p>(<strong>\[(?:Slide|Tarjeta|Gancho|Recap|Cierre).*?)</p>', r'<div class="beat">\1</div>', body, flags=re.S)
css="""@page{size:Letter;margin:16mm 15mm 14mm;} *{-webkit-print-color-adjust:exact;box-sizing:border-box;}
body{font-family:Georgia,serif;color:#1e2e22;background:#faf9f5;font-size:11.5pt;line-height:1.5;margin:0;}
h1{font-size:26pt;color:#2f5a3f;margin:0 0 2pt;} h1+h3{color:#c1683f;font-family:Arial,sans-serif;font-weight:700;font-size:11pt;letter-spacing:2px;text-transform:uppercase;margin:0 0 14pt;}
h2{font-size:16pt;color:#faf9f5;background:#2f5a3f;padding:7pt 12pt;border-radius:6px;margin:22pt 0 10pt;page-break-after:avoid;}
h3{font-size:12.5pt;color:#2f5a3f;font-family:Arial,sans-serif;border-bottom:2px solid #c1683f;padding-bottom:3pt;margin:18pt 0 8pt;}
p{margin:6pt 0;} strong{color:#2f5a3f;}
.beat{background:#f6f1e3;border-left:5px solid #c1683f;padding:6pt 10pt;margin:14pt 0 4pt;border-radius:0 6px 6px 0;page-break-inside:avoid;page-break-after:avoid;font-size:11pt;}
.beat strong{color:#c1683f;font-family:Arial,sans-serif;} .beat em{color:#2f5a3f;}
ul{list-style:none;padding-left:0;margin:2pt 0 10pt;} li{margin:4pt 0;padding:6pt 10pt 6pt 12pt;border-radius:0 5px 5px 0;page-break-inside:avoid;font-size:10.8pt;}
li strong{font-family:Arial,sans-serif;} li.onscreen{background:#eef1ea;border-left:4px solid #7d8f77;} li.onscreen em{color:#2f5a3f;font-weight:bold;font-style:normal;}
li.say{background:#eaf1ec;border-left:4px solid #2f5a3f;font-size:11.4pt;} li.broll{background:#f6efe9;border-left:4px solid #c1683f;color:#5a463c;} li.broll strong{color:#c1683f;}
hr{border:0;border-top:1px dashed #c9beac;margin:16pt 0;} li:not(.onscreen):not(.say):not(.broll){background:transparent;border-left:3px solid #d8cfbe;padding:3pt 8pt;}"""
pathlib.Path(HTML).write_text(f"<!doctype html><html><head><meta charset='utf-8'><style>{css}</style></head><body>{body}</body></html>", encoding="utf-8")
subprocess.run([CHROME,"--headless=new","--no-sandbox","--disable-gpu","--no-pdf-header-footer",f"--print-to-pdf={PDF}",pathlib.Path(HTML).resolve().as_uri()],capture_output=True,text=True,timeout=120)
print("PDF:", PDF, pathlib.Path(PDF).exists(), pathlib.Path(PDF).stat().st_size)
