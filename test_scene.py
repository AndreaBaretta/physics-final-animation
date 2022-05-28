from manim import *
import numpy as np


class SquareToCircle(Scene):
    def construct(self):
        circle = Circle()  # create a circle
        circle.set_fill(PINK, opacity=0.5)  # set color and transparency

        square = Square()  # create a square
        square.rotate(PI / 4)  # rotate a certain amount

        self.play(Create(square))  # animate the creation of the square
        # interpolate the square into the circle
        self.play(Transform(square, circle))
        self.play(FadeOut(square))  # fade out animation


class Minkowski(Scene):
    def construct(self):

        # ---- MINKOWSKI DIAGRAM - STEVE'S PERSPECTIVE

        title = Title(
            # spaces between braces to prevent SyntaxError
            r"Minkowski Diagram of Twin Paradox",
            include_underline=False,
            font_size=40,
        )

        steveFrame = Axes(
            x_range=[0, 15, 1],
            y_range=[0, 15, 1],
            # x_length=5,
            # y_length=5,
            tips=False,
            axis_config={"stroke_color": WHITE},
            x_axis_config={"include_ticks": False, "include_numbers": False},
            y_axis_config={"include_ticks": True, "include_numbers": True},
        )

        y_label_steve = steveFrame.get_y_axis_label(
            r"t", edge=LEFT, direction=LEFT, buff=0.4)
        x_label_steve = steveFrame.get_x_axis_label(
            r"x", edge=DOWN, direction=DOWN)

        ryanGraphSteveFrame = steveFrame.plot(lambda x: x,
                        x_range=[0, 15], use_smoothing=True, color=RED)

        ryanLabelSteveFrame = steveFrame.get_graph_label(
            ryanGraphSteveFrame, Tex("Ryan's Path", font_size=35), x_val=15, direction=UR)

        steveGraphSteveFrame = steveFrame.get_vertical_line(
            steveFrame.c2p(0, 15, 0), color=BLUE, line_func=Line, stroke_width=4)

        steveLabelSteveFrame = steveFrame.get_graph_label(
            ryanGraphSteveFrame, Tex("Steve's Path", font_size=35), x_val=0, direction=DOWN, color=BLUE
        )

        raysSteveFrame = []
        horizontalLinesSteveFrame = []
        for i in range(1, 7):
            m = 2
            raysSteveFrame.append(steveFrame.plot(
                lambda x: i + x/m, x_range=[0, i/(1-1/m)], use_smoothing=True, color=WHITE))
            horizontalLinesSteveFrame.append(DashedVMobject(steveFrame.plot(lambda x: i/(1-1/m), x_range=[0, i/(
                1-1/m)], use_smoothing=True, color=ORANGE), num_dashes=int(2 * i/(1-1/m)), equal_lengths=False))

        # ---- MINKOWSKI DIAGRAM - RYAN'S PERSPECTIVE

        ryanFrame = Axes(
            x_range=[-15, 0, 1],
            y_range=[0, 15, 1],
            # x_length=5,
            # y_length=5,
            tips=False,
            axis_config={"stroke_color": WHITE},
            x_axis_config={"include_ticks": False, "include_numbers": False},
            y_axis_config={"include_ticks": True, "include_numbers": True},
        )

        # print("", ryanFrame.x_range)

        y_label_ryan = ryanFrame.get_y_axis_label(
            r"t", edge=RIGHT, direction=RIGHT, buff=0.4)
        x_label_ryan = ryanFrame.get_x_axis_label(
            r"x", edge=DOWN, direction=DOWN)

        steveGraphRyanFrame = ryanFrame.plot(lambda x: -x,
                        x_range=[-15, 0], use_smoothing=True, color=BLUE)

        ryanGraphRyanFrame = ryanFrame.get_vertical_line(
            ryanFrame.c2p(0, 15, 0), color=RED, line_func=Line, stroke_width=4)

        steveLabelRyanFrame = ryanFrame.get_graph_label(steveGraphRyanFrame, Tex(
            "Steve's Path", font_size=35), x_val=-15, direction=UL, color=BLUE)

        ryanLabelRyanFrame = ryanFrame.get_graph_label(
            ryanGraphRyanFrame, Tex("Ryan's Path", font_size=35), x_val=0, direction=UP*25, color=RED
        )

        raysRyanFrame = []
        horizontalLinesRyanFrame = []
        for i in range(1, 7):
            m = -2
            raysRyanFrame.append(ryanFrame.plot(
                lambda x: i + x/m, x_range=[-i/(1/m+1), 0], use_smoothing=True, color=WHITE))
            horizontalLinesRyanFrame.append(DashedVMobject(ryanFrame.plot(lambda x: i/(1/m+1), x_range=[-i/(
                1/m+1), 0], use_smoothing=True, color=ORANGE), num_dashes=int(2 * i/(1/m+1)), equal_lengths=False))

        self.play(Create(title), run_time=1)
        self.play(Create(steveFrame), FadeIn(y_label_steve),
                  FadeIn(x_label_steve), run_time=3)
        self.play(Create(steveGraphSteveFrame), run_time=2)
        self.play(FadeIn(steveLabelSteveFrame))
        self.play(Create(ryanGraphSteveFrame), run_time=2)
        self.play(FadeIn(ryanLabelSteveFrame))
        for ray in raysSteveFrame:
            self.play(Create(ray))
        self.play(*[Create(x) for x in horizontalLinesSteveFrame])
        self.wait(2)
        self.play(FadeOut(*horizontalLinesSteveFrame),
                  FadeOut(*raysSteveFrame))
        self.play(Transform(steveFrame, ryanFrame), TransformMatchingTex(y_label_steve, y_label_ryan), TransformMatchingTex(x_label_steve, x_label_ryan), Transform(steveGraphSteveFrame, steveGraphRyanFrame), Transform(
            ryanGraphSteveFrame, ryanGraphRyanFrame), TransformMatchingTex(steveLabelSteveFrame, steveLabelRyanFrame), Transform(ryanLabelSteveFrame, ryanLabelRyanFrame), run_time=2)
        self.wait(2)
        self.play(*[Create(x) for x in raysRyanFrame], *[Create(x) for x in horizontalLinesRyanFrame])
        self.wait(3)


class Signal(Scene):
    def get_sine_wave(self, dx=0):
        return FunctionGraph(
            lambda x: np.sin((x+dx)),
            x_range=[-4, 4]
        )

    def construct(self):

        d_theta=ValueTracker(0)
        d_x = ValueTracker(0)

        sine_function = always_redraw(
            lambda : FunctionGraph(
                lambda x: 0.5*np.sin(x+d_theta.get_value()), x_range=[-4 - d_theta.get_value(), 4 + d_theta.get_value()], color=WHITE
            )
        )

        self.play(Create(sine_function))
        self.play(d_theta.animate.set_value(2*PI), run_time=2)
        # d_theta.add_updater(lambda m, dt: m.increment_value(dt))
        self.wait(2)