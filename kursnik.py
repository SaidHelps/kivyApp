from kivy.app import App

from kivy.uix.button import Button
from kivy.uix.label import Label

from kivy.uix.boxlayout import BoxLayout

from kivy.uix.screenmanager import ScreenManager, Screen

class MyApp(App):
    def __init__(self, **kwargs):
        super(MyApp, self).__init__(**kwargs)

    def build(self):
        self.sm = ScreenManager()
        screen1 = Screen(name="Main screen")
        screen2 = Screen(name="second screen")
        bl_main = BoxLayout(orientation='vertical')
        bl_second = BoxLayout(orientation='vertical')

        bl_main.add_widget(Label(text=screen1.name))
        main_btn = Button(text="go to second screen")
        main_btn.bind(on_release=self.toset)
        bl_main.add_widget(main_btn)


        bl_second.add_widget(Label(text=screen2.name))
        second_btn = Button(text="go to main screen")
        second_btn.bind(on_release=self.tomain)
        bl_second.add_widget(second_btn)


        screen1.add_widget(bl_main)
        screen2.add_widget(bl_second)

        self.sm.add_widget(screen1)
        self.sm.add_widget(screen2)
        self.sm.current = "Main screen"

        return self.sm

    def toset(self, instance):
        self.sm.current = "second screen"
    def tomain(self, instance):
        self.sm.current = "Main screen"


if __name__ == "__main__":
    MyApp().run()