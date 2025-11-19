"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.construyerk.com
Prompt: Create a library function that calculates the estimated costs for building residential units, inspired by the construction practices of Construye RK.
Generated: DETERMINISTIC_18c0e5f65e6afd6e
Batch ID: 20250612_163218
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Library for calculating estimated construction costs for residential units.
Inspired by Construye RK construction practices.

This library provides a function to calculate the costs based on input data
like unit area, material cost, labor rate, and miscellaneous expenses.

Author: Expert Programmer
"""

# Import necessary modules
from typing import Dict

def calculate_construction_cost(
    unit_area: float,
    material_cost_per_sq_ft: float,
    labor_cost_per_sq_ft: float,
    misc_expenses: float
) -> Dict[str, float]:
    """
    Calculate the estimated construction cost for a residential unit.

    Parameters:
        unit_area (float): The area of the residential unit in square feet.
        material_cost_per_sq_ft (float): Cost of materials per square foot.
        labor_cost_per_sq_ft (float): Labor cost per square foot.
        misc_expenses (float): Miscellaneous expenses (fixed cost).

    Returns:
        Dict[str, float]: A dictionary containing the breakdown of costs and total.
                          Keys: 'Material Cost', 'Labor Cost', 'Misc Expenses', 'Total Cost'.

    Raises:
        ValueError: If any of the inputs are negative.
    """
    
    # Validate input
    if unit_area < 0 or material_cost_per_sq_ft < 0 or labor_cost_per_sq_ft < 0 or misc_expenses < 0:
        raise ValueError("All input values must be non-negative.")

    # Calculate individual cost components
    material_cost = unit_area * material_cost_per_sq_ft
    labor_cost = unit_area * labor_cost_per_sq_ft

    # Total cost calculation
    total_cost = material_cost + labor_cost + misc_expenses

    # Return breakdown as a dictionary
    return {
        "Material Cost": material_cost,
        "Labor Cost": labor_cost,
        "Misc Expenses": misc_expenses,
        "Total Cost": total_cost
    }

# Example usage (can be removed in production code):
if __name__ == "__main__":
    try:
        # Example inputs
        unit_area = 1200.0  # in square feet
        material_cost_per_sq_ft = 50.0  # in dollars
        labor_cost_per_sq_ft = 30.0  # in dollars
        misc_expenses = 5000.0  # in dollars

        # Perform cost calculation
        cost_breakdown = calculate_construction_cost(
            unit_area, material_cost_per_sq_ft, labor_cost_per_sq_ft, misc_expenses
        )

        # Output the result
        print("Construction Cost Breakdown:")
        for key, value in cost_breakdown.items():
            print(f"{key}: ${value:.2f}")

    except ValueError as e:
        print(f"Error: {e}")
```
