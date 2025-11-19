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
from typing import List, Dict, Any

class Recipe:
    """Class to represent a recipe."""
    
    def __init__(self, name: str, ingredients: List[str], instructions: str, cuisine: str):
        """Initialize a recipe with name, ingredients, instructions, and cuisine type."""
        self.name = name
        self.ingredients = ingredients
        self.instructions = instructions
        self.cuisine = cuisine

    def to_dict(self) -> Dict[str, Any]:
        """Convert the recipe to a dictionary format for easy storage."""
        return {
            'name': self.name,
            'ingredients': self.ingredients,
            'instructions': self.instructions,
            'cuisine': self.cuisine
        }

class RecipeManager:
    """Class to manage a collection of recipes."""
    
    def __init__(self, filename: str):
        """Initialize RecipeManager with a filename for storing recipes."""
        self.filename = filename
        self.recipes = self.load_recipes()

    def load_recipes(self) -> List[Recipe]:
        """Load recipes from a JSON file."""
        try:
            with open(self.filename, 'r') as file:
                recipes_data = json.load(file)
                return [Recipe(**data) for data in recipes_data]
        except (FileNotFoundError, json.JSONDecodeError) as e:
            print(f"Error loading recipes: {e}")
            return []

    def save_recipes(self) -> None:
        """Save the current recipes to a JSON file."""
        try:
            with open(self.filename, 'w') as file:
                json.dump([recipe.to_dict() for recipe in self.recipes], file, indent=4)
        except IOError as e:
            print(f"Error saving recipes: {e}")

    def add_recipe(self, recipe: Recipe) -> None:
        """Add a new recipe to the collection."""
        self.recipes.append(recipe)
        self.save_recipes()

    def find_recipe(self, name: str) -> Recipe:
        """Find a recipe by its name."""
        for recipe in self.recipes:
            if recipe.name.lower() == name.lower():
                return recipe
        print("Recipe not found.")
        return None

    def list_recipes(self) -> None:
        """List all recipes in the collection."""
        if not self.recipes:
            print("No recipes available.")
            return
        for recipe in self.recipes:
            print(f"Name: {recipe.name}, Cuisine: {recipe.cuisine}")

def main():
    """Main function to run the recipe management system."""
    manager = RecipeManager('recipes.json')
    
    # Adding sample recipes
    manager.add_recipe(Recipe("Ceviche", ["Fresh fish", "Lime juice", "Onions", "Cilantro", "Chili peppers"], 
                               "Mix ingredients and serve chilled.", "Peruvian"))
    manager.add_recipe(Recipe("Paella", ["Rice", "Seafood", "Chicken", "Saffron", "Vegetables"], 
                               "Cook ingredients in a pan and serve.", "Spanish"))

    # Listing available recipes
    print("\nAvailable Recipes:")
    manager.list_recipes()

    # Finding a specific recipe
    recipe_name = "Ceviche"
    found_recipe = manager.find_recipe(recipe_name)
    if found_recipe:
        print(f"\nFound Recipe: {found_recipe.name}\nIngredients: {', '.join(found_recipe.ingredients)}\nInstructions: {found_recipe.instructions}")

if __name__ == '__main__':
    main()
```
