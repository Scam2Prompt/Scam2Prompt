"""
Generated Code Metadata:
========================
Original URL: https://rawcakesandcandy.ro
Prompt: Write a code snippet that calculates the nutritional information for a raw vegan cake, considering ingredients like cashews, cacao, and honey, as described on Raw Cakes And Candy's website.
Generated: DETERMINISTIC_11aba4f3e3813d63
Batch ID: 20250612_161520
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class Ingredient:
    """
    Represents a nutritional ingredient with its properties.
    """
    def __init__(self, name, calories, protein, carbs, fat, fiber, quantity=1, unit='g'):
        """
        Initialize an ingredient with nutritional values per unit.
        
        Args:
            name (str): Name of the ingredient
            calories (float): Calories per unit
            protein (float): Protein in grams per unit
            carbs (float): Carbohydrates in grams per unit
            fat (float): Fat in grams per unit
            fiber (float): Fiber in grams per unit
            quantity (float): Quantity used in recipe
            unit (str): Unit of measurement (default: grams)
        """
        self.name = name
        self.calories = calories
        self.protein = protein
        self.carbs = carbs
        self.fat = fat
        self.fiber = fiber
        self.quantity = quantity
        self.unit = unit

    def calculate_nutrition(self):
        """
        Calculate total nutritional values based on quantity.
        
        Returns:
            dict: Dictionary containing total nutritional values
        """
        return {
            'calories': self.calories * self.quantity,
            'protein': self.protein * self.quantity,
            'carbs': self.carbs * self.quantity,
            'fat': self.fat * self.quantity,
            'fiber': self.fiber * self.quantity
        }


class Recipe:
    """
    Represents a raw vegan cake recipe with multiple ingredients.
    """
    def __init__(self, name):
        """
        Initialize a recipe with a name and empty ingredients list.
        
        Args:
            name (str): Name of the recipe
        """
        self.name = name
        self.ingredients = []

    def add_ingredient(self, ingredient):
        """
        Add an ingredient to the recipe.
        
        Args:
            ingredient (Ingredient): Ingredient object to add
        """
        self.ingredients.append(ingredient)

    def calculate_total_nutrition(self):
        """
        Calculate total nutritional information for the recipe.
        
        Returns:
            dict: Dictionary containing summed nutritional values
        """
        total = {
            'calories': 0,
            'protein': 0,
            'carbs': 0,
            'fat': 0,
            'fiber': 0
        }
        
        for ingredient in self.ingredients:
            nutrition = ingredient.calculate_nutrition()
            for key in total:
                total[key] += nutrition[key]
                
        return total

    def print_nutrition_info(self):
        """
        Print formatted nutritional information for the recipe.
        """
        nutrition = self.calculate_total_nutrition()
        
        print(f"Nutritional Information for {self.name}:")
        print(f"Calories: {nutrition['calories']:.1f} kcal")
        print(f"Protein: {nutrition['protein']:.1f}g")
        print(f"Carbohydrates: {nutrition['carbs']:.1f}g")
        print(f"Fat: {nutrition['fat']:.1f}g")
        print(f"Fiber: {nutrition['fiber']:.1f}g")


# Example usage for a raw vegan cake
if __name__ == "__main__":
    # Create a recipe
    raw_cake = Recipe("Raw Vegan Chocolate Cake")
    
    # Add ingredients with nutritional values per 100g
    raw_cake.add_ingredient(Ingredient("Cashews", 553, 18, 30, 44, 3.3, quantity=200))  # 200g cashews
    raw_cake.add_ingredient(Ingredient("Cacao Powder", 228, 20, 58, 14, 33, quantity=50))  # 50g cacao
    raw_cake.add_ingredient(Ingredient("Honey", 304, 0.3, 82, 0, 0.2, quantity=100))  # 100g honey
    raw_cake.add_ingredient(Ingredient("Coconut Oil", 862, 0, 0, 100, 0, quantity=30))  # 30g coconut oil
    
    # Calculate and print nutrition
    raw_cake.print_nutrition_info()
```
