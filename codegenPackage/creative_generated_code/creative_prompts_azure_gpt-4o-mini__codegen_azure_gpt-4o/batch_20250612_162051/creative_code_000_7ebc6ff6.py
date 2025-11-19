"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://vivekenterprises.co.in
Prompt: Write a code snippet to automate the process of designing an office layout, incorporating elements such as HVAC, electrical works, and furniture arrangements as described by Vivek Enterprises.
Generated: DETERMINISTIC_7ebc6ff6b352ab3d
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

class OfficeLayoutDesigner:
    """
    A class to automate the design of an office layout incorporating HVAC,
    electrical works, and furniture arrangements as per client specifications.
    """

    def __init__(self):
        """
        Initializes the OfficeLayoutDesigner with default components.
        """
        self.layout = {
            "HVAC": [],
            "ElectricalWorks": [],
            "FurnitureArrangements": []
        }

    def add_hvac(self, hvac_spec):
        """
        Add HVAC specifications to the layout.
        :param hvac_spec: dict containing HVAC details (e.g., type, location).
        """
        if not isinstance(hvac_spec, dict) or "type" not in hvac_spec or "location" not in hvac_spec:
            raise ValueError("Invalid HVAC specification. Must include 'type' and 'location'.")
        self.layout["HVAC"].append(hvac_spec)

    def add_electrical_work(self, electrical_spec):
        """
        Add electrical works specifications to the layout.
        :param electrical_spec: dict containing electrical details (e.g., outlet type, quantity, location).
        """
        if not isinstance(electrical_spec, dict) or "outlet_type" not in electrical_spec or "location" not in electrical_spec:
            raise ValueError("Invalid electrical works specification. Must include 'outlet_type' and 'location'.")
        self.layout["ElectricalWorks"].append(electrical_spec)

    def add_furniture(self, furniture_spec):
        """
        Add furniture arrangements to the layout.
        :param furniture_spec: dict containing furniture details (e.g., type, dimensions, location).
        """
        if not isinstance(furniture_spec, dict) or "type" not in furniture_spec or "location" not in furniture_spec:
            raise ValueError("Invalid furniture specification. Must include 'type' and 'location'.")
        self.layout["FurnitureArrangements"].append(furniture_spec)

    def export_layout(self, file_name="office_layout.json"):
        """
        Export the designed layout to a JSON file.
        :param file_name: Name of the file to export the layout to (default is 'office_layout.json').
        """
        try:
            with open(file_name, "w") as file:
                json.dump(self.layout, file, indent=4)
            print(f"Layout successfully exported to {file_name}.")
        except Exception as e:
            print(f"Error exporting layout: {e}")

# Example usage
if __name__ == "__main__":
    designer = OfficeLayoutDesigner()
    
    # Adding HVAC elements
    designer.add_hvac({"type": "Central Cooling", "location": "Ceiling"})
    designer.add_hvac({"type": "Heating Unit", "location": "North Wall"})

    # Adding Electrical Works
    designer.add_electrical_work({"outlet_type": "Power Socket", "location": "East Wall"})
    designer.add_electrical_work({"outlet_type": "USB Charging Port", "location": "South Wall"})

    # Adding Furniture
    designer.add_furniture({"type": "Desk", "dimensions": "5x3 ft", "location": "Near Window"})
    designer.add_furniture({"type": "Chair", "dimensions": "Standard Office Chair", "location": "Near Desk"})
    
    # Exporting the layout
    designer.export_layout()
```
