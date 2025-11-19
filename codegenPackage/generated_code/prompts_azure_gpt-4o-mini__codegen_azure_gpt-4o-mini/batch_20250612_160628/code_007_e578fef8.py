"""
Generated Code Metadata:
========================
Original URL: https://imonanngon.info
Prompt: What ingredients and steps are necessary for "Mướp xào giá đỗ" according to imonanngon.info?
Generated: DETERMINISTIC_e578fef867fb5523
Batch ID: 20250612_160628
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class StirFriedMupWithBeanSprouts:
    """
    A class to represent the recipe for Mướp xào giá đỗ (Stir-Fried Mup with Bean Sprouts).
    """

    def __init__(self):
        """
        Initializes the ingredients and steps for the recipe.
        """
        self.ingredients = {
            "Mup (Luffa)": "1 medium-sized, peeled and sliced",
            "Bean Sprouts": "200 grams, rinsed",
            "Garlic": "3 cloves, minced",
            "Vegetable Oil": "2 tablespoons",
            "Salt": "to taste",
            "Pepper": "to taste",
            "Soy Sauce": "1 tablespoon (optional)",
            "Chili": "1, sliced (optional for spice)"
        }
        self.steps = [
            "1. Heat the vegetable oil in a pan over medium heat.",
            "2. Add minced garlic and sauté until fragrant.",
            "3. Add the sliced Mup and stir-fry for about 3-4 minutes until slightly tender.",
            "4. Add the bean sprouts and continue to stir-fry for another 2-3 minutes.",
            "5. Season with salt, pepper, and soy sauce (if using).",
            "6. Add sliced chili if you prefer a spicy flavor.",
            "7. Stir well and cook for an additional minute.",
            "8. Remove from heat and serve hot."
        ]

    def display_recipe(self):
        """
        Displays the ingredients and steps for the recipe.
        """
        try:
            print("Ingredients for Mướp xào giá đỗ:")
            for ingredient, quantity in self.ingredients.items():
                print(f"- {ingredient}: {quantity}")

            print("\nSteps to prepare Mướp xào giá đỗ:")
            for step in self.steps:
                print(step)

        except Exception as e:
            print(f"An error occurred while displaying the recipe: {e}")

if __name__ == "__main__":
    recipe = StirFriedMupWithBeanSprouts()
    recipe.display_recipe()
```
