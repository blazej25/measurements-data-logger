from kivy.app import Builder
from kivy.uix.screenmanager import Screen
from kivy.properties import StringProperty, ObjectProperty, ListProperty
from kivy.uix.textinput import TextInput

class AspirationScreen(Screen):
    Builder.load_file('screens/aspiration.kv')

    number_of_measurements = StringProperty(None)
    print(number_of_measurements)

    def custom_print(self):
        print(self.number_of_measurements)











