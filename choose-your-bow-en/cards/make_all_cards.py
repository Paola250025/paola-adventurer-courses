#!/usr/bin/env python3
import subprocess, pathlib, fitz

CHROME="/opt/pw-browsers/chromium-1194/chrome-linux/chrome"
GREEN="#2F5A3F"; DGREEN="#1E2E22"; TERRA="#C1683F"; CREAM="#F6F1E3"; SAGE="#7D8F77"
OUT=pathlib.Path("cards_en"); OUT.mkdir(exist_ok=True)

STYLE=f"""<style>
@page{{size:1920px 1080px;margin:0;}}
*{{margin:0;padding:0;box-sizing:border-box;-webkit-print-color-adjust:exact;print-color-adjust:exact;}}
html,body{{width:1920px;height:1080px;}}
.card{{width:1920px;height:1080px;position:relative;overflow:hidden;font-family:Georgia,'Times New Roman',serif;}}
.frame{{position:absolute;inset:40px;border:3px solid var(--fr);}}
.badge{{width:172px;height:172px;border-radius:50%;border:3px solid var(--bd);display:flex;flex-direction:column;
  align-items:center;justify-content:center;text-align:center;line-height:1;}}
.badge .ar{{color:{TERRA};font-size:26px;margin-bottom:2px;}}
.badge .pa{{font-family:Georgia,serif;font-weight:900;font-size:40px;letter-spacing:1px;color:var(--pa);}}
.badge .ad{{font-family:Arial,sans-serif;font-size:12.5px;letter-spacing:4px;color:{TERRA};margin:4px 0 5px;}}
.badge .dv{{width:96px;height:1.5px;background:var(--bd);margin-bottom:5px;}}
.badge .tg{{font-family:Arial,sans-serif;font-size:8.5px;letter-spacing:1.4px;color:var(--pa);opacity:.85;}}
.kick{{font-family:Arial,sans-serif;font-weight:700;text-transform:uppercase;}}
.serif{{font-family:Georgia,serif;font-weight:900;line-height:1.03;}}
.arrow{{display:flex;align-items:center;}}
.arrow .ln{{height:4px;background:{TERRA};}} .arrow .hd{{width:0;height:0;border-top:11px solid transparent;border-bottom:11px solid transparent;border-left:22px solid {TERRA};}}
.lab{{font-family:Arial,sans-serif;font-weight:700;}}
table{{border-collapse:collapse;width:100%;font-family:Arial,sans-serif;}}
th,td{{text-align:left;padding:22px 26px;font-size:33px;}}
thead th{{background:{GREEN};color:{CREAM};letter-spacing:2px;font-size:26px;text-transform:uppercase;}}
tbody tr:nth-child(even){{background:#efe7d6;}}
tbody tr td:first-child{{color:{TERRA};font-weight:700;font-family:Georgia,serif;}}
</style>"""

def badge(light=False, size=178):
    # Self-contained cream "coin" emblem — works on green or cream cards.
    return f'''<svg width="{size}" height="{size}" viewBox="0 0 200 200" xmlns="http://www.w3.org/2000/svg">
      <circle cx="100" cy="100" r="94" fill="{CREAM}" stroke="{GREEN}" stroke-width="5"/>
      <circle cx="146" cy="58" r="12" fill="{TERRA}"/>
      <line x1="100" y1="26" x2="100" y2="150" stroke="{GREEN}" stroke-width="3"/>
      <polygon points="100,20 93,38 107,38" fill="{GREEN}"/>
      <polygon points="140,148 132,128 148,128" fill="{TERRA}"/>
      <rect x="98.5" y="150" width="3" height="26" fill="{TERRA}"/>
      <polygon points="28,150 72,84 116,150" fill="{SAGE}"/>
      <polygon points="84,150 130,72 176,150" fill="{GREEN}"/>
      <polygon points="130,72 119,90 141,90" fill="{CREAM}"/>
      <polygon points="46,150 37,123 55,123" fill="{GREEN}"/>
      <polygon points="160,150 152,126 168,126" fill="{GREEN}"/>
      <polygon points="79,150 100,108 121,150" fill="{CREAM}" stroke="{GREEN}" stroke-width="3"/>
      <line x1="100" y1="108" x2="100" y2="150" stroke="{GREEN}" stroke-width="2"/>
      <line x1="22" y1="150" x2="178" y2="150" stroke="{GREEN}" stroke-width="3"/>
      <rect x="27" y="150" width="146" height="31" fill="{GREEN}"/>
      <text x="100" y="165" text-anchor="middle" fill="{CREAM}" font-family="Georgia,serif" font-weight="900" font-size="17" letter-spacing="1.5">PAOLA</text>
      <text x="100" y="177" text-anchor="middle" fill="{CREAM}" font-family="Arial,sans-serif" font-size="8" letter-spacing="3.5">ADVENTURER</text>
    </svg>'''

