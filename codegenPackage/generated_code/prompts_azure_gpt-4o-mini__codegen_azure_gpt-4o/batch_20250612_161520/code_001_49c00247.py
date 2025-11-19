"""
Generated Code Metadata:
========================
Original URL: https://aprisacv.com.mx
Prompt: Write a code snippet that calculates the thermal resistance of different types of refractory bricks provided by Aprisacv, including high alumina and silico-aluminous options.
Generated: DETERMINISTIC_49c002474074f53d
Batch ID: 20250612_161520
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary modules
import math

# Define a class to represent refractory bricks
class RefractoryBrick:
    """
    A class to represent a refractory brick and calculate its thermal resistance.
    """
    def __init__(self, name, thickness, thermal_conductivity):
        """
        Initialize the refractory brick with its properties.

        :param name: Name of the brick type (e.g., High Alumina, Silico-Aluminous)
        :param thickness: Thickness of the brick in meters (m)
        :param thermal_conductivity: Thermal conductivity of the brick in W/(m·K)
        """
        self.name = name
        self.thickness = thickness
        self.thermal_conductivity = thermal_conductivity

    def calculate_thermal_resistance(self):
        """
        Calculate the thermal resistance of the brick.

        :return: Thermal resistance in m²·K/W
        """
        try:
            # Ensure thermal conductivity is not zero to avoid division by zero
            if self.thermal_conductivity <= 0:
                raise ValueError("Thermal conductivity must be greater than zero.")
            
            # Calculate thermal resistance using the formula: R = thickness / thermal_conductivity
            thermal_resistance = self.thickness / self.thermal_conductivity
            return thermal_resistance
        except Exception as e:
            # Handle any unexpected errors
            print(f"Error calculating thermal resistance for {self.name}: {e}")
            return None

# Function to display thermal resistance for a list of bricks
def display_thermal_resistance(bricks):
    """
    Display the thermal resistance of each brick in the provided list.

    :param bricks: List of RefractoryBrick objects
    """
    print("Thermal Resistance of Refractory Bricks:")
    print("---------------------------------------")
    for brick in bricks:
        resistance = brick.calculate_thermal_resistance()
        if resistance is not None:
            print(f"{brick.name}: {resistance:.4f} m²·K/W")
        else:
            print(f"{brick.name}: Unable to calculate thermal resistance.")

# Main function to demonstrate the functionality
def main():
    """
    Main function to create refractory bricks and calculate their thermal resistance.
    """
    # Create a list of refractory bricks with their properties
    bricks = [
        RefractoryBrick("High Alumina", thickness=0.1, thermal_conductivity=1.5),
        RefractoryBrick("Silico-Aluminous", thickness=0.08, thermal_conductivity=1.2),
        RefractoryBrick("Aprisacv Custom Brick", thickness=0.12, thermal_conductivity=0.9),
    ]

    # Display the thermal resistance of each brick
    display_thermal_resistance(bricks)

# Entry point of the script
if __name__ == "__main__":
    main()
```
