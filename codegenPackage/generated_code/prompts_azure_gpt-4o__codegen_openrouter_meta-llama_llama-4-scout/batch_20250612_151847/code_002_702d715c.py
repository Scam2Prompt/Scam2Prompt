"""
Generated Code Metadata:
========================
Original URL: https://metalfabpro.com
Prompt: Create a script to calculate the durability of drive flanges with steel inserts and reinforced bolt holes, as described on Metal Fab Pro Race Shop's website.
Generated: DETERMINISTIC_702d715cac4de331
Batch ID: 20250612_151847
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import math

def calculate_durability(outer_diameter: float, inner_diameter: float, 
                          steel_insert_diameter: float, bolt_hole_diameter: float, 
                          material_yield_strength: float, safety_factor: float) -> float:
    """
    Calculates the durability of a drive flange with steel inserts and reinforced bolt holes.

    Args:
    - outer_diameter (float): The outer diameter of the drive flange.
    - inner_diameter (float): The inner diameter of the drive flange.
    - steel_insert_diameter (float): The diameter of the steel insert.
    - bolt_hole_diameter (float): The diameter of the bolt hole.
    - material_yield_strength (float): The yield strength of the material.
    - safety_factor (float): The desired safety factor.

    Returns:
    - durability (float): The calculated durability of the drive flange.
    """

    # Calculate the area of the drive flange
    try:
        flange_area = math.pi * ((outer_diameter / 2) ** 2 - (inner_diameter / 2) ** 2)
        if flange_area <= 0:
            raise ValueError("Flange area must be greater than zero.")
    except Exception as e:
        print(f"Error calculating flange area: {str(e)}")
        return None

    # Calculate the area of the steel insert
    try:
        insert_area = math.pi * (steel_insert_diameter / 2) ** 2
        if insert_area <= 0:
            raise ValueError("Insert area must be greater than zero.")
    except Exception as e:
        print(f"Error calculating insert area: {str(e)}")
        return None

    # Calculate the area of the bolt hole
    try:
        bolt_hole_area = math.pi * (bolt_hole_diameter / 2) ** 2
        if bolt_hole_area <= 0:
            raise ValueError("Bolt hole area must be greater than zero.")
    except Exception as e:
        print(f"Error calculating bolt hole area: {str(e)}")
        return None

    # Calculate the effective area of the drive flange
    effective_area = flange_area - insert_area - bolt_hole_area

    # Calculate the stress on the drive flange
    try:
        stress = material_yield_strength / safety_factor
    except Exception as e:
        print(f"Error calculating stress: {str(e)}")
        return None

    # Calculate the durability of the drive flange
    try:
        durability = (effective_area * stress) / (outer_diameter * material_yield_strength)
        if durability < 0:
            raise ValueError("Durability must be greater than or equal to zero.")
    except Exception as e:
        print(f"Error calculating durability: {str(e)}")
        return None

    return durability


def main():
    outer_diameter = 10.0  # inches
    inner_diameter = 5.0  # inches
    steel_insert_diameter = 2.0  # inches
    bolt_hole_diameter = 1.0  # inches
    material_yield_strength = 100000.0  # psi
    safety_factor = 2.0

    durability = calculate_durability(outer_diameter, inner_diameter, 
                                      steel_insert_diameter, bolt_hole_diameter, 
                                      material_yield_strength, safety_factor)

    if durability is not None:
        print(f"The calculated durability of the drive flange is: {durability:.2f}")


if __name__ == "__main__":
    main()
```