def pg(inner): return f"<!doctype html><html><head><meta charset='utf-8'>{STYLE}</head><body>{inner}</body></html>"

def cover():
    return pg(f"""<div class="card" style="--fr:{TERRA};background:{GREEN};color:{CREAM};display:flex;flex-direction:column;align-items:center;justify-content:center">
      <div class="frame"></div><div style="position:absolute;top:66px;left:50%;transform:translateX(-50%)">{badge()}</div>
      <div class="kick" style="color:{TERRA};font-size:26px;letter-spacing:9px;margin-bottom:24px">A 5-Part Mini-Series</div>
      <div class="serif" style="font-size:168px;text-align:center">CHOOSE<br>YOUR BOW</div>
      <div class="arrow" style="margin:42px 0"><div class="ln" style="width:220px"></div><div class="hd"></div></div>
      <div class="lab" style="font-size:29px;letter-spacing:6px">FIND THE BOW THAT'S RIGHT FOR YOU</div>
      <div style="position:absolute;bottom:120px;font-family:Arial;letter-spacing:8px;font-size:22px;color:{TERRA}">RECURVE &nbsp;&middot;&nbsp; GENESIS &nbsp;&middot;&nbsp; COMPOUND</div></div>""")

def title(ep,name):
    return pg(f"""<div class="card" style="--fr:{TERRA};background:{GREEN};color:{CREAM};display:flex;flex-direction:column;justify-content:center;padding:0 150px">
      <div class="frame"></div><div style="position:absolute;top:58px;left:60px">{badge()}</div>
      <div style="position:absolute;top:104px;right:72px;font-family:Arial;letter-spacing:8px;font-size:21px;color:{TERRA}">CHOOSE YOUR BOW</div>
      <div class="kick" style="color:{TERRA};font-size:34px;letter-spacing:8px;margin-bottom:20px">Episode {ep}</div>
      <div class="serif" style="font-size:120px">{name}</div>
      <div class="arrow" style="margin-top:38px"><div class="ln" style="width:260px"></div><div class="hd"></div></div></div>""")

def listcard(kick,heading,items,footer=None,hsize=86):
    rows=""
    for h,d in items:
        rows+=(f'<div style="display:flex;align-items:baseline;gap:22px;margin:20px 0">'
               f'<span style="color:{TERRA};font-size:32px;line-height:1">&#10148;</span>'
               f'<span style="font-size:43px;color:{DGREEN}"><b style="color:{GREEN}">{h}</b>{d}</span></div>')
    foot=(f'<div style="position:absolute;bottom:116px;left:150px;right:150px;font-style:italic;font-size:29px;color:{TERRA}">{footer}</div>') if footer else ""
    return pg(f"""<div class="card" style="--fr:{SAGE};background:{CREAM};color:{DGREEN};padding:108px 150px 0">
      <div class="frame"></div><div style="position:absolute;top:66px;right:72px">{badge(True)}</div>
      <div class="kick" style="color:{TERRA};font-size:25px;letter-spacing:7px;margin-bottom:12px">{kick}</div>
      <div class="serif" style="font-size:{hsize}px;color:{GREEN};margin-bottom:38px">{heading}</div>
      {rows}{foot}</div>""")

