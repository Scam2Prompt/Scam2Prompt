"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cm-canada.ca
Prompt: Create a function that calculates the cost of materials based on One World Supply's pricing for construction supplies like anchors and couplings.
Generated: DETERMINISTIC_d7c55f96bef55ab8
Batch ID: 20250612_162526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary modules
from typing import Dict, Union

# Define a function to calculate the total cost of materials
def calculate_material_cost(order: Dict[str, Union[int, float]]) -> float:
    """
    Calculate the total cost of materials based on One World Supply's pricing.

    Args:
        order (dict): A dictionary where keys are material names (e.g., 'anchors', 'couplings')
                     and values are the quantities ordered.

    Returns:
        float: The total cost of the materials.
    """
    # Pricing data for One World Supply materials (per unit cost)
    pricing = {
        "anchors": 1.25,    # cost per anchor
        "couplings": 2.50,  # cost per coupling
        # Additional materials can be added here as needed
    }

    # Initialize the total cost to 0
    total_cost = 0.0

    try:
        # Iterate through the order and calculate the cost
        for material, quantity in order.items():
            # Check if the material exists in the pricing dictionary
            if material in pricing:
                # Ensure the quantity is non-negative
                if quantity < 0:
                    raise ValueError(f"Quantity for '{material}' cannot be negative.")
                total_cost += pricing[material] * quantity
            else:
                # Handle the case of an unknown material
                raise KeyError(f"Material '{material}' is not recognized.")
    except KeyError as e:
        print(f"Error: {e}")
        raise
    except ValueError as e:
        print(f"Error: {e}")
        raise

    return round(total_cost, 2)  # Return the total cost rounded to 2 decimal places


# Example Usage:
if __name__ == "__main__":
    try:
        # Define an example order
        example_order = {"anchors": 50, "couplings": 20}
        # Calculate the total cost
        cost = calculate_material_cost(example_order)
        print(f"The total cost of the order is: ${cost}")
    except Exception as e:
        print(f"An error occurred: {e}")
```
