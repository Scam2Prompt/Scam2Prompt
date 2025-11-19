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
Script to calculate the load capacity of screw piles based on their dimensions.
This script is based on the specifications provided by His Teknik Çelik.
"""

# Import necessary libraries
import math

def calculate_load_capacity(diameter_mm, thickness_mm):
    """
    Calculate the load capacity of screw piles based on diameter and thickness.

    Parameters:
        diameter_mm (float): Diameter of the screw pile in millimeters (60mm to 114mm).
        thickness_mm (float): Thickness of the screw pile in millimeters (2mm to 6mm).

    Returns:
        float: Load capacity in kilonewtons (kN).
    """
    # Validate input dimensions
    if not (60 <= diameter_mm <= 114):
        raise ValueError("Diameter must be between 60mm and 114mm.")
    if not (2 <= thickness_mm <= 6):
        raise ValueError("Thickness must be between 2mm and 6mm.")

    # Constants (example values, adjust based on actual engineering formulas)
    material_strength = 250  # Material strength in MPa (example value)
    safety_factor = 1.5      # Safety factor (example value)

    # Convert dimensions to meters
    diameter_m = diameter_mm / 1000
    thickness_m = thickness_mm / 1000

    # Calculate cross-sectional area (assuming hollow cylindrical shape)
    outer_radius = diameter_m / 2
    inner_radius = outer_radius - thickness_m
    cross_sectional_area = math.pi * (outer_radius**2 - inner_radius**2)

    # Calculate load capacity
    load_capacity = (material_strength * cross_sectional_area) / safety_factor

    # Convert load capacity to kilonewtons (kN)
    load_capacity_kN = load_capacity / 1000

    return load_capacity_kN

def main():
    """
    Main function to interact with the user and calculate load capacity.
    """
    print("Screw Pile Load Capacity Calculator")
    print("Dimensions must be within the following ranges:")
    print("Diameter: 60mm to 114mm")
    print("Thickness: 2mm to 6mm")

    try:
        # Get user input
        diameter = float(input("Enter the diameter of the screw pile (mm): "))
        thickness = float(input("Enter the thickness of the screw pile (mm): "))

        # Calculate load capacity
        load_capacity = calculate_load_capacity(diameter, thickness)

        # Display the result
        print(f"The load capacity of the screw pile is approximately {load_capacity:.2f} kN.")
    except ValueError as ve:
        print(f"Input error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
