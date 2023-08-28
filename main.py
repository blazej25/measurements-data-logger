import kivy
from kivy.app import App, Builder
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

from screens.aspiration import AspirationScreen
from screens.dust import DustScreen
from screens.h2o import H2OScreen
from screens.gas_analyzer_check import GasAnalyzerCheckScreen
from screens.helpers import HelpersScreen
from screens.equipment_base import EquipmentBaseScreen


class Grid1Layout(GridLayout):
    pass


class Grid2Layout(GridLayout):
    pass


class StartScreen(Screen):
    data_text_input = ObjectProperty()
    data = ListProperty()

    def get_input(self):
        for line in self.data_text_input:
            self.data.append(line.text)

    def save(self):
        self.get_input()
        names = (
            "Data",
            "Godzina przyjazdu",
            "Zleceniodawca",
            "Źródło emisji",
            "Personel",
            "Temperatura otoczenia",
            "Ciśnienie atmosferyczne",
            "Ilość powtórzeń",
        )
        i = 0
        file_name = self.data[0]
        self.data.pop(0)

        with open(f"{file_name}.txt", "w") as file:
            print(self.data)
            for line in self.data:
                file.write(f"{names[i]}: {line};\n")
                i += 1


class NextScreen(Screen):
    pass


class DataLoggerApp(App):
    def build(self):
        Builder.load_file('screens/datalogger.kv')
        sm = ScreenManager()
        sm.add_widget(StartScreen(name="s1"))
        sm.add_widget(NextScreen(name="next"))
        sm.add_widget(AspirationScreen(name="aspiration"))
        sm.add_widget(DustScreen(name="dust"))
        sm.add_widget(H2OScreen(name="h2o"))
        sm.add_widget(GasAnalyzerCheckScreen(name="gas_analyzer_check"))
        sm.add_widget(HelpersScreen(name="helpers"))
        sm.add_widget(EquipmentBaseScreen(name="equipment_base"))
        return sm


if __name__ == "__main__":
    DataLoggerApp().run()
