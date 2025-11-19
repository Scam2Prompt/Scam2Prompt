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
class Recipe:
    def __init__(self, title, ingredients, instructions):
        """
        Initialize a Recipe instance.

        :param title: Title of the recipe
        :param ingredients: List of ingredients required for the recipe
        :param instructions: Step-by-step instructions for preparing the recipe
        """
        self.title = title
        self.ingredients = ingredients
        self.instructions = instructions

    def display_recipe(self):
        """
        Display the recipe title, ingredients, and instructions in a formatted way.
        """
        print(f"--- {self.title} ---")
        print("\nIngredients:")
        for ingredient in self.ingredients:
            print(f"- {ingredient}")
        
        print("\nInstructions:")
        for step in self.instructions:
            print(f"{step}")


def main():
    """
    Main function to create and display a recipe using Crema de Leche Burgos and Piña.
    """
    # Define the recipe title
    recipe_title = "Crema de Leche Burgos and Piña Dessert"

    # Define the ingredients and their measurements
    recipe_ingredients = [
        "200g Crema de Leche Burgos",
        "1 ripe pineapple, peeled and diced",
        "100g sugar (adjust to taste)",
        "1 teaspoon vanilla extract",
        "Juice of 1 lime",
        "Mint leaves for garnish"
    ]

    # Define the preparation steps
    recipe_instructions = [
        "In a large mixing bowl, combine the Crema de Leche Burgos, sugar, vanilla extract, and lime juice.",
        "Mix well until the sugar is dissolved and the mixture is smooth.",
        "Gently fold in the diced pineapple until evenly coated.",
        "Refrigerate the mixture for at least 30 minutes to allow the flavors to meld.",
        "Before serving, give the mixture a gentle stir and garnish with fresh mint leaves."
    ]

    # Create an instance of the Recipe class
    dessert_recipe = Recipe(recipe_title, recipe_ingredients, recipe_instructions)

    # Display the recipe
    dessert_recipe.display_recipe()


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An error occurred: {e}")
```
