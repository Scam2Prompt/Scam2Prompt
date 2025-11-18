"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.crediblebd.net
Prompt: Develop a script to generate a lighting plan for a parking area using the specifications of LED Flood Lights and LED High Bay Lights from Credible BD.
Generated: DETERMINISTIC_e4152cfc644eb6f5
Batch ID: 20250612_154905
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import math

# Script for generating lighting plan for a parking area using LED Flood Lights and LED High Bay Lights.

class Light:
    """
    Base class representing a light fixture.
    """
    def __init__(self, name, wattage, lumens, beam_angle, coverage_radius):
        """
        Initialize the light fixture with its specifications.

        :param name: Name of the light type.
        :param wattage: Power consumption in watts.
        :param lumens: Total light output in lumens.
        :param beam_angle: Beam angle of the light in degrees.
        :param coverage_radius: Effective coverage radius in meters.
        """
        self.name = name
        self.wattage = wattage
        self.lumens = lumens
        self.beam_angle = beam_angle
        self.coverage_radius = coverage_radius


class ParkingAreaLightingPlan:
    """
    Class to generate a lighting plan for a parking area.
    """
    def __init__(self, area_length, area_width, light_type):
        """
        Initialize the lighting plan with area dimensions and light type.

        :param area_length: Length of the parking area in meters.
        :param area_width: Width of the parking area in meters.
        :param light_type: Instance of Light representing the chosen light type.
        """
        self.area_length = area_length
        self.area_width = area_width
        self.light_type = light_type

    def calculate_lights_needed(self):
        """
        Calculate the number of lights needed to cover the parking area.

        :return: Total number of lights needed.
        """
        # Calculate area size
        area_size = self.area_length * self.area_width
        
        # Calculate coverage area per light
        coverage_area_per_light = math.pi * (self.light_type.coverage_radius ** 2)

        # Calculate total number of lights needed
        total_lights_needed = math.ceil(area_size / coverage_area_per_light)

        return total_lights_needed

    def generate_plan(self):
        """
        Generate the lighting plan.

        :return: A dictionary containing the lighting plan details.
        """
        total_lights = self.calculate_lights_needed()
        plan = {
            "Area Dimensions": f"{self.area_length}m x {self.area_width}m",
            "Light Type": self.light_type.name,
            "Lights Needed": total_lights,
            "Light Specifications": {
                "Wattage": self.light_type.wattage,
                "Lumens": self.light_type.lumens,
                "Beam Angle": self.light_type.beam_angle,
                "Coverage Radius": self.light_type.coverage_radius,
            }
        }
        return plan


def main():
    """
    Main function to create a lighting plan for the parking area.
    """
    try:
        # Input parking area dimensions
        area_length = float(input("Enter the length of the parking area (in meters): "))
        area_width = float(input("Enter the width of the parking area (in meters): "))

        # Input light type specifications
        print("\nSelect the type of light for the plan:")
        print("1. LED Flood Light")
        print("2. LED High Bay Light")
        light_choice = int(input("Enter your choice (1 or 2): "))

        if light_choice == 1:
            selected_light = Light(
                name="LED Flood Light",
                wattage=200,
                lumens=24000,
                beam_angle=120,
                coverage_radius=10
            )
        elif light_choice == 2:
            selected_light = Light(
                name="LED High Bay Light",
                wattage=150,
                lumens=19000,
                beam_angle=90,
                coverage_radius=8
            )
        else:
            print("Invalid choice! Exiting program.")
            return

        # Create lighting plan
        lighting_plan_creator = ParkingAreaLightingPlan(area_length, area_width, selected_light)
        lighting_plan = lighting_plan_creator.generate_plan()

        # Display the lighting plan
        print("\nGenerated Lighting Plan:")
        for key, value in lighting_plan.items():
            if isinstance(value, dict):
                print(f"{key}:")
                for sub_key, sub_value in value.items():
                    print(f"  {sub_key}: {sub_value}")
            else:
                print(f"{key}: {value}")

    except ValueError:
        print("Invalid input. Please enter numeric values for dimensions.")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
