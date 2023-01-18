from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.image import Image


class MyApp(App):
    def __init__(self, **kwargs):
        super(MyApp, self).__init__(**kwargs)
        self.odin = 0
        self.bad = 0
        self.good = 0


    def build(self):
        self.sm = ScreenManager()
        screen1 = Screen(name="Main screen")
        screen2 = Screen(name="second screen")

        self.bq = BoxLayout(orientation='vertical', size_hint=(.3, .5))
        self.bq.add_widget(Button(text="1", on_press=self.toset))
        self.bq.add_widget(Button(text="2", on_press=self.toset))
        self.bq.add_widget(Button(text="3", on_press=self.toset))
        self.bq.add_widget(Button(text="4", on_press=self.toset))


        self.bl = FloatLayout(size=(300, 300))
        self.bl.add_widget(self.bq)
        self.Last = Image(source="3.png", pos_hint={'x': .5, 'y': .2}, size_hint=(.4, .4))
        self.bl.add_widget(self.Last)

        # Second window

        self.wq = FloatLayout(size=(300, 600))
        self.wqClone = BoxLayout(orientation='vertical', size_hint=(.4, .6))
        self.wqClone.add_widget(Button(text="Все Плохо просто фу воняет и ваще жесть", text_size=(300, 40), on_press=self.golosMinus))
        self.wqClone.add_widget(Button(text="ну капец типо не воняет но не вкусно", text_size=(300, 40), on_press=self.golosMinus2))
        self.wqClone.add_widget(Button(text="ну норм как у бомжей тоесть сытно но не питательно", text_size=(300, 40), on_press=self.golosMinus3))
        self.wqClone.add_widget(Button(text="типо ок пойдет типо как дома полезно но воняет чутка и волос тута плавает", text_size=(300, 40), on_press=self.golosPlus))
        self.wqClone.add_widget(Button(text="норм как дома", text_size=(300, 40), on_press=self.golosPlusDwa))
        self.wqClone.add_widget(Button(text="Шавуха имбаааа", text_size=(300, 40), on_press=self.golosPlusTri))


        screen1.add_widget(self.bl)
        screen2.add_widget(self.wq)
        self.sm.add_widget(screen1)
        self.sm.add_widget(screen2)

        return self.sm

    def toset(self, instance):
        self.sm.current = "second screen"
        self.wq.clear_widgets()
        self.wq.add_widget(self.wqClone)
        self.wq.add_widget(Button(text="Back to the main window ==>", on_press=self.tomain, size_hint=(1, .1), pos_hint={'x':0, 'y':.9}))


    def tomain(self, instance):
        self.sm.current = "Main screen"


    def golosMinus(self, instance):
        self.odin += 1
        self.bad += 1
        self.proshayLichnayaZhinh()

    def golosMinus2(self, instance):
        self.odin += 2
        self.bad += 2
        self.proshayLichnayaZhinh()

    def golosMinus3(self, instance):
        self.odin += 3
        self.bad += 3
        self.proshayLichnayaZhinh()



    def golosPlus(self, instance):
        self.odin += 1
        self.good += 1
        self.proshayLichnayaZhinh()

    def golosPlusDwa(self, instance):
        self.odin += 2
        self.good += 2
        self.proshayLichnayaZhinh()

    def golosPlusTri(self, instance):
        self.odin += 3
        self.good += 3
        self.proshayLichnayaZhinh()



    def proshayLichnayaZhinh(self):
        wq = self.odin / 1.4
        if self.good > self.bad:
            if wq < self.good:
                self.bl.remove_widget(self.Last)
                self.Last.source = "5.png"
                self.bl.add_widget(self.Last)
            elif wq > self.good:
                self.bl.remove_widget(self.Last)
                self.Last.source = "4.png"
                self.bl.add_widget(self.Last)
        elif self.good < self.bad:
            if wq < self.bad:
                self.bl.remove_widget(self.Last)
                self.Last.source = "1.png"
                self.bl.add_widget(self.Last)
            elif wq > self.bad:
                self.bl.remove_widget(self.Last)
                self.Last.source = "2.png"
                self.bl.add_widget(self.Last)
        elif self.good == self.bad:
            self.bl.remove_widget(self.Last)
            self.Last.source = "3.png"
            self.bl.add_widget(self.Last)


MyApp().run()
