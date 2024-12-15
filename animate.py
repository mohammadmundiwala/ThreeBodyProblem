
from manimlib import *
import numpy as np

class CR3BPAnimation(Scene):
    def construct(self):
        # Load trajectory data
        x = np.load('x_periodic.npy')
        y = np.load('y_periodic.npy')
        
        # Create Earth and Moon
        earth = Circle(radius=0.3, color='#A3C1DA').shift(LEFT * 3)
        moon = Circle(radius=0.1, color='#4B4B4B').shift(RIGHT * 3)
        self.add(earth, moon)
        
        # Create trajectory path
        trajectory = VMobject(color='#FF7F50')
        trajectory.set_points_as_corners([earth.get_center()] + 
            [LEFT * 3 + np.array([xi, yi, 0]) for xi, yi in zip(x, y)])
        self.add(trajectory)
        
        # Create moving dot
        dot = Dot(color=GOLD).move_to(trajectory.get_start())
        arrow = Arrow(start=trajectory.get_end() - UP*0.05, end=trajectory.get_end(), color=RED)



        self.add(dot)
        
        # Animate the dot along the path
        self.play(MoveAlongPath(dot, trajectory), run_time=10, rate_func=linear)
