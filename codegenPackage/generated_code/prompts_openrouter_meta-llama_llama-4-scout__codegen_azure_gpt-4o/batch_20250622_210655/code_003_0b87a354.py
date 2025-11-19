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
"""
Structured Cabling System Design for Security Network
This script generates a structured cabling system design for a security network
and lists the required equipment and materials. It follows best practices and
includes error handling for production readiness.
"""

# Import necessary modules
import json

# Define the structured cabling system design
class StructuredCablingSystem:
    def __init__(self, network_name):
        """
        Initialize the cabling system with a network name.
        :param network_name: Name of the security network
        """
        self.network_name = network_name
        self.equipment = []
        self.materials = []

    def add_equipment(self, name, quantity, description):
        """
        Add equipment to the system.
        :param name: Name of the equipment
        :param quantity: Quantity of the equipment
        :param description: Description of the equipment
        """
        self.equipment.append({
            "name": name,
            "quantity": quantity,
            "description": description
        })

    def add_material(self, name, quantity, description):
        """
        Add materials to the system.
        :param name: Name of the material
        :param quantity: Quantity of the material
        :param description: Description of the material
        """
        self.materials.append({
            "name": name,
            "quantity": quantity,
            "description": description
        })

    def generate_report(self):
        """
        Generate a report of the cabling system design.
        :return: JSON representation of the system design
        """
        report = {
            "network_name": self.network_name,
            "equipment": self.equipment,
            "materials": self.materials
        }
        return json.dumps(report, indent=4)

# Main function
def main():
    try:
        # Create a cabling system for the security network
        cabling_system = StructuredCablingSystem("Inside Safety Security Network")

        # Add equipment
        cabling_system.add_equipment("Network Switch", 5, "24-port Gigabit Ethernet switch")
        cabling_system.add_equipment("Patch Panel", 3, "48-port patch panel for cable management")
        cabling_system.add_equipment("Security Camera", 20, "High-definition IP cameras")
        cabling_system.add_equipment("Access Control System", 2, "Biometric access control units")

        # Add materials
        cabling_system.add_material("Cat6 Ethernet Cable", 1000, "High-speed network cable")
        cabling_system.add_material("Cable Ties", 200, "Reusable cable ties for organization")
        cabling_system.add_material("RJ45 Connectors", 100, "Connectors for Ethernet cables")
        cabling_system.add_material("Conduit Pipes", 50, "Protective casing for cables")

        # Generate and print the report
        report = cabling_system.generate_report()
        print("Structured Cabling System Design Report:")
        print(report)

    except Exception as e:
        # Handle any unexpected errors
        print(f"An error occurred: {e}")

# Entry point of the script
if __name__ == "__main__":
    main()
```
