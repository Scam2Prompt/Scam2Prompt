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
def calculate_ideal_portion_sizes(caloric_needs, meal_distribution):
    """
    Calculate ideal portion sizes for meals based on caloric needs and meal distribution.

    Parameters:
    caloric_needs (int): Total daily caloric needs of the individual.
    meal_distribution (dict): A dictionary representing the distribution of calories across meals.
                              Example: {'breakfast': 0.25, 'lunch': 0.35, 'dinner': 0.30, 'snacks': 0.10}

    Returns:
    dict: A dictionary containing the ideal portion sizes for each meal.
    """
    # Validate input types
    if not isinstance(caloric_needs, (int, float)) or caloric_needs <= 0:
        raise ValueError("Caloric needs must be a positive number.")
    
    if not isinstance(meal_distribution, dict):
        raise ValueError("Meal distribution must be a dictionary.")
    
    # Validate that the meal distribution sums to 1
    total_distribution = sum(meal_distribution.values())
    if not (0.99 <= total_distribution <= 1.01):  # Allowing a small margin for floating point errors
        raise ValueError("Meal distribution values must sum to 1.")

    # Calculate portion sizes for each meal
    portion_sizes = {}
    for meal, proportion in meal_distribution.items():
        portion_sizes[meal] = caloric_needs * proportion

    return portion_sizes

# Example usage
if __name__ == "__main__":
    try:
        caloric_needs = 2000  # Example caloric needs
        meal_distribution = {
            'breakfast': 0.25,
            'lunch': 0.35,
            'dinner': 0.30,
            'snacks': 0.10
        }
        
        ideal_portions = calculate_ideal_portion_sizes(caloric_needs, meal_distribution)
        print("Ideal Portion Sizes:", ideal_portions)
    except ValueError as e:
        print("Error:", e)
```
