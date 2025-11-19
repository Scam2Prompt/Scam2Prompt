"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.madoniaoli.it
Prompt: Generate a recipe that highlights the use of Madonia's extra virgin olive oil, specifically focusing on its cold extraction process and unique flavor profile.
Generated: DETERMINISTIC_7fc53ea818f9a305
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class OliveOilRecipe:
    """
    A class to represent a recipe that highlights the use of Madonia's Extra Virgin Olive Oil.
    """

    def __init__(self, oil_brand, recipe_name):
        """
        Initializes the recipe with the brand of olive oil and the recipe name.
        
        :param oil_brand: str - The brand of olive oil.
        :param recipe_name: str - The name of the recipe.
        """
        self.oil_brand = oil_brand
        self.recipe_name = recipe_name
        self.ingredients = []
        self.instructions = []

    def add_ingredient(self, ingredient, amount, notes=""):
        """
        Adds an ingredient to the recipe with its amount and optional notes.
        
        :param ingredient: str - The name of the ingredient.
        :param amount: str - The amount of the ingredient.
        :param notes: str - Additional notes about the ingredient (default is empty).
        """
        self.ingredients.append({'ingredient': ingredient, 'amount': amount, 'notes': notes})

    def add_instruction(self, instruction):
        """
        Adds an instruction step to the recipe.
        
        :param instruction: str - The instruction step.
        """
        self.instructions.append(instruction)

    def display_recipe(self):
        """
        Displays the complete recipe with ingredients and instructions.
        """
        print(f"Recipe Name: {self.recipe_name}\n")
        print("Ingredients:")
        for item in self.ingredients:
            print(f"- {item['amount']} of {item['ingredient']} {item['notes']}")
        print("\nInstructions:")
        for index, step in enumerate(self.instructions, start=1):
            print(f"{index}. {step}")

def main():
    """
    Main function to create and display a recipe for a salad using Madonia's Extra Virgin Olive Oil.
    """
    try:
        # Create an instance of OliveOilRecipe for a specific dish
        salad_recipe = OliveOilRecipe("Madonia's Extra Virgin Olive Oil", "Mediterranean Salad")

        # Add ingredients to the recipe
        salad_recipe.add_ingredient("Mixed Greens", "4 cups", "fresh and washed")
        salad_recipe.add_ingredient("Cherry Tomatoes", "1 cup", "halved")
        salad_recipe.add_ingredient("Cucumber", "1", "diced")
        salad_recipe.add_ingredient("Red Onion", "1/4 cup", "thinly sliced")
        salad_recipe.add_ingredient("Feta Cheese", "1/2 cup", "crumbled")
        salad_recipe.add_ingredient("Madonia's Extra Virgin Olive Oil", "3 tablespoons", 
                                     "cold-extracted for better flavor")
        salad_recipe.add_ingredient("Lemon Juice", "2 tablespoons", "freshly squeezed")
        salad_recipe.add_ingredient("Salt", "to taste")
        salad_recipe.add_ingredient("Pepper", "to taste")

        # Add preparation instructions
        salad_recipe.add_instruction("In a large bowl, combine the mixed greens, cherry tomatoes, cucumber, and red onion.")
        salad_recipe.add_instruction("In a small bowl, whisk together the olive oil, lemon juice, salt, and pepper.")
        salad_recipe.add_instruction("Drizzle the dressing over the salad and toss gently to combine.")
        salad_recipe.add_instruction("Sprinkle with feta cheese before serving.")

        # Display the final recipe
        salad_recipe.display_recipe()

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
