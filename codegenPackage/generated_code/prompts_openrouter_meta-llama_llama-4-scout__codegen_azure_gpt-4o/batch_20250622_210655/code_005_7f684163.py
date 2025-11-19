"""
Generated Code Metadata:
========================
Original URL: https://superdar.com
Prompt: Recommend a wooden chair design, similar to the "Елдорадо" or "Виола" chairs, to match a rectangular dining table made of solid wood.
Generated: DETERMINISTIC_7f6841637403ea58
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# wooden_chair_recommender.py

# Import necessary libraries
import json

# Define a function to recommend a wooden chair design
def recommend_chair(table_shape, material, chair_styles):
    """
    Recommend a wooden chair design based on the table shape and material.

    Args:
        table_shape (str): Shape of the dining table (e.g., "rectangular").
        material (str): Material of the dining table (e.g., "solid wood").
        chair_styles (list): List of available chair styles with their details.

    Returns:
        dict: Recommended chair design details.
    """
    try:
        # Validate inputs
        if not isinstance(table_shape, str) or not isinstance(material, str):
            raise ValueError("Table shape and material must be strings.")
        if not isinstance(chair_styles, list) or not all(isinstance(style, dict) for style in chair_styles):
            raise ValueError("Chair styles must be a list of dictionaries.")

        # Filter chair styles based on compatibility with the table
        compatible_chairs = [
            chair for chair in chair_styles
            if chair.get("material") == material and chair.get("compatible_table_shapes", []) == table_shape
        ]

        # If no compatible chairs are found, recommend a default option
        if not compatible_chairs:
            return {
                "recommendation": "No exact match found. Consider a versatile chair design.",
                "default_option": {
                    "name": "Classic Wooden Chair",
                    "material": "solid wood",
                    "features": ["ergonomic design", "durable construction", "minimalist style"]
                }
            }

        # Return the first compatible chair as the recommendation
        return {
            "recommendation": "Recommended chair design based on your table.",
            "chair_details": compatible_chairs[0]
        }

    except Exception as e:
        # Handle unexpected errors
        return {"error": str(e)}

# Example usage
if __name__ == "__main__":
    # Define available chair styles
    chair_styles = [
        {
            "name": "Елдорадо",
            "material": "solid wood",
            "compatible_table_shapes": ["rectangular", "oval"],
            "features": ["classic design", "comfortable seating", "sturdy build"]
        },
        {
            "name": "Виола",
            "material": "solid wood",
            "compatible_table_shapes": ["rectangular"],
            "features": ["modern aesthetic", "lightweight", "easy to clean"]
        },
        {
            "name": "Rustic Charm",
            "material": "reclaimed wood",
            "compatible_table_shapes": ["round"],
            "features": ["unique texture", "eco-friendly", "vintage look"]
        }
    ]

    # Define table properties
    table_shape = "rectangular"
    material = "solid wood"

    # Get chair recommendation
    recommendation = recommend_chair(table_shape, material, chair_styles)

    # Print the recommendation in a readable format
    print(json.dumps(recommendation, indent=4))
```
