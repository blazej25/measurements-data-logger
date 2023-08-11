import kivy 
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.layout import Layout
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.checkbox import CheckBox
from kivy.properties import StringProperty, ObjectProperty, ListProperty

class StartLayout(GridLayout):
    pass


class StartScreen(Screen):
    data_text_input = ObjectProperty()
    data = ListProperty()

    def get_input(self):
        for line in self.data_text_input:
            self.data.append(line.text)

    def save(self):
        self.get_input()
        with open(f'{self.data[0]}.txt', 'w') as file:
            self.data.pop(0)
            print(self.data)
            for line in self.data:
                file.write(f'{line};\n')



class TestScreen(Screen):
    pass


class DataLoggerApp(App):

    def build(self):
        sm = ScreenManager()
        sm.add_widget(StartScreen(name='s1'))
        sm.add_widget(TestScreen(name='test'))
        return sm
        
if __name__ == '__main__':
    DataLoggerApp().run()