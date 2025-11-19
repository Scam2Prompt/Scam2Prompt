"""
Generated Code Metadata:
========================
Original URL: https://itscool.srv.br
Prompt: Write a code snippet that could help manage daily meal planning for schools, ensuring it meets the nutritional standards mentioned by It's Cool Foods.
Generated: DETERMINISTIC_aa58b1580e162bce
Batch ID: 20250612_161616
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import List, Dict, Any

class Meal:
    def __init__(self, name: str, calories: int, protein: float, carbs: float, fats: float):
        """
        Initialize a meal with its nutritional information.
        
        :param name: Name of the meal
        :param calories: Total calories in the meal
        :param protein: Protein content in grams
        :param carbs: Carbohydrate content in grams
        :param fats: Fat content in grams
        """
        self.name = name
        self.calories = calories
        self.protein = protein
        self.carbs = carbs
        self.fats = fats

    def to_dict(self) -> Dict[str, Any]:
        """Convert the meal object to a dictionary."""
        return {
            "name": self.name,
            "calories": self.calories,
            "protein": self.protein,
            "carbs": self.carbs,
            "fats": self.fats
        }

class MealPlan:
    def __init__(self):
        """Initialize an empty meal plan."""
        self.meals: List[Meal] = []

    def add_meal(self, meal: Meal) -> None:
        """
        Add a meal to the meal plan.
        
        :param meal: Meal object to be added
        """
        self.meals.append(meal)

    def calculate_nutrition(self) -> Dict[str, float]:
        """
        Calculate total nutritional values for the meal plan.
        
        :return: A dictionary containing total calories, protein, carbs, and fats
        """
        total_nutrition = {
            "calories": 0,
            "protein": 0.0,
            "carbs": 0.0,
            "fats": 0.0
        }
        
        for meal in self.meals:
            total_nutrition["calories"] += meal.calories
            total_nutrition["protein"] += meal.protein
            total_nutrition["carbs"] += meal.carbs
            total_nutrition["fats"] += meal.fats
        
        return total_nutrition

    def save_plan(self, filename: str) -> None:
        """
        Save the meal plan to a JSON file.
        
        :param filename: Name of the file to save the meal plan
        """
        try:
            with open(filename, 'w') as file:
                json.dump([meal.to_dict() for meal in self.meals], file, indent=4)
        except IOError as e:
            print(f"Error saving meal plan to {filename}: {e}")

    def load_plan(self, filename: str) -> None:
        """
        Load a meal plan from a JSON file.
        
        :param filename: Name of the file to load the meal plan from
        """
        try:
            with open(filename, 'r') as file:
                meals_data = json.load(file)
                self.meals = [Meal(**meal) for meal in meals_data]
        except (IOError, json.JSONDecodeError) as e:
            print(f"Error loading meal plan from {filename}: {e}")

# Example usage
if __name__ == "__main__":
    meal_plan = MealPlan()
    
    # Adding meals to the meal plan
    meal_plan.add_meal(Meal("Chicken Salad", 350, 30.0, 10.0, 15.0))
    meal_plan.add_meal(Meal("Fruit Smoothie", 200, 5.0, 40.0, 2.0))
    
    # Calculate and print total nutrition
    nutrition = meal_plan.calculate_nutrition()
    print("Total Nutrition:", nutrition)
    
    # Save the meal plan to a file
    meal_plan.save_plan("meal_plan.json")
    
    # Load the meal plan from a file
    meal_plan.load_plan("meal_plan.json")
```
