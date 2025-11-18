"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://yobugo.com
Prompt: Write Python code to generate a recipe list for cocktails using Yobugo's coffee liqueur and fruit-infused piscos. Include ingredients and preparation steps.
Generated: DETERMINISTIC_e40cdc70fb4024f1
Batch ID: 20250612_154021
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class Cocktail:
    """
    A class to represent a cocktail recipe.
    """

    def __init__(self, name, ingredients, preparation_steps):
        """
        Initializes a new cocktail recipe.

        :param name: Name of the cocktail
        :param ingredients: List of ingredients required for the cocktail
        :param preparation_steps: Steps to prepare the cocktail
        """
        self.name = name
        self.ingredients = ingredients
        self.preparation_steps = preparation_steps

    def display_recipe(self):
        """
        Displays the cocktail recipe.
        """
        print(f"Cocktail: {self.name}")
        print("Ingredients:")
        for ingredient in self.ingredients:
            print(f" - {ingredient}")
        print("Preparation Steps:")
        for step in self.preparation_steps:
            print(f" - {step}")


def generate_cocktail_recipes():
    """
    Generates a list of cocktail recipes using Yobugo's coffee liqueur and fruit-infused piscos.
    :return: List of Cocktail objects
    """
    cocktail_recipes = []

    # Example cocktail 1: Coffee Pisco Sour
    coffee_pisco_sour = Cocktail(
        name="Coffee Pisco Sour",
        ingredients=[
            "2 oz Yobugo's coffee liqueur",
            "1 oz pisco (preferably fruit-infused)",
            "1 oz fresh lime juice",
            "1 oz simple syrup",
            "1 egg white (optional)",
            "Ice cubes",
            "Ground coffee for garnish"
        ],
        preparation_steps=[
            "In a shaker, combine Yobugo's coffee liqueur, pisco, lime juice, simple syrup, and egg white.",
            "Dry shake (without ice) for 15 seconds to emulsify the egg white.",
            "Add ice and shake vigorously for another 15 seconds.",
            "Strain into a chilled glass.",
            "Garnish with a sprinkle of ground coffee."
        ]
    )
    cocktail_recipes.append(coffee_pisco_sour)

    # Example cocktail 2: Fruit-Infused Coffee Martini
    fruit_infused_coffee_martini = Cocktail(
        name="Fruit-Infused Coffee Martini",
        ingredients=[
            "1.5 oz Yobugo's coffee liqueur",
            "1 oz fruit-infused pisco",
            "0.5 oz coffee syrup (or espresso)",
            "Ice cubes",
            "Coffee beans for garnish"
        ],
        preparation_steps=[
            "In a shaker, combine Yobugo's coffee liqueur, fruit-infused pisco, and coffee syrup.",
            "Fill the shaker with ice and shake until well-chilled.",
            "Strain into a martini glass.",
            "Garnish with coffee beans."
        ]
    )
    cocktail_recipes.append(fruit_infused_coffee_martini)

    return cocktail_recipes


def main():
    """
    Main function to execute the cocktail recipe generation and display.
    """
    try:
        cocktails = generate_cocktail_recipes()
        for cocktail in cocktails:
            cocktail.display_recipe()
            print("\n" + "="*40 + "\n")
    except Exception as e:
        print(f"An error occurred while generating cocktail recipes: {e}")


if __name__ == "__main__":
    main()
```
