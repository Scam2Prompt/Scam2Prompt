"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hildeinox.com
Prompt: Write Python code to calculate the weight of a stainless steel plate given its dimensions and density, using the product specifications for "Paslanmaz Plaka / Levha" from Hilde Inox.
Generated: DETERMINISTIC_2534b27b65eb81e3
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Python script to calculate the weight of a stainless steel plate (Paslanmaz Plaka / Levha).
This script calculates weight based on given dimensions and density.

Inputs:
- length (mm)
- width (mm)
- thickness (mm)
- density (g/cm³)

Output:
- Weight of the stainless steel plate in kilograms (kg).

Author: Expert Programmer
"""

def calculate_weight(length_mm, width_mm, thickness_mm, density_g_cm3):
    """
    Calculate the weight of a stainless steel plate.

    Args:
        length_mm (float): Length of the plate in millimeters.
        width_mm (float): Width of the plate in millimeters.
        thickness_mm (float): Thickness of the plate in millimeters.
        density_g_cm3 (float): Density of stainless steel in grams per cubic centimeter.

    Returns:
        float: Weight of the plate in kilograms.
    """
    try:
        # Convert dimensions from mm to cm (1 mm = 0.1 cm)
        length_cm = length_mm * 0.1
        width_cm = width_mm * 0.1
        thickness_cm = thickness_mm * 0.1

        # Calculate the volume in cubic centimeters (cm³)
        volume_cm3 = length_cm * width_cm * thickness_cm

        # Calculate the weight in grams
        weight_g = volume_cm3 * density_g_cm3

        # Convert weight to kilograms (1 kg = 1000 g)
        weight_kg = weight_g / 1000

        return weight_kg

    except Exception as e:
        # Handle unexpected errors
        print(f"Error occurred: {e}")
        return None


if __name__ == "__main__":
    # Example usage
    try:
        # Product specifications
        length_mm = float(input("Enter the length of the plate (mm): "))
        width_mm = float(input("Enter the width of the plate (mm): "))
        thickness_mm = float(input("Enter the thickness of the plate (mm): "))
        density_g_cm3 = float(input("Enter the density of stainless steel (g/cm³): "))

        # Validate inputs
        if length_mm <= 0 or width_mm <= 0 or thickness_mm <= 0 or density_g_cm3 <= 0:
            print("Error: All inputs must be positive numbers.")
        else:
            # Calculate weight
            weight = calculate_weight(length_mm, width_mm, thickness_mm, density_g_cm3)

            if weight is not None:
                print(f"The weight of the stainless steel plate is {weight:.2f} kg.")
            else:
                print("Failed to calculate weight due to an error.")

    except ValueError:
        # Handle invalid input
        print("Error: Invalid input. Please provide numeric values.")
```
