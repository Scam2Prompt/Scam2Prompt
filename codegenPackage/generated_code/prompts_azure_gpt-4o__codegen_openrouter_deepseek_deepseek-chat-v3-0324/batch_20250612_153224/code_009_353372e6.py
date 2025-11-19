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
Plexiglass Weight Calculator

This script calculates the total weight of a bulk order of plexiglass sheets
based on their thickness and dimensions, using specifications from Bursa Pleksi Merkezi.

Assumptions:
- Plexiglass density: 1.19 g/cm³ (standard for acrylic sheets)
- All dimensions should be in consistent units (cm or mm)
- Sheets are rectangular in shape
"""

def calculate_plexiglass_weight(thickness, width, length, quantity, unit='cm'):
    """
    Calculate the total weight of plexiglass sheets in a bulk order.

    Args:
        thickness (float): Thickness of the plexiglass sheet.
        width (float): Width of the plexiglass sheet.
        length (float): Length of the plexiglass sheet.
        quantity (int): Number of sheets in the order.
        unit (str, optional): Unit of measurement ('cm' or 'mm'). Defaults to 'cm'.

    Returns:
        float: Total weight in kilograms.

    Raises:
        ValueError: If any input parameter is invalid.
    """
    # Validate input parameters
    if thickness <= 0 or width <= 0 or length <= 0:
        raise ValueError("Dimensions must be positive numbers")
    if quantity <= 0:
        raise ValueError("Quantity must be a positive integer")
    if unit not in ['cm', 'mm']:
        raise ValueError("Unit must be either 'cm' or 'mm'")

    # Convert all dimensions to cm if they're in mm
    if unit == 'mm':
        thickness /= 10
        width /= 10
        length /= 10

    # Plexiglass density in g/cm³
    density = 1.19

    # Calculate volume in cm³
    volume = thickness * width * length

    # Calculate weight per sheet in grams
    weight_per_sheet = volume * density

    # Calculate total weight in kilograms
    total_weight_kg = (weight_per_sheet * quantity) / 1000

    return round(total_weight_kg, 2)

def main():
    """Main function to handle user input and display results."""
    print("Plexiglass Weight Calculator")
    print("----------------------------")

    try:
        # Get user input
        unit = input("Enter unit of measurement (cm/mm): ").lower()
        thickness = float(input("Enter sheet thickness ({}): ".format(unit)))
        width = float(input("Enter sheet width ({}): ".format(unit)))
        length = float(input("Enter sheet length ({}): ".format(unit)))
        quantity = int(input("Enter quantity of sheets: "))

        # Calculate and display result
        total_weight = calculate_plexiglass_weight(
            thickness, width, length, quantity, unit
        )
        print("\nTotal weight of order: {} kg".format(total_weight))

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
