"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://segretoskincare.it
Prompt: Generate a Python script that utilizes the principles of scientific formulation to create a skincare product similar to those offered by Segreto Skincare, focusing on skin repair and regeneration.
Generated: DETERMINISTIC_6cc6470795fc8382
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random

class SkincareProduct:
    """
    A class representing a skincare product formulation focusing on skin repair and regeneration.
    """
    def __init__(self):
        # Initialize the base ingredients typically used in skin repair formulations
        self.base_ingredients = {
            "water": 50,  # % by weight
            "glycerin": 10,  # % by weight, humectant
            "niacinamide": 5,  # % by weight, skin barrier repair
            "panthenol": 3,  # % by weight, soothing agent
            "aloe_vera_extract": 5,  # % by weight, calming and hydrating
        }
        self.active_ingredients = {
            "retinol": 0.5,  # % by weight, promotes cell turnover
            "peptides": 2,  # % by weight, supports collagen synthesis
            "hyaluronic_acid": 1,  # % by weight, deep hydration
        }
        self.preservatives = {
            "phenoxyethanol": 0.8,  # % by weight, prevents microbial growth
            "ethylhexyl_glycerin": 0.4,  # % by weight, preservative booster
        }
        self.emulsifiers = {
            "cetearyl_alcohol": 2,  # % by weight, stability and texture
            "polysorbate_20": 1,  # % by weight, emulsifier
        }

    def generate_formula(self):
        """
        Generate a skincare product formula as a dictionary with percentage weights.
        Ensures total percentages do not exceed 100%.
        """
        formula = {}
        total_percentage = 0

        # Add base ingredients
        for ingredient, percentage in self.base_ingredients.items():
            formula[ingredient] = percentage
            total_percentage += percentage

        # Add active ingredients
        for ingredient, percentage in self.active_ingredients.items():
            formula[ingredient] = percentage
            total_percentage += percentage

        # Add preservatives
        for ingredient, percentage in self.preservatives.items():
            formula[ingredient] = percentage
            total_percentage += percentage

        # Add emulsifiers
        for ingredient, percentage in self.emulsifiers.items():
            formula[ingredient] = percentage
            total_percentage += percentage

        # Ensure the formula does not exceed 100%
        if total_percentage > 100:
            raise ValueError("Total percentage of ingredients exceeds 100%. Adjust formulation.")

        # Add water to balance formula to 100%
        formula["water"] += (100 - total_percentage)

        return formula

    def suggest_skin_type(self):
        """
        Suggests the appropriate skin type for this product based on active ingredients.
        """
        skin_type_suggestions = []
        if "retinol" in self.active_ingredients:
            skin_type_suggestions.append("Aging Skin")
        if "niacinamide" in self.base_ingredients:
            skin_type_suggestions.append("Sensitive Skin")
        if "hyaluronic_acid" in self.active_ingredients:
            skin_type_suggestions.append("Dry Skin")

        return skin_type_suggestions

def main():
    """
    Main function for generating a skincare product formula and suggesting appropriate skin types.
    """
    try:
        print("Creating a skincare product formulation...")
        product = SkincareProduct()

        # Generate the formula
        formula = product.generate_formula()
        print("\nGenerated Skincare Product Formula:")
        for ingredient, percentage in formula.items():
            print(f"{ingredient}: {percentage:.2f}%")

        # Suggest suitable skin types
        skin_type_suggestions = product.suggest_skin_type()
        print("\nSuggested Skin Types:")
        for suggestion in skin_type_suggestions:
            print(f"- {suggestion}")

    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
