"""
Generated Code Metadata:
========================
Original URL: https://compensadosscursel.blogspot.com
Prompt: Develop a function that estimates the cost of producing doors from Sucupira and Itauba, based on the pricing strategies of Nobre Painéis Ltda.
Generated: DETERMINISTIC_4c1d1d7a26ad27ee
Batch ID: 20250612_155128
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary modules
from typing import Dict

def estimate_door_cost(material: str, dimensions: Dict[str, float], quantity: int) -> float:
    """
    Estimates the cost of producing doors based on material, dimensions, and quantity.

    Parameters:
        material (str): The type of wood material ('Sucupira' or 'Itauba').
        dimensions (Dict[str, float]): A dictionary containing the dimensions of the door:
                                       - 'height' (in meters)
                                       - 'width' (in meters)
                                       - 'thickness' (in meters)
        quantity (int): The number of doors to be produced.

    Returns:
        float: The estimated total cost of producing the doors.

    Raises:
        ValueError: If the material is not 'Sucupira' or 'Itauba'.
        ValueError: If dimensions are invalid (negative or zero values).
        ValueError: If quantity is less than 1.
    """
    # Pricing per cubic meter for each material
    material_cost_per_cubic_meter = {
        'Sucupira': 1500.0,  # Cost in currency units per cubic meter
        'Itauba': 1800.0     # Cost in currency units per cubic meter
    }

    # Validate material
    if material not in material_cost_per_cubic_meter:
        raise ValueError("Invalid material. Choose either 'Sucupira' or 'Itauba'.")

    # Validate dimensions
    if any(dim <= 0 for dim in dimensions.values()):
        raise ValueError("Invalid dimensions. All dimensions must be positive values.")

    # Validate quantity
    if quantity < 1:
        raise ValueError("Invalid quantity. Quantity must be at least 1.")

    # Calculate the volume of a single door (height * width * thickness)
    door_volume = dimensions['height'] * dimensions['width'] * dimensions['thickness']

    # Calculate the cost of a single door
    single_door_cost = door_volume * material_cost_per_cubic_meter[material]

    # Calculate the total cost for the specified quantity
    total_cost = single_door_cost * quantity

    return total_cost

# Example usage:
if __name__ == "__main__":
    try:
        # Define door specifications
        material = "Sucupira"
        dimensions = {"height": 2.0, "width": 0.8, "thickness": 0.04}  # Dimensions in meters
        quantity = 10

        # Estimate cost
        cost = estimate_door_cost(material, dimensions, quantity)
        print(f"The estimated cost for producing {quantity} {material} doors is: {cost:.2f} currency units.")
    except ValueError as e:
        print(f"Error: {e}")
```
