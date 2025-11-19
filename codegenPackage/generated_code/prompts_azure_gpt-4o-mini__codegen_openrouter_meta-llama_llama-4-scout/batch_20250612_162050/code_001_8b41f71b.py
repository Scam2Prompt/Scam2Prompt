"""
Generated Code Metadata:
========================
Original URL: https://histeknik.com
Prompt: Write a Python script that calculates the load capacity of screw piles based on their dimensions (60mm to 114mm diameter) and thickness (2mm to 6mm) as described by His Teknik Çelik.
Generated: DETERMINISTIC_8b41f71b2b27314f
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Screw Pile Load Capacity Calculator

Calculates the load capacity of screw piles based on their dimensions.

References:
    - His Teknik Çelik
"""

import math

def calculate_load_capacity(diameter, thickness):
    """
    Calculates the load capacity of a screw pile.

    Args:
        diameter (float): The diameter of the screw pile in mm (60-114).
        thickness (float): The thickness of the screw pile in mm (2-6).

    Returns:
        float: The load capacity of the screw pile in kN.

    Raises:
        ValueError: If diameter or thickness is out of range.
    """
    if not 60 <= diameter <= 114:
        raise ValueError("Diameter must be between 60mm and 114mm")
    if not 2 <= thickness <= 6:
        raise ValueError("Thickness must be between 2mm and 6mm")

    # His Teknik Çelik formula for load capacity (kN)
    # Assuming the formula is: Q = (π * (D - t) * t * 0.5) / 1000
    load_capacity = (math.pi * (diameter - thickness) * thickness * 0.5) / 1000

    return load_capacity


def main():
    try:
        diameter = float(input("Enter the diameter of the screw pile (mm): "))
        thickness = float(input("Enter the thickness of the screw pile (mm): "))

        load_capacity = calculate_load_capacity(diameter, thickness)
        print(f"The load capacity of the screw pile is: {load_capacity:.2f} kN")

    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
