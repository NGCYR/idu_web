from manim import *
import numpy as np


class reflection(ThreeDScene): 
    CONFIG = {
        "x_axis_label": "$x$",
        "y_axis_label": "$y$",
    }
    def construct(self):
        M_y = np.array([
            [-1, 0, 0],
            [0, 1, 0],
            [0, 0, 1]
        ])
        M_x = np.array([
            [1, 0, 0],
            [0, -1, 0],
            [0, 0, 1]
        ])
        M_z = np.array([
            [1, 0, 0],
            [0, 1, 0],
            [0, 0, -1]
        ])
        m_y_label = Matrix([[-1,0,0],[0,1,0],[0,0,1]])
        m_x_label = Matrix([[1,0,0],[0,-1,0],[0,0,1]])
        m_z_label = Matrix([[1,0,0],[0,1,0],[0,0,-1]])
        m_y_label.to_edge()
        m_x_label.to_edge()
        m_z_label.to_edge()
        axes = ThreeDAxes()
        axes.set_color(GRAY)
        axes.add(axes.get_axis_labels())
        self.set_camera_orientation(phi=75 * DEGREES, theta=-45 * DEGREES)
        self.add(axes)
        self.begin_ambient_camera_rotation(rate=0.2)
        cube = Cube(side_length=1, fill_color=GREEN, stroke_width=2, fill_opacity=0.1)
        cone = Cone(resolution = 8)
        cube.set_stroke(GREEN_E)
        text = Tex("Reflection")
        text.to_corner()
        self.add_fixed_in_frame_mobjects(text)
        self.play(Write(text),Create(cone))
        self.wait()
        matrix_anim = ApplyMatrix(M_x, cone)
        self.play(matrix_anim)
        self.play(FadeOut(axes))
        self.add_fixed_in_frame_mobjects(m_x_label)
        self.play(Write(m_x_label))
        self.wait()