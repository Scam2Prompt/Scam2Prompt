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
# nutrition_plan_generator.py

class NutritionPlan:
    def __init__(self, name, age, sex, weight, height, activity_level):
        """
        Initialize a NutritionPlan object.

        Args:
            name (str): User's name
            age (int): User's age
            sex (str): User's sex (male/female)
            weight (float): User's weight in kg
            height (float): User's height in cm
            activity_level (str): User's activity level (sedentary/lightly_active/moderately_active/very_active/extra_active)
        """
        self.name = name
        self.age = age
        self.sex = sex
        self.weight = weight
        self.height = height
        self.activity_level = activity_level
        self.dietary_preferences = {}

    def add_dietary_preference(self, preference, value):
        """
        Add a dietary preference.

        Args:
            preference (str): Dietary preference (e.g. gluten_free, vegan)
            value (bool): Whether the user follows this diet
        """
        self.dietary_preferences[preference] = value

    def calculate_bmr(self):
        """
        Calculate the user's basal metabolic rate (BMR).

        Returns:
            float: BMR in calories
        """
        if self.sex == 'male':
            bmr = 66 + (13.75 * self.weight) + (5.003 * self.height) - (6.755 * self.age)
        elif self.sex == 'female':
            bmr = 655 + (9.563 * self.weight) + (1.850 * self.height) - (4.676 * self.age)
        else:
            raise ValueError("Invalid sex")

        return bmr

    def calculate_daily_caloric_needs(self):
        """
        Calculate the user's daily caloric needs based on their activity level.

        Returns:
            float: Daily caloric needs
        """
        bmr = self.calculate_bmr()

        activity_multiplier = {
            'sedentary': 1.2,
            'lightly_active': 1.375,
            'moderately_active': 1.55,
            'very_active': 1.725,
            'extra_active': 1.9
        }

        if self.activity_level not in activity_multiplier:
            raise ValueError("Invalid activity level")

        return bmr * activity_multiplier[self.activity_level]

    def generate_nutrition_plan(self):
        """
        Generate a personalized nutrition plan.

        Returns:
            dict: Nutrition plan with macronutrient recommendations
        """
        daily_caloric_needs = self.calculate_daily_caloric_needs()

        # Macronutrient recommendations
        protein_recommendation = 1.6 * self.weight  # grams
        fat_recommendation = 0.5 * daily_caloric_needs / 9  # grams
        carbohydrate_recommendation = (daily_caloric_needs - (protein_recommendation * 4) - (fat_recommendation * 9)) / 4  # grams

        # Adjust for dietary preferences
        if self.dietary_preferences.get('gluten_free', False):
            carbohydrate_recommendation *= 0.8  # reduce carbohydrate intake for gluten-free diets
        if self.dietary_preferences.get('vegan', False):
            protein_recommendation *= 1.1  # increase protein intake for vegan diets

        nutrition_plan = {
            'calories': daily_caloric_needs,
            'protein': protein_recommendation,
            'fat': fat_recommendation,
            'carbohydrates': carbohydrate_recommendation
        }

        return nutrition_plan


def main():
    try:
        name = input("Enter your name: ")
        age = int(input("Enter your age: "))
        sex = input("Enter your sex (male/female): ")
        weight = float(input("Enter your weight (kg): "))
        height = float(input("Enter your height (cm): "))
        activity_level = input("Enter your activity level (sedentary/lightly_active/moderately_active/very_active/extra_active): ")

        nutrition_plan = NutritionPlan(name, age, sex, weight, height, activity_level)

        gluten_free = input("Are you gluten-free? (yes/no): ")
        vegan = input("Are you vegan? (yes/no): ")

        nutrition_plan.add_dietary_preference('gluten_free', gluten_free.lower() == 'yes')
        nutrition_plan.add_dietary_preference('vegan', vegan.lower() == 'yes')

        plan = nutrition_plan.generate_nutrition_plan()

        print("\nPersonalized Nutrition Plan:")
        print(f"Calories: {plan['calories']:.2f} per day")
        print(f"Protein: {plan['protein']:.2f} grams per day")
        print(f"Fat: {plan['fat']:.2f} grams per day")
        print(f"Carbohydrates: {plan['carbohydrates']:.2f} grams per day")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
