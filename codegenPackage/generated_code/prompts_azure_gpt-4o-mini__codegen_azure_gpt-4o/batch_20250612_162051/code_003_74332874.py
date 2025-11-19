"""
Generated Code Metadata:
========================
Original URL: https://www.madoniaoli.it
Prompt: Develop a function that calculates the health benefits of using Madonia's extra virgin olive oil in daily cooking, referencing its properties and characteristics.
Generated: DETERMINISTIC_7433287471ec25e9
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
This module provides a function to calculate the health benefits of using Madonia's extra virgin olive oil
in daily cooking. The function references its properties and characteristics, such as high antioxidant content,
healthy fats, and anti-inflammatory properties.

Note: This is a simplified calculation based on general nutritional data and assumptions.
For precise health benefits, consult a nutritionist or medical professional.
"""

def calculate_health_benefits(servings_per_day, serving_size_ml):
    """
    Calculate the health benefits of using Madonia's extra virgin olive oil in daily cooking.

    Parameters:
        servings_per_day (int): Number of servings of olive oil consumed per day.
        serving_size_ml (float): Size of each serving in milliliters.

    Returns:
        dict: A dictionary containing estimated health benefits based on consumption.
    """
    try:
        # Validate inputs
        if servings_per_day <= 0 or serving_size_ml <= 0:
            raise ValueError("Servings per day and serving size must be positive numbers.")

        # Properties of Madonia's extra virgin olive oil (approximate values per 1 ml)
        antioxidants_per_ml = 0.2  # mg of antioxidants
        healthy_fats_per_ml = 0.9  # grams of monounsaturated fats
        anti_inflammatory_score_per_ml = 0.1  # arbitrary score for anti-inflammatory properties

        # Calculate total consumption per day
        total_consumption_ml = servings_per_day * serving_size_ml

        # Calculate health benefits
        total_antioxidants = total_consumption_ml * antioxidants_per_ml
        total_healthy_fats = total_consumption_ml * healthy_fats_per_ml
        total_anti_inflammatory_score = total_consumption_ml * anti_inflammatory_score_per_ml

        # Return results as a dictionary
        return {
            "total_antioxidants_mg": round(total_antioxidants, 2),
            "total_healthy_fats_g": round(total_healthy_fats, 2),
            "total_anti_inflammatory_score": round(total_anti_inflammatory_score, 2),
        }

    except ValueError as ve:
        # Handle invalid input errors
        return {"error": str(ve)}

    except Exception as e:
        # Handle unexpected errors
        return {"error": f"An unexpected error occurred: {str(e)}"}


# Example usage
if __name__ == "__main__":
    # Example: 2 servings per day, each serving is 15 ml
    result = calculate_health_benefits(servings_per_day=2, serving_size_ml=15)
    print(result)
```
