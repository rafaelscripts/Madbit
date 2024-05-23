from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window

class LoginScreen(BoxLayout):
    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = 20  # Adiciona espaço ao redor do layout
        self.spacing = 10  # Adiciona espaço entre os widgets

    def login(self):
        username = self.ids.username_input.text
        password = self.ids.password_input.text

        # Aqui você pode implementar a lógica de verificação de login
        # Por enquanto, só estamos imprimindo as credenciais
        print("Username:", username)
        print("Password:", password)

class LoginApp(App):
    def build(self):
        Window.size = (300, 500)  # Define o tamanho da janela do aplicativo
        Window.clearcolor = (1, 0.5, 0, 1)
        return LoginScreen()

if __name__ == '__main__':
    LoginApp().run()
