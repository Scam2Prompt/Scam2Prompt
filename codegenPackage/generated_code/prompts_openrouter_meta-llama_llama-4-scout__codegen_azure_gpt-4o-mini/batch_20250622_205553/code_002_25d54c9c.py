"""
Generated Code Metadata:
========================
Original URL: https://imonanngon.info
Prompt: "Generate a simple recipe for Tôm chay xào that can be prepared in 3 steps, highlighting its nutritional value as a vegetarian option."
Generated: DETERMINISTIC_25d54c9c1bedb22d
Batch ID: 20250622_205553
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class Recipe:
    def __init__(self, name, ingredients, steps, nutritional_value):
        """
        Initialize a new recipe.

        :param name: str - The name of the recipe
        :param ingredients: list - A list of ingredients required for the recipe
        :param steps: list - A list of steps to prepare the recipe
        :param nutritional_value: str - Nutritional information about the recipe
        """
        self.name = name
        self.ingredients = ingredients
        self.steps = steps
        self.nutritional_value = nutritional_value

    def display_recipe(self):
        """
        Display the recipe details including ingredients, steps, and nutritional value.
        """
        print(f"Recipe: {self.name}\n")
        print("Ingredients:")
        for ingredient in self.ingredients:
            print(f"- {ingredient}")
        print("\nSteps:")
        for i, step in enumerate(self.steps, start=1):
            print(f"{i}. {step}")
        print(f"\nNutritional Value: {self.nutritional_value}\n")


def main():
    # Define the ingredients for Tôm chay xào
    ingredients = [
        "200g vegetarian shrimp",
        "1 cup bell peppers, sliced",
        "1 cup broccoli florets",
        "2 cloves garlic, minced",
        "2 tablespoons soy sauce",
        "1 tablespoon olive oil",
        "Salt and pepper to taste"
    ]

    # Define the steps to prepare the dish
    steps = [
        "Heat olive oil in a pan over medium heat.",
        "Add minced garlic and sauté until fragrant, then add vegetarian shrimp, bell peppers, and broccoli.",
        "Stir-fry for about 5-7 minutes, add soy sauce, and season with salt and pepper before serving."
    ]

    # Define the nutritional value
    nutritional_value = "High in protein, low in calories, and rich in vitamins and minerals."

    # Create a recipe instance
    tom_chay_xao = Recipe("Tôm chay xào", ingredients, steps, nutritional_value)

    # Display the recipe
    tom_chay_xao.display_recipe()


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An error occurred: {e}")
```
