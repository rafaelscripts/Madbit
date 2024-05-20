from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.spinner import Spinner
import os
import json

class RecipeApp(App):
    def build(self):
        self.box_layout = BoxLayout(orientation='vertical')
        self.recipe_name_input = TextInput(hint_text='Recipe Name', size_hint=(1, 0.1))
        self.recipe_type_spinner = Spinner(text='Select Recipe Type', values=('Breakfast', 'Lunch', 'Dinner', 'Dessert'), size_hint=(1, 0.1))
        self.recipe_ingredients_input = TextInput(hint_text='Recipe Ingredients', size_hint=(1, 0.5))
        self.recipe_instructions_input = TextInput(hint_text='Recipe Instructions', size_hint=(1, 0.5))
        self.register_button = Button(text='Register Recipe', size_hint=(1, 0.1))
        self.register_button.bind(on_press=self.register_recipe)
        self.box_layout.add_widget(self.recipe_name_input)
        self.box_layout.add_widget(self.recipe_type_spinner)
        self.box_layout.add_widget(self.recipe_ingredients_input)
        self.box_layout.add_widget(self.recipe_instructions_input)
        self.box_layout.add_widget(self.register_button)
        return self.box_layout

    def register_recipe(self, instance):
        recipe_name = self.recipe_name_input.text
        recipe_type = self.recipe_type_spinner.text
        recipe_ingredients = self.recipe_ingredients_input.text
        recipe_instructions = self.recipe_instructions_input.text

        # Create a folder to store recipes if it doesn't exist
        recipe_folder = 'ecipes'
        if not os.path.exists(recipe_folder):
            os.makedirs(recipe_folder)

        # Save the recipe data to a JSON file
        recipe_data = {
            'name': recipe_name,
            'type': recipe_type,
            'ingredients': recipe_ingredients,
            'instructions': recipe_instructions
        }
        with open(os.path.join(recipe_folder, f'{recipe_name}.json'), 'w') as f:
            json.dump(recipe_data, f)

        print(f'Recipe Registered: {recipe_name} - {recipe_type}')
        print(f'Ingredients: {recipe_ingredients}')
        print(f'Instructions: {recipe_instructions}')
        self.recipe_name_input.text = ''
        self.recipe_type_spinner.text = 'Select Recipe Type'
        self.recipe_ingredients_input.text = ''
        self.recipe_instructions_input.text = ''

if __name__ == '__main__':
    RecipeApp().run()