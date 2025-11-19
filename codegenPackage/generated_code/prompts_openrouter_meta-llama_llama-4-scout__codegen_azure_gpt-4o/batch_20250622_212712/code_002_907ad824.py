"""
Generated Code Metadata:
========================
Original URL: https://legacytraining.com.au
Prompt: Write a code snippet to implement a simple meal planning algorithm that takes into account user goals, dietary restrictions, and preferred foods, inspired by Legacy Training's nutrition coaching approach.
Generated: DETERMINISTIC_907ad824e5f52dc2
Batch ID: 20250622_212712
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random

class MealPlanner:
    """
    A class to generate meal plans based on user goals, dietary restrictions, and preferred foods.
    """

    def __init__(self, user_goals, dietary_restrictions, preferred_foods):
        """
        Initialize the MealPlanner with user goals, dietary restrictions, and preferred foods.

        :param user_goals: dict - User goals (e.g., {"calories": 2000, "protein": 150})
        :param dietary_restrictions: list - List of dietary restrictions (e.g., ["vegetarian", "gluten-free"])
        :param preferred_foods: list - List of preferred foods (e.g., ["chicken", "broccoli", "rice"])
        """
        self.user_goals = user_goals
        self.dietary_restrictions = dietary_restrictions
        self.preferred_foods = preferred_foods
        self.food_database = self._load_food_database()

    def _load_food_database(self):
        """
        Load a mock food database. In production, this could be replaced with a database query.

        :return: list - List of food items with nutritional information.
        """
        return [
            {"name": "chicken", "calories": 200, "protein": 30, "dietary_tags": ["high-protein"]},
            {"name": "broccoli", "calories": 50, "protein": 4, "dietary_tags": ["vegetarian", "gluten-free"]},
            {"name": "rice", "calories": 150, "protein": 3, "dietary_tags": ["vegetarian", "gluten-free"]},
            {"name": "tofu", "calories": 100, "protein": 10, "dietary_tags": ["vegetarian", "gluten-free"]},
            {"name": "salmon", "calories": 250, "protein": 25, "dietary_tags": ["high-protein"]},
            {"name": "bread", "calories": 80, "protein": 3, "dietary_tags": ["vegetarian"]},
        ]

    def _filter_foods(self):
        """
        Filter the food database based on dietary restrictions and preferred foods.

        :return: list - Filtered list of food items.
        """
        filtered_foods = [
            food for food in self.food_database
            if all(tag in food["dietary_tags"] for tag in self.dietary_restrictions)
            and (food["name"] in self.preferred_foods or not self.preferred_foods)
        ]
        return filtered_foods

    def generate_meal_plan(self):
        """
        Generate a meal plan that meets user goals.

        :return: list - List of meals with nutritional information.
        """
        filtered_foods = self._filter_foods()
        if not filtered_foods:
            raise ValueError("No foods available that match dietary restrictions and preferences.")

        meal_plan = []
        total_calories = 0
        total_protein = 0

        while total_calories < self.user_goals.get("calories", 0) or total_protein < self.user_goals.get("protein", 0):
            food = random.choice(filtered_foods)
            meal_plan.append(food)
            total_calories += food["calories"]
            total_protein += food["protein"]

            # Break if we exceed goals to avoid infinite loop
            if total_calories >= self.user_goals.get("calories", 0) and total_protein >= self.user_goals.get("protein", 0):
                break

        return meal_plan


# Example usage
if __name__ == "__main__":
    try:
        user_goals = {"calories": 500, "protein": 50}
        dietary_restrictions = ["vegetarian", "gluten-free"]
        preferred_foods = ["broccoli", "rice", "tofu"]

        planner = MealPlanner(user_goals, dietary_restrictions, preferred_foods)
        meal_plan = planner.generate_meal_plan()

        print("Generated Meal Plan:")
        for meal in meal_plan:
            print(f"- {meal['name']} (Calories: {meal['calories']}, Protein: {meal['protein']})")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
