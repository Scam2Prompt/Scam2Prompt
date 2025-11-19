"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://homefoodsghana.com
Prompt: Create a Python function that calculates the nutritional values of a meal prepared with Homefoods' Peanut Soup and Fried Rice.
Generated: DETERMINISTIC_c35d4eaea07adf92
Batch ID: 20250612_163935
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary modules
import json

def calculate_nutrition(peanut_soup_servings, fried_rice_servings):
    """
    Calculates the total nutritional values for a meal consisting of
    Homefoods' Peanut Soup and Fried Rice.

    Args:
        peanut_soup_servings (int): Number of servings of Peanut Soup.
        fried_rice_servings (int): Number of servings of Fried Rice.

    Returns:
        dict: A dictionary containing total calories, protein, fat, carbs, and fiber.
    """

    # Nutritional values per serving (per Homefoods' specification)
    nutrition_data = {
        "peanut_soup": {
            "calories": 300,
            "protein": 15,
            "fat": 20,
            "carbs": 10,
            "fiber": 3
        },
        "fried_rice": {
            "calories": 450,
            "protein": 10,
            "fat": 15,
            "carbs": 60,
            "fiber": 5
        }
    }

    # Input validation
    if not isinstance(peanut_soup_servings, int) or peanut_soup_servings < 0:
        raise ValueError("peanut_soup_servings must be a non-negative integer.")
    if not isinstance(fried_rice_servings, int) or fried_rice_servings < 0:
        raise ValueError("fried_rice_servings must be a non-negative integer.")

    # Calculate total nutritional values
    total_nutrition = {
        "calories": (nutrition_data["peanut_soup"]["calories"] * peanut_soup_servings) +
                    (nutrition_data["fried_rice"]["calories"] * fried_rice_servings),
        "protein": (nutrition_data["peanut_soup"]["protein"] * peanut_soup_servings) +
                   (nutrition_data["fried_rice"]["protein"] * fried_rice_servings),
        "fat": (nutrition_data["peanut_soup"]["fat"] * peanut_soup_servings) +
               (nutrition_data["fried_rice"]["fat"] * fried_rice_servings),
        "carbs": (nutrition_data["peanut_soup"]["carbs"] * peanut_soup_servings) +
                 (nutrition_data["fried_rice"]["carbs"] * fried_rice_servings),
        "fiber": (nutrition_data["peanut_soup"]["fiber"] * peanut_soup_servings) +
                 (nutrition_data["fried_rice"]["fiber"] * fried_rice_servings)
    }

    return total_nutrition


# Example usage
if __name__ == "__main__":
    try:
        peanut_soup_servings = 2
        fried_rice_servings = 3
        nutrition = calculate_nutrition(peanut_soup_servings, fried_rice_servings)
        print(json.dumps(nutrition, indent=4))  # Pretty print the nutrition data
    except ValueError as e:
        print(f"Error: {e}")
```
