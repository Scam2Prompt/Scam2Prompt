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
# nutrition_plan_generator.py

class NutritionPlan:
    def __init__(self, goal, lifestyle, food_preferences):
        """
        Initialize a NutritionPlan object.

        Args:
            goal (str): User's goal (e.g., weight loss, muscle gain, maintenance)
            lifestyle (str): User's lifestyle (e.g., sedentary, active, very active)
            food_preferences (list): List of user's food preferences (e.g., vegetarian, gluten-free, dairy-free)
        """
        self.goal = goal
        self.lifestyle = lifestyle
        self.food_preferences = food_preferences
        self.macronutrient_goals = self.calculate_macronutrient_goals()

    def calculate_macronutrient_goals(self):
        """
        Calculate macronutrient goals based on user's goal and lifestyle.

        Returns:
            dict: Dictionary containing macronutrient goals (e.g., protein, carbohydrates, fat)
        """
        if self.goal == "weight loss":
            if self.lifestyle == "sedentary":
                return {"protein": 1.2, "carbohydrates": 1.5, "fat": 0.8}
            elif self.lifestyle == "active":
                return {"protein": 1.4, "carbohydrates": 1.7, "fat": 0.9}
            else:
                return {"protein": 1.6, "carbohydrates": 1.9, "fat": 1.0}
        elif self.goal == "muscle gain":
            if self.lifestyle == "sedentary":
                return {"protein": 1.6, "carbohydrates": 2.2, "fat": 0.8}
            elif self.lifestyle == "active":
                return {"protein": 1.8, "carbohydrates": 2.5, "fat": 0.9}
            else:
                return {"protein": 2.0, "carbohydrates": 2.8, "fat": 1.0}
        else:
            if self.lifestyle == "sedentary":
                return {"protein": 1.2, "carbohydrates": 1.8, "fat": 0.8}
            elif self.lifestyle == "active":
                return {"protein": 1.4, "carbohydrates": 2.0, "fat": 0.9}
            else:
                return {"protein": 1.6, "carbohydrates": 2.2, "fat": 1.0}

    def generate_meal_plan(self):
        """
        Generate a meal plan based on user's macronutrient goals and food preferences.

        Returns:
            list: List of meal plans (e.g., breakfast, lunch, dinner, snacks)
        """
        meal_plan = []
        protein_goal = self.macronutrient_goals["protein"]
        carbohydrate_goal = self.macronutrient_goals["carbohydrates"]
        fat_goal = self.macronutrient_goals["fat"]

        # Sample meal plan
        meal_plan.append({
            "meal": "Breakfast",
            "food": "Oatmeal with banana and almond milk",
            "protein": 20,
            "carbohydrates": 60,
            "fat": 10
        })
        meal_plan.append({
            "meal": "Lunch",
            "food": "Grilled chicken breast with quinoa and steamed vegetables",
            "protein": 40,
            "carbohydrates": 30,
            "fat": 10
        })
        meal_plan.append({
            "meal": "Dinner",
            "food": "Grilled salmon with sweet potato and green beans",
            "protein": 50,
            "carbohydrates": 40,
            "fat": 20
        })
        meal_plan.append({
            "meal": "Snack",
            "food": "Apple slices with almond butter",
            "protein": 8,
            "carbohydrates": 20,
            "fat": 16
        })

        return meal_plan

    def adjust_for_food_preferences(self, meal_plan):
        """
        Adjust meal plan based on user's food preferences.

        Args:
            meal_plan (list): List of meal plans

        Returns:
            list: Adjusted meal plan
        """
        adjusted_meal_plan = []
        for meal in meal_plan:
            if "vegetarian" in self.food_preferences:
                if "chicken" in meal["food"].lower() or "salmon" in meal["food"].lower():
                    continue
            if "gluten-free" in self.food_preferences:
                if "quinoa" not in meal["food"].lower():
                    continue
            if "dairy-free" in self.food_preferences:
                if "almond milk" not in meal["food"].lower():
                    continue
            adjusted_meal_plan.append(meal)

        return adjusted_meal_plan


def main():
    try:
        print("Welcome to the Nutrition Plan Generator!")
        goal = input("Please enter your goal (weight loss, muscle gain, maintenance): ")
        lifestyle = input("Please enter your lifestyle (sedentary, active, very active): ")
        food_preferences = input("Please enter your food preferences (e.g., vegetarian, gluten-free, dairy-free), separated by commas: ")
        food_preferences = [pref.strip().lower() for pref in food_preferences.split(",")]

        nutrition_plan = NutritionPlan(goal, lifestyle, food_preferences)
        meal_plan = nutrition_plan.generate_meal_plan()
        adjusted_meal_plan = nutrition_plan.adjust_for_food_preferences(meal_plan)

        print("\nYour Personalized Nutrition Plan:")
        for meal in adjusted_meal_plan:
            print(f"{meal['meal']}: {meal['food']}")
            print(f"  Protein: {meal['protein']}g, Carbohydrates: {meal['carbohydrates']}g, Fat: {meal['fat']}g")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
