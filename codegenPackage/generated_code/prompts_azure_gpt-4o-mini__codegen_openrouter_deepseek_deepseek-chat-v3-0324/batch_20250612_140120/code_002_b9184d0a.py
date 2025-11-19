"""
Generated Code Metadata:
========================
Original URL: https://eco-netz.net
Prompt: Create a quick recipe for Egg Cups that can be prepared in 15 minutes, including ingredients like eggs, milk, and vegetables.
Generated: DETERMINISTIC_b9184d0a3446f677
Batch ID: 20250612_140120
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import time
from typing import List, Dict, Optional

class Recipe:
    """A class to represent a quick recipe for Egg Cups."""
    
    def __init__(self, name: str, prep_time: int, cook_time: int, servings: int):
        """Initialize the Recipe with name, prep time, cook time, and servings."""
        self.name = name
        self.prep_time = prep_time
        self.cook_time = cook_time
        self.servings = servings
        self.ingredients = []
        self.instructions = []
    
    def add_ingredient(self, name: str, quantity: str, notes: Optional[str] = None):
        """Add an ingredient to the recipe.
        
        Args:
            name: Name of the ingredient.
            quantity: Quantity of the ingredient.
            notes: Optional notes about the ingredient.
        """
        ingredient = {
            'name': name,
            'quantity': quantity,
            'notes': notes
        }
        self.ingredients.append(ingredient)
    
    def add_instruction(self, step: str):
        """Add a cooking instruction step to the recipe.
        
        Args:
            step: The instruction step.
        """
        self.instructions.append(step)
    
    def display_recipe(self):
        """Display the recipe in a user-friendly format."""
        print(f"\nRecipe: {self.name}")
        print(f"Prep Time: {self.prep_time} mins | Cook Time: {self.cook_time} mins")
        print(f"Servings: {self.servings}\n")
        
        print("Ingredients:")
        for idx, ingredient in enumerate(self.ingredients, 1):
            note = f" ({ingredient['notes']})" if ingredient['notes'] else ""
            print(f"{idx}. {ingredient['name']}: {ingredient['quantity']}{note}")
        
        print("\nInstructions:")
        for idx, instruction in enumerate(self.instructions, 1):
            print(f"{idx}. {instruction}")
        
        print(f"\nTotal Time: {self.prep_time + self.cook_time} minutes")

def create_egg_cups_recipe() -> Recipe:
    """Create and return a quick Egg Cups recipe."""
    recipe = Recipe(
        name="Quick Egg Cups",
        prep_time=5,
        cook_time=10,
        servings=6
    )
    
    # Add ingredients
    recipe.add_ingredient("Eggs", "6 large")
    recipe.add_ingredient("Milk", "1/4 cup")
    recipe.add_ingredient("Bell Peppers", "1/2 cup, diced", "Any color")
    recipe.add_ingredient("Spinach", "1/2 cup, chopped", "Fresh or frozen")
    recipe.add_ingredient("Cheese", "1/4 cup, shredded", "Cheddar or mozzarella")
    recipe.add_ingredient("Salt", "1/4 tsp")
    recipe.add_ingredient("Black Pepper", "1/8 tsp")
    
    # Add instructions
    recipe.add_instruction("Preheat oven to 375°F (190°C). Grease a muffin tin.")
    recipe.add_instruction("In a bowl, whisk together eggs, milk, salt, and pepper.")
    recipe.add_instruction("Divide the diced bell peppers and spinach evenly into the muffin cups.")
    recipe.add_instruction("Pour the egg mixture over the vegetables, filling each cup about 3/4 full.")
    recipe.add_instruction("Sprinkle shredded cheese on top of each cup.")
    recipe.add_instruction("Bake for 10-12 minutes until eggs are set and slightly golden.")
    recipe.add_instruction("Let cool for 2 minutes before removing from the tin. Serve warm.")
    
    return recipe

def main():
    """Main function to display the Egg Cups recipe."""
    try:
        print("Preparing your quick Egg Cups recipe...\n")
        time.sleep(1)  # Simulate processing
        
        egg_cups = create_egg_cups_recipe()
        egg_cups.display_recipe()
        
    except Exception as e:
        print(f"An error occurred while preparing the recipe: {e}")

if __name__ == "__main__":
    main()
```
