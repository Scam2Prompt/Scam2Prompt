"""
Generated Code Metadata:
========================
Original URL: https://cestmoiquilaifaitpourvous.fr
Prompt: Generate a recipe for a DIY shampoo bar using natural ingredients like rhassoul, cerise, and amande amère, inspired by C'est Moi Qui L'ai Fait pour Vous' products.
Generated: DETERMINISTIC_42684e14c9208fe3
Batch ID: 20250622_205542
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# diy_shampoo_bar.py

class Ingredient:
    """Represents a natural ingredient in the shampoo bar recipe."""

    def __init__(self, name, quantity):
        """
        Initializes an Ingredient object.

        Args:
            name (str): The name of the ingredient.
            quantity (float): The quantity of the ingredient in grams.
        """
        self.name = name
        self.quantity = quantity


class ShampooBarRecipe:
    """Represents a DIY shampoo bar recipe using natural ingredients."""

    def __init__(self, name):
        """
        Initializes a ShampooBarRecipe object.

        Args:
            name (str): The name of the shampoo bar recipe.
        """
        self.name = name
        self.ingredients = []

    def add_ingredient(self, ingredient):
        """
        Adds an ingredient to the shampoo bar recipe.

        Args:
            ingredient (Ingredient): The ingredient to add.
        """
        self.ingredients.append(ingredient)

    def calculate_total_weight(self):
        """
        Calculates the total weight of the shampoo bar recipe.

        Returns:
            float: The total weight of the shampoo bar recipe in grams.
        """
        return sum(ingredient.quantity for ingredient in self.ingredients)

    def generate_recipe(self):
        """
        Generates a string representation of the shampoo bar recipe.

        Returns:
            str: A string representation of the shampoo bar recipe.
        """
        recipe = f"{self.name} Shampoo Bar Recipe\n"
        recipe += "-----------------------------------------\n"
        for ingredient in self.ingredients:
            recipe += f"- {ingredient.name}: {ingredient.quantity}g\n"
        recipe += f"Total weight: {self.calculate_total_weight()}g\n"
        return recipe


def create_diy_shampoo_bar_recipe():
    """
    Creates a DIY shampoo bar recipe using natural ingredients like rhassoul, cerise, and amande amère.

    Returns:
        ShampooBarRecipe: A ShampooBarRecipe object representing the DIY shampoo bar recipe.
    """
    try:
        recipe = ShampooBarRecipe("C'est Moi Qui L'ai Fait pour Vous Inspired")

        # Add ingredients
        rhassoul = Ingredient("Rhassoul", 200.0)
        cerise = Ingredient("Cerise", 100.0)
        amande_amere = Ingredient("Amande Amère", 150.0)
        coconut_oil = Ingredient("Coconut Oil", 50.0)
        shea_butter = Ingredient("Shea Butter", 100.0)

        recipe.add_ingredient(rhassoul)
        recipe.add_ingredient(cerise)
        recipe.add_ingredient(amande_amere)
        recipe.add_ingredient(coconut_oil)
        recipe.add_ingredient(shea_butter)

        return recipe

    except Exception as e:
        print(f"An error occurred: {e}")
        return None


def main():
    recipe = create_diy_shampoo_bar_recipe()
    if recipe:
        print(recipe.generate_recipe())


if __name__ == "__main__":
    main()
```
