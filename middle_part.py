from manim import *

# Colors (kept consistent with opening branding)
COLOR_TEXT = "#424040"
COLOR_BACKGROUND = "#7e7979"


class MiddlePart(Scene):
    def construct(self) -> None:
        self.camera.background_color = COLOR_BACKGROUND

        # Subtle animated background dots
        dots = VGroup(
            *[
                Dot(radius=0.03, color=WHITE, fill_opacity=0.12).shift(
                    np.random.uniform(-6, 6) * RIGHT + np.random.uniform(-3.5, 3.5) * UP
                )
                for _ in range(80)
            ]
        )
        dots.set_z_index(-5)

        self.play(FadeIn(dots, run_time=0.6))

        # Section 1: Introduce yourself (approx. 12s total)
        title1 = Text("About Me", weight=BOLD, color=COLOR_TEXT, font="Calibri").scale(0.9)
        line1 = Text("Hi, I'm Saifur Rahman.", font_size=36, color=COLOR_TEXT, font="Calibri")
        line2 = Paragraph(
            "Background: BSc in Computer Science and Engineering",
            "from North South University",
            alignment="center",
            line_spacing=0.3,
        ).scale(0.8)
        line2.set_color(COLOR_TEXT)

        group1 = VGroup(title1, line1, line2).arrange(DOWN, buff=0.4)
        group1.scale_to_fit_width(12)
        self.play(FadeIn(group1, shift=0.3 * DOWN))
        self.play(dots.animate.shift(0.5 * UP), run_time=6, rate_func=linear)
        self.play(FadeOut(group1))

        # Section 2: Fun fact (approx. 10s total)
        title2 = Text("Fun Fact", weight=BOLD, color=COLOR_TEXT, font="Calibri").scale(0.9)
        fact = Paragraph(
            "I love coding, but I also love cooking.",
            "I often cook for myself.",
            alignment="center",
            line_spacing=0.3,
        ).scale(0.9)
        fact.set_color(COLOR_TEXT)
        group2 = VGroup(title2, fact).arrange(DOWN, buff=0.4)
        group2.scale_to_fit_width(12)
        self.play(FadeIn(group2, shift=0.3 * UP))
        self.play(dots.animate.shift(0.4 * UP), run_time=6, rate_func=linear)
        self.play(FadeOut(group2))

        # Section 3: Excitement about internship (approx. 14s total)
        title3 = Text("Why I'm Excited", weight=BOLD, color=COLOR_TEXT, font="Calibri").scale(0.9)
        line3a = Text("Thrilled to learn and contribute at Imran's Lab.", font_size=34, color=COLOR_TEXT, font="Calibri")
        line3b = Text("Passionate about design, apps, and development.", font_size=30, color=COLOR_TEXT, font="Calibri")
        line3c = Text("Eager to collaborate and build impactful projects!", font_size=30, color=COLOR_TEXT, font="Calibri")
        group3 = VGroup(title3, line3a, line3b, line3c).arrange(DOWN, buff=0.35)
        group3.scale_to_fit_width(12)
        self.play(FadeIn(group3, shift=0.3 * DOWN))
        self.play(dots.animate.shift(0.6 * UP), run_time=8, rate_func=linear)
        self.play(FadeOut(group3))

        # End card (brief)
        end_card = Text("Thank you!", weight=BOLD, color=COLOR_TEXT, font="Calibri")
        self.play(FadeIn(end_card))
        self.play(dots.animate.shift(0.2 * UP), run_time=2, rate_func=linear)
        self.play(FadeOut(Group(end_card, dots)))
