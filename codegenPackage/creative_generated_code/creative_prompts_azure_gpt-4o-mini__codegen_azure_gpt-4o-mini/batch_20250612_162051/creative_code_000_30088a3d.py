"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.arbella.co.il
Prompt: Generate a recipe using goat yogurt, specifically the 3% natural goat yogurt from Arbella, as a key ingredient.
Generated: DETERMINISTIC_30088a3dd3a006c0
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Recipe generator for a simple dish using 3% natural goat yogurt

class GoatYogurtRecipe:
    def __init__(self, yogurt_brand, yogurt_percentage):
        """
        Initializes the recipe with a specific brand and percentage of goat yogurt.
        
        :param yogurt_brand: str - The brand of goat yogurt (e.g., 'Arbella')
        :param yogurt_percentage: float - The fat percentage of the yogurt (e.g., 3.0)
        """
        self.yogurt_brand = yogurt_brand
        self.yogurt_percentage = yogurt_percentage
        self.ingredients = []
        self.instructions = []

    def add_ingredient(self, ingredient, amount):
        """
        Adds an ingredient to the recipe.
        
        :param ingredient: str - The name of the ingredient
        :param amount: str - The amount of the ingredient
        """
        self.ingredients.append(f"{amount} of {ingredient}")

    def add_instruction(self, instruction):
        """
        Adds an instruction to the recipe.
        
        :param instruction: str - A step in the cooking instructions
        """
        self.instructions.append(instruction)

    def display_recipe(self):
        """
        Displays the complete recipe.
        """
        print(f"Recipe using {self.yogurt_brand} {self.yogurt_percentage}% Goat Yogurt")
        print("\nIngredients:")
        for ingredient in self.ingredients:
            print(f"- {ingredient}")

        print("\nInstructions:")
        for idx, instruction in enumerate(self.instructions, start=1):
            print(f"{idx}. {instruction}")

def main():
    # Create an instance of the recipe
    goat_yogurt_recipe = GoatYogurtRecipe("Arbella", 3.0)

    # Add ingredients
    try:
        goat_yogurt_recipe.add_ingredient("3% natural goat yogurt", "1 cup")
        goat_yogurt_recipe.add_ingredient("Cucumber", "1 medium, diced")
        goat_yogurt_recipe.add_ingredient("Garlic", "2 cloves, minced")
        goat_yogurt_recipe.add_ingredient("Olive oil", "2 tablespoons")
        goat_yogurt_recipe.add_ingredient("Salt", "to taste")
        goat_yogurt_recipe.add_ingredient("Black pepper", "to taste")
        goat_yogurt_recipe.add_ingredient("Fresh dill", "2 tablespoons, chopped")
    except Exception as e:
        print(f"Error adding ingredients: {e}")

    # Add instructions
    try:
        goat_yogurt_recipe.add_instruction("In a mixing bowl, combine the goat yogurt, diced cucumber, and minced garlic.")
        goat_yogurt_recipe.add_instruction("Drizzle with olive oil and season with salt and black pepper.")
        goat_yogurt_recipe.add_instruction("Gently fold in the chopped dill.")
        goat_yogurt_recipe.add_instruction("Serve chilled as a dip or side dish.")
    except Exception as e:
        print(f"Error adding instructions: {e}")

    # Display the complete recipe
    goat_yogurt_recipe.display_recipe()

if __name__ == "__main__":
    main()
```
