#!/usr/bin/env python3
import subprocess, pathlib, fitz, base64
LOGO_URI = "data:image/png;base64," + base64.b64encode(
    open("/home/user/Bear-Card/assets/logo-badge-transparent.png","rb").read()).decode()
CHROME="/opt/pw-browsers/chromium-1194/chrome-linux/chrome"
GREEN="#2F5A3F"; DGREEN="#1E2E22"; TERRA="#C1683F"; CREAM="#F6F1E3"; SAGE="#7D8F77"
OUT=pathlib.Path("cards_afz_en"); OUT.mkdir(exist_ok=True)
SERIES="ARCHERY FROM ZERO"

STYLE=f"""<style>
@page{{size:1920px 1080px;margin:0;}}
*{{margin:0;padding:0;box-sizing:border-box;-webkit-print-color-adjust:exact;print-color-adjust:exact;}}
html,body{{width:1920px;height:1080px;}}
.card{{width:1920px;height:1080px;position:relative;overflow:hidden;font-family:Georgia,'Times New Roman',serif;}}
.frame{{position:absolute;inset:40px;border:3px solid var(--fr);}}
.kick{{font-family:Arial,sans-serif;font-weight:700;text-transform:uppercase;}}
.serif{{font-family:Georgia,serif;font-weight:900;line-height:1.03;}}
.arrow{{display:flex;align-items:center;}} .arrow .ln{{height:4px;background:{TERRA};}}
.arrow .hd{{width:0;height:0;border-top:11px solid transparent;border-bottom:11px solid transparent;border-left:22px solid {TERRA};}}
.lab{{font-family:Arial,sans-serif;font-weight:700;}}
</style>"""

def badge(light=False,h=150):
    img=f'<img src="{LOGO_URI}" style="height:{h}px;display:block"/>'
    if light: return img
    return (f'<div style="background:{CREAM};border-radius:26px;padding:16px 20px;display:inline-flex;'
            f'box-shadow:0 0 0 3px rgba(193,104,63,.9)">{img}</div>')

def pg(inner): return f"<!doctype html><html><head><meta charset='utf-8'>{STYLE}</head><body>{inner}</body></html>"

def cover():
    return pg(f"""<div class="card" style="--fr:{TERRA};background:{GREEN};color:{CREAM};display:flex;flex-direction:column;align-items:center;justify-content:center;padding-top:150px">
      <div class="frame"></div><div style="position:absolute;top:60px;left:50%;transform:translateX(-50%)">{badge()}</div>
      <div class="kick" style="color:{TERRA};font-size:26px;letter-spacing:9px;margin-bottom:24px">10 Short Lessons</div>
      <div class="serif" style="font-size:150px;text-align:center">ARCHERY<br>FROM ZERO</div>
      <div class="arrow" style="margin:42px 0"><div class="ln" style="width:220px"></div><div class="hd"></div></div>
      <div class="lab" style="font-size:29px;letter-spacing:6px">LEARN TO SHOOT, STEP BY STEP</div>
      <div style="position:absolute;bottom:120px;font-family:Arial;letter-spacing:5px;font-size:22px;color:{TERRA}">NO EXPERIENCE NEEDED &nbsp;&middot;&nbsp; START TODAY</div></div>""")

def title(n,name,fs=110):
    return pg(f"""<div class="card" style="--fr:{TERRA};background:{GREEN};color:{CREAM};display:flex;flex-direction:column;justify-content:center;padding:0 150px">
      <div class="frame"></div><div style="position:absolute;top:58px;left:60px">{badge()}</div>
      <div style="position:absolute;top:104px;right:72px;font-family:Arial;letter-spacing:8px;font-size:21px;color:{TERRA}">{SERIES}</div>
      <div class="kick" style="color:{TERRA};font-size:34px;letter-spacing:8px;margin-bottom:20px">Lesson {n}</div>
      <div class="serif" style="font-size:{fs}px">{name}</div>
      <div class="arrow" style="margin-top:38px"><div class="ln" style="width:260px"></div><div class="hd"></div></div></div>""")

