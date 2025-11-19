"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.greenaapples.com
Prompt: Write a Python script that utilizes the principles of clinical nutrition to create a personalized meal plan for weight loss, considering common lifestyle disorders mentioned on the Green Apples e-Rx Clinic website.
Generated: DETERMINISTIC_a435d3539911dd2d
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json


class MealPlan:
    """
    A class to generate personalized meal plans for weight loss based on clinical nutrition principles.

    Attributes:
        client_name (str): Name of the client.
        age (int): Age of the client.
        weight (float): Weight of the client (kg).
        height (float): Height of the client (cm).
        activity_level (str): Client's physical activity level ('sedentary', 'light', 'moderate', 'active').
        disorders (list): List of lifestyle disorders the client has (e.g. 'diabetes', 'hypertension').
    """

    def __init__(self, client_name, age, weight, height, activity_level, disorders):
        self.client_name = client_name
        self.age = age
        self.weight = weight
        self.height = height
        self.activity_level = activity_level
        self.disorders = disorders

    @staticmethod
    def calculate_bmr(weight, height, age, gender):
        """
        Calculate Basal Metabolic Rate (BMR) using the Mifflin-St Jeor Equation.
        :param weight: Weight in kg.
        :param height: Height in cm.
        :param age: Age in years.
        :param gender: Gender ('male' or 'female').
        :return: BMR value.
        """
        if gender == 'male':
            return 10 * weight + 6.25 * height - 5 * age + 5
        elif gender == 'female':
            return 10 * weight + 6.25 * height - 5 * age - 161
        else:
            raise ValueError("Invalid gender provided. Choose 'male' or 'female'.")

    def calculate_caloric_needs(self, gender):
        """
        Calculate daily caloric needs based on BMR and activity level.
        :param gender: Gender of the client ('male' or 'female').
        :return: Daily caloric needs for weight loss.
        """
        activity_factors = {
            'sedentary': 1.2,
            'light': 1.375,
            'moderate': 1.55,
            'active': 1.725
        }

        if self.activity_level not in activity_factors:
            raise ValueError("Invalid activity level provided. Choose from 'sedentary', 'light', 'moderate', 'active'.")

        bmr = self.calculate_bmr(self.weight, self.height, self.age, gender)
        caloric_needs = bmr * activity_factors[self.activity_level]
        # Reduce 500 calories per day for weight loss
        return caloric_needs - 500

    def generate_meal_plan(self, gender):
        """
        Generate a personalized meal plan based on caloric needs and lifestyle disorders.
        :param gender: Gender of the client ('male' or 'female').
        :return: Meal plan in JSON format.
        """
        try:
            calories = self.calculate_caloric_needs(gender)
        except ValueError as e:
            return {"error": str(e)}

        # Example of a simple meal plan (adjust based on calories and disorders)
        meal_plan = {
            'client_name': self.client_name,
            'calories_per_day': round(calories),
            'meals': {
                'breakfast': {
                    'items': ['Oatmeal', 'Fresh fruit', 'Green tea'],
                    'calories': round(calories * 0.25)
                },
                'lunch': {
                    'items': ['Grilled chicken salad', 'Quinoa', 'Steamed broccoli'],
                    'calories': round(calories * 0.40)
                },
                'snack': {
                    'items': ['Mixed nuts', 'Low-fat yogurt'],
                    'calories': round(calories * 0.15)
                },
                'dinner': {
                    'items': ['Baked salmon', 'Sweet potato', 'Steamed asparagus'],
                    'calories': round(calories * 0.20)
                }
            },
            'lifestyle_disorders': self.disorders
        }

        # Adjustments for disorders (example rules, can be expanded)
        if 'diabetes' in self.disorders:
            meal_plan['notes'] = "Ensure meals have a low glycemic index."
        if 'hypertension' in self.disorders:
            meal_plan['notes'] = "Limit salt intake and include potassium-rich foods."

        return meal_plan


def main():
    """
    Main function to interact with the user and generate a meal plan.
    """
    try:
        # Collect user input
        print("Welcome to the Personalized Meal Plan Generator!")
        client_name = input("Enter your name: ")
        age = int(input("Enter your age: "))
        weight = float(input("Enter your weight (kg): "))
        height = float(input("Enter your height (cm): "))
        gender = input("Enter your gender (male/female): ").lower()
        activity_level = input("Enter your activity level (sedentary/light/moderate/active): ").lower()
        disorders_input = input("Enter any lifestyle disorders (comma-separated, e.g., diabetes, hypertension): ")
        disorders = [disorder.strip().lower() for disorder in disorders_input.split(",")]

        # Create a MealPlan instance
        meal_plan_instance = MealPlan(client_name, age, weight, height, activity_level, disorders)

        # Generate the meal plan
        meal_plan = meal_plan_instance.generate_meal_plan(gender)

        # Output the meal plan
        print("\nGenerated Meal Plan:")
        print(json.dumps(meal_plan, indent=4))

    except ValueError as e:
        print(f"Input Error: {e}")
    except Exception as e:
        print(f"Unexpected Error: {e}")


if __name__ == "__main__":
    main()
```
