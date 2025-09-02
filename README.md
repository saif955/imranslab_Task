# Imran's Lab Manim Video

This project contains three Manim scenes to create a simple intro video:

- Opening branding (logo + tagline)
- Middle content (intro, fun fact, why excited)
- Full video that stitches opening → middle → opening

## Prerequisites

- Python 3.10+
- Manim Community (tested on v0.19.x)

Install dependencies (recommended in a virtual environment):

```bash
# create and activate a virtual environment (optional but recommended)
python -m venv venv
# Windows PowerShell
./venv/Scripts/Activate.ps1
# macOS/Linux
# source venv/bin/activate

# install dependencies
pip install -r requirements.txt
```

If you plan to render SVG logos, also place your SVG in `assets/imranslab_logo.svg`.

## Assets

- Logo image (preferred): `assets/branding_image.png` (PNG/JPG)
- Optional SVG fallback: `assets/imranslab_logo.svg`

Tagline and colors are defined in `opening_branding.py`.

## Render Individual Scenes

- Opening branding only:

```bash
manim -pql opening_branding.py OpeningBranding
```

- Middle content only:

```bash
manim -pql middle_part.py MiddlePart
```

Use `-pqh` for high quality; omit `-p` to skip preview.

## Render Full Combined Video

This runs opening → middle → opening again:

```bash
manim -pql main_video.py FullVideo
```

Output videos are written to `media/videos/...`.

## Customization

- Opening branding

  - Logo image: add/replace `assets/branding_image.png`
  - Optional SVG: `assets/imranslab_logo.svg`
  - Tagline text: edit the `Text("We Are Experts In Design, App, and Developments")` line
  - Colors: edit `COLOR_TEXT` and `COLOR_BACKGROUND`

- Middle content

  - Replace placeholder lines with your own text in `middle_part.py`
  - Colors/background: `COLOR_TEXT`, `COLOR_BACKGROUND`
  - Background animation: animated dots drift subtly; timing tied to section durations

- Full video
  - Sequence is defined in `main_video.py` by calling the two scene `construct` methods in order

## Notes

- If you change fonts, ensure they are installed on your system (e.g., Calibri). Manim will fall back if unavailable.
- Quick preview quality: `-pql`; high quality: `-pqh`.
- Windows PowerShell examples are the same as above commands.
