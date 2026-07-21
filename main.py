from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.core.window import Window
from kivy.graphics import Color, RoundedRectangle
import math


class MyButton(Button):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # حذف پس زمینه پیش فرض
        self.background_normal = ""
        self.background_down = ""

        # رنگ دکمه
        self.background_color = (0.15, 0.15, 0.18, 1)

        # رنگ نوشته
        self.color = (1, 1, 1, 1)

        # اندازه نوشته
        self.font_size = 20


class Calculator(App):

    def build(self):

        # رنگ صفحه
        Window.clearcolor = (0.05, 0.05, 0.07, 1)

        main = BoxLayout(
            orientation="vertical",
            padding=8,
            spacing=6
        )

        # صفحه نمایش
        self.display = TextInput(
            text="0",
            font_size=35,
            readonly=True,
            halign="right",
            multiline=False,
            background_color=(0.08, 0.08, 0.10, 1),
            foreground_color=(1, 1, 1, 1),
            size_hint_y=0.2
        )

        main.add_widget(self.display)

        # دکمه ها
        grid = GridLayout(
            cols=4,
            spacing=5,
            padding=3,
            size_hint_y=0.8
        )

        buttons = [
            "C", "⌫", "%", "÷",
            "√", "x²", "±", "×",
            "7", "8", "9", "-",
            "4", "5", "6", "+",
            "1", "2", "3", "=",
            "(", "0", ".", ")"
        ]

        for text in buttons:

            button = MyButton(
                text=text
            )

            # دکمه مساوی سبز
            if text == "=":
                button.background_color = (
                    0.1, 0.6, 0.3, 1
                )

            # دکمه های عملیات آبی
            elif text in ["÷", "×", "-", "+"]:
                button.background_color = (
                    0.1, 0.35, 0.7, 1
                )

            # دکمه های بالایی خاکستری
            elif text in ["C", "⌫", "%", "√", "x²", "±"]:
                button.background_color = (
                    0.3, 0.3, 0.35, 1
                )

            grid.add_widget(button)

            button.bind(
                on_press=self.button_pressed
            )

        main.add_widget(grid)

        return main


    def button_pressed(self, instance):

        button = instance.text

        if button == "C":
            self.display.text = "0"

        elif button == "⌫":

            text = self.display.text

            if len(text) > 1:
                self.display.text = text[:-1]
            else:
                self.display.text = "0"

        elif button == "√":

            try:
                value = float(self.display.text)
                self.display.text = str(
                    math.sqrt(value)
                )
            except:
                self.display.text = "Error"

        elif button == "x²":

            try:
                value = float(self.display.text)
                self.display.text = str(
                    value ** 2
                )
            except:
                self.display.text = "Error"

        elif button == "±":

            try:
                value = float(self.display.text)
                self.display.text = str(
                    value * -1
                )
            except:
                self.display.text = "Error"

        elif button == "%":

            try:
                value = float(self.display.text)
                self.display.text = str(
                    value / 100
                )
            except:
                self.display.text = "Error"

        elif button == "=":

            try:

                expression = self.display.text

                expression = expression.replace(
                    "×", "*"
                )

                expression = expression.replace(
                    "÷", "/"
                )

                result = eval(expression)

                self.display.text = str(result)

            except:

                self.display.text = "Error"

        else:

            if self.display.text == "0":
                self.display.text = button
            else:
                self.display.text += button


Calculator().run()
