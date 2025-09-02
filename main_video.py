from manim import *

# Import your existing scenes
from opening_branding import OpeningBranding
from middle_part import MiddlePart


class FullVideo(Scene):
    def construct(self) -> None:
        # Reuse the construct methods on the same Scene to stitch them
        OpeningBranding.construct(self)
        MiddlePart.construct(self)
        OpeningBranding.construct(self) 