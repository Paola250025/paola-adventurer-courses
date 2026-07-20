# Paola Adventurer — Bilingual Archery Presentations · STATUS

_Last saved: 2026-07-19. Two of four deliverable sets complete._

## The goal
Recording decks + scripts for 2 courses, each in EN and ES (4 sets total):
1. **Choose Your Bow / Elige Tu Arco** — 5-episode mini-series (20 cards)
2. **Archery From Zero / Arquería Desde Cero** — 10 lessons

Each set = **two pieces**:
- **Cards PDF/PNGs** = the on-screen presentation (what students see).
- **Script PDF** = word-for-word talking lines + b-roll cues (Paola's private recording notes).
Paola records with **Loom (Screen + Cam)**: show the Cards PDF fullscreen, read from the Script PDF
on her phone, and show the real bow to camera at b-roll cues. NO Canva needed.

## Brand & logo
- Forest green `#2F5A3F` · Terracotta `#C1683F` · Warm cream `#F6F1E3` · off-white `#FAF9F5` · text `#1E2E22`
- REAL logo: `assets/logo-badge-transparent.png` — embedded on every card. (This is the source of truth.)

## HOW THE CARDS ARE BUILT (important — NOT Canva)
Canva's AI generator was abandoned (it forced red, stock photos, reworded copy, ignored the logo,
and its API can't recolor shapes/add boxes/place the logo). We now render cards ourselves:
HTML -> Chromium print-to-PDF -> PNG, full brand control. Build scripts are committed and re-runnable:
- `presentations/choose-your-bow-en/cards/build-cards.py`
- `presentations/elige-tu-arco-es/cards/build-cards.py`
- `presentations/render_script.py`  (markdown script -> branded PDF; usage: `python3 render_script.py in.md out.pdf`)
Chromium path in scripts: /opt/pw-browsers/chromium-1194/chrome-linux/chrome

## STATUS OF THE 4 SETS
| Set | Cards | Script |
|---|---|---|
| 1. Choose Your Bow (EN) | ✅ done | ✅ done |
| 2. Elige Tu Arco (ES) | ✅ done | ✅ done |
| 3. Archery From Zero (EN) | ✅ done (23 cards) | ✅ done |
| 4. Arquería Desde Cero (ES) | ✅ done (23 cards) | ✅ done |

**🎉 ALL 4 SETS COMPLETE.** Each set = Cards PDF + PNG pack + recording Script PDF, in brand colors with the real logo. Folders: `choose-your-bow-en/`, `elige-tu-arco-es/`, `archery-from-zero-en/`, `arqueria-desde-cero-es/`. Remaining polish (optional): Paola pastes her real course link into each CTA/closing card where noted.

_Note: in THIS repo files live at the repo root (e.g. `archery-from-zero-en/`), not under `presentations/`._
_AFZ EN = 23 cards (cover, safety, title+content per lesson, 8-step infographic, closing). Build: `archery-from-zero-en/cards/build-cards.py`. Next: translate to Spanish → `arqueria-desde-cero-es/`._

### Delivered files (all in repo + sent in chat)
- `presentations/choose-your-bow-en/cards/` — ChooseYourBow_EN_Cards.pdf + 20 PNGs
- `presentations/choose-your-bow-en/ChooseYourBow_EN_Script.pdf` (+ .md source)
- `presentations/elige-tu-arco-es/cards/` — EligeTuArco_ES_Cards.pdf + 20 PNGs
- `presentations/elige-tu-arco-es/EligeTuArco_ES_Script.pdf` (+ .md source)

## CARD STRUCTURE (20 cards, both languages)
1 Cover · 2 Ep1 title · 3 Facts · 4 Meet the 3 bows · 5 Ep2 title · 6 Recurve history ·
7 Recurve parts · 8 Recurve who-for · 9 Ep3 title · 10 Genesis history · 11 Genesis parts ·
12 Genesis who-for · 13 Ep4 title · 14 Compound history · 15 Compound parts · 16 Compound who-for ·
17 Ep5 title · 18 4-question framework · 19 Reference table · 20 CTA
- CTA drives to the course (EN: "Get Archery From Zero"; ES: "Consigue Arquería Desde Cero").
  Paola must paste her real course link where it says [add your course link] / [link de tu curso].
- NO in-person classes (removed per Paola).

## NEXT STEPS (set 3 & 4)
1. **Archery From Zero (EN)** — build cards from the 10-lesson guide (source: `presentations/source-guides/ARQUERIA_CERO.txt`, English scripts in Part 6) + script PDF.
   - Note: this course is 10 lessons (safety, space, 8-step cycle, stance/grip, nock/draw/anchor, aim/release, first practice, mistakes, family). It has its own Canva-graphics list + word-for-word scripts in the guide. Decide card count with Paola (likely ~1 title + 1-2 content cards per lesson).
2. **Arquería Desde Cero (ES)** — Spanish version of set 3.
3. Reuse build-cards.py as the template; keep same brand + logo + CTA pattern.

## SOURCE MATERIAL
- `presentations/source-guides/ELIGE_ARCO.txt` — Choose Your Bow guide (EN+ES, 5 episodes)
- `presentations/source-guides/ARQUERIA_CERO.txt` — Archery From Zero guide (EN+ES, 10 lessons)
