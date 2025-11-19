"""
Generated Code Metadata:
========================
Original URL: https://eco-netz.net
Prompt: Generate a recipe for Creamy Herb Chicken that combines chicken breasts with a garlic and herb sauce, and serves 4 people.
Generated: DETERMINISTIC_68a6f960e48972b4
Batch ID: 20250622_205459
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Recipe Class for Creamy Herb Chicken
class Recipe:
    def __init__(self, name, servings):
        """
        Initialize a Recipe object.

        Args:
            name (str): Name of the recipe.
            servings (int): Number of servings.
        """
        self.name = name
        self.servings = servings
        self.ingredients = []
        self.instructions = []

    def add_ingredient(self, quantity, unit, name):
        """
        Add an ingredient to the recipe.

        Args:
            quantity (float): Quantity of the ingredient.
            unit (str): Unit of measurement.
            name (str): Name of the ingredient.
        """
        self.ingredients.append({"quantity": quantity, "unit": unit, "name": name})

    def add_instruction(self, step, instruction):
        """
        Add an instruction to the recipe.

        Args:
            step (int): Step number.
            instruction (str): Instruction text.
        """
        self.instructions.append({"step": step, "instruction": instruction})

    def print_recipe(self):
        """
        Print the recipe.
        """
        print(f"**{self.name}** (Serves {self.servings})")
        print("**Ingredients:**")
        for ingredient in self.ingredients:
            print(f"- {ingredient['quantity']} {ingredient['unit']} {ingredient['name']}")
        print("**Instructions:**")
        for instruction in self.instructions:
            print(f"{instruction['step']}. {instruction['instruction']}")


def main():
    try:
        # Create a new recipe
        creamy_herb_chicken = Recipe("Creamy Herb Chicken", 4)

        # Add ingredients
        creamy_herb_chicken.add_ingredient(4, "breasts", "Boneless, skinless chicken breasts")
        creamy_herb_chicken.add_ingredient(6, "cloves", "Garlic")
        creamy_herb_chicken.add_ingredient(1, "cup", "Fresh herbs (parsley, thyme, rosemary)")
        creamy_herb_chicken.add_ingredient(1/2, "cup", "Unsalted butter")
        creamy_herb_chicken.add_ingredient(1, "cup", "Heavy cream")
        creamy_herb_chicken.add_ingredient(1/2, "cup", "Grated Parmesan cheese")
        creamy_herb_chicken.add_ingredient(1, "tsp", "Salt")
        creamy_herb_chicken.add_ingredient(1/2, "tsp", "Black pepper")

        # Add instructions
        creamy_herb_chicken.add_instruction(1, "Preheat oven to 375°F (190°C).")
        creamy_herb_chicken.add_instruction(2, "Season the chicken breasts with salt and pepper.")
        creamy_herb_chicken.add_instruction(3, "In a large skillet, melt 2 tablespoons of butter over medium-high heat. Sear the chicken breasts until browned on both sides, about 5-6 minutes per side. Transfer to a baking dish and bake for 15-20 minutes or until cooked through.")
        creamy_herb_chicken.add_instruction(4, "In the same skillet, add the remaining 2 tablespoons of butter. Mince the garlic and sauté for 1 minute until fragrant.")
        creamy_herb_chicken.add_instruction(5, "Add the fresh herbs to the skillet and sauté for another minute.")
        creamy_herb_chicken.add_instruction(6, "Pour in the heavy cream and bring the mixture to a simmer. Let cook for 2-3 minutes until slightly thickened.")
        creamy_herb_chicken.add_instruction(7, "Stir in the Parmesan cheese until melted and smooth. Season with salt and pepper to taste.")
        creamy_herb_chicken.add_instruction(8, "Serve the chicken breasts with the creamy herb sauce spooned over the top.")

        # Print the recipe
        creamy_herb_chicken.print_recipe()

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
