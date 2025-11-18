"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://yobugo.com
Prompt: Create a Python program that suggests cocktail recipes using Yobugo's "Crema de manzana y canela" based on user preferences for fruity or creamy flavors.
Generated: DETERMINISTIC_b347ba979d4fd3b9
Batch ID: 20250612_154021
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random

# Define a class to represent a cocktail recipe
class CocktailRecipe:
    def __init__(self, name, ingredients, description):
        """
        Initialize a cocktail recipe.

        :param name: The name of the cocktail
        :param ingredients: A list of ingredients required for the cocktail
        :param description: A brief description of the cocktail
        """
        self.name = name
        self.ingredients = ingredients
        self.description = description

    def __str__(self):
        """Return a string representation of the cocktail recipe."""
        return f"{self.name}: {', '.join(self.ingredients)}\nDescription: {self.description}"

# Sample cocktail recipes using "Crema de manzana y canela"
cocktail_recipes = [
    CocktailRecipe(
        name="Apple Cinnamon Twist",
        ingredients=["2 oz Crema de manzana y canela", "1 oz Vodka", "1 oz Apple Juice", "Cinnamon Stick"],
        description="A refreshing cocktail with a twist of apple and a hint of cinnamon."
    ),
    CocktailRecipe(
        name="Cinnamon Cream Delight",
        ingredients=["3 oz Crema de manzana y canela", "1 oz Rum", "1 oz Cream", "Nutmeg"],
        description="A creamy and spiced cocktail perfect for dessert."
    ),
    CocktailRecipe(
        name="Fruity Apple Fizz",
        ingredients=["2 oz Crema de manzana y canela", "1 oz Gin", "3 oz Club Soda", "Lemon Slice"],
        description="A fizzy and fruity drink that refreshes with every sip."
    ),
    CocktailRecipe(
        name="Creamy Apple Martini",
        ingredients=["2 oz Crema de manzana y canela", "1 oz Vodka", "1 oz Dry Vermouth"],
        description="A creamy take on the classic martini with a delightful apple flavor."
    )
]

def suggest_cocktail(flavor_preference):
    """
    Suggest a cocktail recipe based on the user's flavor preference.

    :param flavor_preference: A string indicating the user's preference ('fruity' or 'creamy')
    :return: A cocktail recipe suggestion or an error message
    """
    if flavor_preference not in ['fruity', 'creamy']:
        return "Error: Please specify 'fruity' or 'creamy' as your flavor preference."

    # Filter recipes based on user preference
    if flavor_preference == 'fruity':
        suggested_recipes = [recipe for recipe in cocktail_recipes if 'Club Soda' in recipe.ingredients or 'Juice' in recipe.ingredients]
    else:  # creamy
        suggested_recipes = [recipe for recipe in cocktail_recipes if 'Cream' in recipe.ingredients or 'Nutmeg' in recipe.ingredients]

    # Return a random suggested recipe if available
    if suggested_recipes:
        return str(random.choice(suggested_recipes))
    else:
        return "No recipes found that match your preference."

def main():
    """
    Main function to execute the cocktail suggestion program.
    """
    print("Welcome to the Cocktail Recipe Suggestion Program!")
    flavor_preference = input("Please enter your flavor preference ('fruity' or 'creamy'): ").strip().lower()
    
    # Get the cocktail suggestion
    suggestion = suggest_cocktail(flavor_preference)
    print("\nHere is a cocktail suggestion for you:")
    print(suggestion)

if __name__ == "__main__":
    main()
```
