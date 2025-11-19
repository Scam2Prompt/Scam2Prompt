"""
Generated Code Metadata:
========================
Original URL: https://neighborgoods.com
Prompt: Design a nutrition consulting service that provides personalized meal plans, incorporating Japanese culinary traditions and locally sourced ingredients, inspired by Kenko Fitness Solutions' services.
Generated: DETERMINISTIC_b2197343b8a2058c
Batch ID: 20250622_205355
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# nutrition_consulting_service.py

from typing import Dict, List
from enum import Enum
from dataclasses import dataclass

class DietaryPreference(Enum):
    """Enum for dietary preferences"""
    VEGETARIAN = 1
    VEGAN = 2
    GLUTEN_FREE = 3
    DAIRY_FREE = 4

@dataclass
class Ingredient:
    """Dataclass for ingredients"""
    name: str
    quantity: str
    unit: str

@dataclass
class Meal:
    """Dataclass for meals"""
    name: str
    ingredients: List[Ingredient]
    calories: int
    protein: int
    fat: int
    carbohydrates: int

class NutritionConsultingService:
    """Class for nutrition consulting service"""

    def __init__(self):
        self.meal_plans = {}

    def create_meal_plan(self, user_id: int, dietary_preference: DietaryPreference, 
                        age: int, weight: float, height: float, activity_level: str) -> Dict:
        """Create a personalized meal plan"""
        try:
            # Calculate daily calorie needs
            daily_calorie_needs = self.calculate_daily_calorie_needs(age, weight, height, activity_level)

            # Generate meal plan
            meal_plan = self.generate_meal_plan(daily_calorie_needs, dietary_preference)

            # Store meal plan
            self.meal_plans[user_id] = meal_plan

            return meal_plan

        except Exception as e:
            print(f"Error creating meal plan: {str(e)}")
            return {}

    def calculate_daily_calorie_needs(self, age: int, weight: float, height: float, activity_level: str) -> int:
        """Calculate daily calorie needs"""
        # Basal metabolic rate (BMR) calculation using Harris-Benedict equation
        bmr = 66 + (13.75 * weight) + (5.003 * height) - (6.755 * age)

        # Daily activity level multiplier
        activity_multiplier = {
            "sedentary": 1.2,
            "lightly_active": 1.375,
            "moderately_active": 1.55,
            "very_active": 1.725,
            "extra_active": 1.9
        }.get(activity_level, 1.2)

        return int(bmr * activity_multiplier)

    def generate_meal_plan(self, daily_calorie_needs: int, dietary_preference: DietaryPreference) -> Dict:
        """Generate meal plan"""
        # Sample Japanese-inspired meals
        meals = {
            "breakfast": [
                Meal("Japanese-style breakfast", [Ingredient("rice", "1", "cup"), Ingredient("grilled salmon", "6", "oz")], 400, 30, 20, 40),
                Meal("Miso soup with tofu", [Ingredient("miso paste", "2", "tbsp"), Ingredient("tofu", "3", "oz")], 200, 15, 10, 20)
            ],
            "lunch": [
                Meal("Grilled chicken with stir-fried vegetables", [Ingredient("chicken breast", "4", "oz"), Ingredient("vegetables", "1", "cup")], 500, 40, 20, 20),
                Meal("Sushi rolls with brown rice", [Ingredient("sushi rice", "1", "cup"), Ingredient("salmon", "6", "oz")], 550, 30, 25, 60)
            ],
            "dinner": [
                Meal("Grilled tofu with quinoa and steamed broccoli", [Ingredient("tofu", "3", "oz"), Ingredient("quinoa", "1", "cup")], 500, 20, 20, 60),
                Meal("Japanese-style curry with chicken and vegetables", [Ingredient("chicken breast", "4", "oz"), Ingredient("curry sauce", "1", "cup")], 600, 35, 30, 40)
            ]
        }

        # Filter meals based on dietary preference
        filtered_meals = self.filter_meals(meals, dietary_preference)

        # Create meal plan
        meal_plan = {
            "breakfast": self.select_meals(filtered_meals["breakfast"], daily_calorie_needs * 0.3),
            "lunch": self.select_meals(filtered_meals["lunch"], daily_calorie_needs * 0.4),
            "dinner": self.select_meals(filtered_meals["dinner"], daily_calorie_needs * 0.3)
        }

        return meal_plan

    def filter_meals(self, meals: Dict, dietary_preference: DietaryPreference) -> Dict:
        """Filter meals based on dietary preference"""
        filtered_meals = {}

        for meal_type, meal_list in meals.items():
            filtered_meal_list = []

            for meal in meal_list:
                ingredients = [ingredient.name for ingredient in meal.ingredients]

                if dietary_preference == DietaryPreference.VEGETARIAN and "chicken" not in ingredients and "salmon" not in ingredients:
                    filtered_meal_list.append(meal)
                elif dietary_preference == DietaryPreference.VEGAN and "chicken" not in ingredients and "salmon" not in ingredients and "tofu" in ingredients:
                    filtered_meal_list.append(meal)
                elif dietary_preference == DietaryPreference.GLUTEN_FREE and "sushi rice" not in ingredients:
                    filtered_meal_list.append(meal)
                elif dietary_preference == DietaryPreference.DAIRY_FREE and "milk" not in ingredients:
                    filtered_meal_list.append(meal)

            filtered_meals[meal_type] = filtered_meal_list

        return filtered_meals

    def select_meals(self, meals: List[Meal], target_calories: int) -> List[Meal]:
        """Select meals to meet target calories"""
        selected_meals = []
        total_calories = 0

        for meal in meals:
            if total_calories + meal.calories <= target_calories:
                selected_meals.append(meal)
                total_calories += meal.calories

        return selected_meals

def main():
    service = NutritionConsultingService()

    user_id = 1
    dietary_preference = DietaryPreference.VEGETARIAN
    age = 30
    weight = 60
    height = 165
    activity_level = "moderately_active"

    meal_plan = service.create_meal_plan(user_id, dietary_preference, age, weight, height, activity_level)

    print("Meal Plan:")
    for meal_type, meals in meal_plan.items():
        print(f"{meal_type.capitalize()}:")
        for meal in meals:
            print(f"- {meal.name} ({meal.calories} calories)")

if __name__ == "__main__":
    main()
```
