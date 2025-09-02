from manim import *

class MyScene(Scene):
    def construct(self):
        rect = Rectangle(width= 4, height= 3, color= RED)
        self.play(Create(rect))
        self.wait(1)
        
        self.play(Create(rect))
        self.wait(1)
        
        
    def create_rect(self):
        rect = Rectangle(width= 4, height= 3, color= RED)
        self.play(Create(rect))
        self.wait(1)
        
