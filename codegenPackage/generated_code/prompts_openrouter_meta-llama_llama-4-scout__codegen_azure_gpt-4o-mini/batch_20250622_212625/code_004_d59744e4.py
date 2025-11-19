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
class CakeRecipe:
    """
    A class to represent a cake recipe.
    """

    def __init__(self, name, ingredients, instructions):
        """
        Initializes the CakeRecipe with a name, ingredients, and instructions.

        :param name: str - The name of the cake.
        :param ingredients: list - A list of ingredients required for the cake.
        :param instructions: list - A list of instructions to prepare the cake.
        """
        self.name = name
        self.ingredients = ingredients
        self.instructions = instructions

    def display_recipe(self):
        """
        Displays the recipe in a formatted manner.
        """
        print(f"Recipe for: {self.name}\n")
        print("Ingredients:")
        for ingredient in self.ingredients:
            print(f"- {ingredient}")
        print("\nInstructions:")
        for step in self.instructions:
            print(f"{step}")

    def save_to_file(self, filename):
        """
        Saves the recipe to a text file.

        :param filename: str - The name of the file to save the recipe.
        """
        try:
            with open(filename, 'w') as file:
                file.write(f"Recipe for: {self.name}\n\n")
                file.write("Ingredients:\n")
                for ingredient in self.ingredients:
                    file.write(f"- {ingredient}\n")
                file.write("\nInstructions:\n")
                for step in self.instructions:
                    file.write(f"{step}\n")
            print(f"Recipe saved to {filename}")
        except IOError as e:
            print(f"Error saving recipe to file: {e}")

# Define the Chocolate Syrup Cake recipe
cake_name = "Chocolate Syrup Cake"
cake_ingredients = [
    "1 cup all-purpose flour",
    "1 cup sugar",
    "1/2 cup unsweetened cocoa powder",
    "1 tsp baking powder",
    "1/2 tsp salt",
    "1/2 cup milk",
    "1/4 cup vegetable oil",
    "1 tsp vanilla extract",
    "1/2 cup chocolate syrup",
    "1/2 cup boiling water"
]
cake_instructions = [
    "Preheat the oven to 350°F (175°C).",
    "Grease and flour a 9-inch round cake pan.",
    "In a large bowl, mix flour, sugar, cocoa powder, baking powder, and salt.",
    "Add milk, vegetable oil, vanilla extract, and chocolate syrup to the dry ingredients.",
    "Mix until well combined.",
    "Stir in boiling water until the batter is smooth.",
    "Pour the batter into the prepared cake pan.",
    "Bake for 30-35 minutes or until a toothpick inserted in the center comes out clean.",
    "Let the cake cool in the pan for 10 minutes, then transfer to a wire rack to cool completely."
]

# Create a CakeRecipe instance
chocolate_syrup_cake = CakeRecipe(cake_name, cake_ingredients, cake_instructions)

# Display the recipe
chocolate_syrup_cake.display_recipe()

# Save the recipe to a file
chocolate_syrup_cake.save_to_file("chocolate_syrup_cake_recipe.txt")
```

### Instructions for Adapting into a Printable Recipe Card:
1. **Open Canva or Adobe Illustrator**: Start a new project with the dimensions suitable for a recipe card (e.g., 5x7 inches).
2. **Choose a Template**: Select a recipe card template that fits your style.
3. **Add Title**: Insert the title "Chocolate Syrup Cake" at the top of the card.
4. **List Ingredients**: Create a section for ingredients and copy the list from the code.
5. **Add Instructions**: Create another section for instructions and copy the steps from the code.
6. **Design Elements**: Customize the card with colors, images, and fonts to enhance its visual appeal.
7. **Export**: Once satisfied, export the design as a PDF or image file for printing.
