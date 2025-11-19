"""
Generated Code Metadata:
========================
Original URL: https://www.eedsjcgt.com
Prompt: Generate a Python script to calculate the tensile strength of seamless steel pipes based on the specifications provided by the company.
Generated: DETERMINISTIC_5a3256b77aa6d8e4
Batch ID: 20250612_161331
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Calculates the tensile strength of seamless steel pipes.

This script uses the formula for tensile strength, which is the maximum stress 
a material can withstand while being stretched or pulled before failing.

Tensile Strength (σ) = Maximum Load / Cross-sectional Area

Where:
- Maximum Load is in Newtons (N)
- Cross-sectional Area is in square millimeters (mm^2)

The formula for the cross-sectional area of a circle (pipe) is:
A = π * (d/2)^2

Where:
- d is the diameter of the pipe in millimeters (mm)
"""

import math

def calculate_tensile_strength(max_load: float, diameter: float) -> float:
    """
    Calculates the tensile strength of a seamless steel pipe.

    Args:
    - max_load (float): The maximum load in Newtons (N).
    - diameter (float): The diameter of the pipe in millimeters (mm).

    Returns:
    - tensile_strength (float): The tensile strength in megapascals (MPa).
    """
    try:
        if max_load <= 0:
            raise ValueError("Maximum load must be greater than zero.")
        if diameter <= 0:
            raise ValueError("Diameter must be greater than zero.")

        # Calculate cross-sectional area
        cross_sectional_area = math.pi * (diameter / 2) ** 2

        # Calculate tensile strength in Pascals (Pa)
        tensile_strength_pa = max_load / cross_sectional_area

        # Convert tensile strength to megapascals (MPa)
        tensile_strength_mpa = tensile_strength_pa / 1e6

        return tensile_strength_mpa

    except ValueError as ve:
        print(f"Error: {ve}")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None


def main():
    # Example usage
    max_load = 10000  # in Newtons (N)
    diameter = 10     # in millimeters (mm)

    tensile_strength = calculate_tensile_strength(max_load, diameter)

    if tensile_strength is not None:
        print(f"The tensile strength of the seamless steel pipe is {tensile_strength:.2f} MPa")


if __name__ == "__main__":
    main()
```
