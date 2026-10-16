# Letra del día

A Spanish "letter of the day" routine for Kindergarten students who are learning letters, built as one web page (`index.html`). It follows an explicit alphabet-knowledge routine: name the letter, say its sound, find it in a sentence, practice its syllables, and write it. Students can respond without speaking (pointing, looking, AAC, keyboard or letter board).

Language of the app: Spanish (es-MX). Teacher documents are in `docs/` in Spanish and English.

## Open the app
Open `index.html` in a browser. No server is needed. If GitHub Pages is turned on for this repository, the page is served from the repository's Pages address.

## What is in this repository
- `index.html`: the finished app (one file, about 10 MB, includes the pictures and sound clips).
- `source/`: files used to build `index.html`.
  - `template.html`: the app's page, styles and code.
  - `data/`: letters, sentences, syllable words, stroke guides, pictures and sound clips (JSON).
  - `build.py`: builds `../index.html`. Run `python3 build.py` inside `source/`.
  - `doc.py`, `doc_en.py`, `deck.py`: build the teacher script (Spanish and English) and the blank sentence-picture deck into `docs/`. They need `python-docx` and `python-pptx`.
- `docs/`: teacher script (Spanish and English), list of pictures for Canva, and the blank sentence deck.

## Accessibility
Checked with scripted tests (axe-core 4.10.2 on 24 states in three themes: no A/AA violations, no 7:1 contrast failures; no horizontal scroll from 320 to 640 px wide; 44 px targets). It has not been tested with screen readers or with students. See `NOTICE.md` for what still needs a specialist.

## License and credits
See `LICENSE.md` and `NOTICE.md`. Short version: Bluebonnet Learning material (Texas Education Agency) is licensed CC BY-NC-SA 4.0, so this adaptation is non-commercial and share-alike. Some pictures and sounds have separate terms listed in `NOTICE.md`.
