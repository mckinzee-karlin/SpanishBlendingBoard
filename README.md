# Letra del día y Tablero de mezcla

Two Spanish tools for Kindergarten reading, plus a page that opens either one from a dropdown.

- Letra del día (`index.html`): for emergent learners. A Spanish "letter of the day" routine for Kindergarten students who are learning letters, built as one web page (`index.html`). It follows an explicit alphabet-knowledge routine: name the letter, say its sound, find it in a sentence, practice its syllables, and write it. Students can respond without speaking (pointing, looking, AAC, keyboard or letter board).

Language of the app: Spanish (es-MX). Teacher documents are in `docs/` in Spanish and English.

## Open the apps
- `letras-y-mezcla.html`: one page with a dropdown ("Emergente: Letra del día" and "Transicional: Tablero de mezcla"). Both apps are embedded unchanged. The Tablero shows Spanish only on this page.
- `index.html`: Letra del día alone.
- `tablero-de-mezcla.html`: Tablero de mezcla alone (letters are placed to build and sound out a word; has a free mode and a scripted mode).

Open any of them in a browser. No server is needed. If GitHub Pages is turned on for this repository, the page is served from the repository's Pages address.

## What is in this repository
- `index.html`: Letra del día (one file, about 10 MB, includes the pictures and sound clips).
- `tablero-de-mezcla.html`: Tablero de mezcla (one file, about 120 KB, includes its sound clips).
- `letras-y-mezcla.html`: the dropdown page that holds both (about 10 MB).
- `source/`: files used to build `index.html`.
  - `template.html`: the app's page, styles and code.
  - `data/`: letters, sentences, syllable words, stroke guides, pictures and sound clips (JSON).
  - `build.py`: builds `../index.html`. Run `python3 build.py` inside `source/`.
  - `build_hub.py` and `hub_template.html`: build `../letras-y-mezcla.html` from `../index.html` and `../tablero-de-mezcla.html`. Run `build.py` first if Letra del día changed.
  - `doc.py`, `doc_en.py`, `deck.py`: build the teacher script (Spanish and English) and the blank sentence-picture deck into `docs/`. They need `python-docx` and `python-pptx`.
- `docs/`: teacher script (Spanish and English), list of pictures for Canva, and the blank sentence deck.

## Accessibility
Checked with scripted tests (axe-core 4.10.2 on 24 states in three themes: no A/AA violations, no 7:1 contrast failures; no horizontal scroll from 320 to 640 px wide; 44 px targets). It has not been tested with screen readers or with students. See `NOTICE.md` for what still needs a specialist.

## License and credits
See `LICENSE.md` and `NOTICE.md`. Short version: Bluebonnet Learning material (Texas Education Agency) is licensed CC BY-NC-SA 4.0, so this adaptation is non-commercial and share-alike. Some pictures and sounds have separate terms listed in `NOTICE.md`.
