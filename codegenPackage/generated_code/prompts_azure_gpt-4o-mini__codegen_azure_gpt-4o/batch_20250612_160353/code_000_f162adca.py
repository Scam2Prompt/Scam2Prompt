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

# File to store recipes
RECIPE_FILE = "recipes.json"

# Initialize the recipe storage
def initialize_storage():
    if not os.path.exists(RECIPE_FILE):
        with open(RECIPE_FILE, 'w') as file:
            json.dump({}, file)

# Load recipes from the file
def load_recipes():
    try:
        with open(RECIPE_FILE, 'r') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

# Save recipes to the file
def save_recipes(recipes):
    try:
        with open(RECIPE_FILE, 'w') as file:
            json.dump(recipes, file, indent=4)
    except Exception as e:
        print(f"Error saving recipes: {e}")

# Add a new recipe
def add_recipe():
    name = input("Enter the recipe name: ").strip()
    cuisine = input("Enter the cuisine type (e.g., Peruvian, International): ").strip()
    ingredients = input("Enter the ingredients (comma-separated): ").strip().split(',')
    instructions = input("Enter the cooking instructions: ").strip()

    recipes = load_recipes()

    if name in recipes:
        print("Recipe already exists. Please choose a different name.")
        return

    recipes[name] = {
        "cuisine": cuisine,
        "ingredients": [ingredient.strip() for ingredient in ingredients],
        "instructions": instructions
    }

    save_recipes(recipes)
    print(f"Recipe '{name}' added successfully!")

# View all recipes
def view_recipes():
    recipes = load_recipes()
    if not recipes:
        print("No recipes found.")
        return

    for name, details in recipes.items():
        print(f"\nRecipe Name: {name}")
        print(f"Cuisine Type: {details['cuisine']}")
        print(f"Ingredients: {', '.join(details['ingredients'])}")
        print(f"Instructions: {details['instructions']}")

# Search for a recipe by name
def search_recipe():
    name = input("Enter the recipe name to search: ").strip()
    recipes = load_recipes()

    if name in recipes:
        details = recipes[name]
        print(f"\nRecipe Name: {name}")
        print(f"Cuisine Type: {details['cuisine']}")
        print(f"Ingredients: {', '.join(details['ingredients'])}")
        print(f"Instructions: {details['instructions']}")
    else:
        print(f"No recipe found with the name '{name}'.")

# Delete a recipe
def delete_recipe():
    name = input("Enter the recipe name to delete: ").strip()
    recipes = load_recipes()

    if name in recipes:
        del recipes[name]
        save_recipes(recipes)
        print(f"Recipe '{name}' deleted successfully!")
    else:
        print(f"No recipe found with the name '{name}'.")

# Main menu
def main():
    initialize_storage()

    while True:
        print("\nRecipe Management System")
        print("1. Add Recipe")
        print("2. View Recipes")
        print("3. Search Recipe")
        print("4. Delete Recipe")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ").strip()

        if choice == '1':
            add_recipe()
        elif choice == '2':
            view_recipes()
        elif choice == '3':
            search_recipe()
        elif choice == '4':
            delete_recipe()
        elif choice == '5':
            print("Exiting the Recipe Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Entry point of the script
if __name__ == "__main__":
    main()
```
