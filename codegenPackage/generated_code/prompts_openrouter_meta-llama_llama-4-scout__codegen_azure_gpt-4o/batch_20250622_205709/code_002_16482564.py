"""
Generated Code Metadata:
========================
Original URL: https://prize-render.net
Prompt: Create a simple recipe for a grilled chicken dish using only 4 ingredients, similar to one featured on The Kitchn.
Generated: DETERMINISTIC_16482564120d6a22
Batch ID: 20250622_205709
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Recipe for a simple grilled chicken dish using only 4 ingredients

def grilled_chicken_recipe():
    """
    Returns a simple recipe for grilled chicken using 4 ingredients.
    """
    try:
        # Define the ingredients
        ingredients = {
            "Chicken Breasts": "2 large, boneless, skinless",
            "Olive Oil": "2 tablespoons",
            "Garlic Powder": "1 teaspoon",
            "Paprika": "1 teaspoon"
        }

        # Define the instructions
        instructions = [
            "1. Preheat your grill to medium-high heat (about 375°F to 400°F).",
            "2. In a small bowl, mix olive oil, garlic powder, and paprika to create a marinade.",
            "3. Brush the marinade evenly over both sides of the chicken breasts.",
            "4. Place the chicken breasts on the grill and cook for 6-8 minutes per side, "
            "   or until the internal temperature reaches 165°F (74°C).",
            "5. Remove the chicken from the grill and let it rest for 5 minutes before serving."
        ]

        # Return the recipe
        return {
            "Ingredients": ingredients,
            "Instructions": instructions
        }

    except Exception as e:
        # Handle any unexpected errors
        print(f"An error occurred while generating the recipe: {e}")
        return None


# Main function to display the recipe
if __name__ == "__main__":
    recipe = grilled_chicken_recipe()
    if recipe:
        print("Grilled Chicken Recipe")
        print("\nIngredients:")
        for ingredient, description in recipe["Ingredients"].items():
            print(f"- {ingredient}: {description}")
        
        print("\nInstructions:")
        for step in recipe["Instructions"]:
            print(step)
```
