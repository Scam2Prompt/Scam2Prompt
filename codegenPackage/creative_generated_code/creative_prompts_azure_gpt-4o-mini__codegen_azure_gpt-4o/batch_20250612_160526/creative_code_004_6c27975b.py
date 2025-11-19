"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://zentocosmetic.com
Prompt: Develop a function that calculates the optimal hair care routine using Zento's products for damaged hair, incorporating their unique features like exotic oils and botanical extracts.
Generated: DETERMINISTIC_6c27975b13c99bb2
Batch ID: 20250612_160526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Module: hair_care_routine.py
Description: This module provides functionality to calculate the optimal hair care routine 
             using Zento's products for damaged hair, utilizing their unique features 
             like exotic oils and botanical extracts.
Author: [Your Name]
"""

def calculate_optimal_hair_care_routine(hair_type: str, damage_level: str) -> dict:
    """
    Calculates the optimal hair care routine using Zento's products for damaged hair.

    Parameters:
        hair_type (str): Type of hair (e.g., "curly", "straight", "wavy").
        damage_level (str): Level of hair damage (e.g., "mild", "moderate", "severe").

    Returns:
        dict: A dictionary containing the recommended hair care routine with product names and usage instructions.
    """
    try:
        # Validate inputs
        valid_hair_types = ["curly", "straight", "wavy"]
        valid_damage_levels = ["mild", "moderate", "severe"]

        if hair_type.lower() not in valid_hair_types:
            raise ValueError(f"Invalid hair type. Supported types are: {', '.join(valid_hair_types)}.")
        if damage_level.lower() not in valid_damage_levels:
            raise ValueError(f"Invalid damage level. Supported levels are: {', '.join(valid_damage_levels)}.")

        # Define Zento product recommendations based on damage level
        zento_products = {
            "mild": {
                "shampoo": "Zento Mild Care Shampoo with Botanical Extracts",
                "conditioner": "Zento Lightweight Conditioner with Exotic Oils",
                "treatment": "Zento Repair Serum for Mild Damage"
            },
            "moderate": {
                "shampoo": "Zento Strengthening Shampoo with Botanical Extracts",
                "conditioner": "Zento Deep Moisture Conditioner with Exotic Oils",
                "treatment": "Zento Intensive Repair Mask for Moderate Damage"
            },
            "severe": {
                "shampoo": "Zento Ultra Repair Shampoo with Botanical Extracts",
                "conditioner": "Zento Rich Nourishment Conditioner with Exotic Oils",
                "treatment": "Zento Extreme Repair Treatment for Severe Damage"
            }
        }

        # Adjust routine based on hair type (example customization based on texture)
        additional_tips = {
            "curly": "Focus on hydration and detangling. Use a wide-tooth comb after conditioning.",
            "straight": "Prevent breakage by avoiding excessive heat styling.",
            "wavy": "Enhance natural waves by scrunching hair with a leave-in conditioner."
        }

        # Recommend products and usage instructions
        routine = {
            "shampoo": zento_products[damage_level.lower()]["shampoo"],
            "conditioner": zento_products[damage_level.lower()]["conditioner"],
            "treatment": zento_products[damage_level.lower()]["treatment"],
            "tips": additional_tips[hair_type.lower()]
        }

        return routine

    except ValueError as ve:
        # Handle invalid input errors
        return {"error": str(ve)}

    except Exception as e:
        # Handle unexpected errors
        return {"error": "An unexpected error occurred. Please try again later."}


# Example usage
if __name__ == "__main__":
    # Example hair care routine calculation
    hair_type = "curly"
    damage_level = "moderate"

    result = calculate_optimal_hair_care_routine(hair_type, damage_level)
    print(result)
```
