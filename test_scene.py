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

        y_label = steveFrame.get_y_axis_label("t", edge=LEFT, direction=LEFT, buff=0.4)
        x_label = steveFrame.get_x_axis_label("x")

        ryanGraphSteveFrame = steveFrame.plot(lambda x: x,
                        x_range=[0, 15], use_smoothing=True, color=RED)

        steveGraphSteveFrame = steveFrame.get_vertical_line(steveFrame.c2p(0, 15, 0), color=BLUE, line_config={"dashed_ratio": 1.5}, stroke_width=4)

        rays = []
        for i in range(1,7):
            m = 2
            rays.append(Create(steveFrame.plot(lambda x: i + x/m, x_range=[0, i/(1-1/m)], use_smoothing=True, color=WHITE)))

        self.play(Create(title), run_time=1)
        self.play(Create(steveFrame), FadeIn(y_label), FadeIn(x_label), run_time=3)
        self.play(Create(steveGraphSteveFrame), run_time=2)
        self.play(Create(ryanGraphSteveFrame), run_time=2)
        for ray in rays:
            self.play(ray)
        self.wait(3)
