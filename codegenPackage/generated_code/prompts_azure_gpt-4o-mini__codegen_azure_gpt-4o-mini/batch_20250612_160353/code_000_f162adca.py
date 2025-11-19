"""
Generated Code Metadata:
========================
Original URL: https://egatur.edu.pe
Prompt: Generate a Python script to create a simple recipe management system for Peruvian and international cuisine, inspired by the courses offered at Egatur.
Generated: DETERMINISTIC_f162adcab79bb95a
Batch ID: 20250612_160353
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import os

class Recipe:
    """Class to represent a recipe."""
    
    def __init__(self, name, ingredients, instructions, cuisine):
        self.name = name
        self.ingredients = ingredients
        self.instructions = instructions
        self.cuisine = cuisine

    def to_dict(self):
        """Convert the recipe to a dictionary for easy JSON serialization."""
        return {
            'name': self.name,
            'ingredients': self.ingredients,
            'instructions': self.instructions,
            'cuisine': self.cuisine
        }

class RecipeManager:
    """Class to manage a collection of recipes."""
    
    def __init__(self, filename='recipes.json'):
        self.filename = filename
        self.recipes = []
        self.load_recipes()

    def load_recipes(self):
        """Load recipes from a JSON file."""
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as file:
                try:
                    self.recipes = [Recipe(**data) for data in json.load(file)]
                except json.JSONDecodeError as e:
                    print(f"Error loading recipes: {e}")
                    self.recipes = []

    def save_recipes(self):
        """Save recipes to a JSON file."""
        with open(self.filename, 'w') as file:
            json.dump([recipe.to_dict() for recipe in self.recipes], file, indent=4)

    def add_recipe(self, name, ingredients, instructions, cuisine):
        """Add a new recipe to the collection."""
        new_recipe = Recipe(name, ingredients, instructions, cuisine)
        self.recipes.append(new_recipe)
        self.save_recipes()

    def get_recipes_by_cuisine(self, cuisine):
        """Retrieve recipes by cuisine type."""
        return [recipe for recipe in self.recipes if recipe.cuisine.lower() == cuisine.lower()]

    def display_recipes(self):
        """Display all recipes in a readable format."""
        for recipe in self.recipes:
            print(f"Recipe Name: {recipe.name}")
            print(f"Cuisine: {recipe.cuisine}")
            print("Ingredients:")
            for ingredient in recipe.ingredients:
                print(f" - {ingredient}")
            print("Instructions:")
            print(recipe.instructions)
            print("-" * 40)

def main():
    """Main function to run the recipe management system."""
    manager = RecipeManager()

    while True:
        print("Recipe Management System")
        print("1. Add Recipe")
        print("2. Display Recipes")
        print("3. Search Recipes by Cuisine")
        print("4. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == '1':
            name = input("Enter recipe name: ")
            ingredients = input("Enter ingredients (comma-separated): ").split(',')
            instructions = input("Enter instructions: ")
            cuisine = input("Enter cuisine type: ")
            manager.add_recipe(name.strip(), [ingredient.strip() for ingredient in ingredients], instructions.strip(), cuisine.strip())
            print("Recipe added successfully!")
        
        elif choice == '2':
            manager.display_recipes()
        
        elif choice == '3':
            cuisine = input("Enter cuisine type to search: ")
            recipes = manager.get_recipes_by_cuisine(cuisine)
            if recipes:
                for recipe in recipes:
                    print(recipe.name)
            else:
                print("No recipes found for this cuisine.")
        
        elif choice == '4':
            print("Exiting the Recipe Management System.")
            break
        
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
```
