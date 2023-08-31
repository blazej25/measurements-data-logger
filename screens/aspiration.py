from kivy.app import Builder
from kivy.uix.screenmanager import Screen
from kivy.properties import StringProperty, ObjectProperty, ListProperty

class AspirationScreen(Screen):
    Builder.load_file('screens/aspiration.kv')

    number_of_measurements = StringProperty(None)

    def print(self):
        print(number_of_measurements)




