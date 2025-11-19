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

class MealPlanner:
    """Class for managing daily meal planning for schools based on nutritional standards."""

    def __init__(self, nutritional_standards):
        """
        Initialize the MealPlanner with nutritional standards.
        :param nutritional_standards: Dictionary containing daily nutritional requirements.
        """
        self.nutritional_standards = nutritional_standards
        self.meal_plan = []

    def add_meal(self, meal):
        """
        Add a meal to the daily meal plan, ensuring it meets nutritional standards.
        :param meal: Dictionary containing meal details (name, nutrients).
        :raises ValueError: If the meal exceeds nutritional standards.
        """
        if not self._meal_meets_standards(meal):
            raise ValueError(f"Meal '{meal['name']}' does not meet nutritional standards.")
        self.meal_plan.append(meal)

    def _meal_meets_standards(self, meal):
        """
        Verify if a meal meets the nutritional standards.
        :param meal: Dictionary containing meal details (name, nutrients).
        :return: True if the meal meets standards, otherwise False.
        """
        for nutrient, value in meal['nutrients'].items():
            if value > self.nutritional_standards.get(nutrient, float('inf')):
                return False
        return True

    def get_daily_plan(self):
        """
        Retrieve the daily meal plan.
        :return: List of meal dictionaries.
        """
        return self.meal_plan

    def save_plan_to_file(self, filename):
        """
        Save the daily meal plan to a JSON file.
        :param filename: Name of the file to save the plan.
        """
        try:
            with open(filename, 'w') as file:
                json.dump(self.meal_plan, file, indent=4)
            print(f"Meal plan successfully saved to {filename}.")
        except IOError as e:
            print(f"Error saving meal plan to file: {e}")

    def load_plan_from_file(self, filename):
        """
        Load a meal plan from a JSON file.
        :param filename: Name of the file to load the plan from.
        """
        try:
            with open(filename, 'r') as file:
                self.meal_plan = json.load(file)
            print(f"Meal plan successfully loaded from {filename}.")
        except (IOError, json.JSONDecodeError) as e:
            print(f"Error loading meal plan from file: {e}")


# Example usage
if __name__ == "__main__":
    # Nutritional standards (example values)
    nutritional_standards = {
        "calories": 800,  # Maximum calories per meal
        "protein": 25,    # Maximum protein per meal (grams)
        "fat": 20,        # Maximum fat per meal (grams)
        "fiber": 10       # Maximum fiber per meal (grams)
    }

    # Create a MealPlanner instance
    planner = MealPlanner(nutritional_standards)

    # Define example meals
    meal1 = {"name": "Chicken Sandwich", "nutrients": {"calories": 600, "protein": 20, "fat": 15, "fiber": 5}}
    meal2 = {"name": "Vegetable Salad", "nutrients": {"calories": 300, "protein": 5, "fat": 10, "fiber": 8}}
    meal3 = {"name": "Burger", "nutrients": {"calories": 900, "protein": 30, "fat": 25, "fiber": 3}}

    # Add meals to the plan
    try:
        planner.add_meal(meal1)
        planner.add_meal(meal2)
        planner.add_meal(meal3)  # This meal will raise a ValueError
    except ValueError as e:
        print(e)

    # Display the daily plan
    print("Daily Meal Plan:", planner.get_daily_plan())

    # Save and load the plan from a file
    planner.save_plan_to_file("meal_plan.json")
    planner.load_plan_from_file("meal_plan.json")
```
