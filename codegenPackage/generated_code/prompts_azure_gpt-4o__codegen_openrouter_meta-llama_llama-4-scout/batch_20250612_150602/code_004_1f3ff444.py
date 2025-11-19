"""
Generated Code Metadata:
========================
Original URL: https://plusmedica-shop.ch
Prompt: Create a Python function that calculates the ideal portion sizes for meals, inspired by the "ELAN Mealsizer" product described on the PlusMedica Shop website.
Generated: DETERMINISTIC_1f3ff444f3a8ef2c
Batch ID: 20250612_150602
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Module for calculating ideal portion sizes for meals.

Inspired by the ELAN Mealsizer product.
"""

def calculate_portion_size(weight, activity_level, age, sex):
    """
    Calculate the ideal portion size for a meal.

    Args:
    - weight (float): Weight in kg.
    - activity_level (str): Activity level ('sedentary', 'lightly_active', 'moderately_active', 'very_active', 'extra_active').
    - age (int): Age in years.
    - sex (str): Sex ('male', 'female').

    Returns:
    - portion_size (float): Ideal portion size in grams.

    Raises:
    - ValueError: If activity level or sex is invalid.
    """

    # Define activity multipliers
    activity_multipliers = {
        'sedentary': 1.2,
        'lightly_active': 1.375,
        'moderately_active': 1.55,
        'very_active': 1.725,
        'extra_active': 1.9
    }

    # Check activity level
    if activity_level not in activity_multipliers:
        raise ValueError("Invalid activity level. Choose from: {}".format(", ".join(activity_multipliers.keys())))

    # Define sex-specific basal metabolic rates (BMR) in kcal
    bmr_values = {
        'male': 66 + (6.2 * weight) + (12.7 * 175) - (6.8 * age),
        'female': 655 + (4.35 * weight) + (4.7 * 175) - (4.7 * age)
    }

    # Check sex
    if sex not in bmr_values:
        raise ValueError("Invalid sex. Choose from: {}".format(", ".join(bmr_values.keys())))

    # Calculate daily caloric needs
    bmr = bmr_values[sex]
    daily_caloric_needs = bmr * activity_multipliers[activity_level]

    # Assume 3 main meals and 2 snacks per day
    meal_count = 5

    # Calculate portion size in kcal
    portion_size_kcal = daily_caloric_needs / meal_count

    # Convert kcal to grams (approx. 4 kcal/g for protein, 9 kcal/g for fat, 4 kcal/g for carbs)
    # Use a rough estimate of macronutrient distribution: 15% protein, 25% fat, 60% carbs
    protein_kcal = portion_size_kcal * 0.15
    fat_kcal = portion_size_kcal * 0.25
    carbs_kcal = portion_size_kcal * 0.6

    protein_g = protein_kcal / 4
    fat_g = fat_kcal / 9
    carbs_g = carbs_kcal / 4

    portion_size_g = protein_g + fat_g + carbs_g

    return portion_size_g


def main():
    try:
        weight = float(input("Enter your weight in kg: "))
        activity_level = input("Enter your activity level (sedentary, lightly_active, moderately_active, very_active, extra_active): ")
        age = int(input("Enter your age in years: "))
        sex = input("Enter your sex (male, female): ")

        portion_size = calculate_portion_size(weight, activity_level, age, sex)
        print("Ideal portion size: {:.2f} grams".format(portion_size))
    except ValueError as e:
        print("Error: {}".format(e))


if __name__ == "__main__":
    main()
```
