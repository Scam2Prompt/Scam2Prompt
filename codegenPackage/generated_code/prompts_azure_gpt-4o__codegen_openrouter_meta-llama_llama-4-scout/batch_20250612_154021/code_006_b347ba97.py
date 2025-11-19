"""
Generated Code Metadata:
========================
Original URL: https://yobugo.com
Prompt: Create a Python program that suggests cocktail recipes using Yobugo's "Crema de manzana y canela" based on user preferences for fruity or creamy flavors.
Generated: DETERMINISTIC_b347ba979d4fd3b9
Batch ID: 20250612_154021
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import json

# Define a class for CocktailRecipe
class CocktailRecipe:
    def __init__(self, name, ingredients, instructions, flavor_profile):
        """
        Initialize a CocktailRecipe object.

        Args:
            name (str): Name of the cocktail recipe.
            ingredients (list): List of ingredients required for the recipe.
            instructions (list): List of instructions to prepare the recipe.
            flavor_profile (str): Flavor profile of the recipe (fruity or creamy).
        """
        self.name = name
        self.ingredients = ingredients
        self.instructions = instructions
        self.flavor_profile = flavor_profile

# Define a class for CocktailSuggester
class CocktailSuggester:
    def __init__(self, base_recipe):
        """
        Initialize a CocktailSuggester object.

        Args:
            base_recipe (CocktailRecipe): Base cocktail recipe to suggest variations of.
        """
        self.base_recipe = base_recipe
        self.recipes = self.load_recipes()

    def load_recipes(self):
        """
        Load a list of cocktail recipes from a JSON file.

        Returns:
            list: List of CocktailRecipe objects.
        """
        try:
            with open('recipes.json', 'r') as f:
                data = json.load(f)
                recipes = []
                for recipe_data in data:
                    recipe = CocktailRecipe(
                        recipe_data['name'],
                        recipe_data['ingredients'],
                        recipe_data['instructions'],
                        recipe_data['flavor_profile']
                    )
                    recipes.append(recipe)
                return recipes
        except FileNotFoundError:
            print("Error: recipes.json file not found.")
            return []
        except json.JSONDecodeError:
            print("Error: Invalid JSON format in recipes.json file.")
            return []

    def suggest_recipes(self, flavor_preference):
        """
        Suggest cocktail recipes based on the user's flavor preference.

        Args:
            flavor_preference (str): User's flavor preference (fruity or creamy).

        Returns:
            list: List of suggested CocktailRecipe objects.
        """
        suggested_recipes = [self.base_recipe]
        for recipe in self.recipes:
            if recipe.flavor_profile == flavor_preference:
                suggested_recipes.append(recipe)
        return suggested_recipes

# Define the base recipe for "Crema de manzana y canela"
base_recipe = CocktailRecipe(
    "Crema de manzana y canela",
    ["Apple cream liqueur", "Cinnamon syrup", "Heavy cream"],
    ["Combine ingredients in a shaker", "Shake well", "Strain into a glass"],
    "creamy"
)

# Create a CocktailSuggester object
suggester = CocktailSuggester(base_recipe)

# Main function
def main():
    print("Welcome to the Cocktail Suggester!")
    flavor_preference = input("Enter your flavor preference (fruity or creamy): ")
    suggested_recipes = suggester.suggest_recipes(flavor_preference)
    if suggested_recipes:
        print("Suggested recipes:")
        for i, recipe in enumerate(suggested_recipes):
            print(f"{i+1}. {recipe.name}")
            print(f"Ingredients: {', '.join(recipe.ingredients)}")
            print("Instructions:")
            for instruction in recipe.instructions:
                print(f"- {instruction}")
            print(f"Flavor profile: {recipe.flavor_profile}\n")
    else:
        print("No recipes found.")

if __name__ == "__main__":
    main()
```

**recipes.json**
```json
[
    {
        "name": "Apple Martini",
        "ingredients": ["Vodka", "Apple puree", "Lime juice"],
        "instructions": ["Combine ingredients in a shaker", "Shake well", "Strain into a martini glass"],
        "flavor_profile": "fruity"
    },
    {
        "name": "Cinnamon Apple Cider",
        "ingredients": ["Apple cider", "Cinnamon syrup", "Rum"],
        "instructions": ["Combine ingredients in a mug", "Heat well", "Top with whipped cream"],
        "flavor_profile": "creamy"
    },
    {
        "name": "Creamy Pina Colada",
        "ingredients": ["Pineapple juice", "Coconut cream", "Rum"],
        "instructions": ["Combine ingredients in a blender", "Blend well", "Pour into a glass"],
        "flavor_profile": "creamy"
    }
]
```
