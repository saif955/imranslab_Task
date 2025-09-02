from manim import *
from pathlib import Path
import random

BRAND_IMAGE_PATH = Path("assets/branding_image.png")
BRAND_LOGO_SVG_PATH = Path("assets/imranslab_logo.svg")
COLOR_TEXT = "#424040"
COLOR_BACKGROUND = "#7e7979"


class OpeningBranding(Scene):
    def construct(self) -> None:
        self.camera.background_color = COLOR_BACKGROUND
        
        # Subtle animated background dots
        dots = VGroup(
            *[
                Dot(radius=0.03, color=GRAY, fill_opacity=0.12).shift(
                    random.uniform(-6, 6) * RIGHT + random.uniform(-3.5, 3.5) * UP
                )
                for _ in range(60)
            ]
        )
        dots.set_z_index(-5)

        visual = None

        if BRAND_IMAGE_PATH.exists():
            try:
                visual = ImageMobject(str(BRAND_IMAGE_PATH))
                visual.set_height(3.0)
            except Exception:
                visual = None

        if visual is None and BRAND_LOGO_SVG_PATH.exists():
            try:
                visual = SVGMobject(str(BRAND_LOGO_SVG_PATH))
                visual.set_height(3.0)
            except Exception:
                visual = None

        if visual is None:
            visual = Text("Imran's Lab", weight=BOLD)

        # Rectangle around the logo
        rect = SurroundingRectangle(visual, buff=0.2, corner_radius=0.15)
        rect.set_stroke(color=COLOR_TEXT, width=2)
        group_main = Group(visual, rect)

        tagline = Text("We Are Experts In Design, App, and Developments").scale(0.5)
        tagline.set_color(COLOR_TEXT )
        tagline.next_to(group_main, DOWN, buff=0.4)

        self.play(FadeIn(dots, run_time=0.6))
        self.play(FadeIn(group_main, shift=0.2 * DOWN))
        self.play(FadeIn(tagline, shift=0.2 * UP))

        # Between ~2s and ~5s: subtle pulse while background drifts
        self.play(dots.animate.shift(0.2 * UP), group_main.animate.scale(1.05), run_time=1.5, rate_func=linear)
        self.play(dots.animate.shift(0.2 * UP), group_main.animate.scale(1/1.05), run_time=1.5, rate_func=linear)

        # Remaining drift to keep total scene ≈ 10s
        self.play(dots.animate.shift(0.4 * UP), run_time=2.8, rate_func=linear)

        # Pop the logo group, then fade everything out
        self.play(group_main.animate.scale(1.1), run_time=0.6, rate_func=there_and_back)
        self.play(FadeOut(Group(group_main, tagline, dots))) 
        







