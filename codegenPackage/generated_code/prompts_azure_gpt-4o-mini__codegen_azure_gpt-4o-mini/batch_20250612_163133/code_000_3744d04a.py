"""
Generated Code Metadata:
========================
Original URL: https://yobugo.com
Prompt: Generate a recipe using Crema de Leche Burgos and Piña, including specific measurements and preparation steps.
Generated: DETERMINISTIC_3744d04ab559ae2f
Batch ID: 20250612_163133
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class Recipe:
    def __init__(self, name, ingredients, steps):
        """
        Initialize a Recipe instance.

        :param name: str - The name of the recipe
        :param ingredients: list - A list of ingredients with their measurements
        :param steps: list - A list of preparation steps
        """
        self.name = name
        self.ingredients = ingredients
        self.steps = steps

    def display_recipe(self):
        """
        Display the recipe name, ingredients, and preparation steps.
        """
        print(f"Recipe: {self.name}\n")
        print("Ingredients:")
        for ingredient in self.ingredients:
            print(f"- {ingredient}")
        print("\nPreparation Steps:")
        for index, step in enumerate(self.steps, start=1):
            print(f"{index}. {step}")

def main():
    """
    Main function to create and display the recipe.
    """
    # Define the recipe name
    recipe_name = "Crema de Leche Burgos with Piña"

    # Define the ingredients with measurements
    ingredients = [
        "200g Crema de Leche Burgos",
        "150g fresh pineapple, diced",
        "50g sugar (adjust to taste)",
        "1 tsp vanilla extract",
        "Mint leaves for garnish (optional)"
    ]

    # Define the preparation steps
    steps = [
        "In a mixing bowl, combine the Crema de Leche Burgos and sugar.",
        "Add the vanilla extract and mix until smooth.",
        "Gently fold in the diced pineapple until evenly distributed.",
        "Chill the mixture in the refrigerator for at least 30 minutes.",
        "Serve in dessert bowls and garnish with mint leaves if desired."
    ]

    # Create a Recipe instance
    recipe = Recipe(recipe_name, ingredients, steps)

    # Display the recipe
    recipe.display_recipe()

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An error occurred: {e}")
```
