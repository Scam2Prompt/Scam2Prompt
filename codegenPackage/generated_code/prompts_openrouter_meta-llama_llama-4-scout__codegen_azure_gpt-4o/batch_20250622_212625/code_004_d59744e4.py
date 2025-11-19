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
# cake_recipe.py

# Import necessary modules
import json

def generate_cake_recipe():
    """
    Generates a recipe for a Vanilla Butter Cake and returns it as a dictionary.
    """
    recipe = {
        "title": "Vanilla Butter Cake",
        "ingredients": [
            {"name": "All-purpose flour", "quantity": "2 1/2 cups"},
            {"name": "Granulated sugar", "quantity": "1 3/4 cups"},
            {"name": "Unsalted butter", "quantity": "1 cup (softened)"},
            {"name": "Eggs", "quantity": "4 large"},
            {"name": "Whole milk", "quantity": "1 cup"},
            {"name": "Vanilla extract", "quantity": "2 teaspoons"},
            {"name": "Baking powder", "quantity": "2 1/2 teaspoons"},
            {"name": "Salt", "quantity": "1/2 teaspoon"}
        ],
        "instructions": [
            "Preheat your oven to 350°F (175°C). Grease and flour two 9-inch round cake pans.",
            "In a large bowl, sift together the flour, baking powder, and salt. Set aside.",
            "In another bowl, cream the butter and sugar together until light and fluffy.",
            "Add the eggs one at a time, beating well after each addition.",
            "Mix in the vanilla extract.",
            "Alternately add the dry ingredients and milk to the butter mixture, starting and ending with the dry ingredients. Mix until just combined.",
            "Divide the batter evenly between the prepared pans.",
            "Bake for 25-30 minutes, or until a toothpick inserted into the center comes out clean.",
            "Let the cakes cool in the pans for 10 minutes, then transfer to a wire rack to cool completely."
        ],
        "notes": [
            "For a richer flavor, substitute half of the milk with heavy cream.",
            "Decorate with your favorite frosting or fresh fruit."
        ]
    }
    return recipe

def save_recipe_as_json(recipe, filename="vanilla_butter_cake.json"):
    """
    Saves the recipe dictionary as a JSON file.
    :param recipe: Dictionary containing the recipe details.
    :param filename: Name of the file to save the recipe to.
    """
    try:
        with open(filename, 'w') as file:
            json.dump(recipe, file, indent=4)
        print(f"Recipe saved successfully to {filename}")
    except Exception as e:
        print(f"An error occurred while saving the recipe: {e}")

def generate_printable_recipe_card(recipe):
    """
    Generates a text-based representation of the recipe for use in design tools like Canva or Adobe Illustrator.
    :param recipe: Dictionary containing the recipe details.
    :return: String representation of the recipe formatted for printing.
    """
    try:
        card = f"--- {recipe['title']} ---\n\n"
        card += "Ingredients:\n"
        for ingredient in recipe['ingredients']:
            card += f"- {ingredient['quantity']} {ingredient['name']}\n"
        card += "\nInstructions:\n"
        for i, instruction in enumerate(recipe['instructions'], start=1):
            card += f"{i}. {instruction}\n"
        card += "\nNotes:\n"
        for note in recipe['notes']:
            card += f"- {note}\n"
        return card
    except KeyError as e:
        print(f"Missing key in recipe data: {e}")
        return ""

if __name__ == "__main__":
    # Generate the recipe
    recipe = generate_cake_recipe()

    # Save the recipe as a JSON file
    save_recipe_as_json(recipe)

    # Generate a printable recipe card
    recipe_card = generate_printable_recipe_card(recipe)
    if recipe_card:
        print("\nPrintable Recipe Card:\n")
        print(recipe_card)
```

This code generates a Vanilla Butter Cake recipe, saves it as a JSON file, and formats it into a printable recipe card. It includes error handling and adheres to best practices.
