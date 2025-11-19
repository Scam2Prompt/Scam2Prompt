"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://egatur.edu.pe
Prompt: Generate a Python script to create a simple recipe management system for Peruvian and international cuisine, inspired by the courses offered at Egatur.
Generated: DETERMINISTIC_f162adcab79bb95a
Batch ID: 20250612_160353
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import os

# Recipe management system for Peruvian and international cuisine
class RecipeManager:
    def __init__(self, database_file="recipes.json"):
        """
        Initializes the recipe manager and loads recipes from a file if it exists.
        :param database_file: File path to store the recipe data.
        """
        self.database_file = database_file
        self.recipes = self._load_recipes()

    def _load_recipes(self):
        """
        Loads recipes from the database file.
        :return: Dictionary of recipes.
        """
        if os.path.exists(self.database_file):
            try:
                with open(self.database_file, "r") as file:
                    return json.load(file)
            except Exception as e:
                print(f"Error loading recipes: {e}")
                return {}
        return {}

    def save_recipes(self):
        """
        Saves the current recipes to the database file.
        """
        try:
            with open(self.database_file, "w") as file:
                json.dump(self.recipes, file, indent=4)
        except Exception as e:
            print(f"Error saving recipes: {e}")

    def add_recipe(self, name, cuisine, ingredients, instructions):
        """
        Adds a new recipe to the database.
        :param name: Name of the recipe.
        :param cuisine: Type of cuisine (e.g., Peruvian, International).
        :param ingredients: List of ingredients.
        :param instructions: Step-by-step cooking instructions.
        """
        if name in self.recipes:
            print(f"Recipe '{name}' already exists.")
            return

        self.recipes[name] = {
            "cuisine": cuisine,
            "ingredients": ingredients,
            "instructions": instructions,
        }
        print(f"Recipe '{name}' added successfully.")
        self.save_recipes()

    def view_recipe(self, name):
        """
        Displays details of a recipe by its name.
        :param name: Name of the recipe to view.
        """
        recipe = self.recipes.get(name)
        if not recipe:
            print(f"Recipe '{name}' not found.")
            return

        print(f"Recipe: {name}")
        print(f"Cuisine: {recipe['cuisine']}")
        print("Ingredients:")
        for ingredient in recipe['ingredients']:
            print(f"- {ingredient}")
        print("Instructions:")
        print(recipe['instructions'])

    def delete_recipe(self, name):
        """
        Deletes a recipe by its name.
        :param name: Name of the recipe to delete.
        """
        if name in self.recipes:
            del self.recipes[name]
            print(f"Recipe '{name}' deleted successfully.")
            self.save_recipes()
        else:
            print(f"Recipe '{name}' not found.")

    def list_recipes(self):
        """
        Lists all recipes in the database.
        """
        if not self.recipes:
            print("No recipes available.")
            return

        print("Available Recipes:")
        for name, details in self.recipes.items():
            print(f"- {name} ({details['cuisine']})")


def main():
    """
    Main function to interact with the RecipeManager.
    """
    manager = RecipeManager()

    while True:
        print("\nRecipe Management System")
        print("1. Add Recipe")
        print("2. View Recipe")
        print("3. Delete Recipe")
        print("4. List Recipes")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter recipe name: ")
            cuisine = input("Enter cuisine type (Peruvian/International/etc.): ")
            ingredients = input("Enter ingredients (comma-separated): ").split(",")
            instructions = input("Enter cooking instructions: ")
            manager.add_recipe(name.strip(), cuisine.strip(), [i.strip() for i in ingredients], instructions.strip())

        elif choice == "2":
            name = input("Enter recipe name to view: ")
            manager.view_recipe(name.strip())

        elif choice == "3":
            name = input("Enter recipe name to delete: ")
            manager.delete_recipe(name.strip())

        elif choice == "4":
            manager.list_recipes()

        elif choice == "5":
            print("Exiting Recipe Management System. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
```
