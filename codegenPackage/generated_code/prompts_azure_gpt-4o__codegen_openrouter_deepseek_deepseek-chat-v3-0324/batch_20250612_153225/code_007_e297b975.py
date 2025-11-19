"""
Generated Code Metadata:
========================
Original URL: https://olgastepanova.com.ua
Prompt: Write a script that automates the generation of personalized nutrition plans based on user input, such as gluten-free diets or vegan preferences, inspired by Olga Stepanova's services.
Generated: DETERMINISTIC_e297b9759a06c4a2
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import Dict, List, Optional

class NutritionPlanGenerator:
    """
    A class to generate personalized nutrition plans based on user preferences.
    """

    def __init__(self):
        """
        Initialize the generator with predefined meal templates and dietary options.
        """
        self.meal_templates = self._load_meal_templates()
        self.dietary_options = self._load_dietary_options()

    def _load_meal_templates(self) -> Dict[str, List[Dict]]:
        """
        Load meal templates from a JSON file or return default templates.

        Returns:
            Dict[str, List[Dict]]: A dictionary of meal categories with their templates.
        """
        try:
            with open('meal_templates.json', 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return {
                "breakfast": [
                    {"name": "Oatmeal", "ingredients": ["oats", "milk", "honey"], "calories": 300},
                    {"name": "Smoothie", "ingredients": ["banana", "spinach", "almond milk"], "calories": 250}
                ],
                "lunch": [
                    {"name": "Salad", "ingredients": ["lettuce", "tomato", "cucumber", "chicken"], "calories": 400},
                    {"name": "Soup", "ingredients": ["vegetables", "broth", "tofu"], "calories": 350}
                ],
                "dinner": [
                    {"name": "Grilled Fish", "ingredients": ["salmon", "lemon", "asparagus"], "calories": 450},
                    {"name": "Stir Fry", "ingredients": ["tofu", "rice", "vegetables"], "calories": 500}
                ]
            }

    def _load_dietary_options(self) -> Dict[str, List[str]]:
        """
        Load dietary options from a JSON file or return default options.

        Returns:
            Dict[str, List[str]]: A dictionary of dietary restrictions with their options.
        """
        try:
            with open('dietary_options.json', 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return {
                "gluten_free": ["oats", "rice", "vegetables", "tofu", "salmon", "chicken", "almond milk"],
                "vegan": ["oats", "banana", "spinach", "almond milk", "tofu", "vegetables", "rice"],
                "vegetarian": ["oats", "milk", "honey", "banana", "spinach", "almond milk", "tofu", "vegetables", "rice"]
            }

    def _filter_meals_by_diet(self, meals: List[Dict], diet: str) -> List[Dict]:
        """
        Filter meals based on dietary restrictions.

        Args:
            meals (List[Dict]): List of meal templates to filter.
            diet (str): Dietary restriction to apply.

        Returns:
            List[Dict]: Filtered list of meals that comply with the dietary restriction.
        """
        if diet not in self.dietary_options:
            return meals

        allowed_ingredients = set(self.dietary_options[diet])
        filtered_meals = []

        for meal in meals:
            if all(ingredient in allowed_ingredients for ingredient in meal["ingredients"]):
                filtered_meals.append(meal)

        return filtered_meals

    def generate_plan(self, preferences: Dict[str, str]) -> Dict[str, List[Dict]]:
        """
        Generate a personalized nutrition plan based on user preferences.

        Args:
            preferences (Dict[str, str]): User preferences including dietary restrictions.

        Returns:
            Dict[str, List[Dict]]: A dictionary of meal categories with personalized meals.
        """
        diet = preferences.get("diet", None)
        plan = {}

        for category, meals in self.meal_templates.items():
            if diet:
                filtered_meals = self._filter_meals_by_diet(meals, diet)
                plan[category] = filtered_meals
            else:
                plan[category] = meals

        return plan

    def save_plan_to_file(self, plan: Dict[str, List[Dict]], filename: str = "nutrition_plan.json") -> None:
        """
        Save the generated nutrition plan to a JSON file.

        Args:
            plan (Dict[str, List[Dict]]): The nutrition plan to save.
            filename (str): The name of the file to save the plan to.
        """
        try:
            with open(filename, 'w') as file:
                json.dump(plan, file, indent=4)
        except IOError as e:
            print(f"Error saving plan to file: {e}")

def main():
    """
    Main function to interact with the user and generate a nutrition plan.
    """
    print("Welcome to the Personalized Nutrition Plan Generator!")
    print("Please answer the following questions to generate your plan.\n")

    preferences = {}
    diet = input("Do you have any dietary restrictions? (e.g., gluten_free, vegan, vegetarian, none): ").strip().lower()
    if diet != "none":
        preferences["diet"] = diet

    generator = NutritionPlanGenerator()
    plan = generator.generate_plan(preferences)

    print("\nYour personalized nutrition plan has been generated!\n")
    for category, meals in plan.items():
        print(f"{category.capitalize()}:")
        for meal in meals:
            print(f"  - {meal['name']}: {', '.join(meal['ingredients'])} ({meal['calories']} calories)")
        print()

    save = input("Would you like to save this plan to a file? (yes/no): ").strip().lower()
    if save == "yes":
        filename = input("Enter the filename to save to (default: nutrition_plan.json): ").strip()
        if not filename:
            filename = "nutrition_plan.json"
        generator.save_plan_to_file(plan, filename)
        print(f"Plan saved to {filename}")

if __name__ == "__main__":
    main()
```
