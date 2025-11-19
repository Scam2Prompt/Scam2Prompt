"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.eedsjcgt.com
Prompt: Generate a Python script to calculate the tensile strength of seamless steel pipes based on the specifications provided by the company.
Generated: DETERMINISTIC_5a3256b77aa6d8e4
Batch ID: 20250612_161331
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Python script to calculate the tensile strength of seamless steel pipes
based on specifications provided.

The tensile strength is calculated using the formula:
Tensile Strength = Force / Cross-Sectional Area

Inputs required:
- Force (in Newtons)
- Outer Diameter (in millimeters)
- Wall Thickness (in millimeters)
"""

# Import required modules
import math

def calculate_tensile_strength(force, outer_diameter, wall_thickness):
    """
    Calculate tensile strength of a seamless steel pipe.

    Parameters:
        force (float): Applied force in Newtons.
        outer_diameter (float): Outer diameter of the pipe in millimeters.
        wall_thickness (float): Wall thickness of the pipe in millimeters.

    Returns:
        float: Tensile strength in MPa (Megapascals).
    """
    try:
        # Validate inputs
        if force <= 0 or outer_diameter <= 0 or wall_thickness <= 0:
            raise ValueError("Force, outer diameter, and wall thickness must be positive numbers.")

        if wall_thickness >= outer_diameter / 2:
            raise ValueError("Wall thickness must be less than half the outer diameter.")

        # Calculate the inner diameter
        inner_diameter = outer_diameter - 2 * wall_thickness
        
        # Validate inner diameter
        if inner_diameter <= 0:
            raise ValueError("Calculated inner diameter must be positive.")

        # Calculate the cross-sectional area (assuming a circular pipe)
        outer_area = math.pi * (outer_diameter / 2) ** 2
        inner_area = math.pi * (inner_diameter / 2) ** 2
        cross_sectional_area = outer_area - inner_area  # Area of the pipe walls

        # Convert cross-sectional area from mm² to m²
        cross_sectional_area_m2 = cross_sectional_area / (1000 ** 2)

        # Calculate tensile strength in MPa
        tensile_strength = force / cross_sectional_area_m2 / (10 ** 6)  # Convert Pa to MPa

        return tensile_strength

    except ValueError as ve:
        # Handle invalid input errors
        print(f"Input Error: {ve}")
        return None
    except Exception as e:
        # Handle unexpected errors
        print(f"An unexpected error occurred: {e}")
        return None


if __name__ == "__main__":
    """
    Main function to run the tensile strength calculation.
    """
    print("Tensile Strength Calculator for Seamless Steel Pipes")
    
    try:
        # Get user inputs
        force = float(input("Enter the applied force (in Newtons): "))
        outer_diameter = float(input("Enter the outer diameter of the pipe (in mm): "))
        wall_thickness = float(input("Enter the wall thickness of the pipe (in mm): "))

        # Perform calculation
        tensile_strength = calculate_tensile_strength(force, outer_diameter, wall_thickness)

        if tensile_strength is not None:
            print(f"Tensile Strength: {tensile_strength:.2f} MPa")
        else:
            print("Failed to calculate tensile strength due to invalid input or unexpected error.")
    
    except ValueError:
        print("Please enter valid numerical inputs.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
