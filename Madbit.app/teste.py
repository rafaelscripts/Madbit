from kivy.uix.accordion import ObjectProperty
from kivy.uix.screenmanager import ScreenManager
from kivy.app import MDApp 
from kivy.lang import Builder 
from kivy.core.window import Clock 
from kivy.properties import ObjectProperty
 

kivy.require('1.0.8')

Window.size(350,580)

class LoginApp(MDApp): 
    self.mananger = ScreenManager(transition = NoTrasition())
    self.mananger.add_widget(Builder.load_file("pre-splash.kv"))
    return self.mananger


if __name__ == '__main__':
    LoginApp().run()