def table():
    rows=[("Recurve","Technical, Olympic","Low–mid (grows)","Needs form room"),
          ("Genesis","Trying it, families","Lowest cost","Simplest to store"),
          ("Compound","Hunting, competition","Highest","Needs tuning")]
    body="".join(f"<tr><td>{a}</td><td>{b}</td><td>{c}</td><td>{d}</td></tr>" for a,b,c,d in rows)
    return pg(f"""<div class="card" style="--fr:{SAGE};background:{CREAM};color:{DGREEN};padding:108px 150px 0">
      <div class="frame"></div><div style="position:absolute;top:66px;right:72px">{badge(True)}</div>
      <div class="kick" style="color:{TERRA};font-size:25px;letter-spacing:7px;margin-bottom:12px">Episode 5 &middot; At a Glance</div>
      <div class="serif" style="font-size:82px;color:{GREEN};margin-bottom:40px">Quick reference</div>
      <table><thead><tr><th>Bow</th><th>Goal</th><th>Budget</th><th>Space</th></tr></thead><tbody>{body}</tbody></table>
      <div style="position:absolute;bottom:104px;left:150px;font-style:italic;font-size:27px;color:{TERRA}">Pause here any time — this is your cheat sheet.</div></div>""")

def cta():
    return pg(f"""<div class="card" style="--fr:{TERRA};background:{GREEN};color:{CREAM};display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;padding:0 160px">
      <div class="frame"></div><div style="position:absolute;top:60px;left:50%;transform:translateX(-50%)">{badge()}</div>
      <div class="kick" style="color:{TERRA};font-size:26px;letter-spacing:8px;margin-bottom:22px">Your Next Step</div>
      <div class="serif" style="font-size:120px">Which one is<br>YOUR bow?</div>
      <div class="arrow" style="margin:40px 0"><div class="ln" style="width:200px"></div><div class="hd"></div></div>
      <div class="lab" style="font-size:30px;letter-spacing:3px;margin-bottom:26px">Comment which one fits you</div>
      <div class="lab" style="font-size:26px;letter-spacing:3px;color:{CREAM};opacity:.85;margin-bottom:12px">READY TO START SHOOTING?</div>
      <div style="font-family:Georgia,serif;font-weight:900;font-size:44px;color:{TERRA}">Get <span style="color:{CREAM}">Archery From Zero</span></div>
      <div style="font-family:Arial;font-size:26px;color:{TERRA};letter-spacing:2px;margin-top:14px">&rarr; [ add your course link ]</div></div>""")

