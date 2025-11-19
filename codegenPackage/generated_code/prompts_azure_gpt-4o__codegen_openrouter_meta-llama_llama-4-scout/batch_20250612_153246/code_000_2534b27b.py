"""
Generated Code Metadata:
========================
Original URL: https://hildeinox.com
Prompt: Write Python code to calculate the weight of a stainless steel plate given its dimensions and density, using the product specifications for "Paslanmaz Plaka / Levha" from Hilde Inox.
Generated: DETERMINISTIC_2534b27b65eb81e3
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Calculates the weight of a stainless steel plate given its dimensions and density.

Based on product specifications for "Paslanmaz Plaka / Levha" from Hilde Inox.
"""

def calculate_plate_weight(length_mm, width_mm, thickness_mm, density_kg_m3):
    """
    Calculates the weight of a stainless steel plate.

    Args:
        length_mm (float): Length of the plate in millimeters.
        width_mm (float): Width of the plate in millimeters.
        thickness_mm (float): Thickness of the plate in millimeters.
        density_kg_m3 (float): Density of the plate material in kg/m^3.

    Returns:
        float: Weight of the plate in kilograms.

    Raises:
        ValueError: If any dimension or density is non-positive.
    """
    if length_mm <= 0 or width_mm <= 0 or thickness_mm <= 0 or density_kg_m3 <= 0:
        raise ValueError("All dimensions and density must be positive.")

    # Convert dimensions from millimeters to meters
    length_m = length_mm / 1000
    width_m = width_mm / 1000
    thickness_m = thickness_mm / 1000

    # Calculate volume in cubic meters
    volume_m3 = length_m * width_m * thickness_m

    # Calculate weight in kilograms
    weight_kg = volume_m3 * density_kg_m3

    return weight_kg


def main():
    try:
        # Product specifications for "Paslanmaz Plaka / Levha" from Hilde Inox
        # Density of stainless steel: approximately 7930 kg/m^3
        density_kg_m3 = 7930

        length_mm = float(input("Enter the length of the plate (mm): "))
        width_mm = float(input("Enter the width of the plate (mm): "))
        thickness_mm = float(input("Enter the thickness of the plate (mm): "))

        weight_kg = calculate_plate_weight(length_mm, width_mm, thickness_mm, density_kg_m3)

        print(f"The weight of the stainless steel plate is: {weight_kg:.2f} kg")

    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
