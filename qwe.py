from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.animation import Animation
from kivy.uix.floatlayout import FloatLayout


from kivy.app import App
from kivy.lang import Builder

kv = '''
<ErkisWidget@Button>:
    angle: 0
    size_hint: .3, .3
    canvas.before:
        PushMatrix:
        Rotate:
            angle: root.angle
            axis: 0, 0, 1
            origin: root.center
    canvas.after:
        PopMatrix


FloatLayout:
    ErkisWidget:
        on_press:
            app.stop(self)
'''


class RotationApp(App):
    def stop(self, widget, *args):
        anim = Animation(
            angle=90,
            duration=1
        )
        anim.start(widget)

    def build(self):
        return Builder.load_string(kv)

RotationApp().run()

"""bl = BoxLayout(orientation='vertical', padding=50, spacing=20)
        lb = Label(text="Hello World!", font_size=32)
        button = Button(text="press me", size_hint=(.5, .5), pos_hint={"center_x": 0.5}, font_size=32)
        bl.add_widget(lb)
        bl.add_widget(button)
        animate = Animation(
            background_color=(0,0,1,1),
            duration=1
        )
        animate += Animation(size_hint=(1,1),
                             duration=1)

        animate += Animation(size_hint=(.5, .5),
                             duration=1)

        animate += Animation(pos_hint = {"center_x":0.1},
                             duration=1)

        animate += Animation(pos_hint={"center_x": 1},
                             duration=1)

        animate += Animation(pos_hint={"center_x": 0.5},
                             duration=1)

        animate.start(button)
        return bl"""