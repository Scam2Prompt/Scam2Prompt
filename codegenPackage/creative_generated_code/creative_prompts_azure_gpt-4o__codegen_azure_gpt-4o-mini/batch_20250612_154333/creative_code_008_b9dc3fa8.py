"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fmt.co.id
Prompt: Generate a program to calculate the torque required for an earth auger drill to dig through various soil types, referencing the product details on PT. Fuji Metal Teknik's website.
Generated: DETERMINISTIC_b9dc3fa8df437b68
Batch ID: 20250612_154333
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import math

class SoilType:
    """Class representing different types of soil and their respective parameters."""
    def __init__(self, name, cohesion, angle_of_internal_friction):
        """
        Initializes a SoilType instance.

        :param name: Name of the soil type.
        :param cohesion: Cohesion of the soil in kPa.
        :param angle_of_internal_friction: Angle of internal friction in degrees.
        """
        self.name = name
        self.cohesion = cohesion  # kPa
        self.angle_of_internal_friction = angle_of_internal_friction  # degrees

class EarthAuger:
    """Class to calculate the torque required for an earth auger drill."""
    def __init__(self, auger_radius, depth, soil_type):
        """
        Initializes an EarthAuger instance.

        :param auger_radius: Radius of the auger in meters.
        :param depth: Depth to drill in meters.
        :param soil_type: An instance of SoilType.
        """
        self.auger_radius = auger_radius
        self.depth = depth
        self.soil_type = soil_type

    def calculate_torque(self):
        """
        Calculate the torque required to drill through the specified soil type.

        :return: Torque required in Nm.
        """
        try:
            # Convert angle from degrees to radians for calculations
            phi_radians = math.radians(self.soil_type.angle_of_internal_friction)
            
            # Calculate the effective stress
            effective_stress = self.soil_type.cohesion + (self.depth * 9.81)

            # Calculate torque (in Nm) using: Torque = (π/2) * radius * effective_stress
            torque = (math.pi / 2) * self.auger_radius * effective_stress * math.cos(phi_radians)
            return torque
        
        except Exception as e:
            print(f"Error calculating torque: {e}")
            return None

def main():
    """Main function to run the torque calculation."""
    # Example usage
    try:
        # Define different soil types
        clay = SoilType("Clay", 30, 25)
        sand = SoilType("Sand", 10, 30)
        
        # Initialize an earth auger for each soil type
        auger_radius = 0.1  # meters
        depth = 2  # meters

        clay_auger = EarthAuger(auger_radius, depth, clay)
        sand_auger = EarthAuger(auger_radius, depth, sand)

        # Calculate and print required torque for each soil type
        clay_torque = clay_auger.calculate_torque()
        sand_torque = sand_auger.calculate_torque()

        if clay_torque is not None:
            print(f"Torque required for drilling through {clay.name}: {clay_torque:.2f} Nm")
        if sand_torque is not None:
            print(f"Torque required for drilling through {sand.name}: {sand_torque:.2f} Nm")

    except Exception as e:
        print(f"An error occurred in the main function: {e}")

if __name__ == "__main__":
    main()
```
