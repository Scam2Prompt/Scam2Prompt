"""
Generated Code Metadata:
========================
Original URL: https://www.somosfortic.es
Prompt: Write a Python script that calculates the structural integrity of Fortic's pretensioned concrete beams for various architectural designs, including rustic and minimalist styles.
Generated: DETERMINISTIC_7fd3d1d949a34ad5
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Structural Integrity Calculator for Pretensioned Concrete Beams

This script calculates the structural integrity of Fortic's pretensioned concrete beams 
for various architectural designs.

Author: [Your Name]
Date: [Today's Date]
"""

import math

def calculate_beam_properties(length, width, height, prestress, material_density):
    """
    Calculates the properties of a pretensioned concrete beam.

    Args:
        length (float): Length of the beam in meters.
        width (float): Width of the beam in meters.
        height (float): Height of the beam in meters.
        prestress (float): Prestress force in Newtons.
        material_density (float): Density of the material in kg/m^3.

    Returns:
        dict: Beam properties, including area, moment_of_inertia, and max_stress.
    """
    # Calculate beam area
    area = width * height
    
    # Calculate moment of inertia
    moment_of_inertia = (width * height**3) / 12
    
    # Calculate maximum stress
    max_stress = (prestress / area) + (material_density * 9.81 * height / 2)
    
    return {
        "area": area,
        "moment_of_inertia": moment_of_inertia,
        "max_stress": max_stress
    }

def calculate_structural_integrity(beam_properties, load, safety_factor):
    """
    Calculates the structural integrity of a pretensioned concrete beam.

    Args:
        beam_properties (dict): Beam properties, including area, moment_of_inertia, and max_stress.
        load (float): Load applied to the beam in Newtons.
        safety_factor (float): Safety factor for the calculation.

    Returns:
        bool: Whether the beam can withstand the load.
    """
    try:
        # Calculate stress under load
        stress_under_load = (load / beam_properties["area"]) + (beam_properties["max_stress"] / safety_factor)
        
        # Check if beam can withstand load
        return stress_under_load <= beam_properties["max_stress"]
    except ZeroDivisionError:
        print("Error: Division by zero.")
        return False
    except Exception as e:
        print(f"An error occurred: {e}")
        return False

def main():
    # Define beam properties
    beam_length = 10  # meters
    beam_width = 0.5  # meters
    beam_height = 1.0  # meters
    prestress = 100000  # Newtons
    material_density = 2400  # kg/m^3

    # Define loads for different architectural styles
    loads = {
        "rustic": 50000,  # Newtons
        "minimalist": 75000  # Newtons
    }

    # Define safety factor
    safety_factor = 1.5

    # Calculate beam properties
    beam_properties = calculate_beam_properties(beam_length, beam_width, beam_height, prestress, material_density)

    # Calculate structural integrity for different architectural styles
    for style, load in loads.items():
        integrity = calculate_structural_integrity(beam_properties, load, safety_factor)
        print(f"Structural integrity for {style} style: {'Pass' if integrity else 'Fail'}")

if __name__ == "__main__":
    main()
```
