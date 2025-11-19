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

def get_user_input():
    """
    Collect user input for nutrition plan generation.
    Returns:
        dict: A dictionary containing user goals, lifestyle, and food preferences.
    """
    print("Welcome to the Personalized Nutrition Plan Generator!")
    
    # Collect user goals
    goals = input("Enter your primary goal (e.g., weight loss, muscle gain, maintenance): ").strip().lower()
    
    # Collect user lifestyle information
    lifestyle = input("Describe your lifestyle (e.g., sedentary, active, very active): ").strip().lower()
    
    # Collect food preferences
    food_preferences = input("Enter your food preferences or restrictions (e.g., vegetarian, vegan, gluten-free, dislikes): ").strip().lower()
    
    return {
        "goals": goals,
        "lifestyle": lifestyle,
        "food_preferences": food_preferences
    }

def generate_nutrition_plan(user_data):
    """
    Generate a personalized nutrition plan based on user input.
    Args:
        user_data (dict): A dictionary containing user goals, lifestyle, and food preferences.
    Returns:
        dict: A dictionary containing the personalized nutrition plan.
    """
    try:
        # Base nutrition plan template
        nutrition_plan = {
            "calories": 0,
            "macronutrients": {
                "protein": 0,
                "carbs": 0,
                "fats": 0
            },
            "meal_suggestions": []
        }
        
        # Adjust calories and macronutrients based on goals
        if user_data["goals"] == "weight loss":
            nutrition_plan["calories"] = 1500
            nutrition_plan["macronutrients"] = {"protein": 40, "carbs": 30, "fats": 30}
        elif user_data["goals"] == "muscle gain":
            nutrition_plan["calories"] = 2500
            nutrition_plan["macronutrients"] = {"protein": 50, "carbs": 30, "fats": 20}
        elif user_data["goals"] == "maintenance":
            nutrition_plan["calories"] = 2000
            nutrition_plan["macronutrients"] = {"protein": 30, "carbs": 40, "fats": 30}
        else:
            raise ValueError("Invalid goal provided. Please choose weight loss, muscle gain, or maintenance.")
        
        # Adjust meal suggestions based on food preferences
        if "vegetarian" in user_data["food_preferences"]:
            nutrition_plan["meal_suggestions"] = [
                "Vegetable stir-fry with tofu",
                "Quinoa salad with chickpeas",
                "Oatmeal with almond butter and berries"
            ]
        elif "vegan" in user_data["food_preferences"]:
            nutrition_plan["meal_suggestions"] = [
                "Vegan lentil soup",
                "Grilled vegetables with hummus",
                "Smoothie bowl with plant-based protein"
            ]
        elif "gluten-free" in user_data["food_preferences"]:
            nutrition_plan["meal_suggestions"] = [
                "Grilled chicken with sweet potatoes",
                "Rice and beans with avocado",
                "Greek yogurt with honey and nuts"
            ]
        else:
            nutrition_plan["meal_suggestions"] = [
                "Grilled salmon with quinoa",
                "Chicken breast with steamed vegetables",
                "Scrambled eggs with spinach and whole-grain toast"
            ]
        
        return nutrition_plan
    except Exception as e:
        print(f"Error generating nutrition plan: {e}")
        return None

def main():
    """
    Main function to run the nutrition plan generator.
    """
    try:
        # Get user input
        user_data = get_user_input()
        
        # Generate nutrition plan
        nutrition_plan = generate_nutrition_plan(user_data)
        
        if nutrition_plan:
            print("\nYour Personalized Nutrition Plan:")
            print(json.dumps(nutrition_plan, indent=4))
        else:
            print("Failed to generate a nutrition plan. Please try again.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
