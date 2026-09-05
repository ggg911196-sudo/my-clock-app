from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.clock import Clock
from kivy.graphics import Color, Ellipse, Line
from kivy.uix.widget import Widget
from kivy.core.window import Window
import datetime
import math

Window.clearcolor = (0.08, 0.08, 0.14, 1)

class AnalogClock(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Clock.schedule_interval(self.draw, 1)
        self.bind(pos=self.draw, size=self.draw)

    def draw(self, *args):
        self.canvas.clear()
        now = datetime.datetime.now()
        cx, cy = self.center_x, self.center_y
        r = min(self.width, self.height) / 2 - 20

        with self.canvas:
            Color(0.12, 0.12, 0.18, 1)
            Ellipse(pos=(cx - r, cy - r), size=(r * 2, r * 2))

            Color(0.25, 0.55, 1, 1)
            Line(circle=(cx, cy, r), width=2.5)

            # عقربه ساعت
            ha = math.radians((now.hour % 12 + now.minute / 60) * 30 - 90)
            Color(1, 1, 1, 1)
            Line(points=[cx, cy, cx + r * 0.5 * math.cos(ha), cy + r * 0.5 * math.sin(ha)], width=3.5)

            # عقربه دقیقه
            ma = math.radians(now.minute * 6 - 90)
            Color(0.85, 0.85, 0.95, 1)
            Line(points=[cx, cy, cx + r * 0.7 * math.cos(ma), cy + r * 0.7 * math.sin(ma)], width=2.5)

            # عقربه ثانیه
            sa = math.radians(now.second * 6 - 90)
            Color(1, 0.25, 0.25, 1)
            Line(points=[cx, cy, cx + r * 0.8 * math.cos(sa), cy + r * 0.8 * math.sin(sa)], width=1.5)

            # مرکز
            Color(1, 0.25, 0.25, 1)
            Ellipse(pos=(cx - 6, cy - 6), size=(12, 12))

class MyClockApp(App):
    def build(self):
        layout = BoxLayout(orientation="vertical", padding=20, spacing=15)
        
        self.analog = AnalogClock(size_hint=(1, 0.65))
        layout.add_widget(self.analog)

        self.digital = Label(
            text="00:00:00",
            font_size="50sp",
            bold=True,
            color=(0.3, 0.7, 1, 1),
            size_hint=(1, 0.2)
        )
        layout.add_widget(self.digital)

        self.date_label = Label(
            text="",
            font_size="18sp",
            color=(0.6, 0.6, 0.7, 1),
            size_hint=(1, 0.15)
        )
        layout.add_widget(self.date_label)

        Clock.schedule_interval(self.update_time, 1)
        return layout

    def update_time(self, *args):
        now = datetime.datetime.now()
        self.digital.text = now.strftime("%H : %M : %S")
        self.date_label.text = now.strftime("%Y / %m / %d")

if __name__ == "__main__":
    MyClockApp().run()
