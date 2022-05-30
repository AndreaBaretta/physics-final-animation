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
        length = ValueTracker(7)
        opacity = ValueTracker(1)
        color = ValueTracker(0)
        color2 = ValueTracker(0)
        redShift = ValueTracker(1)

        sine_function = always_redraw(
            lambda : FunctionGraph(
                lambda x: 0.3*np.sin(4*x+d_theta.get_value()), x_range=[-length.get_value()/2, length.get_value()/2], color=rgb_to_color(color_to_rgb(WHITE)*(1-color.get_value()) + color_to_rgb(RED)*color.get_value())
            ) if (redShift.get_value() >= 0.5) else FunctionGraph(
                lambda x: 0.3*np.sin(4*x+d_theta.get_value()), x_range=[-length.get_value()/2, length.get_value()/2], color=rgb_to_color(color_to_rgb(RED)*(1-color2.get_value()) + color_to_rgb(BLUE)*color2.get_value())
            )
        )

        steveCircle = always_redraw(
            lambda : Circle(radius=0.5, fill_opacity=opacity.get_value(), color=BLUE).move_to(sine_function.get_left()).set_style(stroke_width=opacity.get_value())
        )

        steveLabel = always_redraw(
            lambda : Tex("Steve", font_size=35).move_to(steveCircle.get_center()).set_opacity(opacity.get_value())
        )

        ryanCircle = always_redraw(
            lambda : Circle(radius=0.5, fill_opacity=1, color=RED).move_to(sine_function.get_right())
        )

        ryanLabel = always_redraw(
            lambda : Tex("Ryan", font_size=35).move_to(ryanCircle.get_center())
        )

        # ryanCircle = always_redraw()

        self.play(Create(sine_function), Create(steveCircle), FadeIn(steveLabel), Create(ryanCircle), FadeIn(ryanLabel))
        # self.play(d_theta.animate.set_value(4*TAU, rate), d_x.animate.set_value(2), run_time=2)
        self.play(d_theta.animate.increment_value(8*TAU), rate_func=linear, run_time=4)
        self.play(d_theta.animate.increment_value(8*TAU), length.animate.increment_value(5), opacity.animate.set_value(1), color.animate.set_value(1), rate_func=linear, run_time=4)
        redShift.set_value(0)
        self.play(d_theta.animate.increment_value(6*TAU), rate_func=linear, run_time=3)
        self.play(d_theta.animate.increment_value(8*TAU), length.animate.increment_value(-5), opacity.animate.set_value(1), color2.animate.set_value(1), rate_func=linear, run_time=4)
        self.play(d_theta.animate.increment_value(6*TAU), rate_func=linear, run_time=3)
        # d_theta.add_updater(lambda m, dt: m.increment_value(dt))

