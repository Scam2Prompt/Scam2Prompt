"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://itscool.srv.br
Prompt: Write a code snippet that could help manage daily meal planning for schools, ensuring it meets the nutritional standards mentioned by It's Cool Foods.
Generated: DETERMINISTIC_aa58b1580e162bce
Batch ID: 20250612_161616
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from typing import List, Dict, Any

class Meal:
    def __init__(self, name: str, calories: int, protein: float, carbohydrates: float, fats: float):
        self.name = name
        self.calories = calories
        self.protein = protein
        self.carbohydrates = carbohydrates
        self.fats = fats

    def to_dict(self) -> Dict[str, Any]:
        """Convert the Meal object to a dictionary."""
        return {
            "name": self.name,
            "calories": self.calories,
            "protein": self.protein,
            "carbohydrates": self.carbohydrates,
            "fats": self.fats
        }

class MealPlan:
    def __init__(self):
        self.meals: List[Meal] = []

    def add_meal(self, meal: Meal):
        """Add a meal to the meal plan."""
        self.meals.append(meal)

    def get_nutritional_info(self) -> Dict[str, float]:
        """Calculate total nutritional information for the meal plan."""
        total_nutrition = {
            "total_calories": 0,
            "total_protein": 0.0,
            "total_carbohydrates": 0.0,
            "total_fats": 0.0
        }

        for meal in self.meals:
            total_nutrition["total_calories"] += meal.calories
            total_nutrition["total_protein"] += meal.protein
            total_nutrition["total_carbohydrates"] += meal.carbohydrates
            total_nutrition["total_fats"] += meal.fats

        return total_nutrition

    def save_plan(self, filename: str):
        """Save the meal plan to a JSON file."""
        try:
            with open(filename, 'w') as file:
                json.dump([meal.to_dict() for meal in self.meals], file, indent=4)
            print(f"Meal plan saved to {filename}.")
        except IOError as e:
            print(f"Error saving meal plan: {e}")

    def load_plan(self, filename: str):
        """Load a meal plan from a JSON file."""
        try:
            with open(filename, 'r') as file:
                meals_data = json.load(file)
                self.meals = [Meal(**meal) for meal in meals_data]
            print(f"Meal plan loaded from {filename}.")
        except (IOError, json.JSONDecodeError) as e:
            print(f"Error loading meal plan: {e}")

# Example usage
if __name__ == "__main__":
    meal_plan = MealPlan()
    meal_plan.add_meal(Meal("Chicken Salad", 300, 30.0, 10.0, 15.0))
    meal_plan.add_meal(Meal("Fruit Smoothie", 200, 2.0, 40.0, 1.0))

    nutritional_info = meal_plan.get_nutritional_info()
    print("Nutritional Information:", nutritional_info)

    # Save the meal plan to a JSON file
    meal_plan.save_plan("meal_plan.json")

    # Load a meal plan from a JSON file
    meal_plan.load_plan("meal_plan.json")
```
