"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nordson.vn
Prompt: Provide a sample configuration for the FoamMelt glue dispensing machine, including parameters for optimal performance.
Generated: DETERMINISTIC_0ade840f5d638bf4
Batch ID: 20250612_164316
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

class FoamMeltConfig:
    """
    Class to represent the configuration for the FoamMelt glue dispensing machine.
    """

    def __init__(self, temperature, pressure, dispense_speed, nozzle_diameter):
        """
        Initialize the FoamMelt configuration with required parameters.

        :param temperature: Optimal temperature for glue dispensing in Celsius.
        :param pressure: Operating pressure in PSI.
        :param dispense_speed: Speed of dispensing in mm/s.
        :param nozzle_diameter: Diameter of the nozzle in mm.
        """
        self.temperature = temperature
        self.pressure = pressure
        self.dispense_speed = dispense_speed
        self.nozzle_diameter = nozzle_diameter

    def validate_parameters(self):
        """
        Validate the configuration parameters to ensure they are within acceptable ranges.
        
        :raises ValueError: If any parameter is out of the acceptable range.
        """
        if not (180 <= self.temperature <= 220):
            raise ValueError("Temperature must be between 180 and 220 Celsius.")
        if not (20 <= self.pressure <= 80):
            raise ValueError("Pressure must be between 20 and 80 PSI.")
        if not (5 <= self.dispense_speed <= 100):
            raise ValueError("Dispense speed must be between 5 and 100 mm/s.")
        if not (1 <= self.nozzle_diameter <= 5):
            raise ValueError("Nozzle diameter must be between 1 and 5 mm.")

    def to_json(self):
        """
        Convert the configuration to a JSON string.

        :return: JSON string representation of the configuration.
        """
        return json.dumps({
            "temperature": self.temperature,
            "pressure": self.pressure,
            "dispense_speed": self.dispense_speed,
            "nozzle_diameter": self.nozzle_diameter
        }, indent=4)


def main():
    """
    Main function to create a FoamMelt configuration and display it in JSON format.
    """
    try:
        # Sample configuration parameters for optimal performance
        config = FoamMeltConfig(
            temperature=200,      # Optimal temperature
            pressure=50,          # Optimal pressure
            dispense_speed=30,    # Optimal dispense speed
            nozzle_diameter=2     # Optimal nozzle diameter
        )

        # Validate the parameters
        config.validate_parameters()

        # Output the configuration as JSON
        print("FoamMelt Glue Dispensing Machine Configuration:")
        print(config.to_json())

    except ValueError as ve:
        print(f"Configuration error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
