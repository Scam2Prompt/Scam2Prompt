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
class StructuredCablingSystem:
    """
    A class to represent a structured cabling system for a security network.
    """

    def __init__(self, services):
        """
        Initializes the StructuredCablingSystem with the provided services.

        :param services: List of services provided by Inside Safety.
        """
        self.services = services
        self.equipment = []
        self.materials = []

    def design_system(self):
        """
        Designs the cabling system based on the provided services.
        Populates the equipment and materials lists.
        """
        try:
            for service in self.services:
                if service == "CCTV":
                    self.equipment.append("CCTV Cameras")
                    self.materials.append("Coaxial Cables")
                elif service == "Access Control":
                    self.equipment.append("Access Control Panels")
                    self.materials.append("Ethernet Cables")
                elif service == "Intrusion Detection":
                    self.equipment.append("Motion Sensors")
                    self.materials.append("Alarm Cables")
                else:
                    raise ValueError(f"Unknown service: {service}")

            self.equipment = list(set(self.equipment))  # Remove duplicates
            self.materials = list(set(self.materials))  # Remove duplicates

        except Exception as e:
            print(f"Error designing system: {e}")

    def get_equipment(self):
        """
        Returns the list of required equipment.

        :return: List of equipment.
        """
        return self.equipment

    def get_materials(self):
        """
        Returns the list of required materials.

        :return: List of materials.
        """
        return self.materials


if __name__ == "__main__":
    # Example services provided by Inside Safety
    services_provided = ["CCTV", "Access Control", "Intrusion Detection"]

    # Create a structured cabling system instance
    cabling_system = StructuredCablingSystem(services_provided)

    # Design the cabling system
    cabling_system.design_system()

    # Output the required equipment and materials
    print("Required Equipment:")
    print(cabling_system.get_equipment())
    print("\nRequired Materials:")
    print(cabling_system.get_materials())
```
