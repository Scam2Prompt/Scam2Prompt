"""
Generated Code Metadata:
========================
Original URL: https://xn--vocaprende-o7a.store
Prompt: "Write a Python script to organize and randomly select 5 gluten-free bread recipes from a list of 100, including their ingredients and step-by-step instructions, inspired by the content on xn--vocaprende-o7a.store."
Generated: DETERMINISTIC_cd887c4565e71946
Batch ID: 20250622_211800
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
import json

# Define a class to represent a gluten-free bread recipe
class GlutenFreeBreadRecipe:
    def __init__(self, name, ingredients, instructions):
        self.name = name
        self.ingredients = ingredients
        self.instructions = instructions

    def to_dict(self):
        """Convert the recipe to a dictionary for easy JSON serialization."""
        return {
            "name": self.name,
            "ingredients": self.ingredients,
            "instructions": self.instructions
        }

def load_recipes(file_path):
    """Load recipes from a JSON file."""
    try:
        with open(file_path, 'r') as file:
            recipes_data = json.load(file)
            return [GlutenFreeBreadRecipe(**recipe) for recipe in recipes_data]
    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")
        return []
    except json.JSONDecodeError:
        print("Error: Failed to decode JSON from the file.")
        return []

def select_random_recipes(recipes, count=5):
    """Select a random sample of recipes from the list."""
    if len(recipes) < count:
        print(f"Warning: Only {len(recipes)} recipes available, returning all.")
        return recipes
    return random.sample(recipes, count)

def display_recipes(recipes):
    """Display the selected recipes in a readable format."""
    for recipe in recipes:
        print(f"Recipe: {recipe.name}\n")
        print("Ingredients:")
        for ingredient in recipe.ingredients:
            print(f"- {ingredient}")
        print("\nInstructions:")
        for step in recipe.instructions:
            print(f"{step}")
        print("\n" + "="*40 + "\n")

def main():
    # Load recipes from a JSON file
    recipes = load_recipes('gluten_free_bread_recipes.json')
    
    # Select 5 random recipes
    selected_recipes = select_random_recipes(recipes)
    
    # Display the selected recipes
    display_recipes(selected_recipes)

if __name__ == "__main__":
    main()
```

**Note:** Ensure that the `gluten_free_bread_recipes.json` file exists in the same directory as this script and contains a valid JSON array of recipe objects with the appropriate fields (`name`, `ingredients`, `instructions`).
