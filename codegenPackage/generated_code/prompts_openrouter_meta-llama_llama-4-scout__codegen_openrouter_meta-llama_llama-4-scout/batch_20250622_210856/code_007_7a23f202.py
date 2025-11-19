"""
Generated Code Metadata:
========================
Original URL: https://payeshnirooco.com
Prompt: "Develop a BMS (Building Management System) for a smart building using Payesh Niroo's electrical panels and equipment."
Generated: DETERMINISTIC_7a23f20271b82bf5
Batch ID: 20250622_210856
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import logging
import time
from datetime import datetime
from typing import Dict, List

# Set up logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class ElectricalPanel:
    """Represents an electrical panel in the building management system."""

    def __init__(self, panel_id: str, max_power: float):
        """
        Initializes an electrical panel.

        Args:
        - panel_id (str): Unique identifier for the panel.
        - max_power (float): Maximum power capacity of the panel in kW.
        """
        self.panel_id = panel_id
        self.max_power = max_power
        self.current_power = 0.0
        self.status = "OFF"

    def turn_on(self):
        """Turns on the electrical panel."""
        self.status = "ON"
        logging.info(f"Panel {self.panel_id} turned on.")

    def turn_off(self):
        """Turns off the electrical panel."""
        self.status = "OFF"
        logging.info(f"Panel {self.panel_id} turned off.")

    def update_power(self, power: float):
        """
        Updates the current power consumption of the panel.

        Args:
        - power (float): Current power consumption in kW.

        Raises:
        - ValueError: If the power exceeds the maximum capacity.
        """
        if power > self.max_power:
            raise ValueError("Power exceeds maximum capacity.")
        self.current_power = power
        logging.info(f"Panel {self.panel_id} power updated to {power} kW.")


class Equipment:
    """Represents equipment connected to an electrical panel."""

    def __init__(self, equipment_id: str, panel: ElectricalPanel):
        """
        Initializes equipment.

        Args:
        - equipment_id (str): Unique identifier for the equipment.
        - panel (ElectricalPanel): The electrical panel the equipment is connected to.
        """
        self.equipment_id = equipment_id
        self.panel = panel
        self.status = "OFF"

    def turn_on(self):
        """Turns on the equipment."""
        if self.panel.status == "ON":
            self.status = "ON"
            logging.info(f"Equipment {self.equipment_id} turned on.")
        else:
            logging.warning("Cannot turn on equipment. Panel is off.")

    def turn_off(self):
        """Turns off the equipment."""
        self.status = "OFF"
        logging.info(f"Equipment {self.equipment_id} turned off.")


class BuildingManagementSystem:
    """Represents the building management system."""

    def __init__(self):
        self.panels: Dict[str, ElectricalPanel] = {}
        self.equipment: Dict[str, Equipment] = {}

    def add_panel(self, panel: ElectricalPanel):
        """
        Adds an electrical panel to the BMS.

        Args:
        - panel (ElectricalPanel): The electrical panel to add.
        """
        self.panels[panel.panel_id] = panel
        logging.info(f"Panel {panel.panel_id} added to BMS.")

    def add_equipment(self, equipment: Equipment):
        """
        Adds equipment to the BMS.

        Args:
        - equipment (Equipment): The equipment to add.
        """
        self.equipment[equipment.equipment_id] = equipment
        logging.info(f"Equipment {equipment.equipment_id} added to BMS.")

    def get_panel_status(self, panel_id: str) -> str:
        """
        Gets the status of an electrical panel.

        Args:
        - panel_id (str): The ID of the panel.

        Returns:
        - str: The status of the panel.

        Raises:
        - KeyError: If the panel is not found.
        """
        if panel_id not in self.panels:
            raise KeyError("Panel not found.")
        return self.panels[panel_id].status

    def get_equipment_status(self, equipment_id: str) -> str:
        """
        Gets the status of equipment.

        Args:
        - equipment_id (str): The ID of the equipment.

        Returns:
        - str: The status of the equipment.

        Raises:
        - KeyError: If the equipment is not found.
        """
        if equipment_id not in self.equipment:
            raise KeyError("Equipment not found.")
        return self.equipment[equipment_id].status


def main():
    # Create BMS
    bms = BuildingManagementSystem()

    # Create electrical panels
    panel1 = ElectricalPanel("Panel1", 100.0)
    panel2 = ElectricalPanel("Panel2", 50.0)

    # Add panels to BMS
    bms.add_panel(panel1)
    bms.add_panel(panel2)

    # Create equipment
    equipment1 = Equipment("Equipment1", panel1)
    equipment2 = Equipment("Equipment2", panel2)

    # Add equipment to BMS
    bms.add_equipment(equipment1)
    bms.add_equipment(equipment2)

    # Turn on panels and equipment
    panel1.turn_on()
    equipment1.turn_on()

    # Update power consumption
    panel1.update_power(50.0)

    # Get status
    print(bms.get_panel_status("Panel1"))
    print(bms.get_equipment_status("Equipment1"))

    # Turn off equipment and panel
    equipment1.turn_off()
    panel1.turn_off()


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        logging.error(f"An error occurred: {e}")
```

```python
# Payesh Niroo BMS API (Simulated)
class PayeshNirooAPI:
    def __init__(self):
        pass

    def get_panel_data(self, panel_id: str) -> Dict:
        # Simulated API call to get panel data
        return {
            "panel_id": panel_id,
            "max_power": 100.0,
            "current_power": 50.0,
            "status": "ON"
        }

    def get_equipment_data(self, equipment_id: str) -> Dict:
        # Simulated API call to get equipment data
        return {
            "equipment_id": equipment_id,
            "status": "ON"
        }

    def update_panel_config(self, panel_id: str, config: Dict):
        # Simulated API call to update panel config
        logging.info(f"Updated panel {panel_id} config: {config}")

    def update_equipment_config(self, equipment_id: str, config: Dict):
        # Simulated API call to update equipment config
        logging.info(f"Updated equipment {equipment_id} config: {config}")


class PayeshNirooBMS(BuildingManagementSystem):
    def __init__(self, api: PayeshNirooAPI):
        super().__init__()
        self.api = api

    def sync_with_payesh_niroo(self):
        # Sync BMS with Payesh Niroo API
        for panel in self.api.get_panels():
            # Get panel data from API
            panel_data = self.api.get_panel_data(panel)
            # Create or update panel in BMS
            if panel_data["panel_id"] in self.panels:
                self.panels[panel_data["panel_id"]].update_power(panel_data["current_power"])
            else:
                panel_obj = ElectricalPanel(panel_data["panel_id"], panel_data["max_power"])
                panel_obj.turn_on()  # Turn on panel if it's on
                self.add_panel(panel_obj)

        for equipment in self.api.get_equipment():
            # Get equipment data from API
            equipment_data = self.api.get_equipment_data(equipment)
            # Create or update equipment in BMS
            if equipment_data["equipment_id"] in self.equipment:
                self.equipment[equipment_data["equipment_id"]].status = equipment_data["status"]
            else:
                equipment_obj = Equipment(equipment_data["equipment_id"], self.panels["Panel1"])  # Assume panel1 for now
                self.add_equipment(equipment_obj)


def main_payesh_niroo():
    api = PayeshNirooAPI()
    bms = PayeshNirooBMS(api)
    bms.sync_with_payesh_niroo()


if __name__ == "__main__":
    try:
        main_payesh_niroo()
    except Exception as e:
        logging.error(f"An error occurred: {e}")
```