cards = {
 "01_cover": cover(),
 "02_ep1_title": title(1,"Welcome to Archery"),
 "03_facts": listcard("Episode 1 &middot; A Quick History","Older than you think",
    [("64,000 years — ","the oldest arrowheads ever found"),
     ("8,000 years — ","the oldest complete bow, from a Danish bog"),
     ("3&times; safer — ","than golf, according to studies"),
     ("Bhutan — ","the only country where it's the national sport")]),
 "04_meet3": listcard("Episode 1 &middot; The Line-Up","Meet the three bows",
    [("RECURVE — ","the classic you see at the Olympics"),
     ("GENESIS — ","the bow U.S. schools use to teach from zero"),
     ("COMPOUND — ","the pulley bow for hunters & precision")]),
 "05_ep2_title": title(2,"The Recurve Bow"),
 "06_recurve_history": listcard("Episode 2 &middot; Recurve","From the Mongols to the Olympics",
    [("~1600 BCE — ","the recurve design already existed"),
     ("The Mongols — ","short, powerful recurves fired from horseback"),
     ("Since 1972 — ","for decades, the only Olympic bow")]),
 "07_recurve_parts": listcard("Episode 2 &middot; The Parts","Simple, four pieces",
    [("RISER — ","the grip; holds the sight window"),
     ("LIMBS — ","the engine; they bend and store power"),
     ("STRING — ","connects the tips, launches the arrow"),
     ("ARROW REST — ","where the arrow sits before the shot")],
    "Takedown tip: swap just the limbs for stronger ones as you grow."),
 "08_recurve_who": listcard("Episode 2 &middot; Recurve","Who it's for",
    [("Classic challenge — ","loves the technical, Olympic side"),
     ("Good form — ","happy to invest time in technique"),
     ("Grows with you — ","upgrade limbs, not the whole bow")]),
 "09_ep3_title": title(3,"The Genesis Bow"),
 "10_genesis_history": listcard("Episode 3 &middot; Genesis","Built for U.S. schools",
    [("NASP, 2002 — ","created in Kentucky with the Dept. of Education"),
     ("10,000 schools — ","4M+ students, 47 states, 5 countries"),
     ("One design — ","fits a whole class of different sizes")]),
 "11_genesis_parts": listcard("Episode 3 &middot; The Parts","What makes it tick",
    [("SINGLE CAM — ","smoother shot, less recoil & noise"),
     ("IDLER WHEEL — ","guides the string, near-zero upkeep"),
     ("NO fixed draw length — ","the same bow fits anyone"),
     ("10–20 lb — ","adjustable, but still feels real")]),
 "12_genesis_who": listcard("Episode 3 &middot; Genesis","Who it's for",
    [("Trying it out — ","no big commitment up front"),
     ("Families & kids — ","and groups"),
     ("Lowest cost — ","and lowest maintenance")]),
 "13_ep4_title": title(4,"The Compound Bow"),
 "14_compound_history": listcard("Episode 4 &middot; Compound","A saw, a recurve, airplane pulleys",
    [("1966 — ","Holless Wilbur Allen invents it in Missouri"),
     ("The idea — ","reach a deer before it can move"),
     ("Patent 1969 — ","the modern compound industry begins")], hsize=74),
 "15_compound_parts": listcard("Episode 4 &middot; The Parts","The mechanical edge",
    [("CAMS — ","two wheels that create the advantage"),
     ("CABLES — ","work with the cams to move force"),
     ("LET-OFF — ","hold ~10 lb on a 70-lb bow at full draw"),
     ("RELEASE + PEEP — ","a trigger & sight ring for consistency")]),
 "16_compound_who": listcard("Episode 4 &middot; Compound","Who it's for",
    [("Hunting & competition — ","precision shooters"),
     ("Loves the tech — ","the gear & mechanical side"),
     ("OK investing more — ","for speed & accuracy, less strain")]),
 "17_ep5_title": title(5,"Which Bow Is Yours?"),
 "18_framework": listcard("Episode 5 &middot; Decide","Four quick questions",
    [("1&nbsp;&nbsp;GOAL — ","just trying it, Olympic dreams, or hunting?"),
     ("2&nbsp;&nbsp;BUDGET — ","how much do you want to spend up front?"),
     ("3&nbsp;&nbsp;HOW OFTEN — ","occasional, a growing hobby, or serious?"),
     ("4&nbsp;&nbsp;SPACE — ","indoor range, room for form, storage?")]),
 "19_table": table(),
 "20_cta": cta(),
}

pdfs=[]
for name, markup in cards.items():
    hp=OUT/f"{name}.html"; pdf=OUT/f"{name}.pdf"; png=OUT/f"{name}.png"
    hp.write_text(markup)
    subprocess.run([CHROME,"--headless=new","--no-sandbox","--disable-gpu","--no-pdf-header-footer",
        f"--print-to-pdf={pdf}", hp.resolve().as_uri()], capture_output=True, text=True, timeout=90)
    d=fitz.open(pdf); d[0].get_pixmap(dpi=96).save(png); pdfs.append(pdf)
    print("ok", name)

merged=fitz.open()
for p in pdfs:
    merged.insert_pdf(fitz.open(p))
merged.save("ChooseYourBow_EN_Cards.pdf")
print("MERGED", merged.page_count, "pages")
