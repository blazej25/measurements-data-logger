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
from kivy.config import Config

from screens.aspiration import AspirationScreen
from screens.dust import DustScreen
from screens.h2o import H2OScreen
from screens.gas_analyzer_check import GasAnalyzerCheckScreen
from screens.helpers import HelpersScreen
from screens.equipment_base import EquipmentBaseScreen
from screens.menu import MenuScreen
from screens.flows import FlowsScreen

Config.set('graphics', 'window_state', 'maximized')

pomiary = {0: 'Przepływ PN-Z-04030-7:1994',
           1: 'Przepływ PN-EN-ISO 16911:2013-07',
           2: 'O2:  PMD wg PN-EN 14789:2006',
           3: 'CO2: NDIR wg PN-ISO 10396:2001',
           4: 'SO2: NDIR wg PN-ISO 10396:2001',
           5: 'NOx: CLD wg PN-EN 14792:2006',
           6: 'CO: NDIR wg PN-ISO 10396:2001',
           7: 'TOC: FID wg PN- EN 12619:2013',
           8: 'N2O: NDIR wg PN-EN ISO 21258',
           9: 'Pył PN-Z-04030-7:1994',
           10: 'Pył PN-EN 13284-1:2017',
           11: 'HCl: PN-EN 1911:2011',
           12: 'HF ISO 15713:2006',
           13: 'Hg PN-EN 13211:2006',
           14: 'SO2 PN-EN 14791:2017',
           15: 'H2O PN-EN 14790:2017',
           16: 'NH3 PN-EN-ISO 21877:2020-03',
           17: 'Metale PN-EN 14385:2005',
           18: 'Procedura własna'}


class StartScreen(Screen):
    data_text_input = ObjectProperty()
    data = ListProperty()

    def get_input(self):
        for line in self.data_text_input:
            self.data.append(line.text)

    def save(self):
        self.get_input()
        names = ('Data',
                'Godzina przyjazdu',
                'Zleceniodawca',
                'Źródło emisj',
                'Personel',
                'Temperatura otoczenia',
                'Ciśnienie atmosferyczne',
                'Ilość powtórzeń')
        i = 0
        file_name = self.data[0]
        self.data.pop(0)

        with open(f'{file_name}.txt', 'w') as file:
            print(self.data)
            for line in self.data:
                file.write(f'{names[i]}: {line};\n')
                i += 1


class NextScreen(Screen):
    selected = ListProperty([0] * 19)

    def update(self, index):
        if self.selected[index] == 0:
            self.selected[index] = 1
        else:
            self.selected[index] = 0

    def print_s(self):
        for i in range(19):
            if self.selected[i] == 1:
                print(pomiary[i])

        print(self.selected)


class DataLoggerApp(App):
    def build(self):
        Builder.load_file('screens/datalogger.kv')
        sm = ScreenManager()
        sm.add_widget(StartScreen(name="s1"))
        sm.add_widget(NextScreen(name="next"))
        sm.add_widget(MenuScreen(name="menu"))
        sm.add_widget(AspirationScreen(name="aspiration"))
        sm.add_widget(DustScreen(name="dust"))
        sm.add_widget(H2OScreen(name="h2o"))
        sm.add_widget(GasAnalyzerCheckScreen(name="gas_analyzer_check"))
        sm.add_widget(HelpersScreen(name="helpers"))
        sm.add_widget(EquipmentBaseScreen(name="equipment_base"))
        sm.add_widget(FlowsScreen(name="flows"))
        return sm


if __name__ == "__main__":
    DataLoggerApp().run()
