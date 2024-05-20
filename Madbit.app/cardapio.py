# Import necessary modules
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.storage.jsonstore import JsonStore



# Create a class for the main app
class RecipeApp(App):
    def _init_(self, **kwargs):
        super()._init_(**kwargs)
        self.store = JsonStore('recipes.json')

    # Build the user interface
    def build(self):
        layout = GridLayout(cols=2)
        self.recipe_name = TextInput(multiline=False)
        layout.add_widget(Label(text='Recipe Name:'))
        layout.add_widget(self.recipe_name)
        self.recipe_ingredients = TextInput(multiline=True)
        layout.add_widget(Label(text='Recipe Ingredients:'))
        layout.add_widget(self.recipe_ingredients)
        self.add_recipe_button = Button(text='Add Recipe', on_press=self.add_recipe)
        layout.add_widget(self.add_recipe_button)
        return layout

    # Add a recipe to the JSON store
    def add_recipe(self, instance):
        recipe_name = self.recipe_name.text
        recipe_ingredients = self.recipe_ingredients.text
        self.store.add(recipe_name=recipe_name, ingredients=recipe_ingredients)

# Run the app
if __name__ == '__main__':
    RecipeApp().run()