def listcard(kick,heading,items,footer=None,hsize=82):
    rows=""
    for h,d in items:
        rows+=(f'<div style="display:flex;align-items:baseline;gap:22px;margin:19px 0">'
               f'<span style="color:{TERRA};font-size:32px;line-height:1">&#10148;</span>'
               f'<span style="font-size:42px;color:{DGREEN}"><b style="color:{GREEN}">{h}</b>{d}</span></div>')
    foot=(f'<div style="position:absolute;bottom:112px;left:150px;right:150px;font-style:italic;font-size:29px;color:{TERRA}">{footer}</div>') if footer else ""
    return pg(f"""<div class="card" style="--fr:{SAGE};background:{CREAM};color:{DGREEN};padding:104px 150px 0">
      <div class="frame"></div><div style="position:absolute;top:62px;right:72px">{badge(True,h=136)}</div>
      <div class="kick" style="color:{TERRA};font-size:25px;letter-spacing:7px;margin-bottom:12px">{kick}</div>
      <div class="serif" style="font-size:{hsize}px;color:{GREEN};margin-bottom:34px">{heading}</div>
      {rows}{foot}</div>""")

def safety():
    return pg(f"""<div class="card" style="--fr:{TERRA};background:{GREEN};color:{CREAM};display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;padding:150px 220px 0">
      <div class="frame"></div><div style="position:absolute;top:56px;left:50%;transform:translateX(-50%)">{badge()}</div>
      <div class="kick" style="color:{TERRA};font-size:28px;letter-spacing:9px;margin-bottom:26px">Before You Begin</div>
      <div class="serif" style="font-size:82px;margin-bottom:34px">Safety First</div>
      <div style="font-size:40px;line-height:1.5;color:{CREAM}">Always practice in a <b>safe area</b>, with <b>proper equipment</b>, a <b>suitable target</b>, and <b>adult supervision</b> for children. If something feels unsafe, <b>stop</b> and get help from a qualified instructor or archery shop.</div></div>""")

def cycle8():
    steps=[("1","Stance","Sideways"),("2","Grip","Relaxed"),("3","Nock","Same spot"),("4","Draw","Smooth"),
           ("5","Anchor","Same point"),("6","Aim","Look at target"),("7","Release","Let go"),("8","Follow through","Hold still")]
    def col(items):
        r=""
        for n,s,w in items:
            r+=(f'<div style="display:flex;align-items:baseline;gap:20px;margin:16px 0">'
                f'<span style="font-family:Georgia,serif;font-weight:900;font-size:52px;color:{TERRA};min-width:54px">{n}</span>'
                f'<span><b style="font-size:40px;color:{GREEN}">{s}</b><br><span style="font-family:Arial;font-size:26px;color:{SAGE};letter-spacing:1px">{w}</span></span></div>')
        return r
    return pg(f"""<div class="card" style="--fr:{SAGE};background:{CREAM};color:{DGREEN};padding:104px 150px 0">
      <div class="frame"></div><div style="position:absolute;top:62px;right:72px">{badge(True,h=136)}</div>
      <div class="kick" style="color:{TERRA};font-size:25px;letter-spacing:7px;margin-bottom:12px">Lesson 4 &middot; The Whole Process</div>
      <div class="serif" style="font-size:82px;color:{GREEN};margin-bottom:30px">The 8-Step Shot Cycle</div>
      <div style="display:flex;gap:120px"><div style="flex:1">{col(steps[:4])}</div><div style="flex:1">{col(steps[4:])}</div></div>
      <div style="position:absolute;bottom:104px;left:150px;font-style:italic;font-size:28px;color:{TERRA}">Smooth and repeatable is the goal — not speed.</div></div>""")

def closing():
    return pg(f"""<div class="card" style="--fr:{TERRA};background:{GREEN};color:{CREAM};display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;padding:150px 200px 0">
      <div class="frame"></div><div style="position:absolute;top:56px;left:50%;transform:translateX(-50%)">{badge()}</div>
      <div class="kick" style="color:{TERRA};font-size:26px;letter-spacing:8px;margin-bottom:22px">You Did It</div>
      <div class="serif" style="font-size:88px;line-height:1.1">"It doesn't have to be<br>perfect. It has to happen."</div>
      <div class="arrow" style="margin:38px 0"><div class="ln" style="width:200px"></div><div class="hd"></div></div>
      <div class="lab" style="font-size:29px;letter-spacing:2px;margin-bottom:14px">Loved it? Leave a review &#10084;</div>
      <div style="font-family:Arial;font-size:27px;color:{TERRA};letter-spacing:2px">New to bows? Watch <span style="color:{CREAM}">Choose Your Bow</span></div></div>""")

