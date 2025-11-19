"""
Generated Code Metadata:
========================
Original URL: https://landoparafusos.blogspot.com
Prompt: "Generate code for calculating the required torque for Porca Sextavada Flangeada in solar panel installations."
Generated: DETERMINISTIC_004e6dcc8b69314a
Batch ID: 20250622_212142
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import math

def calculate_torque(bolt_diameter, material_yield_strength, safety_factor=2.0):
    """
    Calculates the required torque for a Porca Sextavada Flangeada in solar panel installations.

    Args:
        bolt_diameter (float): The diameter of the bolt in mm.
        material_yield_strength (float): The yield strength of the material in MPa.
        safety_factor (float, optional): The safety factor. Defaults to 2.0.

    Returns:
        float: The required torque in Nm.
    """
    # Assuming a friction coefficient of 0.2 for a lubricated bolt
    friction_coefficient = 0.2

    # Calculate the bolt stress
    bolt_stress = material_yield_strength / safety_factor

    # Calculate the bolt tension
    bolt_tension = bolt_stress * math.pi * (bolt_diameter ** 2) / 4

    # Calculate the torque
    torque = (bolt_tension * bolt_diameter * friction_coefficient) / 1000

    return torque


def main():
    try:
        bolt_diameter = float(input("Enter the bolt diameter (mm): "))
        material_yield_strength = float(input("Enter the material yield strength (MPa): "))

        torque = calculate_torque(bolt_diameter, material_yield_strength)
        print(f"The required torque is: {torque:.2f} Nm")

    except ValueError:
        print("Invalid input. Please enter a valid number.")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
