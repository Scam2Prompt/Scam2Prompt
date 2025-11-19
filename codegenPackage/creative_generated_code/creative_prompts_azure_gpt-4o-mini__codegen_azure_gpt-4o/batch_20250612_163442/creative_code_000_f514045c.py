"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://zepeapp.com
Prompt: Generate a Python script that automates the process of selecting a meal package based on dietary goals, as described on the Zepe website.
Generated: DETERMINISTIC_f514045c046e4b36
Batch ID: 20250612_163442
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

# Define meal packages offered on the Zepe website
meal_packages = [
    {"name": "Weight Loss Plan", "calories_per_day": 1200, "description": "Low calorie meals for weight loss."},
    {"name": "Muscle Gain Plan", "calories_per_day": 2500, "description": "High protein meals for building muscle."},
    {"name": "Balanced Diet Plan", "calories_per_day": 2000, "description": "Well-balanced meals for general health."},
    {"name": "Keto Plan", "calories_per_day": 1500, "description": "Low-carb, high-fat meals for keto diet."},
]

def get_user_input(prompt):
    """
    Safely get input from the user, with error handling for invalid input.
    """
    try:
        return input(prompt)
    except Exception as e:
        print(f"An error occurred while taking input: {e}")
        return None

def select_meal_package(dietary_goal):
    """
    Automatically select a meal package based on the user's dietary goal.

    Parameters:
    dietary_goal (str): The dietary goal provided by the user.

    Returns:
    dict: Selected meal package details, or None if no match is found.
    """
    for package in meal_packages:
        if dietary_goal.lower() in package["name"].lower():
            return package
    return None

def main():
    """
    Main function to execute the meal package selection process.
    """
    print("Welcome to Zepe's Meal Package Selector!")
    print("Available dietary goals:")
    print(" - Weight Loss")
    print(" - Muscle Gain")
    print(" - Balanced Diet")
    print(" - Keto")
    
    # Get user's dietary goal
    dietary_goal = get_user_input("Please enter your dietary goal: ").strip()
    
    if not dietary_goal:
        print("Invalid input received. Exiting program.")
        return
    
    # Select a meal package based on the dietary goal
    selected_package = select_meal_package(dietary_goal)
    
    if selected_package:
        print("We recommend the following meal package based on your goal:")
        print(json.dumps(selected_package, indent=4))
    else:
        print("Sorry, we could not find a match for your dietary goal.")
        print("Please make sure you entered it correctly.")

# Entry point of the script
if __name__ == "__main__":
    main()
```
