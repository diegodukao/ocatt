import kivy
from kivy.app import App
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.factory import Factory
from kivy.properties import StringProperty
from kivy.uix.widget import Widget
from kivent_core.managers.resource_managers import texture_manager
from random import randint, choice

from gamesystems import VelocitySystem2D

kivy.require('1.9.1')
texture_manager.load_atlas('assets/background_objects.atlas')

Factory.register('VelocitySystem2D', cls=VelocitySystem2D)


class DebugPanel(Widget):
    fps = StringProperty(None)

    def __init__(self, **kwargs):
        super(DebugPanel, self).__init__(**kwargs)
        Clock.schedule_once(self.update_fps)

    def update_fps(self, dt):
        self.fps = str(int(Clock.get_fps()))
        Clock.schedule_once(self.update_fps, .05)


class TestGame(Widget):
    def __init__(self, **kwargs):
        super(TestGame, self).__init__(**kwargs)
        self.gameworld.init_gameworld(
            ['renderer', 'position'],
            callback=self.init_game)

    def init_game(self):
        self.setup_states()
        self.load_models()
        self.set_state()
        self.draw_some_stuff()

    def setup_states(self):
        self.gameworld.add_state(
            state_name='main',
            systems_added=['renderer'],
            systems_removed=[],
            systems_paused=[],
            systems_unpaused=['renderer'],
            screenmanager_screen='main')

    def set_state(self):
        self.gameworld.state = 'main'

    def load_models(self):
        model_manager = self.gameworld.model_manager
        model_manager.load_textured_rectangle(
            'vertex_format_4f', 7., 7., 'star1', 'star1-4')
        model_manager.load_textured_rectangle(
            'vertex_format_4f', 10., 10., 'star1', 'star1-4-2')

    def draw_some_stuff(self):
        init_entity = self.gameworld.init_entity
        for x in range(1000):
            pos = randint(0, Window.width), randint(0, Window.height)
            model_key = choice(['star1-4', 'star1-4-2'])
            create_dict = {
                'position': pos,
                'renderer': {
                    'texture': 'star1',
                    'model_key': model_key},
            }
            # in addition to the args dict we pass in a list dictating
            # the order to create the components in.
            init_entity(create_dict, ['position', 'renderer'])
        # If you do not set Renderer.force_update to True, call update_trigger
        # self.ids.renderer.update_trigger()


class OcattApp(App):
    def build(self):
        Window.clearcolor = (0, 0, 0, 1.)


if __name__ == '__main__':
    OcattApp().run()
