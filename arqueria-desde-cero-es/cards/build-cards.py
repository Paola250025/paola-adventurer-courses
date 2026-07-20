#!/usr/bin/env python3
import subprocess, pathlib, fitz, base64
LOGO_URI = "data:image/png;base64," + base64.b64encode(
    open("/home/user/Bear-Card/assets/logo-badge-transparent.png","rb").read()).decode()
CHROME="/opt/pw-browsers/chromium-1194/chrome-linux/chrome"
GREEN="#2F5A3F"; DGREEN="#1E2E22"; TERRA="#C1683F"; CREAM="#F6F1E3"; SAGE="#7D8F77"
OUT=pathlib.Path("cards_afz_es"); OUT.mkdir(exist_ok=True)
SERIES="ARQUERÍA DESDE CERO"

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
      <div class="kick" style="color:{TERRA};font-size:26px;letter-spacing:9px;margin-bottom:24px">10 Lecciones Cortas</div>
      <div class="serif" style="font-size:132px;text-align:center">ARQUERÍA<br>DESDE CERO</div>
      <div class="arrow" style="margin:42px 0"><div class="ln" style="width:220px"></div><div class="hd"></div></div>
      <div class="lab" style="font-size:29px;letter-spacing:6px">APRENDE A TIRAR, PASO A PASO</div>
      <div style="position:absolute;bottom:120px;font-family:Arial;letter-spacing:5px;font-size:22px;color:{TERRA}">SIN EXPERIENCIA &nbsp;&middot;&nbsp; EMPIEZA HOY</div></div>""")

def title(n,name,fs=104):
    return pg(f"""<div class="card" style="--fr:{TERRA};background:{GREEN};color:{CREAM};display:flex;flex-direction:column;justify-content:center;padding:0 150px">
      <div class="frame"></div><div style="position:absolute;top:58px;left:60px">{badge()}</div>
      <div style="position:absolute;top:104px;right:72px;font-family:Arial;letter-spacing:6px;font-size:20px;color:{TERRA}">{SERIES}</div>
      <div class="kick" style="color:{TERRA};font-size:34px;letter-spacing:8px;margin-bottom:20px">Lección {n}</div>
      <div class="serif" style="font-size:{fs}px">{name}</div>
      <div class="arrow" style="margin-top:38px"><div class="ln" style="width:260px"></div><div class="hd"></div></div></div>""")

def listcard(kick,heading,items,footer=None,hsize=80):
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
    return pg(f"""<div class="card" style="--fr:{TERRA};background:{GREEN};color:{CREAM};display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;padding:150px 210px 0">
      <div class="frame"></div><div style="position:absolute;top:56px;left:50%;transform:translateX(-50%)">{badge()}</div>
      <div class="kick" style="color:{TERRA};font-size:28px;letter-spacing:9px;margin-bottom:26px">Antes de Empezar</div>
      <div class="serif" style="font-size:82px;margin-bottom:34px">Seguridad Primero</div>
      <div style="font-size:39px;line-height:1.5;color:{CREAM}">El tiro con arco siempre debe practicarse en un <b>área segura</b>, con <b>equipo adecuado</b>, un <b>blanco apropiado</b> y <b>supervisión de un adulto</b> con niños. Si algo se siente inseguro, <b>detente</b> y busca ayuda de un instructor certificado o una tienda de arquería.</div></div>""")

def cycle8():
    steps=[("1","Postura","De lado"),("2","Agarre","Relajado"),("3","Colocar","Mismo lugar"),("4","Tensar","Suave"),
           ("5","Anclar","Mismo punto"),("6","Apuntar","Mira el blanco"),("7","Soltar","Relaja"),("8","Seguimiento","Quédate quieto")]
    def col(items):
        r=""
        for n,s,w in items:
            r+=(f'<div style="display:flex;align-items:baseline;gap:20px;margin:16px 0">'
                f'<span style="font-family:Georgia,serif;font-weight:900;font-size:52px;color:{TERRA};min-width:54px">{n}</span>'
                f'<span><b style="font-size:38px;color:{GREEN}">{s}</b><br><span style="font-family:Arial;font-size:26px;color:{SAGE};letter-spacing:1px">{w}</span></span></div>')
        return r
    return pg(f"""<div class="card" style="--fr:{SAGE};background:{CREAM};color:{DGREEN};padding:104px 150px 0">
      <div class="frame"></div><div style="position:absolute;top:62px;right:72px">{badge(True,h=136)}</div>
      <div class="kick" style="color:{TERRA};font-size:25px;letter-spacing:7px;margin-bottom:12px">Lección 4 &middot; Todo el Proceso</div>
      <div class="serif" style="font-size:80px;color:{GREEN};margin-bottom:30px">El Ciclo de 8 Pasos</div>
      <div style="display:flex;gap:120px"><div style="flex:1">{col(steps[:4])}</div><div style="flex:1">{col(steps[4:])}</div></div>
      <div style="position:absolute;bottom:104px;left:150px;font-style:italic;font-size:28px;color:{TERRA}">Lo suave y repetible es la meta — no la velocidad.</div></div>""")

def closing():
    return pg(f"""<div class="card" style="--fr:{TERRA};background:{GREEN};color:{CREAM};display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;padding:150px 200px 0">
      <div class="frame"></div><div style="position:absolute;top:56px;left:50%;transform:translateX(-50%)">{badge()}</div>
      <div class="kick" style="color:{TERRA};font-size:26px;letter-spacing:8px;margin-bottom:22px">Lo Lograste</div>
      <div class="serif" style="font-size:84px;line-height:1.1">"No tiene que ser perfecto.<br>Tiene que pasar."</div>
      <div class="arrow" style="margin:38px 0"><div class="ln" style="width:200px"></div><div class="hd"></div></div>
      <div class="lab" style="font-size:29px;letter-spacing:2px;margin-bottom:14px">¿Te gustó? Deja una reseña &#10084;</div>
      <div style="font-family:Arial;font-size:27px;color:{TERRA};letter-spacing:2px">¿Nuevo en arcos? Mira <span style="color:{CREAM}">Elige Tu Arco</span></div></div>""")

cards={
 "01_portada": cover(),
 "02_seguridad": safety(),
 "03_l1_titulo": title(1,"Bienvenida"),
 "04_l1_contenido": listcard("Lección 1 &middot; Empieza Aquí","Lo que necesitas para empezar",
    [("Un arco — ","recurvo, Genesis o compuesto"),("Flechas — ","que combinen con tu arco"),
     ("Un blanco — ","con un respaldo seguro detrás"),("Un protector de brazo — ","y zapatos cerrados")],
    "No necesitas experiencia ni ser atlético — solo estas diez lecciones cortas."),
 "05_l2_titulo": title(2,"Seguridad Primero"),
 "06_l2_contenido": listcard("Lección 2 &middot; Las Reglas","Las tres reglas",
    [("Apunta solo al blanco — ","nunca a otro lado"),("Sabe qué hay detrás — ","siempre"),
     ("¿Inseguro? Detente — ","sin excepción")],
    "Arco abajo cuando no disparas. Revisa cada flecha por grietas o dobleces."),
 "07_l3_titulo": title(3,"Tu Espacio de Práctica", fs=84),
 "08_l3_contenido": listcard("Lección 3 &middot; Prepáralo","Un espacio seguro en minutos",
    [("Empieza cerca — ","10 a 15 yardas es suficiente"),("Marca la línea de tiro — ","conos, cuerda o cinta"),
     ("Respaldo seguro — ","detrás del blanco"),("Escanea siempre — ","izquierda, derecha, detrás")],
    "Lo que hay detrás del blanco importa aún más que el blanco."),
 "09_l4_titulo": title(4,"El Ciclo de 8 Pasos", fs=80),
 "10_l4_ciclo": cycle8(),
 "11_l5_titulo": title(5,"Postura y Agarre"),
 "12_l5_contenido": listcard("Lección 5 &middot; Tu Base","Construye tu base",
    [("De lado al blanco — ","pies al ancho de hombros"),("Balanceado y relajado — ","sin tensarte"),
     ("No aprietes el agarre — ","déjalo reposar"),("Mano relajada — ","el arco se mueve igual cada vez")]),
 "13_l6_titulo": title(6,"Coloca, Tensa y Ancla", fs=76),
 "14_l6_contenido": listcard("Lección 6 &middot; Igual Cada Vez","Llévala atrás igual cada vez",
    [("Coloca en la línea — ","solo cuando estés listo"),("Tensa suave, no rápido — ","nivelado al blanco"),
     ("Ancla — ","mismo punto en tu cara, cada vez"),("Ese punto repetido — ","hace que las flechas agrupen")]),
 "15_l7_titulo": title(7,"Apunta y Suelta"),
 "16_l7_contenido": listcard("Lección 7 &middot; Deja Que Pase","Deja que el tiro pase",
    [("Mira el blanco — ","mantente firme"),("Relaja los dedos — ","no jales la cuerda"),
     ("Seguimiento — ","quédate quieto un segundo más"),("Busca un grupo — ","no un centro perfecto")]),
 "17_l8_titulo": title(8,"Tu Primera Práctica", fs=88),
 "18_l8_contenido": listcard("Lección 8 &middot; Tu Rutina","3 flechas a la vez",
    [("Dispara 3, recoge seguro — ","siempre"),("Un enfoque por ronda — ","postura O anclaje, no ambos"),
     ("Anota una nota rápida — ","qué se sintió bien, qué ajustar"),("15–20 minutos — ","es más que suficiente")]),
 "19_l9_titulo": title(9,"Errores Comunes", fs=100),
 "20_l9_contenido": listcard("Lección 9 &middot; Corrige Uno","Corrige lo pequeño",
    [("Agarre apretado — ","&rarr; relájalo"),("Moverte al soltar — ","&rarr; mantén el seguimiento"),
     ("Anclaje inconsistente — ","&rarr; mismo punto siempre"),("Apurar — ","&rarr; haz el ciclo despacio")],
    "Casi siempre es UNA cosa pequeña — corrige una a la vez."),
 "21_l10_titulo": title(10,"Tiro en Familia", fs=100),
 "22_l10_contenido": listcard("Lección 10 &middot; Familia","Diversión, calma y seguridad",
    [("Los adultos lideran — ","la seguridad, siempre"),("Adulto detrás y al lado — ","nunca frente al arco"),
     ("Flechas abajo — ","hasta el momento de disparar"),("Recojan juntos — ","solo tras la señal de 'despejado'")]),
 "23_cierre": closing(),
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
merged.save("ArqueriaDesdeCero_ES_Cards.pdf"); print("MERGED", merged.page_count)
