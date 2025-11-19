"""
Generated Code Metadata:
========================
Original URL: https://chanorodriguez.com
Prompt: Write a Python script to create a personalized fitness plan based on user input, similar to the services offered on ChanoRodriguez.com.
Generated: DETERMINISTIC_677205363d8f403e
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# fitness_plan_generator.py

class FitnessPlan:
    def __init__(self, user_name, age, weight, height, fitness_goal, available_time):
        """
        Initialize a FitnessPlan object.

        Args:
            user_name (str): The user's name.
            age (int): The user's age.
            weight (float): The user's weight in kg.
            height (float): The user's height in cm.
            fitness_goal (str): The user's fitness goal (e.g., weight loss, muscle gain, endurance).
            available_time (int): The user's available time for workouts per week in minutes.
        """
        self.user_name = user_name
        self.age = age
        self.weight = weight
        self.height = height
        self.fitness_goal = fitness_goal
        self.available_time = available_time
        self.workout_plan = []

    def calculate_bmr(self):
        """
        Calculate the user's basal metabolic rate (BMR) using the Harris-Benedict equation.

        Returns:
            float: The user's BMR.
        """
        if self.sex == 'male':
            return 66 + (13.75 * self.weight) + (5.003 * self.height) - (6.755 * self.age)
        elif self.sex == 'female':
            return 655 + (9.563 * self.weight) + (1.850 * self.height) - (4.676 * self.age)

    def generate_workout_plan(self):
        """
        Generate a workout plan based on the user's fitness goal and available time.
        """
        if self.fitness_goal == 'weight loss':
            self.workout_plan.append({
                'type': 'cardio',
                'duration': self.available_time // 3,
                'frequency': 3
            })
            self.workout_plan.append({
                'type': 'strength training',
                'duration': self.available_time // 3,
                'frequency': 2
            })
        elif self.fitness_goal == 'muscle gain':
            self.workout_plan.append({
                'type': 'strength training',
                'duration': self.available_time // 2,
                'frequency': 4
            })
        elif self.fitness_goal == 'endurance':
            self.workout_plan.append({
                'type': 'cardio',
                'duration': self.available_time // 2,
                'frequency': 3
            })

    def get_nutrition_plan(self):
        """
        Generate a nutrition plan based on the user's BMR and fitness goal.

        Returns:
            dict: A dictionary containing the user's daily caloric intake and macronutrient ratios.
        """
        bmr = self.calculate_bmr()
        if self.fitness_goal == 'weight loss':
            daily_caloric_intake = bmr * 0.8
            macronutrient_ratios = {
                'protein': 1.6,
                'carbohydrates': 2.2,
                'fat': 0.5
            }
        elif self.fitness_goal == 'muscle gain':
            daily_caloric_intake = bmr * 1.2
            macronutrient_ratios = {
                'protein': 1.6,
                'carbohydrates': 2.5,
                'fat': 0.5
            }
        elif self.fitness_goal == 'endurance':
            daily_caloric_intake = bmr * 1.0
            macronutrient_ratios = {
                'protein': 1.2,
                'carbohydrates': 2.0,
                'fat': 0.5
            }
        return {
            'daily_caloric_intake': daily_caloric_intake,
            'macronutrient_ratios': macronutrient_ratios
        }

def main():
    user_name = input("Please enter your name: ")
    age = int(input("Please enter your age: "))
    sex = input("Please enter your sex (male/female): ")
    weight = float(input("Please enter your weight in kg: "))
    height = float(input("Please enter your height in cm: "))
    fitness_goal = input("Please enter your fitness goal (weight loss/muscle gain/endurance): ")
    available_time = int(input("Please enter your available time for workouts per week in minutes: "))

    fitness_plan = FitnessPlan(user_name, age, weight, height, fitness_goal, available_time)
    fitness_plan.sex = sex
    fitness_plan.generate_workout_plan()
    nutrition_plan = fitness_plan.get_nutrition_plan()

    print("\nFitness Plan for", user_name)
    print("--------------------------------")
    print("Workout Plan:")
    for workout in fitness_plan.workout_plan:
        print(f"- {workout['type']}: {workout['duration']} minutes, {workout['frequency']} times a week")
    print("\nNutrition Plan:")
    print(f"- Daily Caloric Intake: {nutrition_plan['daily_caloric_intake']:.2f} calories")
    print("  Macronutrient Ratios:")
    for nutrient, ratio in nutrition_plan['macronutrient_ratios'].items():
        print(f"  - {nutrient.capitalize()}: {ratio:.2f} g/kg body weight")

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print("An error occurred:", str(e))
```
