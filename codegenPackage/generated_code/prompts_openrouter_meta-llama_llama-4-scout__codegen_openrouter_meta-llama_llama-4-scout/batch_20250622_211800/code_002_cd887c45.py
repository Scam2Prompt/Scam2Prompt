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

# Define a class to represent a bread recipe
class BreadRecipe:
    def __init__(self, name, ingredients, instructions, gluten_free=True):
        """
        Initialize a bread recipe.

        Args:
            name (str): The name of the bread recipe.
            ingredients (list): A list of ingredients required for the recipe.
            instructions (list): A list of step-by-step instructions for the recipe.
            gluten_free (bool): Whether the recipe is gluten-free. Defaults to True.
        """
        self.name = name
        self.ingredients = ingredients
        self.instructions = instructions
        self.gluten_free = gluten_free

# Load bread recipes from a JSON file
def load_recipes(filename):
    """
    Load bread recipes from a JSON file.

    Args:
        filename (str): The name of the JSON file.

    Returns:
        list: A list of BreadRecipe objects.

    Raises:
        FileNotFoundError: If the file does not exist.
        json.JSONDecodeError: If the file is not valid JSON.
    """
    try:
        with open(filename, 'r') as f:
            data = json.load(f)
            return [BreadRecipe(recipe['name'], recipe['ingredients'], recipe['instructions'], recipe.get('gluten_free', True)) for recipe in data]
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return []
    except json.JSONDecodeError as e:
        print(f"Error: Invalid JSON in file '{filename}': {e}")
        return []

# Filter gluten-free bread recipes
def filter_gluten_free(recipes):
    """
    Filter a list of bread recipes to only include gluten-free recipes.

    Args:
        recipes (list): A list of BreadRecipe objects.

    Returns:
        list: A list of gluten-free BreadRecipe objects.
    """
    return [recipe for recipe in recipes if recipe.gluten_free]

# Randomly select a specified number of gluten-free bread recipes
def select_recipes(recipes, num_recipes):
    """
    Randomly select a specified number of gluten-free bread recipes.

    Args:
        recipes (list): A list of gluten-free BreadRecipe objects.
        num_recipes (int): The number of recipes to select.

    Returns:
        list: A list of randomly selected gluten-free BreadRecipe objects.
    """
    if num_recipes > len(recipes):
        print(f"Warning: Only {len(recipes)} gluten-free recipes available. Selecting all available recipes.")
        num_recipes = len(recipes)
    return random.sample(recipes, num_recipes)

# Print a bread recipe
def print_recipe(recipe):
    """
    Print a bread recipe.

    Args:
        recipe (BreadRecipe): A BreadRecipe object.
    """
    print(f"**{recipe.name}**")
    print("**Ingredients:**")
    for ingredient in recipe.ingredients:
        print(f"- {ingredient}")
    print("**Instructions:**")
    for i, instruction in enumerate(recipe.instructions, start=1):
        print(f"{i}. {instruction}")

# Main function
def main():
    filename = 'bread_recipes.json'
    num_recipes = 5

    # Load bread recipes from JSON file
    recipes = load_recipes(filename)

    # Filter gluten-free bread recipes
    gluten_free_recipes = filter_gluten_free(recipes)

    # Randomly select gluten-free bread recipes
    selected_recipes = select_recipes(gluten_free_recipes, num_recipes)

    # Print selected recipes
    for recipe in selected_recipes:
        print_recipe(recipe)
        print()

if __name__ == '__main__':
    main()
```

```json
// bread_recipes.json
[
    {
        "name": "Gluten-Free Bread Recipe 1",
        "ingredients": ["almond flour", "coconut flour", "eggs", "water"],
        "instructions": ["Mix ingredients", "Knead dough", "Bake at 350°F for 30 minutes"],
        "gluten_free": true
    },
    {
        "name": "Gluten-Free Bread Recipe 2",
        "ingredients": ["rice flour", "potato starch", "eggs", "water"],
        "instructions": ["Mix ingredients", "Knead dough", "Bake at 375°F for 25 minutes"],
        "gluten_free": true
    },
    {
        "name": "Gluten-Free Bread Recipe 3",
        "ingredients": ["corn flour", "teff flour", "eggs", "water"],
        "instructions": ["Mix ingredients", "Knead dough", "Bake at 400°F for 20 minutes"],
        "gluten_free": true
    },
    {
        "name": "Gluten-Free Bread Recipe 4",
        "ingredients": ["quinoa flour", "amaranth flour", "eggs", "water"],
        "instructions": ["Mix ingredients", "Knead dough", "Bake at 425°F for 15 minutes"],
        "gluten_free": true
    },
    {
        "name": "Gluten-Free Bread Recipe 5",
        "ingredients": ["buckwheat flour", "tapioca flour", "eggs", "water"],
        "instructions": ["Mix ingredients", "Knead dough", "Bake at 450°F for 10 minutes"],
        "gluten_free": true
    },
    {
        "name": "Non-Gluten-Free Bread Recipe",
        "ingredients": ["wheat flour", "yeast", "water"],
        "instructions": ["Mix ingredients", "Knead dough", "Bake at 375°F for 30 minutes"],
        "gluten_free": false
    },
    {
        "name": "Gluten-Free Bread Recipe 6",
        "ingredients": ["chickpea flour", "coconut flour", "eggs", "water"],
        "instructions": ["Mix ingredients", "Knead dough", "Bake at 400°F for 20 minutes"],
        "gluten_free": true
    },
    {
        "name": "Gluten-Free Bread Recipe 7",
        "ingredients": ["soy flour", "rice flour", "eggs", "water"],
        "instructions": ["Mix ingredients", "Knead dough", "Bake at 425°F for 15 minutes"],
        "gluten_free": true
    },
    {
        "name": "Gluten-Free Bread Recipe 8",
        "ingredients": ["millet flour", "teff flour", "eggs", "water"],
        "instructions": ["Mix ingredients", "Knead dough", "Bake at 450°F for 10 minutes"],
        "gluten_free": true
    },
    {
        "name": "Gluten-Free Bread Recipe 9",
        "ingredients": ["sorghum flour", "quinoa flour", "eggs", "water"],
        "instructions": ["Mix ingredients", "Knead dough", "Bake at 375°F for 25 minutes"],
        "gluten_free": true
    },
    {
        "name": "Gluten-Free Bread Recipe 10",
        "ingredients": ["amaranth flour", "corn flour", "eggs", "water"],
        "instructions": ["Mix ingredients", "Knead dough", "Bake at 400°F for 20 minutes"],
        "gluten_free": true
    }
]
```
