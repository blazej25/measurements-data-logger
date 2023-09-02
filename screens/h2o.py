from kivy.app import Builder
from kivy.uix.screenmanager import Screen
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.properties import StringProperty, ListProperty 

class H2OScreen(Screen):
    Builder.load_file('screens/h2o.kv')

    number_of_measurements = StringProperty()

    def on_text_print(self):
        print(self.number_of_measurements)
