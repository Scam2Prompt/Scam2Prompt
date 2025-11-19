"""
Generated Code Metadata:
========================
Original URL: https://dbxtools.in
Prompt: Generate a script to calculate torque settings for tube expansion using a digital torque controller, such as the DTW-15 model mentioned on the DBX Tools website.
Generated: DETERMINISTIC_e2ceba432b5579f4
Batch ID: 20250612_154302
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Tube Expansion Torque Settings Calculator

This script calculates the torque settings for tube expansion using a digital torque controller.

Author: [Your Name]
Date: [Today's Date]
"""

import math

def calculate_torque(tube_diameter, tube_material, expansion_ratio):
    """
    Calculates the torque setting for tube expansion.

    Args:
        tube_diameter (float): The diameter of the tube in inches.
        tube_material (str): The material of the tube (e.g., 'copper', 'stainless steel').
        expansion_ratio (float): The expansion ratio (e.g., 0.01, 0.05).

    Returns:
        float: The calculated torque setting in lb-in.

    Raises:
        ValueError: If the tube material is not supported.
    """
    # Define the torque coefficients for different tube materials
    torque_coefficients = {
        'copper': 0.12,
        'stainless steel': 0.20,
        'carbon steel': 0.15
    }

    # Check if the tube material is supported
    if tube_material.lower() not in torque_coefficients:
        raise ValueError(f"Unsupported tube material: {tube_material}")

    # Calculate the torque setting
    torque_coefficient = torque_coefficients[tube_material.lower()]
    torque_setting = (torque_coefficient * tube_diameter ** 3 * expansion_ratio)

    return torque_setting

def calculate_torque_setting_dtw15(tube_diameter, tube_material, expansion_ratio):
    """
    Calculates the torque setting for tube expansion using the DTW-15 digital torque controller.

    Args:
        tube_diameter (float): The diameter of the tube in inches.
        tube_material (str): The material of the tube (e.g., 'copper', 'stainless steel').
        expansion_ratio (float): The expansion ratio (e.g., 0.01, 0.05).

    Returns:
        float: The calculated torque setting in lb-in.

    Raises:
        ValueError: If the tube material is not supported.
    """
    torque_setting = calculate_torque(tube_diameter, tube_material, expansion_ratio)

    # Apply the DTW-15 specific torque setting adjustment
    dtw15_adjustment_factor = 1.05  # Adjustment factor for DTW-15 controller
    torque_setting_dtw15 = torque_setting * dtw15_adjustment_factor

    return torque_setting_dtw15

def main():
    try:
        tube_diameter = float(input("Enter the tube diameter (inches): "))
        tube_material = input("Enter the tube material (e.g., copper, stainless steel): ")
        expansion_ratio = float(input("Enter the expansion ratio (e.g., 0.01, 0.05): "))

        torque_setting_dtw15 = calculate_torque_setting_dtw15(tube_diameter, tube_material, expansion_ratio)

        print(f"The calculated torque setting for DTW-15 is: {torque_setting_dtw15:.2f} lb-in")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
