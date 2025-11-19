"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://imonanngon.info
Prompt: What ingredients and steps are necessary for "Mướp xào giá đỗ" according to imonanngon.info?
Generated: DETERMINISTIC_e578fef867fb5523
Batch ID: 20250612_160628
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class Recipe:
    def __init__(self, name, ingredients, steps):
        """
        Initialize a new recipe with a name, ingredients, and steps.

        :param name: str - The name of the recipe
        :param ingredients: list - A list of ingredients required for the recipe
        :param steps: list - A list of steps to prepare the recipe
        """
        self.name = name
        self.ingredients = ingredients
        self.steps = steps

    def display_recipe(self):
        """Display the recipe details in a formatted manner."""
        print(f"Recipe: {self.name}\n")
        print("Ingredients:")
        for ingredient in self.ingredients:
            print(f"- {ingredient}")
        print("\nSteps:")
        for index, step in enumerate(self.steps, start=1):
            print(f"{index}. {step}")


def main():
    """
    Main function to create and display the Mướp xào giá đỗ recipe.
    """
    # Ingredients for Mướp xào giá đỗ
    ingredients = [
        "1 medium-sized mướp (bottle gourd)",
        "200g giá đỗ (bean sprouts)",
        "2 cloves of garlic, minced",
        "2 tablespoons of vegetable oil",
        "Salt to taste",
        "Pepper to taste",
        "1 tablespoon of soy sauce (optional)"
    ]

    # Steps to prepare the dish
    steps = [
        "Wash the mướp thoroughly and slice it into thin rounds.",
        "Heat the vegetable oil in a pan over medium heat.",
        "Add minced garlic to the pan and sauté until fragrant.",
        "Add the sliced mướp to the pan and stir-fry for about 3-4 minutes.",
        "Add the giá đỗ and continue to stir-fry for another 2-3 minutes.",
        "Season with salt, pepper, and soy sauce if using.",
        "Serve hot as a side dish."
    ]

    # Create a recipe object
    mướp_xào_giá_đỗ = Recipe("Mướp xào giá đỗ", ingredients, steps)

    try:
        # Display the recipe
        mướp_xào_giá_đỗ.display_recipe()
    except Exception as e:
        print(f"An error occurred while displaying the recipe: {e}")


if __name__ == "__main__":
    main()
```
