"""
Generated Code Metadata:
========================
Original URL: https://pinkpolkadotcreations.com
Prompt: "Generate a recipe for a cake, similar to the Chocolate Syrup Cake, and provide instructions for adapting it into a printable recipe card using a tool like Canva or Adobe Illustrator."
Generated: DETERMINISTIC_d59744e405ca7d0a
Batch ID: 20250622_212625
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# recipe_generator.py

class Recipe:
    def __init__(self, name, ingredients, instructions):
        """
        Initialize a Recipe object.

        Args:
            name (str): The name of the recipe.
            ingredients (list): A list of ingredient dictionaries.
            instructions (list): A list of instruction strings.
        """
        self.name = name
        self.ingredients = ingredients
        self.instructions = instructions

    def to_dict(self):
        """
        Convert the Recipe object to a dictionary.

        Returns:
            dict: A dictionary representation of the Recipe object.
        """
        return {
            "name": self.name,
            "ingredients": self.ingredients,
            "instructions": self.instructions,
        }

    def generate_printable_recipe(self):
        """
        Generate a printable recipe card.

        Returns:
            str: A string representation of the printable recipe card.
        """
        recipe_card = f"**{self.name}**\n\n"

        # Ingredients section
        recipe_card += "**Ingredients:**\n"
        for ingredient in self.ingredients:
            recipe_card += f"- {ingredient['quantity']} {ingredient['unit']} {ingredient['name']}\n"

        # Instructions section
        recipe_card += "\n**Instructions:**\n"
        for i, instruction in enumerate(self.instructions, start=1):
            recipe_card += f"{i}. {instruction}\n"

        return recipe_card


def generate_chocolate_syrup_cake_recipe():
    """
    Generate a recipe for a cake similar to the Chocolate Syrup Cake.

    Returns:
        Recipe: A Recipe object for the Chocolate Syrup Cake.
    """
    name = "Moist Chocolate Cake"

    ingredients = [
        {"name": "all-purpose flour", "quantity": 2, "unit": "cups"},
        {"name": "granulated sugar", "quantity": 1.5, "unit": "cups"},
        {"name": "unsweetened cocoa powder", "quantity": 1, "unit": "cup"},
        {"name": "baking powder", "quantity": 2, "unit": "teaspoons"},
        {"name": "salt", "quantity": 1, "unit": "teaspoon"},
        {"name": "whole milk", "quantity": 1, "unit": "cup"},
        {"name": "large eggs", "quantity": 2, "unit": ""},
        {"name": "vegetable oil", "quantity": 1, "unit": "cup"},
        {"name": "chocolate syrup", "quantity": 1, "unit": "cup"},
    ]

    instructions = [
        "Preheat the oven to 350°F (180°C). Grease two 9-inch round cake pans.",
        "In a medium bowl, whisk together flour, sugar, cocoa powder, baking powder, and salt.",
        "In a large bowl, whisk together milk, eggs, and vegetable oil.",
        "Add the dry ingredients to the wet ingredients and whisk until smooth.",
        "Pour in the chocolate syrup and whisk until well combined.",
        "Divide the batter evenly between the prepared pans.",
        "Bake for 30-35 minutes or until a toothpick inserted comes out clean.",
        "Let the cakes cool in the pans for 10 minutes before transferring to a wire rack to cool completely.",
    ]

    return Recipe(name, ingredients, instructions)


def main():
    try:
        recipe = generate_chocolate_syrup_cake_recipe()
        printable_recipe = recipe.generate_printable_recipe()
        print(printable_recipe)

        # Example usage with Canva or Adobe Illustrator:
        # You can copy the printable recipe string and paste it into Canva or Adobe Illustrator
        # to create a visually appealing recipe card.

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
