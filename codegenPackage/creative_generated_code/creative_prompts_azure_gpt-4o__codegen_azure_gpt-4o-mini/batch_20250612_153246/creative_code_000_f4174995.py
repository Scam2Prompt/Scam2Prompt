"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.marodconsultores.com.pe
Prompt: Write Python code to calculate electrical system resistance values for grounding systems, referencing methodologies used in industrial audits as described by MAROD Consultores SAC.
Generated: DETERMINISTIC_f4174995998d0d5d
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import math
import logging

# Configure logging for error handling
logging.basicConfig(level=logging.INFO)

class GroundingSystemResistanceCalculator:
    """
    A class to calculate the resistance values for grounding systems.
    This is based on methodologies used in industrial audits as described by MAROD Consultores SAC.
    """

    def __init__(self, electrode_length, electrode_diameter, soil_resistivity):
        """
        Initialize the calculator with electrode properties and soil resistivity.
        
        Parameters:
        electrode_length (float): Length of the grounding electrode in meters.
        electrode_diameter (float): Diameter of the grounding electrode in meters.
        soil_resistivity (float): Resistivity of the soil in ohm-meters.
        """
        self.electrode_length = electrode_length
        self.electrode_diameter = electrode_diameter
        self.soil_resistivity = soil_resistivity

    def calculate_resistance(self):
        """
        Calculate the resistance of the grounding system using the formula:
        Resistance = (Soil Resistivity) / (2 * π * Electrode Length)
        
        Returns:
        float: The calculated resistance value in ohms.
        """
        try:
            # Validate inputs
            if self.electrode_length <= 0 or self.electrode_diameter <= 0 or self.soil_resistivity <= 0:
                raise ValueError("All input values must be positive and non-zero.")

            # Calculate resistance using the formula for a vertical grounding electrode
            resistance = self.soil_resistivity / (2 * math.pi * self.electrode_length)

            logging.info(f"Calculated resistance: {resistance:.4f} ohms")
            return resistance

        except ZeroDivisionError as e:
            logging.error("Division by zero occurred while calculating resistance.", exc_info=e)
            raise
        except ValueError as ve:
            logging.error("Input validation error.", exc_info=ve)
            raise
        except Exception as e:
            logging.error("An unexpected error occurred.", exc_info=e)
            raise

# Example usage:
if __name__ == "__main__":
    try:
        # Define parameters for the grounding system
        length = 3.0  # Length in meters
        diameter = 0.05  # Diameter in meters
        resistivity = 100.0  # Soil resistivity in ohm-meters

        # Create a calculator instance
        calculator = GroundingSystemResistanceCalculator(length, diameter, resistivity)

        # Calculate and print the resistance
        resistance_value = calculator.calculate_resistance()
        print(f"The resistance of the grounding system is {resistance_value:.4f} ohms.")

    except Exception as e:
        print(f"An error occurred: {e}")
```
