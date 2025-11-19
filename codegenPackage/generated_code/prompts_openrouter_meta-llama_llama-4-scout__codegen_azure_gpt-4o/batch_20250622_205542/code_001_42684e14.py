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
# DIY Shampoo Bar Recipe Generator
# This script generates a recipe for a natural shampoo bar using ingredients like rhassoul clay, cherry (cerise), and bitter almond (amande amère).
# The recipe is inspired by C'est Moi Qui L'ai Fait pour Vous' products.

import json

def generate_shampoo_bar_recipe():
    """
    Generates a recipe for a DIY shampoo bar using natural ingredients.
    Returns:
        dict: A dictionary containing the recipe details.
    """
    try:
        # Define the ingredients and their quantities
        ingredients = {
            "Rhassoul Clay": "50g",  # Natural clay for cleansing and detoxifying
            "Cherry Extract (Cerise)": "10ml",  # Adds a fruity scent and mild conditioning properties
            "Bitter Almond Oil (Amande Amère)": "15ml",  # Nourishing oil for hydration and shine
            "Coconut Oil": "30g",  # Base oil for moisturizing and lather
            "Shea Butter": "20g",  # Adds creaminess and conditioning
            "Essential Oil (optional)": "5 drops",  # Optional for fragrance (e.g., lavender or rosemary)
            "Lye (Sodium Hydroxide)": "10g",  # Used for saponification (handle with care)
            "Distilled Water": "50ml",  # Used to dissolve the lye
        }

        # Define the instructions
        instructions = [
            "1. Wear gloves and safety goggles before handling lye.",
            "2. In a heat-resistant container, carefully dissolve the lye in distilled water. Stir until fully dissolved and let it cool.",
            "3. Melt the coconut oil and shea butter in a double boiler until fully liquefied.",
            "4. Combine the melted oils with the rhassoul clay, cherry extract, and bitter almond oil. Mix thoroughly.",
            "5. Slowly add the lye solution to the oil mixture, stirring continuously.",
            "6. Blend the mixture using an immersion blender until it reaches 'trace' (a pudding-like consistency).",
            "7. Add essential oil (if using) and mix well.",
            "8. Pour the mixture into silicone molds and smooth the surface.",
            "9. Allow the shampoo bars to harden for 24-48 hours.",
            "10. Remove the bars from the molds and cure them in a cool, dry place for 4-6 weeks before use.",
        ]

        # Combine the recipe details into a dictionary
        recipe = {
            "Title": "DIY Shampoo Bar Recipe",
            "Ingredients": ingredients,
            "Instructions": instructions,
        }

        return recipe

    except Exception as e:
        # Handle any unexpected errors
        print(f"An error occurred while generating the recipe: {e}")
        return None


def save_recipe_to_file(recipe, filename="shampoo_bar_recipe.json"):
    """
    Saves the recipe to a JSON file.
    Args:
        recipe (dict): The recipe dictionary to save.
        filename (str): The name of the file to save the recipe to.
    """
    try:
        with open(filename, "w") as file:
            json.dump(recipe, file, indent=4)
        print(f"Recipe successfully saved to {filename}")
    except Exception as e:
        print(f"An error occurred while saving the recipe: {e}")


if __name__ == "__main__":
    # Generate the recipe
    recipe = generate_shampoo_bar_recipe()

    if recipe:
        # Print the recipe to the console
        print(json.dumps(recipe, indent=4))

        # Save the recipe to a file
        save_recipe_to_file(recipe)
```
