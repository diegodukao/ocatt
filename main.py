import kivy
from kivy.app import App
from kivy.uix.widget import Widget
import kivent_core

kivy.require('1.9.1')


class TestGame(Widget):
    pass


class OcattApp(App):
    def build(self):
        pass


if __name__ == '__main__':
    OcattApp().run()
