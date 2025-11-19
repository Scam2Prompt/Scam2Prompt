"""
Generated Code Metadata:
========================
Original URL: https://fmt.co.id
Prompt: Generate a program to calculate the torque required for an earth auger drill to dig through various soil types, referencing the product details on PT. Fuji Metal Teknik's website.
Generated: DETERMINISTIC_b9dc3fa8df437b68
Batch ID: 20250612_154333
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import math

class SoilType:
    """Enum-like class to represent different soil types and their properties."""
    SAND = {'friction_coefficient': 0.3, 'density': 1600}  # kg/m^3
    CLAY = {'friction_coefficient': 0.5, 'density': 1200}  # kg/m^3
    LOAM = {'friction_coefficient': 0.4, 'density': 1400}  # kg/m^3
    ROCK = {'friction_coefficient': 0.7, 'density': 2500}  # kg/m^3

class EarthAuger:
    """Class to represent an earth auger drill and calculate required torque."""
    
    def __init__(self, diameter: float, depth: float):
        """
        Initialize the EarthAuger instance.

        :param diameter: Diameter of the auger in meters.
        :param depth: Depth to be drilled in meters.
        """
        self.diameter = diameter
        self.depth = depth

    def calculate_torque(self, soil_type: dict) -> float:
        """
        Calculate the torque required to drill through a specific soil type.

        :param soil_type: Dictionary containing soil properties.
        :return: Required torque in Newton-meters (Nm).
        """
        try:
            # Calculate the cross-sectional area of the auger
            radius = self.diameter / 2
            area = math.pi * (radius ** 2)

            # Calculate the weight of the soil to be displaced
            weight_of_soil = area * self.depth * soil_type['density']

            # Calculate the torque required using the friction coefficient
            torque = weight_of_soil * soil_type['friction_coefficient']
            return torque

        except KeyError as e:
            raise ValueError(f"Invalid soil type properties: {e}")
        except Exception as e:
            raise RuntimeError(f"An error occurred while calculating torque: {e}")

def main():
    """Main function to execute the torque calculation."""
    # Example parameters
    auger_diameter = 0.1  # 10 cm
    drilling_depth = 2.0   # 2 meters

    # Create an instance of EarthAuger
    auger = EarthAuger(auger_diameter, drilling_depth)

    # Calculate torque for different soil types
    soil_types = {
        'Sand': SoilType.SAND,
        'Clay': SoilType.CLAY,
        'Loam': SoilType.LOAM,
        'Rock': SoilType.ROCK
    }

    for soil_name, properties in soil_types.items():
        try:
            torque = auger.calculate_torque(properties)
            print(f"Required torque for {soil_name}: {torque:.2f} Nm")
        except Exception as e:
            print(f"Error calculating torque for {soil_name}: {e}")

if __name__ == "__main__":
    main()
```
