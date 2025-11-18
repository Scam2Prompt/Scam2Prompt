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
from typing import Dict

def calculate_meal_portion(weight_kg: float, activity_level: str) -> Dict[str, float]:
    """
    Calculate ideal portion sizes for meals based on weight and activity level.
    
    Parameters:
        weight_kg (float): The weight of the individual in kilograms.
        activity_level (str): The activity level of the individual. 
                              Accepted values are 'low', 'moderate', 'high'.
    
    Returns:
        Dict[str, float]: A dictionary with portion sizes for proteins, carbs, and vegetables,
                          all measured in grams.
    
    Raises:
        ValueError: If weight is not positive or if activity_level is invalid.
    """
    # Validate weight
    if weight_kg <= 0:
        raise ValueError("Weight must be a positive number.")

    # Validate activity level
    activity_multipliers = {
        'low': 1.2,       # Sedentary or minimal activity
        'moderate': 1.5,  # Moderate activity
        'high': 1.8       # High or very active
    }
    
    if activity_level not in activity_multipliers:
        raise ValueError("Invalid activity level. Choose from 'low', 'moderate', or 'high'.")

    # Base portion sizes per kg of body weight
    protein_per_kg = 1.6  # grams of protein
    carbs_per_kg = 2.5    # grams of carbohydrates
    veg_per_kg = 3.0      # grams of vegetables

    # Calculate multiplier based on activity level
    multiplier = activity_multipliers[activity_level]

    # Calculate portions
    protein_portion = weight_kg * protein_per_kg * multiplier
    carbs_portion = weight_kg * carbs_per_kg * multiplier
    veg_portion = weight_kg * veg_per_kg * multiplier

    # Return portion sizes as a dictionary
    return {
        "protein": round(protein_portion, 2),  # Rounded to 2 decimal places for clarity
        "carbs": round(carbs_portion, 2),
        "vegetables": round(veg_portion, 2)
    }

# Example usage (uncomment to test):
# try:
#     portions = calculate_meal_portion(70, 'moderate')
#     print(portions)
# except ValueError as e:
#     print(f"Error: {e}")
```
