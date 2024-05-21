from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
import os
import json

class RecipeApp(App):
    def build(self):
        Window.size = (400, 550)
        Window.clearcolor = (1, 0.5, 0, 1)  # Define a cor de fundo
        return RecipeBoxLayout()

    def register_recipe(self):
        recipe_name = self.root.ids.recipe_name_input.text
        recipe_type = self.root.ids.recipe_type_spinner.text
        recipe_ingredients = self.root.ids.recipe_ingredients_input.text
        recipe_instructions = self.root.ids.recipe_instructions_input.text

        # Cria uma pasta para armazenar receitas, se não existir
        recipe_folder = 'recipes'
        if not os.path.exists(recipe_folder):
            os.makedirs(recipe_folder)

        # Salva os dados da receita em um arquivo JSON
        recipe_data = {
            'name': recipe_name,
            'type': recipe_type,
            'ingredients': recipe_ingredients,
            'instructions': recipe_instructions  # Adiciona as instruções da receita
        }
        with open(os.path.join(recipe_folder, f'{recipe_name}.json'), 'w') as f:
            json.dump(recipe_data, f)

        print(f'Recipe Registered: {recipe_name} - {recipe_type}')
        print(f'Ingredients: {recipe_ingredients}')
        print(f'Instructions: {recipe_instructions}')
        self.root.ids.recipe_name_input.text = ''
        self.root.ids.recipe_type_spinner.text = 'Select Recipe Type'
        self.root.ids.recipe_ingredients_input.text = ''
        self.root.ids.recipe_instructions_input.text = ''

class RecipeBoxLayout(BoxLayout):
    pass

if __name__ == '__main__':
    RecipeApp().run()
