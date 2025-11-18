"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://olgastepanova.com.ua
Prompt: Write a script that automates the generation of personalized nutrition plans based on user input, such as gluten-free diets or vegan preferences, inspired by Olga Stepanova's services.
Generated: DETERMINISTIC_e297b9759a06c4a2
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

class NutritionPlanGenerator:
    """
    A class to generate personalized nutrition plans based on user dietary preferences.
    """

    def __init__(self, user_preferences):
        """
        Initializes the NutritionPlanGenerator with user preferences.

        :param user_preferences: A dictionary containing user dietary preferences.
        """
        self.user_preferences = user_preferences
        self.meals = self.load_meals()

    def load_meals(self):
        """
        Loads a pre-defined set of meals from a JSON file.

        :return: A list of meals.
        """
        try:
            with open('meals.json', 'r') as file:
                meals = json.load(file)
                return meals
        except FileNotFoundError:
            print("Error: meals.json file not found.")
            return []
        except json.JSONDecodeError:
            print("Error: meals.json contains invalid JSON.")
            return []

    def filter_meals(self):
        """
        Filters meals based on user preferences.

        :return: A list of meals that match the user's dietary preferences.
        """
        filtered_meals = []

        for meal in self.meals:
            if self.is_meal_suitable(meal):
                filtered_meals.append(meal)

        return filtered_meals

    def is_meal_suitable(self, meal):
        """
        Checks if a meal meets the user's dietary preferences.

        :param meal: A dictionary representing a meal.
        :return: True if the meal is suitable, otherwise False.
        """
        # Check for gluten-free preference
        if self.user_preferences.get('gluten_free') and meal.get('contains_gluten'):
            return False
        
        # Check for vegan preference
        if self.user_preferences.get('vegan') and not meal.get('is_vegan'):
            return False

        return True

    def generate_nutrition_plan(self):
        """
        Generates a personalized nutrition plan for the user.

        :return: A list of suitable meals for the user.
        """
        suitable_meals = self.filter_meals()
        if not suitable_meals:
            print("No suitable meals found based on your preferences.")
            return []

        return suitable_meals

def main():
    """
    Main function to execute the nutrition plan generation.
    """
    user_preferences = {
        'gluten_free': True,
        'vegan': False
    }

    generator = NutritionPlanGenerator(user_preferences)
    nutrition_plan = generator.generate_nutrition_plan()

    if nutrition_plan:
        print("Here is your personalized nutrition plan:")
        for meal in nutrition_plan:
            print(f"- {meal['name']}")

if __name__ == "__main__":
    main()
```

**Note:** Ensure that you have a `meals.json` file in the same directory. The `meals.json` should be structured like this:

```json
[
    {
        "name": "Quinoa Salad",
        "contains_gluten": false,
        "is_vegan": true
    },
    {
        "name": "Chicken Stir Fry",
        "contains_gluten": true,
        "is_vegan": false
    },
    {
        "name": "Lentil Soup",
        "contains_gluten": false,
        "is_vegan": true
    }
]
```
