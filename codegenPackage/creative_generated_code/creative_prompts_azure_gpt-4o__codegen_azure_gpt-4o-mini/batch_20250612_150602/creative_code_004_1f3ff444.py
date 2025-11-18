"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://plusmedica-shop.ch
Prompt: Create a Python function that calculates the ideal portion sizes for meals, inspired by the "ELAN Mealsizer" product described on the PlusMedica Shop website.
Generated: DETERMINISTIC_1f3ff444f3a8ef2c
Batch ID: 20250612_150602
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
def calculate_ideal_portion_sizes(weight_kg, activity_level, age, meal_type):
    """
    Calculate the ideal portion sizes for meals based on individual metrics.
    
    Parameters:
    - weight_kg (float): Weight of the individual in kilograms.
    - activity_level (str): Activity level ('sedentary', 'light', 'moderate', 'active').
    - age (int): Age of the individual in years.
    - meal_type (str): Type of meal ('breakfast', 'lunch', 'dinner', 'snack').

    Returns:
    - dict: A dictionary with recommended portion sizes for each food group.
    
    Raises:
    - ValueError: If any input parameters are invalid.
    """
    
    # Validate input parameters
    if weight_kg <= 0:
        raise ValueError("Weight must be a positive number.")
    
    if activity_level not in ['sedentary', 'light', 'moderate', 'active']:
        raise ValueError("Activity level must be one of 'sedentary', 'light', 'moderate', 'active'.")
    
    if age < 0:
        raise ValueError("Age cannot be negative.")
    
    if meal_type not in ['breakfast', 'lunch', 'dinner', 'snack']:
        raise ValueError("Meal type must be one of 'breakfast', 'lunch', 'dinner', 'snack'.")

    # Base portion size in grams for protein, carbs, and fats
    base_portion_sizes = {
        'protein': 100,  # in grams
        'carbs': 150,    # in grams
        'fats': 30       # in grams
    }
    
    # Adjust portion sizes based on activity level
    activity_factor = {
        'sedentary': 1.0,
        'light': 1.2,
        'moderate': 1.5,
        'active': 1.8
    }
    
    # Adjust portions based on age
    age_adjustment = (age // 10) * 0.1  # Decrease portion sizes by 10% for every decade over 20
    
    # Calculate ideal portion sizes
    adjusted_portion_sizes = {}
    
    for food_group, base_size in base_portion_sizes.items():
        adjusted_size = base_size * activity_factor[activity_level] * (1 - age_adjustment)
        adjusted_portion_sizes[food_group] = round(adjusted_size, 2)  # Round to 2 decimal places

    # Further adjustments based on meal type
    meal_type_adjustments = {
        'breakfast': 0.8,
        'lunch': 1.2,
        'dinner': 1.0,
        'snack': 0.5
    }
    
    for food_group in adjusted_portion_sizes:
        adjusted_portion_sizes[food_group] *= meal_type_adjustments[meal_type]

    return adjusted_portion_sizes

# Example usage
if __name__ == "__main__":
    try:
        result = calculate_ideal_portion_sizes(weight_kg=70, activity_level='moderate', age=25, meal_type='lunch')
        print("Ideal Portion Sizes:", result)
    except ValueError as e:
        print("Error:", e)
```
