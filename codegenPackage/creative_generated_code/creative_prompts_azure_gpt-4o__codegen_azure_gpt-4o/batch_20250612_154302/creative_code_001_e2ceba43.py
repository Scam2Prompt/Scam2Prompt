"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dbxtools.in
Prompt: Generate a script to calculate torque settings for tube expansion using a digital torque controller, such as the DTW-15 model mentioned on the DBX Tools website.
Generated: DETERMINISTIC_e2ceba432b5579f4
Batch ID: 20250612_154302
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Script to calculate torque settings for tube expansion using a digital torque controller (e.g., DTW-15 model).
This script is intended to assist in determining appropriate torque settings based on user input such as tube material,
diameter, wall thickness, and expansion factor.

Author: [Your Name]
Date: [Insert Date]
"""

# Import necessary modules
import math

def calculate_torque(material, tube_diameter, wall_thickness, expansion_factor):
    """
    Calculate the torque setting for tube expansion.

    Parameters:
        material (str): The material of the tube (e.g., "steel", "aluminum", "copper").
        tube_diameter (float): The outer diameter of the tube in millimeters.
        wall_thickness (float): The wall thickness of the tube in millimeters.
        expansion_factor (float): The desired expansion factor, typically between 1.1 and 1.5.

    Returns:
        float: Recommended torque setting in Nm.

    Raises:
        ValueError: If input values are invalid (e.g., negative numbers or unsupported materials).
    """
    # Material torque coefficient mapping
    material_coefficients = {
        "steel": 1.2,  # Steel has a higher coefficient due to its strength
        "aluminum": 0.8,  # Aluminum is softer than steel
        "copper": 0.9  # Copper is somewhere in between
    }

    # Validate inputs
    if material not in material_coefficients:
        raise ValueError(f"Unsupported material: {material}. Supported materials are: {', '.join(material_coefficients.keys())}")
    if tube_diameter <= 0 or wall_thickness <= 0 or expansion_factor <= 1.0:
        raise ValueError("Invalid input: All values must be positive and expansion_factor must be > 1.0.")

    # Calculate the torque based on material properties and geometric factors
    base_torque = material_coefficients[material] * tube_diameter * wall_thickness
    adjusted_torque = base_torque * expansion_factor

    return round(adjusted_torque, 2)

def main():
    """
    Main function to gather user input and calculate the torque setting.
    """
    print("Torque Setting Calculator for Tube Expansion")
    print("------------------------------------------")

    try:
        # Gather user input
        material = input("Enter tube material (steel, aluminum, copper): ").strip().lower()
        tube_diameter = float(input("Enter tube diameter in mm: "))
        wall_thickness = float(input("Enter wall thickness in mm: "))
        expansion_factor = float(input("Enter expansion factor (e.g., 1.1 to 1.5): "))

        # Calculate torque
        torque = calculate_torque(material, tube_diameter, wall_thickness, expansion_factor)
        print(f"\nRecommended Torque Setting: {torque} Nm")

    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
