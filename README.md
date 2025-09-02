# imranslabTask

A minimal workspace containing a Python example script and sample media assets (images, texts, and videos). Use this repo as a starting point for experimenting with media processing or scripting tasks.

## Requirements

- Python 3.9+ (recommended)
- Windows PowerShell (instructions below use PowerShell)

## Quick Start (Windows PowerShell)

```powershell
# From the project root
cd C:\Users\saif\imranslabTask

# (Optional) Create & activate a virtual environment
python -m venv venv
.\venv\Scripts\Activate.ps1

# (Optional) Install dependencies if you add a requirements file later
# pip install -r requirements.txt

# Run the example script
python .\example.py
```

## Using Manim

Manim renders mathematical animations and saves outputs under `media/`.

### Install

```powershell
# Inside your (optional) virtual environment
pip install manim
```

### Render a scene

```powershell
# Render a Scene class from a Python file
# -p: preview after render, -ql: low quality (fast), -pqh: high quality with preview
manim -p -ql .\example.py SceneName

# For higher quality
manim -pqh .\example.py SceneName
```

- Outputs will appear in `media/videos/` (MP4s) and `media/images/` (stills) with resolution-specific subfolders.
- Manim also creates `media/texts/`, `media/Tex/`, and `partial_movie_files/` while rendering.

## Project Structure

```
imranslabTask/
  ├─ example.py                   # Sample Python script
  ├─ media/
  │  ├─ images/
  │  │  └─ example/
  │  ├─ texts/
  │  │  └─ a9c85f761c428e91.svg   # Sample text-based SVG asset
  │  └─ videos/
  │     └─ example/
  │        └─ 480p15/
  │           ├─ MyScene.mp4
  │           ├─ SquareToCircle.mp4
  │           └─ partial_movie_files/
  │              ├─ MyScene/              # Chunked/temporary parts for MyScene
  │              └─ SquareToCircle/       # Chunked/temporary parts for SquareToCircle
  └─ venv/                       # (Optional) Python virtual environment
```

## Notes

- The `media/videos/example/480p15/partial_movie_files/` folders contain temporary/partial files often created by video processing tools; they can be re-generated and are typically safe to ignore in version control.
- If `example.py` requires third‑party libraries, add a `requirements.txt` and install via `pip install -r requirements.txt`.
- On PowerShell, you may need to allow script execution for activating virtual environments:

```powershell
Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
```

Revert or tighten this policy after setup as needed.
