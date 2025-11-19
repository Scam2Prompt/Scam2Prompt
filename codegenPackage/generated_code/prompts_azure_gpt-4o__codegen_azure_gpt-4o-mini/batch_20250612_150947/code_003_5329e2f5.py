"""
Generated Code Metadata:
========================
Original URL: https://mirayaelectricsac.com
Prompt: Create a script to model the integration of conduit accessories and electrical panels in a commercial building, using specifications similar to those provided by Miraya Electric S.A.C.
Generated: DETERMINISTIC_5329e2f515264c2b
Batch ID: 20250612_150947
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import List, Dict

class ElectricalPanel:
    """Class to represent an electrical panel in a commercial building."""
    
    def __init__(self, panel_id: str, capacity: int):
        """
        Initialize an ElectricalPanel instance.

        :param panel_id: Unique identifier for the electrical panel.
        :param capacity: Maximum capacity of the panel in Amperes.
        """
        self.panel_id = panel_id
        self.capacity = capacity
        self.conduit_accessories = []

    def add_conduit_accessory(self, accessory: 'ConduitAccessory'):
        """
        Add a conduit accessory to the electrical panel.

        :param accessory: An instance of ConduitAccessory to be added.
        """
        if accessory not in self.conduit_accessories:
            self.conduit_accessories.append(accessory)
        else:
            raise ValueError(f"Accessory {accessory.accessory_id} already exists in the panel.")

    def total_capacity(self) -> int:
        """
        Calculate the total capacity used by the conduit accessories.

        :return: Total capacity used by all accessories.
        """
        return sum(accessory.power_rating for accessory in self.conduit_accessories)

    def __str__(self):
        return f"ElectricalPanel(ID: {self.panel_id}, Capacity: {self.capacity}A, Accessories: {len(self.conduit_accessories)})"


class ConduitAccessory:
    """Class to represent a conduit accessory."""
    
    def __init__(self, accessory_id: str, power_rating: int):
        """
        Initialize a ConduitAccessory instance.

        :param accessory_id: Unique identifier for the conduit accessory.
        :param power_rating: Power rating of the accessory in Watts.
        """
        self.accessory_id = accessory_id
        self.power_rating = power_rating

    def __str__(self):
        return f"ConduitAccessory(ID: {self.accessory_id}, Power Rating: {self.power_rating}W)"


class BuildingElectricalSystem:
    """Class to model the electrical system of a commercial building."""
    
    def __init__(self):
        """Initialize the BuildingElectricalSystem with an empty list of panels."""
        self.panels: List[ElectricalPanel] = []

    def add_panel(self, panel: ElectricalPanel):
        """
        Add an electrical panel to the building's electrical system.

        :param panel: An instance of ElectricalPanel to be added.
        """
        if panel not in self.panels:
            self.panels.append(panel)
        else:
            raise ValueError(f"Panel {panel.panel_id} already exists in the system.")

    def total_power_consumption(self) -> int:
        """
        Calculate the total power consumption of all panels.

        :return: Total power consumption in Watts.
        """
        return sum(panel.total_capacity() for panel in self.panels)

    def __str__(self):
        return f"BuildingElectricalSystem(Panels: {len(self.panels)})"


def load_specifications(file_path: str) -> Dict:
    """
    Load electrical specifications from a JSON file.

    :param file_path: Path to the JSON file containing specifications.
    :return: Dictionary containing the specifications.
    """
    try:
        with open(file_path, 'r') as file:
            specifications = json.load(file)
        return specifications
    except FileNotFoundError:
        raise FileNotFoundError(f"Specification file not found: {file_path}")
    except json.JSONDecodeError:
        raise ValueError(f"Error decoding JSON from the file: {file_path}")


def main():
    """Main function to demonstrate the electrical system modeling."""
    # Load specifications from a JSON file
    try:
        specifications = load_specifications('specifications.json')
    except Exception as e:
        print(f"Error loading specifications: {e}")
        return

    # Create a building electrical system
    building_system = BuildingElectricalSystem()

    # Create electrical panels and conduit accessories based on specifications
    for panel_spec in specifications.get('panels', []):
        panel = ElectricalPanel(panel_id=panel_spec['id'], capacity=panel_spec['capacity'])
        building_system.add_panel(panel)

        for accessory_spec in panel_spec.get('accessories', []):
            accessory = ConduitAccessory(accessory_id=accessory_spec['id'], power_rating=accessory_spec['power_rating'])
            panel.add_conduit_accessory(accessory)

    # Output the total power consumption of the building's electrical system
    print(f"Total Power Consumption: {building_system.total_power_consumption()}W")
    print(building_system)

if __name__ == "__main__":
    main()
```