cards={
 "01_cover": cover(),
 "02_safety": safety(),
 "03_l1_title": title(1,"Welcome"),
 "04_l1_content": listcard("Lesson 1 &middot; Start Here","What you need to start",
    [("A bow — ","recurve, Genesis or compound"),("Arrows — ","that match your bow"),
     ("A target — ","with a safe backstop behind it"),("An arm guard — ","and closed shoes")],
    "No experience or athleticism needed — just these 10 short lessons."),
 "05_l2_title": title(2,"Safety First"),
 "06_l2_content": listcard("Lesson 2 &middot; The Rules","The three rules",
    [("Point only at the target — ","never anywhere else"),("Know what's behind it — ","every time"),
     ("Feels unsafe? Stop — ","no exceptions")],
    "Bow down when you're not shooting. Check each arrow for cracks or bends."),
 "07_l3_title": title(3,"Your Practice Space", fs=92),
 "08_l3_content": listcard("Lesson 3 &middot; Set It Up","A safe space in minutes",
    [("Start close — ","10 to 15 yards is plenty"),("Mark a clear shooting line — ","cones, rope or tape"),
     ("Safe backstop — ","behind the target"),("Scan every time — ","left, right, behind")],
    "What's behind the target matters even more than the target."),
 "09_l4_title": title(4,"The 8-Step Cycle", fs=92),
 "10_l4_cycle": cycle8(),
 "11_l5_title": title(5,"Stance & Grip"),
 "12_l5_content": listcard("Lesson 5 &middot; Your Base","Build your base",
    [("Sideways to the target — ","feet shoulder-width"),("Balanced and relaxed — ","don't tense up"),
     ("Don't squeeze the grip — ","let it rest naturally"),("Relaxed hand — ","bow moves the same every time")]),
 "13_l6_title": title(6,"Nock, Draw & Anchor", fs=84),
 "14_l6_content": listcard("Lesson 6 &middot; Every Shot the Same","Bring it back the same way",
    [("Nock at the line — ","only when ready to shoot"),("Draw smooth, not fast — ","bow level to the target"),
     ("Anchor — ","same spot on your face, every time"),("That repeated spot — ","is what makes arrows group")]),
 "15_l7_title": title(7,"Aim & Release"),
 "16_l7_content": listcard("Lesson 7 &middot; Let It Happen","Let the shot happen",
    [("Look at the target — ","stay steady"),("Relax your fingers — ","don't pull the string"),
     ("Follow-through — ","hold one extra second"),("Chase a group — ","not one perfect bullseye")]),
 "17_l8_title": title(8,"Your First Practice", fs=96),
 "18_l8_content": listcard("Lesson 8 &middot; Your Routine","3 arrows at a time",
    [("Shoot 3, then retrieve — ","safely, every time"),("One focus per round — ","stance OR anchor, not both"),
     ("Jot a quick note — ","what felt good, what to adjust"),("15–20 minutes — ","is more than enough")]),
 "19_l9_title": title(9,"Common Mistakes", fs=104),
 "20_l9_content": listcard("Lesson 9 &middot; Fix One Thing","Fix the small things",
    [("Tight grip — ","&rarr; relax it"),("Moving after release — ","&rarr; hold your follow-through"),
     ("Inconsistent anchor — ","&rarr; same spot every time"),("Rushing — ","&rarr; slow the 8-step cycle")],
    "It's almost always ONE small thing — fix one at a time."),
 "21_l10_title": title(10,"Archery With Kids", fs=100),
 "22_l10_content": listcard("Lesson 10 &middot; Family","Fun, calm, and safe",
    [("Adults lead on safety — ","always"),("Adult behind & beside — ","never in front of the bow"),
     ("Arrows down — ","until it's time to shoot"),("Collect together — ","only after the 'all clear'")]),
 "23_closing": closing(),
}

pdfs=[]
for name,markup in cards.items():
    hp=OUT/f"{name}.html"; pdf=OUT/f"{name}.pdf"; png=OUT/f"{name}.png"
    hp.write_text(markup, encoding="utf-8")
    subprocess.run([CHROME,"--headless=new","--no-sandbox","--disable-gpu","--no-pdf-header-footer",
        f"--print-to-pdf={pdf}", hp.resolve().as_uri()], capture_output=True, text=True, timeout=90)
    d=fitz.open(pdf); d[0].get_pixmap(dpi=96).save(png); pdfs.append(pdf); print("ok",name)
merged=fitz.open()
for p in pdfs: merged.insert_pdf(fitz.open(p))
merged.save("ArcheryFromZero_EN_Cards.pdf"); print("MERGED", merged.page_count)
