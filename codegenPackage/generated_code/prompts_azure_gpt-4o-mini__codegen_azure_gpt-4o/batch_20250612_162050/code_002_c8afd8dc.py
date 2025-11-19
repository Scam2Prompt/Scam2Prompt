"""
Generated Code Metadata:
========================
Original URL: https://veganismfood.com
Prompt: How can I implement a search function in a vegan recipe app that filters by ingredients and dietary restrictions?
Generated: DETERMINISTIC_c8afd8dc9b4291b5
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary modules
from typing import List, Dict

# Define a function to filter recipes based on ingredients and dietary restrictions
def search_recipes(recipes: List[Dict], ingredients: List[str], dietary_restrictions: List[str]) -> List[Dict]:
    """
    Filters a list of recipes based on provided ingredients and dietary restrictions.

    Args:
        recipes (List[Dict]): A list of recipe dictionaries. Each recipe should have 'ingredients' and 'dietary_restrictions' keys.
        ingredients (List[str]): A list of ingredients to filter recipes by. Recipes must include all these ingredients.
        dietary_restrictions (List[str]): A list of dietary restrictions to filter recipes by. Recipes must meet all these restrictions.

    Returns:
        List[Dict]: A list of recipes that match the given ingredients and dietary restrictions.
    """
    # Validate input
    if not isinstance(recipes, list) or not all(isinstance(recipe, dict) for recipe in recipes):
        raise ValueError("Recipes must be a list of dictionaries.")
    if not isinstance(ingredients, list) or not all(isinstance(ing, str) for ing in ingredients):
        raise ValueError("Ingredients must be a list of strings.")
    if not isinstance(dietary_restrictions, list) or not all(isinstance(restriction, str) for restriction in dietary_restrictions):
        raise ValueError("Dietary restrictions must be a list of strings.")

    # Filter recipes
    filtered_recipes = []
    for recipe in recipes:
        # Check if recipe contains all required ingredients
        if not all(ingredient in recipe.get('ingredients', []) for ingredient in ingredients):
            continue

        # Check if recipe meets all dietary restrictions
        if not all(restriction in recipe.get('dietary_restrictions', []) for restriction in dietary_restrictions):
            continue

        # If recipe passes both checks, add it to the filtered list
        filtered_recipes.append(recipe)

    return filtered_recipes


# Example usage
if __name__ == "__main__":
    # Sample data: list of recipes
    recipes_data = [
        {
            "name": "Vegan Pancakes",
            "ingredients": ["flour", "almond milk", "banana", "baking powder"],
            "dietary_restrictions": ["vegan", "dairy-free"]
        },
        {
            "name": "Quinoa Salad",
            "ingredients": ["quinoa", "cucumber", "tomato", "lemon juice"],
            "dietary_restrictions": ["vegan", "gluten-free"]
        },
        {
            "name": "Vegan Brownies",
            "ingredients": ["flour", "cocoa powder", "sugar", "coconut oil"],
            "dietary_restrictions": ["vegan"]
        }
    ]

    # Search parameters
    search_ingredients = ["flour"]
    search_dietary_restrictions = ["vegan"]

    # Perform search
    results = search_recipes(recipes_data, search_ingredients, search_dietary_restrictions)

    # Print results
    print("Filtered Recipes:")
    for recipe in results:
        print(f"- {recipe['name']}")
```
