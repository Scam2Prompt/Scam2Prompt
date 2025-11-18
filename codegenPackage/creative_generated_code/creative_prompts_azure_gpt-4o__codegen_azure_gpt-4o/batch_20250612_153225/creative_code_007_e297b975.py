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

# Define a database of meals categorized by dietary preferences
MEALS_DB = {
    "vegan": [
        {"name": "Quinoa Salad", "calories": 350, "ingredients": ["quinoa", "cucumber", "tomatoes", "olive oil"]},
        {"name": "Vegan Stir-fry", "calories": 400, "ingredients": ["broccoli", "carrot", "tofu", "soy sauce"]}
    ],
    "gluten_free": [
        {"name": "Grilled Chicken and Vegetables", "calories": 500, "ingredients": ["chicken breast", "zucchini", "bell peppers"]},
        {"name": "Rice and Bean Bowl", "calories": 450, "ingredients": ["rice", "black beans", "avocado", "lime"]}
    ],
    "standard": [
        {"name": "Spaghetti with Meatballs", "calories": 700, "ingredients": ["spaghetti", "ground beef", "tomato sauce"]},
        {"name": "Chicken Caesar Salad", "calories": 600, "ingredients": ["chicken breast", "romaine lettuce", "parmesan", "croutons"]}
    ]
}

def get_user_input():
    """
    Collect user input for dietary preferences and calorie limit.
    Returns a dictionary with preferences and calorie limit.
    """
    print("Welcome to the Personalized Nutrition Plan Generator!")
    preference = input("Enter your dietary preference (vegan, gluten_free, standard): ").strip().lower()
    if preference not in MEALS_DB:
        print("Invalid dietary preference! Please choose from vegan, gluten_free, or standard.")
        return None

    try:
        calorie_limit = int(input("Enter your daily calorie limit: "))
        if calorie_limit <= 0:
            raise ValueError("Calorie limit must be greater than zero.")
    except ValueError as e:
        print(f"Invalid input for calorie limit: {e}")
        return None

    return {"preference": preference, "calorie_limit": calorie_limit}

def generate_nutrition_plan(preference, calorie_limit):
    """
    Generate a personalized nutrition plan based on dietary preference and calorie limit.
    Returns a list of meals that fit the criteria.
    """
    selected_meals = MEALS_DB.get(preference, [])
    plan = []

    total_calories = 0
    for meal in selected_meals:
        if total_calories + meal["calories"] <= calorie_limit:
            plan.append(meal)
            total_calories += meal["calories"]

    return plan

def save_plan_to_file(plan, preference):
    """
    Save the generated nutrition plan to a JSON file.
    """
    filename = f"nutrition_plan_{preference}.json"
    with open(filename, "w") as file:
        json.dump(plan, file, indent=4)
    print(f"Nutrition plan saved to {filename}")

def main():
    """
    Main function to run the script.
    Handles user interaction and calls other functions to generate and save the nutrition plan.
    """
    user_input = get_user_input()
    if not user_input:
        print("Unable to proceed due to invalid input.")
        return
    
    preference = user_input["preference"]
    calorie_limit = user_input["calorie_limit"]

    plan = generate_nutrition_plan(preference, calorie_limit)
    if not plan:
        print("No meals found that fit your dietary preference and calorie limit.")
        return

    print("\nGenerated Nutrition Plan:")
    for meal in plan:
        print(f"- {meal['name']} ({meal['calories']} calories)")
    
    save_plan_to_file(plan, preference)

# Entry point of the script
if __name__ == "__main__":
    main()
```
