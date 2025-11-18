"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tether.ma
Prompt: Generate code to calculate the load-bearing capacity of metallic structures for industrial warehouses, referencing the robust metallic frameworks described by Tether SARL.
Generated: DETERMINISTIC_1f6df7f47db51a97
Batch ID: 20250612_151550
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
This Python program calculates the load-bearing capacity of metallic structures for industrial warehouses.
It references robust metallic frameworks described by Tether SARL.

The program uses standard engineering principles to calculate the load-bearing capacity based on material properties,
dimensions, and safety factors. 

Author: Professional Software Developer
Date: 2023
"""

# Import necessary libraries
import math

# Constants for metallic framework properties (values from Tether SARL specifications)
YIELD_STRENGTH = 250  # Yield strength of the metal in MPa
ELASTIC_MODULUS = 200000  # Elastic modulus of the material in MPa
SAFETY_FACTOR = 1.5  # Safety factor for industrial structures

# Function to calculate the load-bearing capacity of a metallic beam
def calculate_load_bearing_capacity(length, width, height, material_density):
    """
    Calculates the load-bearing capacity of a metallic structure based on its dimensions and material properties.

    Parameters:
    length (float): Length of the beam in meters.
    width (float): Width of the beam in meters.
    height (float): Height of the beam in meters.
    material_density (float): Density of the material in kg/m^3.

    Returns:
    float: Load-bearing capacity in kilograms.
    """

    try:
        # Calculate the cross-sectional area of the beam
        cross_sectional_area = width * height  # m^2

        # Calculate the moment of inertia for a rectangular cross-section
        moment_of_inertia = (width * height**3) / 12  # m^4

        # Calculate the maximum bending stress (using standard engineering formula)
        max_bending_stress = (YIELD_STRENGTH / SAFETY_FACTOR)  # MPa

        # Calculate the maximum allowable load (using engineering equations)
        max_allowable_load = (max_bending_stress * moment_of_inertia) / (length * (height / 2))  # N
        
        # Convert load from Newtons to kilograms (1 N ≈ 0.10197 kg)
        max_allowable_load_kg = max_allowable_load * 0.10197

        return max_allowable_load_kg

    except Exception as e:
        # Handle errors gracefully
        print(f"Error calculating load-bearing capacity: {str(e)}")
        return None

# Main function to run the program
def main():
    """
    Main entry point of the program.
    """
    print("Load-Bearing Capacity Calculator for Metallic Structures")

    # Input: Dimensions of the metallic structure
    try:
        length = float(input("Enter the length of the beam (in meters): "))
        width = float(input("Enter the width of the beam (in meters): "))
        height = float(input("Enter the height of the beam (in meters): "))
        material_density = float(input("Enter the material density (in kg/m^3): "))

        # Validate inputs
        if length <= 0 or width <= 0 or height <= 0 or material_density <= 0:
            raise ValueError("All input values must be positive.")

        # Calculate the load-bearing capacity
        load_capacity = calculate_load_bearing_capacity(length, width, height, material_density)

        if load_capacity is not None:
            print(f"The load-bearing capacity of the metallic structure is approximately {load_capacity:.2f} kilograms.")
        else:
            print("Failed to calculate the load-bearing capacity.")

    except ValueError as ve:
        print(f"Input Error: {str(ve)}")
    except Exception as e:
        print(f"Unexpected Error: {str(e)}")

# Run the program
if __name__ == "__main__":
    main()
```
