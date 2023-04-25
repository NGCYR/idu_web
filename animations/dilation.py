from manim import *
import numpy as np
import os

def dilation_anim(render,user_x_factor,user_y_factor,user_z_factor):
    if render == True:
        class Dilation(ThreeDScene):
            CONFIG = {
                "x_axis_label": "$x$",
                "y_axis_label": "$y$",
            }
            def construct(self):
                M = np.array([
                    [float(user_x_factor), 0, 0],
                    [0, float(user_y_factor), 0],
                    [0, 0, float(user_z_factor)]
                ])
                M_matrix = Matrix([[int(user_x_factor),  0,  0],[0,int(user_y_factor),0],[0,0,int(user_z_factor)]]).scale(0.7)
                M2_matrix = MathTex(r"\begin{bmatrix}1&0&0\\ 0&\cos x&-\sin x\\ 0&\sin x&\cos x\end{bmatrix}").scale(0.7)
                M_matrix.to_edge()
                M2_matrix.to_edge()
                axes = ThreeDAxes()
                axes.set_color(GRAY)
                axes.add(axes.get_axis_labels())
                self.set_camera_orientation(phi=75 * DEGREES, theta=-45 * DEGREES)
                self.add(axes)
                self.begin_ambient_camera_rotation(rate=0.2)
                cube = Cube(side_length=1, fill_color=BLUE, stroke_width=2, fill_opacity=0.1)
                cube.set_stroke(BLUE_E)
                text = Tex("Dilation")
                text.to_corner()
                self.add_fixed_in_frame_mobjects(text)
                self.play(Create(cube),Write(text))
                self.wait()
                matrix_anim = ApplyMatrix(M, cube)
                self.play(matrix_anim)
                self.play(FadeOut(axes))
                self.add_fixed_in_frame_mobjects(M_matrix)
                self.play(Write(M_matrix))
                self.wait(3)
        # os.chdir('/Users/Ralph/Desktop/Code/python/idu_web/animations')
        # path = os.getcwd()
        # print(path)
        # os.system("manim -pqh dilation.py Dilation")
        scene = Dilation()
        scene.render()
        return 1