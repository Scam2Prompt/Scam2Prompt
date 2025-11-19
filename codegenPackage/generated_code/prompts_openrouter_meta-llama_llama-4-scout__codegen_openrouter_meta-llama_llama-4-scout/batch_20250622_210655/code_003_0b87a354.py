"""
Generated Code Metadata:
========================
Original URL: https://insidesafety.com.mx
Prompt: "Design a structured cabling system for a security network, as per the services provided by Inside Safety, and list the required equipment and materials."
Generated: DETERMINISTIC_0b87a354bdf2bb30
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Structured Cabling System Design for Security Network

class CablingSystem:
    def __init__(self, num_cameras, num_access_points, num_sensors):
        """
        Initialize the cabling system design.

        Args:
            num_cameras (int): Number of security cameras.
            num_access_points (int): Number of access points.
            num_sensors (int): Number of sensors.
        """
        self.num_cameras = num_cameras
        self.num_access_points = num_access_points
        self.num_sensors = num_sensors

    def calculate_required_equipment(self):
        """
        Calculate the required equipment and materials.

        Returns:
            dict: Dictionary containing the required equipment and materials.
        """
        required_equipment = {
            "cables": self.calculate_cable_requirements(),
            "connectors": self.calculate_connector_requirements(),
            "switches": self.calculate_switch_requirements(),
            "patch_panels": self.calculate_patch_panel_requirements(),
            "racks": self.calculate_rack_requirements()
        }
        return required_equipment

    def calculate_cable_requirements(self):
        """
        Calculate the required cables.

        Returns:
            dict: Dictionary containing the required cables.
        """
        cable_requirements = {
            "cat5e": self.num_cameras * 2 + self.num_access_points * 2 + self.num_sensors,
            "cat6": self.num_cameras * 2 + self.num_access_points * 2
        }
        return cable_requirements

    def calculate_connector_requirements(self):
        """
        Calculate the required connectors.

        Returns:
            int: Number of required connectors.
        """
        return (self.num_cameras + self.num_access_points + self.num_sensors) * 2

    def calculate_switch_requirements(self):
        """
        Calculate the required switches.

        Returns:
            int: Number of required switches.
        """
        return (self.num_cameras + self.num_access_points + self.num_sensors) // 48 + 1

    def calculate_patch_panel_requirements(self):
        """
        Calculate the required patch panels.

        Returns:
            int: Number of required patch panels.
        """
        return (self.num_cameras + self.num_access_points + self.num_sensors) // 48 + 1

    def calculate_rack_requirements(self):
        """
        Calculate the required racks.

        Returns:
            int: Number of required racks.
        """
        return 1

def main():
    try:
        num_cameras = int(input("Enter the number of security cameras: "))
        num_access_points = int(input("Enter the number of access points: "))
        num_sensors = int(input("Enter the number of sensors: "))

        cabling_system = CablingSystem(num_cameras, num_access_points, num_sensors)
        required_equipment = cabling_system.calculate_required_equipment()

        print("Required Equipment and Materials:")
        for equipment, quantity in required_equipment.items():
            if equipment == "cables":
                print(f"Cables:")
                for cable_type, length in quantity.items():
                    print(f"  {cable_type}: {length} meters")
            elif equipment == "connectors":
                print(f"Connectors: {quantity}")
            elif equipment == "switches":
                print(f"Switches: {quantity}")
            elif equipment == "patch_panels":
                print(f"Patch Panels: {quantity}")
            elif equipment == "racks":
                print(f"Racks: {quantity}")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
