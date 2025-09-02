from manim import *

# Colors (kept consistent with opening branding)
COLOR_TEXT = "#424040"
COLOR_BACKGROUND = "#7e7979"


class SectionBase:
    """Base class for all sections with common functionality"""
    
    def __init__(self, scene):
        self.scene = scene
    
    def create_text_group(self, title_text, content_texts, title_scale=0.9, content_scale=0.8):
        """Helper method to create a VGroup with title and content"""
        title = Text(title_text, weight=BOLD, color=COLOR_TEXT, font="Calibri").scale(title_scale)
        
        if isinstance(content_texts, str):
            content = Text(content_texts, color=COLOR_TEXT, font="Calibri").scale(content_scale)
        elif isinstance(content_texts, list):
            content = Paragraph(
                *content_texts,
                alignment="center",
                line_spacing=0.3,
            ).scale(content_scale)
            content.set_color(COLOR_TEXT)
        else:
            content = content_texts
        
        group = VGroup(title, content).arrange(DOWN, buff=0.4)
        group.scale_to_fit_width(12)
        return group
    
    def animate_section(self, group, dots, shift_direction=0.3, shift_axis=DOWN, 
                       dots_shift=0.5, run_time=6, fade_direction=DOWN):
        """Common animation pattern for sections"""
        self.scene.play(FadeIn(group, shift=shift_direction * shift_axis))
        self.scene.play(dots.animate.shift(dots_shift * UP), run_time=run_time, rate_func=linear)
        self.scene.play(FadeOut(group))


class AboutMeSection(SectionBase):
    """Section 1: Introduce yourself"""
    
    def show(self, dots):
        title = "About Me"
        content = [
            "Hi, I'm Saifur Rahman.",
            "Background: BSc in Computer Science and Engineering",
            "from North South University"
        ]
        
        # Create title and content separately for better control
        title_obj = Text(title, weight=BOLD, color=COLOR_TEXT, font="Calibri").scale(0.9)
        name_obj = Text("Hi, I'm Saifur Rahman.", font_size=36, color=COLOR_TEXT, font="Calibri")
        background_obj = Paragraph(
            "Background: BSc in Computer Science and Engineering",
            "from North South University",
            alignment="center",
            line_spacing=0.3,
        ).scale(0.8)
        background_obj.set_color(COLOR_TEXT)
        
        group = VGroup(title_obj, name_obj, background_obj).arrange(DOWN, buff=0.4)
        group.scale_to_fit_width(12)
        
        self.animate_section(group, dots, shift_direction=0.3, shift_axis=DOWN, 
                           dots_shift=0.5, run_time=6)


class FunFactSection(SectionBase):
    """Section 2: Fun fact"""
    
    def show(self, dots):
        title = "Fun Fact"
        content = [
            "I love coding, but I also love cooking.",
            "I often cook for myself."
        ]
        
        group = self.create_text_group(title, content, title_scale=0.9, content_scale=0.9)
        self.animate_section(group, dots, shift_direction=0.3, shift_axis=UP, 
                           dots_shift=0.4, run_time=6)


class ExcitementSection(SectionBase):
    """Section 3: Excitement about internship"""
    
    def show(self, dots):
        title = "Why I'm Excited"
        
        # Create individual text objects for better control
        title_obj = Text(title, weight=BOLD, color=COLOR_TEXT, font="Calibri").scale(0.9)
        line1 = Text("Thrilled to learn and contribute at Imran's Lab.", 
                    font_size=34, color=COLOR_TEXT, font="Calibri")
        line2 = Text("Passionate about design, apps, and development.", 
                    font_size=30, color=COLOR_TEXT, font="Calibri")
        line3 = Text("Eager to collaborate and build impactful projects!", 
                    font_size=30, color=COLOR_TEXT, font="Calibri")
        
        group = VGroup(title_obj, line1, line2, line3).arrange(DOWN, buff=0.35)
        group.scale_to_fit_width(12)
        
        self.animate_section(group, dots, shift_direction=0.3, shift_axis=DOWN, 
                           dots_shift=0.6, run_time=8)


class EndCardSection(SectionBase):
    """End card"""
    
    def show(self, dots):
        end_card = Text("Thank you!", weight=BOLD, color=COLOR_TEXT, font="Calibri")
        self.scene.play(FadeIn(end_card))
        self.scene.play(dots.animate.shift(0.2 * UP), run_time=2, rate_func=linear)
        self.scene.play(FadeOut(Group(end_card, dots)))
