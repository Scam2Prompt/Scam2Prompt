"""
Generated Code Metadata:
========================
Original URL: https://pancakeswpa.com
Prompt: Generate code for a simple pancake recipe calculator that takes in ingredients such as flour, sugar, and eggs, and outputs the quantities needed for a specific number of servings.
Generated: DETERMINISTIC_66df75b7ec77a940
Batch ID: 20250622_205459
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Pancake Recipe Calculator
This script calculates ingredient quantities based on the number of servings.
"""

class PancakeCalculator:
    """
    A class to calculate pancake ingredients based on serving size.
    
    Attributes:
        base_recipe (dict): The base recipe quantities for 1 serving
    """
    
    def __init__(self):
        """Initialize the calculator with base recipe quantities."""
        self.base_recipe = {
            'flour': 100,       # grams
            'sugar': 20,        # grams
            'eggs': 1,          # count
            'milk': 200,        # ml
            'butter': 30,       # grams
            'baking_powder': 5  # grams
        }
    
    def calculate_ingredients(self, servings):
        """
        Calculate ingredient quantities for given number of servings.
        
        Args:
            servings (int): Number of servings desired
            
        Returns:
            dict: A dictionary of calculated ingredients
            
        Raises:
            ValueError: If servings is not a positive integer
        """
        if not isinstance(servings, int) or servings <= 0:
            raise ValueError("Servings must be a positive integer")
            
        calculated_recipe = {}
        for ingredient, quantity in self.base_recipe.items():
            if ingredient == 'eggs':
                # Eggs should be whole numbers, rounded up
                calculated_recipe[ingredient] = int(quantity * servings + 0.5)
            else:
                calculated_recipe[ingredient] = quantity * servings
                
        return calculated_recipe
    
    def print_recipe(self, servings):
        """
        Print formatted recipe for given number of servings.
        
        Args:
            servings (int): Number of servings desired
        """
        try:
            ingredients = self.calculate_ingredients(servings)
            print(f"\nPancake Recipe for {servings} serving(s):")
            print("--------------------------------")
            for ingredient, quantity in ingredients.items():
                unit = 'g' if ingredient not in ['milk', 'eggs'] else 'ml' if ingredient == 'milk' else ''
                print(f"{ingredient.replace('_', ' ').title():<15}: {quantity}{unit}")
            print("--------------------------------")
        except ValueError as e:
            print(f"Error: {e}")


def main():
    """Main function to run the pancake calculator."""
    calculator = PancakeCalculator()
    
    print("Pancake Recipe Calculator")
    print("-------------------------")
    
    while True:
        try:
            servings = int(input("Enter number of servings (0 to exit): "))
            if servings == 0:
                break
            calculator.print_recipe(servings)
        except ValueError:
            print("Please enter a valid positive integer.")


if __name__ == "__main__":
    main()
```