class Equations(Scene):
    def construct(self):
        DopplerName = Tex("Relativistic Doppler Effect", font_size=100)
        DopplerEquation = Tex(r"$\frac{f_S}{f_R} = \sqrt{\frac{1+\beta}{1-\beta}}$", font_size=100)
        Beta = Tex(r"$\beta = \frac{v}{c}$", font_size=100)
        group1 = VGroup(DopplerName, DopplerEquation, Beta).arrange(DOWN*5)

        DopplerEquationFr = Tex(r"$f_R = f_S \sqrt{\frac{1-\beta}{1+\beta}}$", font_size=100).move_to(DopplerEquation.get_center())

        table1 = Tex(r"""
        Observers
        \begin{table}[]
        \centering
        \begin{tabular}{|c|c|c|c|}\hline
        & Steve & Ryan (outbound) & Ryan (inbound) \\ \hline
        $f$ & $f_S$ & $f_{\text{Outbound}} = f_S \sqrt{\frac{1-\beta}{1+\beta}}$ & \\ \hline
        \end{tabular}
        \end{table}
        """)

        table2 = Tex(r"""
        Observers
        \begin{table}[]
        \centering
        \begin{tabular}{|c|c|c|c|}\hline
        & Steve & Ryan (outbound) & Ryan (inbound) \\ \hline
        $f$ & $f_S$ & $f_{\text{Outbound}} = f_S \sqrt{\frac{1-\beta}{1+\beta}}$ & $f_{\text{Inbound}} = f_S \sqrt{\frac{1+\beta}{1-\beta}}$ \\ \hline
        \end{tabular}
        \end{table}
        """)

        axes = Axes(
            x_range=[-1, TAU + 1, 1],
            y_range=[-1, 1, 1],
            x_length=4,
            y_length=2,
            tips=False,
            axis_config={"stroke_color": WHITE},
            x_axis_config={"include_ticks": False, "include_numbers": False},
            y_axis_config={"include_ticks": False, "include_numbers": False},
        )

        frequencyTimeEquation = Tex(r"$\text{t} = \frac{k}{f}$")

        group2 = VGroup(axes, frequencyTimeEquation).arrange(RIGHT*2)

        fakeLine = axes.plot(lambda x : 1, x_range=[0, TAU])
        sine_wave = axes.plot(lambda x: 1 * np.sin(x), color=YELLOW)
        brace = Brace(fakeLine, direction=UP)
        braceText = brace.get_text("One Period")

        outboundTime1 = Tex(r"$\text{Outbound Time} = \frac{k}{f_{\text{Outbound}}}$", font_size=100)
        outboundTime2 = Tex(r"$\text{Outbound Time} = \frac{k}{f_S \sqrt{\frac{1-\beta}{1+\beta}}}$", font_size=100)
        outboundTime3 = Tex(r"$\text{Outbound Time} = \frac{k}{f_S} \sqrt{\frac{1+\beta}{1-\beta}}$", font_size=100)
        
        outboundTime4 = Tex(r"$\text{Outbound Time} = \frac{k}{f_S} \sqrt{\frac{1+\beta}{1-\beta}}$")
        inboundTime = Tex(r"$\text{Outbound Time} = \text{Inbound Time}$")
        totalTime1 = Tex(r"$\text{Ryan Total Time} = \text{Outbound Time} + \text{Inbound Time}$")
        totalTime2 = Tex(r"$\text{Ryan Total Time} = 2 \frac{k}{f_S} \sqrt{\frac{1+\beta}{1-\beta}}$")

        group3 = VGroup(outboundTime4, inboundTime, totalTime1).arrange(DOWN * 2)

        totalTime2.move_to(totalTime1)

        steveTime1 = Tex(r"$\text{Periods Measured on Return} = k'$")
        steveTime2 = Tex(r"$\text{Inbound Time} = \frac{k'}{f_{\text{Inbound}}}$")
        steveTime3 = Tex(r"$\text{Outbound Time} = \frac{k}{f_{\text{Outbound}}}$")
        steveTime4 = Tex(r"$\text{Outbound Time} = \text{Inbound Time}$")
        steveTime5 = Tex(r"$\frac{k}{f_{\text{Outbound}}} = \frac{k'}{f_{\text{Inbound}}}$")
        steveTime6 = Tex(r"$\frac{k}{f_S \sqrt{\frac{1-\beta}{1+\beta}}} = \frac{k'}{f_S \sqrt{\frac{1+\beta}{1-\beta}}}$")
        steveTime7 = Tex(r"$\frac{k}{f_S} \sqrt{\frac{1+\beta}{1-\beta}} = \frac{k'}{f_S} \sqrt{\frac{1-\beta}{1+\beta}}$")
        steveTime8 = Tex(r"$k' = k\left( \frac{1+\beta}{1-\beta} \right)$")

        group4 = VGroup(steveTime1, steveTime2, steveTime3).arrange(DOWN * 2)
        steveTime4.move_to(steveTime3)
        steveTime5.move_to(steveTime3)
        steveTime6.move_to(steveTime3)
        steveTime7.move_to(steveTime3)
        steveTime8.move_to(steveTime3)

        steveTotal1 = Tex(r"$\text{Steve Total Time} = \frac{k + k'}{f_S}$")
        steveTotal2 = Tex(r"$\text{Steve Total Time} = \frac{k + k\left( \frac{1+\beta}{1-\beta} \right)}{f_S}$")
        steveTotal3 = Tex(r"$\text{Steve Total Time} = \frac{k}{f_S} \left( 1+ \frac{1+\beta}{1-\beta} \right)$")
        ryanTotal = Tex(r"$\text{Ryan Total Time} = 2 \frac{k}{f_S} \sqrt{\frac{1+\beta}{1-\beta}}$")
        group5 = VGroup(steveTotal1, ryanTotal).arrange(DOWN * 2)
        steveTotal2.move_to(steveTotal1.get_center())
        steveTotal3.move_to(steveTotal1.get_center())

        axes2 = Axes(
            x_range=[-0.2, 1.2, 1],
            y_range=[-0.2, 7, 2],
            # x_length=4,
            # y_length=2,
            tips=True,
            axis_config={"stroke_color": WHITE},
            x_axis_config={"include_ticks": True, "include_numbers": True},
            y_axis_config={"include_ticks": True, "include_numbers": False},
        )

        stevePlot = axes2.plot(lambda x: 1 + (1.0+x)/(1.0-x), x_range=[0, 0.88], color=BLUE, use_smoothing=True)
        ryanPlot = axes2.plot(lambda x: 2*np.sqrt((1+x)/(1-x)), x_range=[0, 0.88], color=RED, use_smoothing=True)

        steveLabel = axes2.get_graph_label(
            stevePlot, Tex("Steve's Time", font_size=35, color=BLUE), x_val=0.7, direction=UL)

        ryanLabel = axes2.get_graph_label(
            ryanPlot, Tex("Ryan's Time", font_size=35, color=RED), x_val=0.78, direction=DR)

        y_label = axes2.get_y_axis_label(
            Tex(r"t"), edge=LEFT, direction=LEFT)
        x_label = axes2.get_x_axis_label(
            Tex(r"$\beta$"), edge=DOWN, direction=DOWN)

        self.add(group1)
        self.wait(2)
        self.play(ReplacementTransform(DopplerEquation, DopplerEquationFr))
        self.wait(2)
        self.play(FadeOut(group1, DopplerEquationFr))
        self.wait(1)
        self.play(FadeIn(table1))
        self.wait(1)
        self.play(FadeTransform(table1, table2))
        self.wait(1)
        self.play(FadeOut(table2))
        self.play(Create(axes))
        self.play(Create(sine_wave), DrawBorderThenFill(brace), Create(braceText))
        self.play(Create(frequencyTimeEquation))
        self.wait(1)
        self.play(FadeOut(sine_wave, brace, braceText, frequencyTimeEquation, axes))
        self.wait(1)
        self.play(FadeIn(outboundTime1))
        self.wait(1)
        self.play(ReplacementTransform(outboundTime1, outboundTime2))
        self.wait(1)
        self.play(ReplacementTransform(outboundTime2, outboundTime3))
        self.wait(1)
        self.play(FadeOut(outboundTime3))
        self.wait(1)
        self.play(Create(outboundTime4))
        self.play(Create(inboundTime))
        self.play(Create(totalTime1))
        self.wait(1)
        self.play(ReplacementTransform(totalTime1, totalTime2))
        self.wait(1)
        self.play(FadeOut(outboundTime4, inboundTime, totalTime2))
        self.play(FadeIn(steveTime1))
        self.play(FadeIn(steveTime2))
        self.play(FadeIn(steveTime3))
        self.wait(1)
        self.play(ReplacementTransform(steveTime3, steveTime4))
        self.wait(1)
        self.play(ReplacementTransform(steveTime4, steveTime5))
        self.wait(1)
        self.play(ReplacementTransform(steveTime5, steveTime6))
        self.wait(1)
        self.play(ReplacementTransform(steveTime6, steveTime7))
        self.wait(1)
        self.play(ReplacementTransform(steveTime7, steveTime8))
        self.wait(1)
        self.play(FadeOut(steveTime8, steveTime1, steveTime2))
        self.play(Create(steveTotal1))
        self.wait(1)
        self.play(ReplacementTransform(steveTotal1, steveTotal2))
        self.wait(1)
        self.play(ReplacementTransform(steveTotal2, steveTotal3))
        self.wait(1)
        self.play(Create(ryanTotal))
        self.wait(1)
        self.play(FadeOut(steveTotal3, ryanTotal))
        self.wait(1)
        self.play(Create(axes2))
        self.play(Create(stevePlot), Create(ryanPlot), Create(y_label), Create(x_label))
        self.play(Create(steveLabel), Create(ryanLabel))
        self.wait(1)