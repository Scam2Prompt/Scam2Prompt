"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://paslanmazspider.org
Prompt: Develop a script to automate the selection of stainless steel railing components, such as spider fittings and glass connectors, based on user input for material grade and design constraints, referencing DEKSAN Paslanmaz Çelik's product offerings.
Generated: DETERMINISTIC_7227d33a5738a655
Batch ID: 20250612_153606
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# stainless_steel_selector.py
# Script to automate the selection of stainless steel railing components based on user input.
# This script references DEKSAN Paslanmaz Çelik's product offerings.

import json

# Sample product catalog (replace with real DEKSAN product data)
PRODUCT_CATALOG = [
    {
        "name": "Spider Fitting A",
        "type": "Spider Fitting",
        "material_grade": "304",
        "design_constraints": {"max_glass_weight": 100, "max_glass_thickness": 12},
    },
    {
        "name": "Spider Fitting B",
        "type": "Spider Fitting",
        "material_grade": "316",
        "design_constraints": {"max_glass_weight": 150, "max_glass_thickness": 15},
    },
    {
        "name": "Glass Connector A",
        "type": "Glass Connector",
        "material_grade": "304",
        "design_constraints": {"max_glass_thickness": 10},
    },
    {
        "name": "Glass Connector B",
        "type": "Glass Connector",
        "material_grade": "316",
        "design_constraints": {"max_glass_thickness": 12},
    },
]

# Function to get user input for selection criteria
def get_user_input():
    """
    Prompt the user to input material grade and design constraints.

    Returns:
        dict: A dictionary containing the user's criteria.
    """
    print("Welcome to the Stainless Steel Component Selector!")
    material_grade = input("Enter desired material grade (e.g., 304, 316): ").strip()
    try:
        max_glass_weight = float(input("Enter maximum glass weight (kg) (or press Enter to skip): ").strip() or 0)
        max_glass_thickness = float(input("Enter maximum glass thickness (mm): ").strip())
    except ValueError:
        print("Invalid input. Please enter numeric values for weight and thickness.")
        exit(1)

    return {
        "material_grade": material_grade,
        "design_constraints": {
            "max_glass_weight": max_glass_weight,
            "max_glass_thickness": max_glass_thickness,
        },
    }

# Function to filter products based on user criteria
def filter_products(catalog, criteria):
    """
    Filter the product catalog based on user input.

    Args:
        catalog (list): The product catalog containing product details.
        criteria (dict): User-provided selection criteria.

    Returns:
        list: A list of products that meet the criteria.
    """
    filtered_products = []
    for product in catalog:
        # Check material grade
        if product["material_grade"] != criteria["material_grade"]:
            continue
        
        # Check design constraints
        constraints = product["design_constraints"]
        user_constraints = criteria["design_constraints"]

        if (
            user_constraints["max_glass_thickness"] <= constraints.get("max_glass_thickness", float('inf')) and
            user_constraints["max_glass_weight"] <= constraints.get("max_glass_weight", float('inf'))
        ):
            filtered_products.append(product)
    
    return filtered_products

# Main function
def main():
    """
    Main function to drive the script.
    """
    user_criteria = get_user_input()
    selected_products = filter_products(PRODUCT_CATALOG, user_criteria)

    if selected_products:
        print("\nMatching Products:")
        for product in selected_products:
            print(json.dumps(product, indent=4))
    else:
        print("\nNo products match the provided criteria. Please try again with different inputs.")

# Entry point
if __name__ == "__main__":
    main()
```
