"""
Generated Code Metadata:
========================
Original URL: https://citygardenmexico.com.mx
Prompt: Generate code to simulate an irrigation system design for a rooftop garden, incorporating features mentioned in City Garden México's services.
Generated: DETERMINISTIC_8cf2f8a24d33bd82
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# irrigation_system.py

class IrrigationZone:
    """Represents an irrigation zone in the rooftop garden."""

    def __init__(self, name, area, plant_type, water_requirement):
        """
        Initializes an IrrigationZone.

        Args:
            name (str): Zone name.
            area (float): Zone area in square meters.
            plant_type (str): Type of plants in the zone.
            water_requirement (float): Water requirement in liters per day.
        """
        self.name = name
        self.area = area
        self.plant_type = plant_type
        self.water_requirement = water_requirement

    def __str__(self):
        return f"Zone: {self.name}, Area: {self.area}m², Plant Type: {self.plant_type}, Water Requirement: {self.water_requirement}L/day"


class IrrigationSystem:
    """Simulates an irrigation system design for a rooftop garden."""

    def __init__(self):
        self.zones = []
        self.water_source = None
        self.pump = None

    def add_zone(self, zone):
        """
        Adds an irrigation zone to the system.

        Args:
            zone (IrrigationZone): Zone to add.
        """
        self.zones.append(zone)

    def set_water_source(self, water_source):
        """
        Sets the water source for the system.

        Args:
            water_source (str): Water source (e.g., rainwater, potable water).
        """
        self.water_source = water_source

    def set_pump(self, pump):
        """
        Sets the pump for the system.

        Args:
            pump (str): Pump type and specifications.
        """
        self.pump = pump

    def calculate_total_water_requirement(self):
        """
        Calculates the total water requirement for all zones.

        Returns:
            float: Total water requirement in liters per day.
        """
        return sum(zone.water_requirement for zone in self.zones)

    def design_irrigation_system(self):
        """
        Designs the irrigation system based on the added zones and settings.

        Returns:
            dict: Irrigation system design details.
        """
        design_details = {
            "water_source": self.water_source,
            "pump": self.pump,
            "zones": [str(zone) for zone in self.zones],
            "total_water_requirement": self.calculate_total_water_requirement(),
        }
        return design_details


def main():
    try:
        # Create irrigation zones
        zone1 = IrrigationZone("Zone 1", 100, "Herbs", 50)
        zone2 = IrrigationZone("Zone 2", 200, "Vegetables", 100)

        # Create irrigation system
        irrigation_system = IrrigationSystem()
        irrigation_system.add_zone(zone1)
        irrigation_system.add_zone(zone2)
        irrigation_system.set_water_source("Rainwater")
        irrigation_system.set_pump("Centrifugal Pump, 1 HP")

        # Design irrigation system
        design_details = irrigation_system.design_irrigation_system()

        # Print design details
        print("Irrigation System Design:")
        print("---------------------------")
        print(f"Water Source: {design_details['water_source']}")
        print(f"Pump: {design_details['pump']}")
        print("Zones:")
        for zone in design_details["zones"]:
            print(zone)
        print(f"Total Water Requirement: {design_details['total_water_requirement']}L/day")

    except Exception as e:
        print(f"An error occurred: {str(e)}")


if __name__ == "__main__":
    main()
```
