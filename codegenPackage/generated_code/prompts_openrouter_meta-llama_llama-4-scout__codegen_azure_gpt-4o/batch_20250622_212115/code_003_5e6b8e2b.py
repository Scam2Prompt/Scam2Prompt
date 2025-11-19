"""
Generated Code Metadata:
========================
Original URL: https://pancakesrus.net
Prompt: Write a code snippet to calculate the nutritional information of a meal, considering factors like lean protein, good fats, and complex carbohydrates, as discussed in the Iron Man Healthy Choices section of PancakesRus.
Generated: DETERMINISTIC_5e6b8e2bd124ee0d
Batch ID: 20250622_212115
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
import json

# Define a class to represent a food item
class FoodItem:
    def __init__(self, name, protein, fats, carbs, calories):
        """
        Initialize a food item with its nutritional values.
        :param name: Name of the food item (str)
        :param protein: Amount of protein in grams (float)
        :param fats: Amount of fats in grams (float)
        :param carbs: Amount of carbohydrates in grams (float)
        :param calories: Total calories (float)
        """
        self.name = name
        self.protein = protein
        self.fats = fats
        self.carbs = carbs
        self.calories = calories

# Define a function to calculate the total nutritional information of a meal
def calculate_meal_nutrition(food_items):
    """
    Calculate the total nutritional values for a meal.
    :param food_items: List of FoodItem objects
    :return: Dictionary containing total protein, fats, carbs, and calories
    """
    total_protein = 0.0
    total_fats = 0.0
    total_carbs = 0.0
    total_calories = 0.0

    for item in food_items:
        total_protein += item.protein
        total_fats += item.fats
        total_carbs += item.carbs
        total_calories += item.calories

    return {
        "total_protein": round(total_protein, 2),
        "total_fats": round(total_fats, 2),
        "total_carbs": round(total_carbs, 2),
        "total_calories": round(total_calories, 2),
    }

# Define a function to display nutritional information in a user-friendly format
def display_nutrition_info(nutrition_info):
    """
    Display the nutritional information in a readable format.
    :param nutrition_info: Dictionary containing nutritional values
    """
    print("Meal Nutritional Information:")
    print(f"  Total Protein: {nutrition_info['total_protein']} g")
    print(f"  Total Fats: {nutrition_info['total_fats']} g")
    print(f"  Total Carbohydrates: {nutrition_info['total_carbs']} g")
    print(f"  Total Calories: {nutrition_info['total_calories']} kcal")

# Example usage
if __name__ == "__main__":
    try:
        # Define food items for the meal
        food_items = [
            FoodItem("Grilled Chicken Breast", protein=31.0, fats=3.6, carbs=0.0, calories=165.0),
            FoodItem("Avocado", protein=2.0, fats=15.0, carbs=9.0, calories=160.0),
            FoodItem("Quinoa", protein=8.0, fats=2.0, carbs=39.0, calories=222.0),
        ]

        # Calculate the total nutritional information
        nutrition_info = calculate_meal_nutrition(food_items)

        # Display the nutritional information
        display_nutrition_info(nutrition_info)

    except Exception as e:
        # Handle unexpected errors gracefully
        print(f"An error occurred: {e}")
```
