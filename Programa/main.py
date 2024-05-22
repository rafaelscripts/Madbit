from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
import firebase_admin
from firebase_admin import credentials, firestore
import os

class RecipeApp(App):
    def build(self):
        Window.size = (400, 550)
        Window.clearcolor = (1, 0.5, 0, 1)  # Define a cor de fundo

        # Inicializar Firebase
        self.initialize_firebase()

        return RecipeBoxLayout()

    def initialize_firebase(self):
        # Caminho para o seu arquivo de credenciais JSON
        cred_path = os.path.join(os.path.dirname(__file__), 'serviceAccountKey.json')
        cred = credentials.Certificate(cred_path)
        firebase_admin.initialize_app(cred)
        self.db = firestore.client()

    def register_recipe(self):
        recipe_name = self.root.ids.recipe_name_input.text
        recipe_type = self.root.ids.recipe_type_spinner.text
        recipe_ingredients = self.root.ids.recipe_ingredients_input.text
        recipe_instructions = self.root.ids.recipe_instructions_input.text

        # Salva os dados da receita no Firestore
        recipe_data = {
            'name': recipe_name,
            'type': recipe_type,
            'ingredients': recipe_ingredients,
            'instructions': recipe_instructions  # Adiciona as instruções da receita
        }
        self.db.collection('recipes').add(recipe_data)

        print(f'Recipe Registered: {recipe_name} - {recipe_type}')
        print(f'Ingredients: {recipe_ingredients}')
        print(f'Instructions: {recipe_instructions}')
        
        # Limpar os campos de entrada
        self.root.ids.recipe_name_input.text = ''
        self.root.ids.recipe_type_spinner.text = 'Select Recipe Type'
        self.root.ids.recipe_ingredients_input.text = ''
        self.root.ids.recipe_instructions_input.text = ''

class RecipeBoxLayout(BoxLayout):
    pass

if __name__ == '__main__':
    RecipeApp().run()
