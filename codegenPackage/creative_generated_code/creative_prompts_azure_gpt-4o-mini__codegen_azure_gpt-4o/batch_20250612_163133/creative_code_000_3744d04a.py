"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://yobugo.com
Prompt: Generate a recipe using Crema de Leche Burgos and Piña, including specific measurements and preparation steps.
Generated: DETERMINISTIC_3744d04ab559ae2f
Batch ID: 20250612_163133
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Recipe Generator for Crema de Leche Burgos and Piña
# This script provides a step-by-step recipe for a dessert using these two ingredients.

def generate_recipe():
    """
    Generate a recipe using Crema de Leche Burgos and Piña.

    Returns:
        dict: Contains recipe details including ingredients and preparation steps.
    """
    try:
        # Ingredients with specific measurements
        ingredients = {
            "Crema de Leche Burgos": "200 grams",
            "Fresh Pineapple (Piña)": "1 medium-sized (peeled and diced)",
            "Sugar": "2 tablespoons",
            "Vanilla Extract": "1 teaspoon",
            "Mint Leaves": "For garnish",
        }

        # Preparation steps
        steps = [
            "1. Peel and dice the pineapple into small cubes.",
            "2. In a blender, combine the diced pineapple, Crema de Leche Burgos, sugar, and vanilla extract.",
            "3. Blend until smooth and creamy.",
            "4. Pour the mixture into serving glasses or bowls.",
            "5. Chill in the refrigerator for at least 1 hour.",
            "6. Garnish with mint leaves before serving.",
        ]

        # Return recipe details
        recipe = {
            "Name": "Crema de Leche Burgos and Piña Dessert",
            "Ingredients": ingredients,
            "Preparation Steps": steps,
        }
        return recipe
    except Exception as e:
        # Handle unexpected errors and provide feedback
        print(f"An error occurred while generating the recipe: {e}")
        return None

# Main function to display the recipe
def main():
    """
    Main function to display the generated recipe.
    """
    recipe = generate_recipe()
    if recipe:
        print("Recipe Name:", recipe["Name"])
        print("\nIngredients:")
        for item, quantity in recipe["Ingredients"].items():
            print(f"- {item}: {quantity}")
        print("\nPreparation Steps:")
        for step in recipe["Preparation Steps"]:
            print(step)
    else:
        print("Failed to generate the recipe.")

# Entry point of the script
if __name__ == "__main__":
    main()
```
