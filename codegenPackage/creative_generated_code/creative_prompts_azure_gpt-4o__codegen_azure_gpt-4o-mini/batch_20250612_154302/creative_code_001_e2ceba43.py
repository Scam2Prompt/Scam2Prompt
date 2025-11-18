"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dbxtools.in
Prompt: Generate a script to calculate torque settings for tube expansion using a digital torque controller, such as the DTW-15 model mentioned on the DBX Tools website.
Generated: DETERMINISTIC_e2ceba432b5579f4
Batch ID: 20250612_154302
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import math

class TorqueCalculator:
    """
    A class to calculate torque settings for tube expansion using a digital torque controller.
    """

    def __init__(self, diameter: float, thickness: float, material_strength: float):
        """
        Initialize the TorqueCalculator with the tube's diameter, thickness, and material strength.

        Parameters:
        diameter (float): The outer diameter of the tube in mm.
        thickness (float): The wall thickness of the tube in mm.
        material_strength (float): The yield strength of the tube material in N/mm^2.
        """
        self.diameter = diameter
        self.thickness = thickness
        self.material_strength = material_strength

    def calculate_torque(self) -> float:
        """
        Calculate the torque required for tube expansion.

        Returns:
        float: The calculated torque in Nm.
        """
        # Calculate the radius of the tube
        radius = self.diameter / 2
        
        # Calculate the torque using the formula: Torque = (π / 2) * (Diameter * Thickness * Material Strength)
        torque = (math.pi / 2) * (self.diameter * self.thickness * self.material_strength)
        
        return torque

    def display_torque(self) -> None:
        """
        Display the calculated torque in a formatted manner.
        """
        try:
            torque = self.calculate_torque()
            print(f"Calculated Torque for tube expansion:")
            print(f"Diameter: {self.diameter} mm")
            print(f"Thickness: {self.thickness} mm")
            print(f"Material Strength: {self.material_strength} N/mm^2")
            print(f"Required Torque: {torque:.2f} Nm")
        except Exception as e:
            print(f"Error calculating torque: {e}")

def main():
    """
    Main function to execute the torque calculation.
    """
    try:
        # Input parameters for the tube
        diameter = float(input("Enter the outer diameter of the tube (mm): "))
        thickness = float(input("Enter the wall thickness of the tube (mm): "))
        material_strength = float(input("Enter the yield strength of the material (N/mm^2): "))

        # Validate inputs
        if diameter <= 0 or thickness <= 0 or material_strength <= 0:
            raise ValueError("Diameter, thickness, and material strength must be positive values.")

        # Create a TorqueCalculator instance
        torque_calculator = TorqueCalculator(diameter, thickness, material_strength)

        # Display the calculated torque
        torque_calculator.display_torque()

    except ValueError as ve:
        print(f"Input Error: {ve}")
    except Exception as e:
        print(f"Unexpected Error: {e}")

if __name__ == "__main__":
    main()
```
