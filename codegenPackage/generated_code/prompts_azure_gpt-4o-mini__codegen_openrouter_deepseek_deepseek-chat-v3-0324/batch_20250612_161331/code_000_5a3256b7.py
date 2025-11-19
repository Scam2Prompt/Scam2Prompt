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
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Script to calculate the tensile strength of seamless steel pipes based on specifications.

The script takes input parameters such as outer diameter, wall thickness, and material grade,
then calculates the tensile strength using standard formulas.

Error handling is included for invalid inputs and edge cases.
"""

import math
from enum import Enum

class MaterialGrade(Enum):
    """Enumeration of common material grades for seamless steel pipes."""
    ASTM_A106 = "ASTM A106"
    ASTM_A53 = "ASTM A53"
    API_5L_B = "API 5L B"
    API_5L_X42 = "API 5L X42"
    API_5L_X52 = "API 5L X52"

# Material properties: minimum tensile strength in MPa
MATERIAL_PROPERTIES = {
    MaterialGrade.ASTM_A106: 415,
    MaterialGrade.ASTM_A53: 330,
    MaterialGrade.API_5L_B: 414,
    MaterialGrade.API_5L_X42: 414,
    MaterialGrade.API_5L_X52: 455,
}

def calculate_tensile_strength(outer_diameter: float, wall_thickness: float, material_grade: MaterialGrade) -> float:
    """
    Calculate the tensile strength of a seamless steel pipe.
    
    Args:
        outer_diameter: Outer diameter of the pipe in millimeters
        wall_thickness: Wall thickness of the pipe in millimeters
        material_grade: Material grade from the MaterialGrade enum
    
    Returns:
        Tensile strength in Newtons
    
    Raises:
        ValueError: If inputs are invalid or out of range
    """
    # Input validation
    if outer_diameter <= 0:
        raise ValueError("Outer diameter must be positive")
    if wall_thickness <= 0:
        raise ValueError("Wall thickness must be positive")
    if outer_diameter <= 2 * wall_thickness:
        raise ValueError("Wall thickness cannot be greater than or equal to half the outer diameter")
    if material_grade not in MATERIAL_PROPERTIES:
        raise ValueError("Invalid material grade specified")
    
    # Calculate cross-sectional area (mm²)
    inner_diameter = outer_diameter - 2 * wall_thickness
    cross_sectional_area = (math.pi / 4) * (outer_diameter**2 - inner_diameter**2)
    
    # Get material tensile strength (MPa)
    tensile_strength_mpa = MATERIAL_PROPERTIES[material_grade]
    
    # Convert MPa to N/mm² (1 MPa = 1 N/mm²)
    tensile_strength_n = tensile_strength_mpa * cross_sectional_area
    
    return tensile_strength_n

def main():
    """Main function to demonstrate the tensile strength calculation."""
    try:
        # Example usage
        od = float(input("Enter outer diameter (mm): "))
        wt = float(input("Enter wall thickness (mm): "))
        
        print("\nAvailable material grades:")
        for grade in MaterialGrade:
            print(f"- {grade.value}")
        
        grade_input = input("\nEnter material grade: ")
        try:
            material_grade = MaterialGrade(grade_input)
        except ValueError:
            raise ValueError(f"Invalid material grade. Please choose from {[g.value for g in MaterialGrade]}")
        
        strength = calculate_tensile_strength(od, wt, material_grade)
        print(f"\nTensile strength: {strength:.2f} N")
        
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
