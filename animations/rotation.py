from manim import *
import numpy as np

class Roataion(ThreeDScene):
    CONFIG = {
        "x_axis_label": "$x$",
        "y_axis_label": "$y$",
    }
    def construct(self):
        M_matrix = MathTex(r"\begin{bmatrix}1&0&0\\ 0&\cos x&-\sin x\\ 0&\sin x&\cos x\end{bmatrix}").scale(0.7)
        M_matrix.to_edge()
        axes = ThreeDAxes()
        axes.set_color(GRAY)
        axes.add(axes.get_axis_labels())
        self.set_camera_orientation(phi=75 * DEGREES, theta=-45 * DEGREES)
        self.add(axes)
        self.begin_ambient_camera_rotation(rate=0.2)
        cube = Cube(side_length=1, fill_color=BLUE, stroke_width=2, fill_opacity=0.1)
        cube.set_stroke(BLUE_E)
        text = Tex("Rotation")
        text.to_corner()
        self.add_fixed_in_frame_mobjects(text)
        self.play(Create(cube),Write(text))
        self.wait()
        self.play(FadeOut(axes))
        self.play(Rotate(cube,angle = PI/3,about_edge = Y_AXIS))
        self.add_fixed_in_frame_mobjects(M_matrix)
        self.play(Write(M_matrix))
        self.wait()