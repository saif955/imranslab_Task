from manim import *
from sections import AboutMeSection, FunFactSection, ExcitementSection, EndCardSection

# Colors (kept consistent with opening branding)
COLOR_TEXT = "#424040"
COLOR_BACKGROUND = "#7e7979"


class MiddlePart(Scene):
    def construct(self) -> None:
        self.camera.background_color = COLOR_BACKGROUND
        
        # Create and animate background dots
        dots = self.create_background_dots()
        self.play(FadeIn(dots, run_time=0.6))
        
        # Initialize section objects
        about_me = AboutMeSection(self)
        fun_fact = FunFactSection(self)
        excitement = ExcitementSection(self)
        end_card = EndCardSection(self)
        
        # Run each section
        about_me.show(dots)
        fun_fact.show(dots)
        excitement.show(dots)
        end_card.show(dots)
    
    def create_background_dots(self):
        """Create subtle animated background dots"""
        dots = VGroup(
            *[
                Dot(radius=0.03, color=WHITE, fill_opacity=0.12).shift(
                    np.random.uniform(-6, 6) * RIGHT + np.random.uniform(-3.5, 3.5) * UP
                )
                for _ in range(80)
            ]
        )
        dots.set_z_index(-5)
        return dots
