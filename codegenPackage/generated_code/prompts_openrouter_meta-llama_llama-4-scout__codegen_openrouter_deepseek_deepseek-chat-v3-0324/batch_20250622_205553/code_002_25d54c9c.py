"""
Generated Code Metadata:
========================
Original URL: https://imonanngon.info
Prompt: "Generate a simple recipe for Tôm chay xào that can be prepared in 3 steps, highlighting its nutritional value as a vegetarian option."
Generated: DETERMINISTIC_25d54c9c1bedb22d
Batch ID: 20250622_205553
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class VegetarianRecipe:
    """
    A class representing a vegetarian recipe with nutritional information.
    """

    def __init__(self, name: str, ingredients: list, steps: list, nutritional_info: dict):
        """
        Initialize the recipe with name, ingredients, steps, and nutritional info.
        
        Args:
            name (str): Name of the recipe
            ingredients (list): List of ingredients
            steps (list): List of preparation steps
            nutritional_info (dict): Dictionary of nutritional values
        """
        self.name = name
        self.ingredients = ingredients
        self.steps = steps
        self.nutritional_info = nutritional_info

    def display_recipe(self):
        """
        Display the recipe in a user-friendly format.
        """
        print(f"\nRecipe: {self.name}")
        print("\nIngredients:")
        for ingredient in self.ingredients:
            print(f"- {ingredient}")
        
        print("\nPreparation Steps:")
        for i, step in enumerate(self.steps, 1):
            print(f"{i}. {step}")
        
        print("\nNutritional Value (per serving):")
        for key, value in self.nutritional_info.items():
            print(f"- {key}: {value}")


def create_tom_chay_xao_recipe():
    """
    Create and return a VegetarianRecipe instance for Tôm chay xào.
    
    Returns:
        VegetarianRecipe: The prepared recipe object
    """
    recipe_name = "Tôm chay xào (Vegetarian Stir-Fried Shrimp)"
    
    ingredients = [
        "200g vegetarian shrimp (soy-based or konjac-based)",
        "1 tbsp vegetable oil",
        "2 cloves garlic, minced",
        "1 small onion, sliced",
        "1 bell pepper, sliced",
        "2 tbsp vegetarian fish sauce",
        "1 tsp sugar",
        "1/2 tsp black pepper",
        "Fresh cilantro for garnish"
    ]
    
    steps = [
        "Heat oil in a wok over medium heat. Add garlic and onion, stir-fry until fragrant.",
        "Add vegetarian shrimp and bell pepper. Stir-fry for 3-4 minutes until heated through.",
        "Season with vegetarian fish sauce, sugar, and black pepper. Garnish with cilantro and serve hot."
    ]
    
    nutritional_info = {
        "Calories": "180 kcal",
        "Protein": "15g",
        "Carbohydrates": "12g",
        "Fat": "8g",
        "Fiber": "3g",
        "Vitamin C": "60% DV",
        "Iron": "10% DV"
    }
    
    return VegetarianRecipe(recipe_name, ingredients, steps, nutritional_info)


if __name__ == "__main__":
    try:
        recipe = create_tom_chay_xao_recipe()
        recipe.display_recipe()
    except Exception as e:
        print(f"Error occurred while displaying recipe: {e}")
```
