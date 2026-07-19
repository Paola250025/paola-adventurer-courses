#!/usr/bin/env python3
import subprocess, pathlib, fitz, base64
LOGO_URI = "data:image/png;base64," + base64.b64encode(
    open("/home/user/Bear-Card/assets/logo-badge-transparent.png","rb").read()).decode()

CHROME="/opt/pw-browsers/chromium-1194/chrome-linux/chrome"
GREEN="#2F5A3F"; DGREEN="#1E2E22"; TERRA="#C1683F"; CREAM="#F6F1E3"; SAGE="#7D8F77"
OUT=pathlib.Path("cards_es"); OUT.mkdir(exist_ok=True)
SERIES="ELIGE TU ARCO"

STYLE=f"""<style>
@page{{size:1920px 1080px;margin:0;}}
*{{margin:0;padding:0;box-sizing:border-box;-webkit-print-color-adjust:exact;print-color-adjust:exact;}}
html,body{{width:1920px;height:1080px;}}
.card{{width:1920px;height:1080px;position:relative;overflow:hidden;font-family:Georgia,'Times New Roman',serif;}}
.frame{{position:absolute;inset:40px;border:3px solid var(--fr);}}
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

def badge(light=False, h=150):
    img=f'<img src="{LOGO_URI}" style="height:{h}px;display:block"/>'
    if light: return img
    return (f'<div style="background:{CREAM};border-radius:26px;padding:16px 20px;display:inline-flex;'
            f'box-shadow:0 0 0 3px rgba(193,104,63,.9)">{img}</div>')

def pg(inner): return f"<!doctype html><html><head><meta charset='utf-8'>{STYLE}</head><body>{inner}</body></html>"

def cover():
    return pg(f"""<div class="card" style="--fr:{TERRA};background:{GREEN};color:{CREAM};display:flex;flex-direction:column;align-items:center;justify-content:center;padding-top:150px">
      <div class="frame"></div><div style="position:absolute;top:60px;left:50%;transform:translateX(-50%)">{badge()}</div>
      <div class="kick" style="color:{TERRA};font-size:26px;letter-spacing:9px;margin-bottom:24px">Una Miniserie de 5 Partes</div>
      <div class="serif" style="font-size:150px;text-align:center">ELIGE<br>TU ARCO</div>
      <div class="arrow" style="margin:42px 0"><div class="ln" style="width:220px"></div><div class="hd"></div></div>
      <div class="lab" style="font-size:29px;letter-spacing:6px">ENCUENTRA EL ARCO IDEAL PARA TI</div>
      <div style="position:absolute;bottom:120px;font-family:Arial;letter-spacing:8px;font-size:22px;color:{TERRA}">RECURVO &nbsp;&middot;&nbsp; GENESIS &nbsp;&middot;&nbsp; COMPUESTO</div></div>""")

def title(ep,name,fs=120):
    return pg(f"""<div class="card" style="--fr:{TERRA};background:{GREEN};color:{CREAM};display:flex;flex-direction:column;justify-content:center;padding:0 150px">
      <div class="frame"></div><div style="position:absolute;top:58px;left:60px">{badge()}</div>
      <div style="position:absolute;top:104px;right:72px;font-family:Arial;letter-spacing:8px;font-size:21px;color:{TERRA}">{SERIES}</div>
      <div class="kick" style="color:{TERRA};font-size:34px;letter-spacing:8px;margin-bottom:20px">Episodio {ep}</div>
      <div class="serif" style="font-size:{fs}px">{name}</div>
      <div class="arrow" style="margin-top:38px"><div class="ln" style="width:260px"></div><div class="hd"></div></div></div>""")

def listcard(kick,heading,items,footer=None,hsize=86):
    rows=""
    for h,d in items:
        rows+=(f'<div style="display:flex;align-items:baseline;gap:22px;margin:20px 0">'
               f'<span style="color:{TERRA};font-size:32px;line-height:1">&#10148;</span>'
               f'<span style="font-size:43px;color:{DGREEN}"><b style="color:{GREEN}">{h}</b>{d}</span></div>')
    foot=(f'<div style="position:absolute;bottom:116px;left:150px;right:150px;font-style:italic;font-size:29px;color:{TERRA}">{footer}</div>') if footer else ""
    return pg(f"""<div class="card" style="--fr:{SAGE};background:{CREAM};color:{DGREEN};padding:108px 150px 0">
      <div class="frame"></div><div style="position:absolute;top:66px;right:72px">{badge(True, h=140)}</div>
      <div class="kick" style="color:{TERRA};font-size:25px;letter-spacing:7px;margin-bottom:12px">{kick}</div>
      <div class="serif" style="font-size:{hsize}px;color:{GREEN};margin-bottom:38px">{heading}</div>
      {rows}{foot}</div>""")

def table():
    rows=[("Recurvo","Técnico, olímpico","Bajo–medio (crece)","Espacio para forma"),
          ("Genesis","Probar, familias","El más bajo","El más fácil de guardar"),
          ("Compuesto","Caza, competencia","El más alto","Requiere ajuste")]
    body="".join(f"<tr><td>{a}</td><td>{b}</td><td>{c}</td><td>{d}</td></tr>" for a,b,c,d in rows)
    return pg(f"""<div class="card" style="--fr:{SAGE};background:{CREAM};color:{DGREEN};padding:108px 150px 0">
      <div class="frame"></div><div style="position:absolute;top:66px;right:72px">{badge(True, h=140)}</div>
      <div class="kick" style="color:{TERRA};font-size:25px;letter-spacing:7px;margin-bottom:12px">Episodio 5 &middot; De Un Vistazo</div>
      <div class="serif" style="font-size:82px;color:{GREEN};margin-bottom:40px">Referencia rápida</div>
      <table><thead><tr><th>Arco</th><th>Meta</th><th>Presupuesto</th><th>Espacio</th></tr></thead><tbody>{body}</tbody></table>
      <div style="position:absolute;bottom:104px;left:150px;font-style:italic;font-size:27px;color:{TERRA}">Pausa aquí cuando quieras — es tu chuleta.</div></div>""")

def cta():
    return pg(f"""<div class="card" style="--fr:{TERRA};background:{GREEN};color:{CREAM};display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;padding:140px 160px 0">
      <div class="frame"></div><div style="position:absolute;top:58px;left:50%;transform:translateX(-50%)">{badge()}</div>
      <div class="kick" style="color:{TERRA};font-size:26px;letter-spacing:8px;margin-bottom:22px">Tu Siguiente Paso</div>
      <div class="serif" style="font-size:116px">¿Cuál es<br>TU arco?</div>
      <div class="arrow" style="margin:40px 0"><div class="ln" style="width:200px"></div><div class="hd"></div></div>
      <div class="lab" style="font-size:30px;letter-spacing:3px;margin-bottom:26px">Comenta cuál va contigo</div>
      <div class="lab" style="font-size:26px;letter-spacing:3px;color:{CREAM};opacity:.85;margin-bottom:12px">¿LISTO PARA EMPEZAR A TIRAR?</div>
      <div style="font-family:Georgia,serif;font-weight:900;font-size:44px;color:{TERRA}">Consigue <span style="color:{CREAM}">Arquería Desde Cero</span></div>
      <div style="font-family:Arial;font-size:26px;color:{TERRA};letter-spacing:2px;margin-top:14px">&rarr; [ agrega el link de tu curso ]</div></div>""")

cards = {
 "01_portada": cover(),
 "02_ep1_titulo": title(1,"Bienvenida a la Arquería", fs=104),
 "03_datos": listcard("Episodio 1 &middot; Un Poco de Historia","Más antigua de lo que crees",
    [("64,000 años — ","las puntas de flecha más antiguas encontradas"),
     ("8,000 años — ","el arco completo más antiguo, de un pantano danés"),
     ("3&times; más segura — ","que el golf, según estudios"),
     ("Bután — ","el único país donde es deporte nacional")]),
 "04_los3": listcard("Episodio 1 &middot; Los Tres","Conoce los tres arcos",
    [("RECURVO — ","el clásico de los Juegos Olímpicos"),
     ("GENESIS — ","el que usan las escuelas de EE.UU. desde cero"),
     ("COMPUESTO — ","el de poleas, para caza y precisión")]),
 "05_ep2_titulo": title(2,"El Arco Recurvo"),
 "06_recurvo_historia": listcard("Episodio 2 &middot; Recurvo","De los mongoles a los Juegos Olímpicos",
    [("~1600 a.C. — ","ya existía el diseño recurvo"),
     ("Los mongoles — ","recurvos potentes disparados a caballo"),
     ("Desde 1972 — ","por décadas, el único arco olímpico")], hsize=72),
 "07_recurvo_partes": listcard("Episodio 2 &middot; Las Partes","Simple, cuatro piezas",
    [("RISER — ","la empuñadura; tiene la ventana de mira"),
     ("VARILLAS — ","el motor; se doblan y guardan la energía"),
     ("CUERDA — ","conecta las puntas y lanza la flecha"),
     ("REPOSAFLECHAS — ","donde se apoya la flecha antes del tiro")],
    "Tip: en los arcos 'takedown' cambias solo las varillas al mejorar."),
 "08_recurvo_paraquien": listcard("Episodio 2 &middot; Recurvo","¿Para quién es?",
    [("Reto clásico — ","le atrae lo técnico y olímpico"),
     ("Buena técnica — ","dispuesto a invertir tiempo en la forma"),
     ("Crece contigo — ","cambias varillas, no todo el arco")]),
 "09_ep3_titulo": title(3,"El Arco Genesis"),
 "10_genesis_historia": listcard("Episodio 3 &middot; Genesis","Creado para las escuelas de EE.UU.",
    [("NASP, 2002 — ","nació en Kentucky con el Depto. de Educación"),
     ("10,000 escuelas — ","4M+ estudiantes, 47 estados, 5 países"),
     ("Un solo diseño — ","le queda a toda una clase distinta")]),
 "11_genesis_partes": listcard("Episodio 3 &middot; Las Partes","Cómo funciona",
    [("UNA POLEA — ","disparo más suave, menos ruido y retroceso"),
     ("RUEDA GUÍA — ","guía la cuerda, casi sin mantenimiento"),
     ("SIN LONGITUD FIJA — ","el mismo arco le queda a cualquiera"),
     ("10–20 lb — ","peso ajustable, pero se siente real")]),
 "12_genesis_paraquien": listcard("Episodio 3 &middot; Genesis","¿Para quién es?",
    [("Para probar — ","sin un gran compromiso inicial"),
     ("Familias y niños — ","y grupos"),
     ("Menor costo — ","y el menor mantenimiento")]),
 "13_ep4_titulo": title(4,"El Arco Compuesto"),
 "14_compuesto_historia": listcard("Episodio 4 &middot; Compuesto","Una sierra, un recurvo y poleas de avión",
    [("1966 — ","Holless Wilbur Allen lo inventa en Missouri"),
     ("La idea — ","llegar al venado antes de que se mueva"),
     ("Patente 1969 — ","nace la industria del arco compuesto")], hsize=64),
 "15_compuesto_partes": listcard("Episodio 4 &middot; Las Partes","La ventaja mecánica",
    [("POLEAS (CAMS) — ","dos ruedas que dan la ventaja mecánica"),
     ("CABLES — ","trabajan junto con las poleas"),
     ("LET-OFF — ","sostienes ~10 lb en un arco de 70 lb"),
     ("RELEASE + PEEP — ","gatillo y anillo de mira, más consistencia")]),
 "16_compuesto_paraquien": listcard("Episodio 4 &middot; Compuesto","¿Para quién es?",
    [("Caza y competencia — ","tiradores de precisión"),
     ("Le gusta la técnica — ","el lado mecánico del equipo"),
     ("Invierte más — ","por velocidad y precisión, con menos esfuerzo")]),
 "17_ep5_titulo": title(5,"¿Cuál Es Tu Arco?"),
 "18_marco": listcard("Episodio 5 &middot; Decide","Cuatro preguntas rápidas",
    [("1&nbsp;&nbsp;META — ","¿solo probar, sueño olímpico o caza?"),
     ("2&nbsp;&nbsp;PRESUPUESTO — ","¿cuánto quieres invertir al inicio?"),
     ("3&nbsp;&nbsp;QUÉ TAN SEGUIDO — ","¿ocasional, un hobby o en serio?"),
     ("4&nbsp;&nbsp;ESPACIO — ","¿rango, espacio para la forma, guardado?")]),
 "19_tabla": table(),
 "20_cta": cta(),
}

pdfs=[]
for name, markup in cards.items():
    hp=OUT/f"{name}.html"; pdf=OUT/f"{name}.pdf"; png=OUT/f"{name}.png"
    hp.write_text(markup, encoding="utf-8")
    subprocess.run([CHROME,"--headless=new","--no-sandbox","--disable-gpu","--no-pdf-header-footer",
        f"--print-to-pdf={pdf}", hp.resolve().as_uri()], capture_output=True, text=True, timeout=90)
    d=fitz.open(pdf); d[0].get_pixmap(dpi=96).save(png); pdfs.append(pdf)
    print("ok", name)

merged=fitz.open()
for p in pdfs: merged.insert_pdf(fitz.open(p))
merged.save("EligeTuArco_ES_Cards.pdf")
print("MERGED", merged.page_count)
