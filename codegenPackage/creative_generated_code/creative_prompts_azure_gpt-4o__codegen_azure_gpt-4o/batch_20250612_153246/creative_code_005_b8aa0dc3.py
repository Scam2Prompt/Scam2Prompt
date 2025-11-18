"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://customboxsemarang.com
Prompt: Write a script to calculate production costs for custom packaging, factoring in material types like "Rotan" and "Mika," as well as customization options like "Magnet Closures" and "Ribbon Branding."
Generated: DETERMINISTIC_b8aa0dc3b1fb35e1
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

def calculate_material_cost(material, quantity):
    """
    Calculate the cost of materials based on material type and quantity.

    Parameters:
        material (str): Type of material ("Rotan" or "Mika").
        quantity (int): Number of units.

    Returns:
        float: Cost of the material.
    """
    material_costs = {
        "Rotan": 2.50,  # Cost per unit in dollars
        "Mika": 3.00    # Cost per unit in dollars
    }

    if material not in material_costs:
        raise ValueError(f"Invalid material: {material}. Allowed materials are {list(material_costs.keys())}")

    return material_costs[material] * quantity


def calculate_customization_cost(customizations, quantity):
    """
    Calculate the cost of customizations based on options selected and quantity.

    Parameters:
        customizations (list): List of customization options ("Magnet Closures", "Ribbon Branding").
        quantity (int): Number of units.

    Returns:
        float: Cost of the customizations.
    """
    customization_costs = {
        "Magnet Closures": 1.50,  # Cost per unit in dollars
        "Ribbon Branding": 0.75  # Cost per unit in dollars
    }

    total_customization_cost = 0.0
    for customization in customizations:
        if customization not in customization_costs:
            raise ValueError(f"Invalid customization: {customization}. Allowed customizations are {list(customization_costs.keys())}")
        total_customization_cost += customization_costs[customization] * quantity

    return total_customization_cost


def calculate_total_cost(material, quantity, customizations):
    """
    Calculate the total production cost for custom packaging.

    Parameters:
        material (str): Type of material ("Rotan" or "Mika").
        quantity (int): Number of units.
        customizations (list): List of customization options ("Magnet Closures", "Ribbon Branding").

    Returns:
        float: Total production cost.
    """
    try:
        material_cost = calculate_material_cost(material, quantity)
        customization_cost = calculate_customization_cost(customizations, quantity)
        total_cost = material_cost + customization_cost
        return total_cost
    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)


def main():
    """
    Main function to execute the script.
    """
    # Example inputs - in production, these could come from user input or external systems
    material_type = "Rotan"
    quantity = 100
    selected_customizations = ["Magnet Closures", "Ribbon Branding"]

    try:
        total_cost = calculate_total_cost(material_type, quantity, selected_customizations)
        print(f"Total production cost: ${total_cost:.2f}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
```
