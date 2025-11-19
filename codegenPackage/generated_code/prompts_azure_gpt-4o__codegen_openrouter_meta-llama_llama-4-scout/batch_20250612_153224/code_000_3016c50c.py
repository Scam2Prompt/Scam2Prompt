"""
Generated Code Metadata:
========================
Original URL: https://atilumber.com
Prompt: Write a Python script to calculate the volume of sawn timber required for a construction project, using dimensions and specifications similar to those described by Askar Trading International.
Generated: DETERMINISTIC_3016c50c924556bd
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
Calculates the volume of sawn timber required for a construction project.

This script uses dimensions and specifications similar to those described by 
Askar Trading International.

Author: [Your Name]
Date: [Today's Date]
"""

def calculate_timber_volume(length, width, thickness, quantity):
    """
    Calculates the volume of sawn timber in cubic meters.

    Args:
        length (float): Length of the timber in meters.
        width (float): Width of the timber in meters.
        thickness (float): Thickness of the timber in meters.
        quantity (int): Quantity of timber required.

    Returns:
        float: Volume of timber required in cubic meters.
    """
    if length <= 0 or width <= 0 or thickness <= 0 or quantity <= 0:
        raise ValueError("All dimensions and quantity must be greater than zero.")

    volume = length * width * thickness * quantity
    return volume


def calculate_board_feet(length, width, thickness, quantity):
    """
    Calculates the volume of sawn timber in board feet.

    1 board foot = 0.002359737 cubic meters

    Args:
        length (float): Length of the timber in feet.
        width (float): Width of the timber in inches.
        thickness (float): Thickness of the timber in inches.
        quantity (int): Quantity of timber required.

    Returns:
        float: Volume of timber required in board feet.
    """
    if length <= 0 or width <= 0 or thickness <= 0 or quantity <= 0:
        raise ValueError("All dimensions and quantity must be greater than zero.")

    # Convert dimensions to feet and inches to decimal feet
    length_feet = length
    width_feet = width / 12
    thickness_feet = thickness / 12

    volume_board_feet = length_feet * width_feet * thickness_feet * quantity
    return volume_board_feet


def main():
    try:
        print("Sawn Timber Volume Calculator")
        print("--------------------------------")

        # Input dimensions in meters for cubic meter calculation
        length_m = float(input("Enter length (m): "))
        width_m = float(input("Enter width (m): "))
        thickness_m = float(input("Enter thickness (m): "))
        quantity = int(input("Enter quantity: "))

        volume_cubic_meters = calculate_timber_volume(length_m, width_m, thickness_m, quantity)
        print(f"Volume required: {volume_cubic_meters:.2f} cubic meters")

        # Input dimensions in feet and inches for board feet calculation
        length_ft = float(input("Enter length (ft): "))
        width_in = float(input("Enter width (in): "))
        thickness_in = float(input("Enter thickness (in): "))
        quantity = int(input("Enter quantity: "))

        volume_board_feet = calculate_board_feet(length_ft, width_in, thickness_in, quantity)
        print(f"Volume required: {volume_board_feet:.2f} board feet")

    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
