"""
Generated Code Metadata:
========================
Original URL: https://www.bursapleksi.com.tr
Prompt: Create a Python script to calculate the total weight of a bulk order of plexiglass sheets based on their thickness and dimensions, using the specifications provided by Bursa Pleksi Merkezi.
Generated: DETERMINISTIC_353372e6da89b89d
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Calculates the total weight of a bulk order of plexiglass sheets.

Based on specifications provided by Bursa Pleksi Merkezi.
"""

import math

def calculate_plexiglass_weight(thickness, length, width, density=1.18):
    """
    Calculates the weight of a single plexiglass sheet.

    Args:
        thickness (float): Thickness of the plexiglass sheet in mm.
        length (float): Length of the plexiglass sheet in meters.
        width (float): Width of the plexiglass sheet in meters.
        density (float, optional): Density of plexiglass in g/cm^3. Defaults to 1.18.

    Returns:
        float: Weight of the plexiglass sheet in kilograms.
    """
    # Convert thickness from mm to cm
    thickness_cm = thickness / 10

    # Calculate area in square meters
    area_m2 = length * width

    # Convert area from square meters to square centimeters
    area_cm2 = area_m2 * 10_000

    # Calculate volume in cubic centimeters
    volume_cm3 = area_cm2 * thickness_cm

    # Calculate weight in grams
    weight_g = volume_cm3 * density

    # Convert weight from grams to kilograms
    weight_kg = weight_g / 1_000

    return weight_kg


def calculate_total_weight(sheets, thickness, length, width, density=1.18):
    """
    Calculates the total weight of a bulk order of plexiglass sheets.

    Args:
        sheets (int): Number of plexiglass sheets in the order.
        thickness (float): Thickness of the plexiglass sheets in mm.
        length (float): Length of the plexiglass sheets in meters.
        width (float): Width of the plexiglass sheets in meters.
        density (float, optional): Density of plexiglass in g/cm^3. Defaults to 1.18.

    Returns:
        float: Total weight of the bulk order in kilograms.
    """
    try:
        if sheets <= 0:
            raise ValueError("Number of sheets must be a positive integer.")

        if thickness <= 0 or length <= 0 or width <= 0:
            raise ValueError("Thickness, length, and width must be positive numbers.")

        weight_per_sheet = calculate_plexiglass_weight(thickness, length, width, density)
        total_weight = weight_per_sheet * sheets

        return total_weight

    except ValueError as e:
        print(f"Error: {e}")
        return None


def main():
    try:
        num_sheets = int(input("Enter the number of plexiglass sheets: "))
        thickness_mm = float(input("Enter the thickness of the plexiglass sheets in mm: "))
        length_m = float(input("Enter the length of the plexiglass sheets in meters: "))
        width_m = float(input("Enter the width of the plexiglass sheets in meters: "))

        total_weight = calculate_total_weight(num_sheets, thickness_mm, length_m, width_m)

        if total_weight is not None:
            print(f"The total weight of the bulk order is: {total_weight:.2f} kg")

    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
