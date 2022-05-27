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
            x_range=[0, 10, 1],
            y_range=[0, 10, 2],
            x_length=5,
            y_length=5,
            tips=True,
            axis_config={"stroke_color": WHITE},
            x_axis_config={"include_ticks" : False, "include_numbers": False},
        )
        ryanGraphSteveFrame = steveFrame.plot(lambda x: x,
                        x_range=[0, 10], use_smoothing=True, color=RED)

        steveGraphSteveFrame = steveFrame.get_vertical_line(steveFrame.c2p(0, 10, 0), color=BLUE, line_config={"dashed_ratio": 1.5}, stroke_width=5)

        self.add(title)
        self.play(Create(steveFrame), run_time=2)
        self.play(Create(ryanGraphSteveFrame), Create(steveGraphSteveFrame), run_time=2)
