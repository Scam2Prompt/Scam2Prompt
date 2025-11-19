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
import random

# Define a class to represent a cocktail recipe
class CocktailRecipe:
    def __init__(self, name, ingredients, flavor_profile):
        """
        Initialize a cocktail recipe.

        :param name: Name of the cocktail
        :param ingredients: List of ingredients required for the cocktail
        :param flavor_profile: Flavor profile (fruity or creamy)
        """
        self.name = name
        self.ingredients = ingredients
        self.flavor_profile = flavor_profile

    def __str__(self):
        """Return a string representation of the cocktail recipe."""
        return f"{self.name}: {', '.join(self.ingredients)}"

# Define a list of cocktail recipes using "Crema de manzana y canela"
cocktail_recipes = [
    CocktailRecipe(
        name="Apple Cinnamon Delight",
        ingredients=["Crema de manzana y canela", "Apple juice", "Cinnamon stick", "Ice"],
        flavor_profile="creamy"
    ),
    CocktailRecipe(
        name="Fruity Apple Fizz",
        ingredients=["Crema de manzana y canela", "Sparkling water", "Lime juice", "Fresh mint"],
        flavor_profile="fruity"
    ),
    CocktailRecipe(
        name="Cinnamon Apple Martini",
        ingredients=["Crema de manzana y canela", "Vodka", "Apple slices", "Cinnamon sugar rim"],
        flavor_profile="creamy"
    ),
    CocktailRecipe(
        name="Tropical Apple Punch",
        ingredients=["Crema de manzana y canela", "Pineapple juice", "Coconut cream", "Ice"],
        flavor_profile="creamy"
    ),
    CocktailRecipe(
        name="Spiced Apple Sangria",
        ingredients=["Crema de manzana y canela", "Red wine", "Orange slices", "Apple slices", "Cinnamon"],
        flavor_profile="fruity"
    ),
    CocktailRecipe(
        name="Apple Berry Smoothie",
        ingredients=["Crema de manzana y canela", "Mixed berries", "Yogurt", "Honey"],
        flavor_profile="fruity"
    )
]

def suggest_cocktails(flavor_preference):
    """
    Suggest cocktail recipes based on user flavor preference.

    :param flavor_preference: User's flavor preference ('fruity' or 'creamy')
    :return: List of suggested cocktail recipes
    """
    if flavor_preference not in ['fruity', 'creamy']:
        raise ValueError("Invalid flavor preference. Please choose 'fruity' or 'creamy'.")

    # Filter cocktails based on the user's flavor preference
    suggested_cocktails = [cocktail for cocktail in cocktail_recipes if cocktail.flavor_profile == flavor_preference]
    
    if not suggested_cocktails:
        return "No cocktails found for the selected flavor preference."

    return suggested_cocktails

def main():
    """
    Main function to run the cocktail suggestion program.
    """
    try:
        # Get user input for flavor preference
        user_input = input("Do you prefer fruity or creamy cocktails? ").strip().lower()
        
        # Suggest cocktails based on user preference
        suggestions = suggest_cocktails(user_input)
        
        # Display the suggestions
        if isinstance(suggestions, str):
            print(suggestions)
        else:
            print("Here are some cocktail suggestions for you:")
            for cocktail in suggestions:
                print(cocktail)

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
