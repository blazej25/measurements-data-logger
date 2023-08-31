from kivy.app import Builder
from kivy.uix.screenmanager import Screen
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout

class MenuScreen(Screen):
    Builder.load_file('screens/menu.kv')

class Grid1Layout(GridLayout):
    pass