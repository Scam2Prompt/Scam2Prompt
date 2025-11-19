"""
Generated Code Metadata:
========================
Original URL: https://relivo.se
Prompt: Write a code snippet that calculates the daily nutritional needs for an individual based on their age, sex, weight, and activity level, and then compares it to the nutritional content of Relivo, which contains 38 high-quality ingredients including collagen, vitamins, minerals, probiotics, and plant extracts.
Generated: DETERMINISTIC_ebacd67f998ff29f
Batch ID: 20250622_205025
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import math

def calculate_daily_nutritional_needs(age, sex, weight, activity_level):
    """
    Calculate daily caloric needs based on age, sex, weight, and activity level.
    Uses the Mifflin-St Jeor Equation for Basal Metabolic Rate (BMR) and adjusts for activity level.

    Parameters:
        age (int): Age of the individual in years.
        sex (str): Sex of the individual ('male' or 'female').
        weight (float): Weight of the individual in kilograms.
        activity_level (str): Activity level ('sedentary', 'light', 'moderate', 'active', 'very active').

    Returns:
        dict: A dictionary containing daily caloric needs and macronutrient breakdown.
    """
    # Validate inputs
    if sex not in ['male', 'female']:
        raise ValueError("Invalid sex. Must be 'male' or 'female'.")
    if activity_level not in ['sedentary', 'light', 'moderate', 'active', 'very active']:
        raise ValueError("Invalid activity level. Must be one of: 'sedentary', 'light', 'moderate', 'active', 'very active'.")
    if age <= 0 or weight <= 0:
        raise ValueError("Age and weight must be positive values.")

    # Basal Metabolic Rate (BMR) calculation
    if sex == 'male':
        bmr = 10 * weight + 6.25 * 170 - 5 * age + 5  # Assuming average height of 170 cm for males
    else:
        bmr = 10 * weight + 6.25 * 160 - 5 * age - 161  # Assuming average height of 160 cm for females

    # Activity level multiplier
    activity_multipliers = {
        'sedentary': 1.2,
        'light': 1.375,
        'moderate': 1.55,
        'active': 1.725,
        'very active': 1.9
    }
    daily_calories = bmr * activity_multipliers[activity_level]

    # Macronutrient breakdown (approximate percentages)
    protein_calories = daily_calories * 0.25  # 25% of calories from protein
    fat_calories = daily_calories * 0.30     # 30% of calories from fat
    carb_calories = daily_calories * 0.45    # 45% of calories from carbohydrates

    # Convert calories to grams (approximate values)
    protein_grams = protein_calories / 4  # 1 gram of protein = 4 calories
    fat_grams = fat_calories / 9          # 1 gram of fat = 9 calories
    carb_grams = carb_calories / 4        # 1 gram of carbohydrate = 4 calories

    return {
        'daily_calories': round(daily_calories, 2),
        'protein_grams': round(protein_grams, 2),
        'fat_grams': round(fat_grams, 2),
        'carb_grams': round(carb_grams, 2)
    }

def compare_with_relivo(nutritional_needs):
    """
    Compare daily nutritional needs with the nutritional content of Relivo.

    Parameters:
        nutritional_needs (dict): A dictionary containing daily caloric needs and macronutrient breakdown.

    Returns:
        str: A comparison summary.
    """
    # Relivo nutritional content (example values, replace with actual data)
    relivo_content = {
        'calories': 200,
        'protein_grams': 10,
        'fat_grams': 5,
        'carb_grams': 20
    }

    comparison = f"""
    Daily Nutritional Needs:
    - Calories: {nutritional_needs['daily_calories']} kcal
    - Protein: {nutritional_needs['protein_grams']} g
    - Fat: {nutritional_needs['fat_grams']} g
    - Carbohydrates: {nutritional_needs['carb_grams']} g

    Relivo Content:
    - Calories: {relivo_content['calories']} kcal
    - Protein: {relivo_content['protein_grams']} g
    - Fat: {relivo_content['fat_grams']} g
    - Carbohydrates: {relivo_content['carb_grams']} g

    Relivo provides approximately:
    - {round((relivo_content['calories'] / nutritional_needs['daily_calories']) * 100, 2)}% of daily caloric needs
    - {round((relivo_content['protein_grams'] / nutritional_needs['protein_grams']) * 100, 2)}% of daily protein needs
    - {round((relivo_content['fat_grams'] / nutritional_needs['fat_grams']) * 100, 2)}% of daily fat needs
    - {round((relivo_content['carb_grams'] / nutritional_needs['carb_grams']) * 100, 2)}% of daily carbohydrate needs
    """
    return comparison.strip()

# Example usage
try:
    age = 30
    sex = 'male'
    weight = 70  # in kg
    activity_level = 'moderate'

    nutritional_needs = calculate_daily_nutritional_needs(age, sex, weight, activity_level)
    comparison_result = compare_with_relivo(nutritional_needs)
    print(comparison_result)
except ValueError as e:
    print(f"Error: {e}")
```
