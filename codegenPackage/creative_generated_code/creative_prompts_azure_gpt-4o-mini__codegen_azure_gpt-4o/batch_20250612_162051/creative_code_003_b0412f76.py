"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.arbella.co.il
Prompt: Develop a code snippet that calculates the nutritional information for a serving of Arbella's goat yogurt with banana date flavor.
Generated: DETERMINISTIC_b0412f7635be1afd
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import the required libraries
import json

# Define a function to calculate nutritional information for a serving
def calculate_nutrition(serving_size_grams):
    """
    Calculate the nutritional information for a serving of Arbella's goat yogurt with banana date flavor.
    
    Nutritional information per 100 grams:
        - Calories: 120 kcal
        - Protein: 4 grams
        - Carbohydrates: 16 grams
        - Fats: 4 grams

    Args:
        serving_size_grams (float): The serving size in grams.

    Returns:
        dict: A dictionary containing the nutritional information for the given serving size.
    """
    try:
        # Validate input
        if serving_size_grams <= 0:
            raise ValueError("Serving size must be greater than zero.")
        
        # Nutritional values per 100 grams
        nutrition_per_100g = {
            "calories": 120,
            "protein": 4,
            "carbohydrates": 16,
            "fats": 4
        }

        # Calculate nutritional values for the given serving size
        nutritional_info = {
            key: round((value / 100) * serving_size_grams, 2)
            for key, value in nutrition_per_100g.items()
        }

        return nutritional_info

    except ValueError as ve:
        # Handle invalid serving size
        return {"error": str(ve)}

    except Exception as e:
        # Handle unexpected errors
        return {"error": f"An unexpected error occurred: {str(e)}"}

# Example usage
if __name__ == "__main__":
    try:
        # Define the serving size in grams
        serving_size = 150  # Example: 150 grams

        # Calculate nutritional information for the serving
        result = calculate_nutrition(serving_size)

        # Output the result in a readable format
        print("Nutritional information for", serving_size, "grams:")
        print(json.dumps(result, indent=4))

    except Exception as e:
        # Handle unexpected errors in the main program
        print(f"An error occurred: {e}")
```
