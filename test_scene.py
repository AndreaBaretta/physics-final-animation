from manim import *


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


class Animation(Scene):
    def construct(self):
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
            tips=True,
            axis_config={"stroke_color": WHITE},
            x_axis_config={"include_ticks" : False, "include_numbers": False},
            y_axis_config={"include_ticks" : True, "include_numbers": True},
        )

        y_label = steveFrame.get_y_axis_label(r"t", edge=LEFT, direction=LEFT, buff=0.4)
        x_label = steveFrame.get_x_axis_label(r"x", edge=DOWN, direction=DOWN)

        ryanGraphSteveFrame = steveFrame.plot(lambda x: x,
                        x_range=[0, 15], use_smoothing=True, color=RED)

        ryanLabel = steveFrame.get_graph_label(ryanGraphSteveFrame, Tex("Ryan's Path", font_size=35), x_val=15, direction=UR)

        steveGraphSteveFrame = steveFrame.get_vertical_line(steveFrame.c2p(0, 15, 0), color=BLUE, line_func=Line, stroke_width=4)

        # steveLabel = steveFrame.get_graph_label(steveGraphSteveFrame, "Steve's Path", x_val=0, direction=UP / 2)

        steveLabel = steveFrame.get_graph_label(
            ryanGraphSteveFrame, Tex("Steve's Path", font_size=35), x_val=0, direction=DOWN, color=BLUE
        )

        rays = []
        horizontal_lines = []
        for i in range(1,7):
            m = 2
            rays.append(Create(steveFrame.plot(lambda x: i + x/m, x_range=[0, i/(1-1/m)], use_smoothing=True, color=WHITE)))
            horizontal_lines.append(Create(DashedVMobject(steveFrame.plot(lambda x: i/(1-1/m), x_range=[0, i/(1-1/m)], use_smoothing=True, color=ORANGE))))

        self.play(Create(title), run_time=1)
        self.play(Create(steveFrame), FadeIn(y_label), FadeIn(x_label), run_time=3)
        self.play(Create(steveGraphSteveFrame), run_time=2)
        self.play(FadeIn(steveLabel))
        self.play(Create(ryanGraphSteveFrame), run_time=2)
        self.play(FadeIn(ryanLabel))
        for ray in rays:
            self.play(ray)
        self.wait(3)
