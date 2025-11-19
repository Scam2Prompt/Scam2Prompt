"""
Generated Code Metadata:
========================
Original URL: https://www.marodconsultores.com.pe
Prompt: Write Python code to calculate electrical system resistance values for grounding systems, referencing methodologies used in industrial audits as described by MAROD Consultores SAC.
Generated: DETERMINISTIC_f4174995998d0d5d
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import math

class GroundingSystem:
    """
    A class to represent a grounding system and calculate its resistance values.
    """

    def __init__(self, electrode_length: float, electrode_diameter: float, soil_resistivity: float):
        """
        Initializes the GroundingSystem with electrode parameters and soil resistivity.

        :param electrode_length: Length of the grounding electrode in meters.
        :param electrode_diameter: Diameter of the grounding electrode in meters.
        :param soil_resistivity: Resistivity of the soil in ohm-meters.
        """
        self.electrode_length = electrode_length
        self.electrode_diameter = electrode_diameter
        self.soil_resistivity = soil_resistivity

    def calculate_resistance(self) -> float:
        """
        Calculates the resistance of the grounding system using the formula:
        R = (ρ / (2 * π * L)) * ln(4 * L / d)

        :return: The calculated resistance in ohms.
        """
        try:
            if self.electrode_length <= 0 or self.electrode_diameter <= 0 or self.soil_resistivity <= 0:
                raise ValueError("All parameters must be positive values.")

            # Calculate the resistance
            resistance = (self.soil_resistivity / (2 * math.pi * self.electrode_length)) * \
                         math.log(4 * self.electrode_length / self.electrode_diameter)

            return resistance

        except ValueError as e:
            print(f"Error in input values: {e}")
            return None
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            return None

def main():
    """
    Main function to execute the grounding system resistance calculation.
    """
    # Example parameters for the grounding system
    electrode_length = 3.0  # Length in meters
    electrode_diameter = 0.05  # Diameter in meters
    soil_resistivity = 100.0  # Resistivity in ohm-meters

    # Create a GroundingSystem instance
    grounding_system = GroundingSystem(electrode_length, electrode_diameter, soil_resistivity)

    # Calculate and display the resistance
    resistance = grounding_system.calculate_resistance()
    if resistance is not None:
        print(f"The calculated grounding system resistance is: {resistance:.2f} ohms")

if __name__ == "__main__":
    main()
```
