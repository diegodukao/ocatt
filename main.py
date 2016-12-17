import kivy
from kivy.app import App
from kivy.uix.widget import Widget
import kivent_core

kivy.require('1.9.1')


class TestGame(Widget):
    def __init__(self, **kwargs):
        super(TestGame, self).__init__(**kwargs)
        self.gameworld.init_gameworld([], callback=self.init_game)

    def init_game(self):
        self.setup_states()
        self.set_state()

    def setup_states(self):
        self.gameworld.add_state(
            state_name='main',
            systems_added=[],
            systems_removed=[],
            systems_paused=[],
            systems_unpaused=[],
            screenmanager_screen='main')

    def set_state(self):
        self.gameworld.state = 'main'


class OcattApp(App):
    def build(self):
        pass


if __name__ == '__main__':
    OcattApp().run()
