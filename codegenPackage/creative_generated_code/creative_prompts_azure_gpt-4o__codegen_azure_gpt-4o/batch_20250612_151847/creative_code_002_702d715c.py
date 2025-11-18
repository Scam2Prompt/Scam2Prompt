"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metalfabpro.com
Prompt: Create a script to calculate the durability of drive flanges with steel inserts and reinforced bolt holes, as described on Metal Fab Pro Race Shop's website.
Generated: DETERMINISTIC_702d715cac4de331
Batch ID: 20250612_151847
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is the Python script that calculates the durability of drive flanges based on steel inserts and reinforced bolt holes:

```python
import math

# Define constants (these may need to be adjusted based on actual materials and specs)
STEEL_INSERT_STRENGTH = 250  # Tensile strength of steel inserts in MPa
BOLT_HOLE_REINFORCEMENT_FACTOR = 1.5  # Strength multiplier for reinforced bolt holes
SAFETY_FACTOR = 1.2  # Safety factor for real-world durability

# Function to calculate flange durability
def calculate_flange_durability(material_strength, flange_thickness, bolt_hole_diameter, num_bolt_holes):
    """
    Calculate the durability of drive flanges.

    Parameters:
        material_strength (float): Strength of the flange material in MPa.
        flange_thickness (float): Thickness of the flange in mm.
        bolt_hole_diameter (float): Diameter of bolt holes in mm.
        num_bolt_holes (int): Number of bolt holes in the flange.

    Returns:
        float: Estimated durability value for the drive flange.
    """
    try:
        # Calculate base durability using material strength and flange thickness
        base_durability = material_strength * flange_thickness

        # Calculate the reduction in durability caused by bolt holes
        bolt_holes_weakness = num_bolt_holes * (math.pi * (bolt_hole_diameter / 2) ** 2)

        # Adjust for reinforced bolt holes
        reinforced_bolt_holes_effect = bolt_holes_weakness / BOLT_HOLE_REINFORCEMENT_FACTOR

        # Adjust for steel inserts
        steel_insert_effect = STEEL_INSERT_STRENGTH * flange_thickness

        # Combine effects to calculate final durability
        durability = (base_durability + steel_insert_effect - reinforced_bolt_holes_effect) / SAFETY_FACTOR

        # Ensure durability is non-negative
        return max(durability, 0)

    except Exception as e:
        # Handle any errors gracefully
        print(f"Error calculating flange durability: {e}")
        return None

# Example usage
if __name__ == "__main__":
    # Parameters for calculation
    material_strength = 180  # MPa
    flange_thickness = 10  # mm
    bolt_hole_diameter = 8  # mm
    num_bolt_holes = 6

    # Calculate durability
    durability = calculate_flange_durability(material_strength, flange_thickness, bolt_hole_diameter, num_bolt_holes)

    # Output result
    if durability is not None:
        print(f"The calculated durability of the drive flange is: {durability:.2f}")
```

This script calculates the durability of a drive flange based on physical properties and material strengths. Adjust the provided constants and parameters as needed to fit the actual specifications from Metal Fab Pro Race Shop's website.
