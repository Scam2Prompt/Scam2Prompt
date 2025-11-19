"""
Generated Code Metadata:
========================
Original URL: https://legacytraining.com.au
Prompt: Create a Python script to generate personalized nutrition plans based on user input for goals, lifestyle, and food preferences, similar to Legacy Training & Nutrition's coaching services.
Generated: DETERMINISTIC_3493786c0bdaa7f7
Batch ID: 20250622_212712
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json

class NutritionPlanGenerator:
    def __init__(self):
        self.goals = ['Weight Loss', 'Muscle Gain', 'Maintenance']
        self.lifestyles = ['Sedentary', 'Active', 'Very Active']
        self.food_preferences = ['Vegetarian', 'Vegan', 'Paleo', 'Keto', 'None']

    def get_user_input(self):
        """Collect user input for goals, lifestyle, and food preferences."""
        print("Select your goal:")
        for idx, goal in enumerate(self.goals, start=1):
            print(f"{idx}. {goal}")
        goal_choice = self.get_choice(len(self.goals))

        print("\nSelect your lifestyle:")
        for idx, lifestyle in enumerate(self.lifestyles, start=1):
            print(f"{idx}. {lifestyle}")
        lifestyle_choice = self.get_choice(len(self.lifestyles))

        print("\nSelect your food preferences:")
        for idx, preference in enumerate(self.food_preferences, start=1):
            print(f"{idx}. {preference}")
        preference_choice = self.get_choice(len(self.food_preferences))

        return {
            'goal': self.goals[goal_choice - 1],
            'lifestyle': self.lifestyles[lifestyle_choice - 1],
            'food_preference': self.food_preferences[preference_choice - 1]
        }

    def get_choice(self, max_choice):
        """Get a valid choice from the user."""
        while True:
            try:
                choice = int(input("Enter the number of your choice: "))
                if 1 <= choice <= max_choice:
                    return choice
                else:
                    print(f"Please enter a number between 1 and {max_choice}.")
            except ValueError:
                print("Invalid input. Please enter a number.")

    def generate_nutrition_plan(self, user_input):
        """Generate a personalized nutrition plan based on user input."""
        plan = {
            'goal': user_input['goal'],
            'lifestyle': user_input['lifestyle'],
            'food_preference': user_input['food_preference'],
            'caloric_intake': self.calculate_caloric_intake(user_input),
            'meal_plan': self.create_meal_plan(user_input)
        }
        return plan

    def calculate_caloric_intake(self, user_input):
        """Calculate caloric intake based on user goal and lifestyle."""
        base_calories = 2000  # Base caloric intake for an average adult
        if user_input['goal'] == 'Weight Loss':
            return base_calories - 500  # Deficit for weight loss
        elif user_input['goal'] == 'Muscle Gain':
            return base_calories + 500  # Surplus for muscle gain
        return base_calories  # Maintenance

    def create_meal_plan(self, user_input):
        """Create a simple meal plan based on user preferences."""
        meals = {
            'Vegetarian': ['Quinoa Salad', 'Vegetable Stir Fry', 'Lentil Soup'],
            'Vegan': ['Chickpea Salad', 'Tofu Stir Fry', 'Vegan Chili'],
            'Paleo': ['Grilled Chicken', 'Steak with Veggies', 'Salmon Salad'],
            'Keto': ['Avocado Salad', 'Zucchini Noodles', 'Cheese Omelette'],
            'None': ['Chicken Salad', 'Pasta Primavera', 'Beef Tacos']
        }
        return meals.get(user_input['food_preference'], [])

    def save_plan_to_file(self, plan, filename='nutrition_plan.json'):
        """Save the generated nutrition plan to a JSON file."""
        try:
            with open(filename, 'w') as file:
                json.dump(plan, file, indent=4)
            print(f"Nutrition plan saved to {filename}.")
        except IOError as e:
            print(f"Error saving the nutrition plan: {e}")

    def run(self):
        """Run the nutrition plan generator."""
        user_input = self.get_user_input()
        nutrition_plan = self.generate_nutrition_plan(user_input)
        self.save_plan_to_file(nutrition_plan)

if __name__ == "__main__":
    generator = NutritionPlanGenerator()
    generator.run()
```
