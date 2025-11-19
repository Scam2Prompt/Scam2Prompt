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
"""
Building Management System (BMS) for a smart building using Payesh Niroo's electrical panels and equipment.
This script monitors and controls electrical panels and equipment, providing real-time data and control functionality.
"""

import json
import time
import logging
from typing import Dict, Any

# Configure logging for the application
logging.basicConfig(
    filename="bms.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

class PayeshNirooPanel:
    """
    Represents an electrical panel from Payesh Niroo.
    Provides methods to monitor and control the panel.
    """
    def __init__(self, panel_id: str, equipment: Dict[str, Any]):
        """
        Initialize the panel with a unique ID and associated equipment.

        :param panel_id: Unique identifier for the panel.
        :param equipment: Dictionary of equipment connected to the panel.
        """
        self.panel_id = panel_id
        self.equipment = equipment

    def get_status(self) -> Dict[str, Any]:
        """
        Retrieve the current status of the panel and its equipment.

        :return: Dictionary containing the status of the panel and equipment.
        """
        try:
            # Simulate fetching status from the panel
            status = {
                "panel_id": self.panel_id,
                "equipment_status": {key: "OK" for key in self.equipment.keys()},
                "timestamp": time.time()
            }
            logging.info(f"Status retrieved for panel {self.panel_id}: {status}")
            return status
        except Exception as e:
            logging.error(f"Error retrieving status for panel {self.panel_id}: {e}")
            return {"error": str(e)}

    def control_equipment(self, equipment_id: str, action: str) -> str:
        """
        Control a specific piece of equipment connected to the panel.

        :param equipment_id: ID of the equipment to control.
        :param action: Action to perform (e.g., "ON", "OFF").
        :return: Result of the control operation.
        """
        try:
            if equipment_id not in self.equipment:
                raise ValueError(f"Equipment {equipment_id} not found in panel {self.panel_id}.")
            
            # Simulate controlling the equipment
            self.equipment[equipment_id] = action
            logging.info(f"Equipment {equipment_id} in panel {self.panel_id} set to {action}.")
            return f"Equipment {equipment_id} set to {action}."
        except Exception as e:
            logging.error(f"Error controlling equipment {equipment_id} in panel {self.panel_id}: {e}")
            return f"Error: {str(e)}"

class BuildingManagementSystem:
    """
    Main class for the Building Management System (BMS).
    Manages multiple Payesh Niroo panels and provides system-wide functionality.
    """
    def __init__(self):
        """
        Initialize the BMS with an empty list of panels.
        """
        self.panels = {}

    def add_panel(self, panel: PayeshNirooPanel):
        """
        Add a new panel to the BMS.

        :param panel: Instance of PayeshNirooPanel to add.
        """
        self.panels[panel.panel_id] = panel
        logging.info(f"Panel {panel.panel_id} added to the BMS.")

    def get_system_status(self) -> Dict[str, Any]:
        """
        Retrieve the status of all panels in the system.

        :return: Dictionary containing the status of all panels.
        """
        try:
            system_status = {panel_id: panel.get_status() for panel_id, panel in self.panels.items()}
            logging.info("System status retrieved.")
            return system_status
        except Exception as e:
            logging.error(f"Error retrieving system status: {e}")
            return {"error": str(e)}

    def control_panel_equipment(self, panel_id: str, equipment_id: str, action: str) -> str:
        """
        Control a specific piece of equipment in a specific panel.

        :param panel_id: ID of the panel containing the equipment.
        :param equipment_id: ID of the equipment to control.
        :param action: Action to perform (e.g., "ON", "OFF").
        :return: Result of the control operation.
        """
        try:
            if panel_id not in self.panels:
                raise ValueError(f"Panel {panel_id} not found in the system.")
            
            panel = self.panels[panel_id]
            return panel.control_equipment(equipment_id, action)
        except Exception as e:
            logging.error(f"Error controlling equipment {equipment_id} in panel {panel_id}: {e}")
            return f"Error: {str(e)}"

# Example usage
if __name__ == "__main__":
    # Initialize the BMS
    bms = BuildingManagementSystem()

    # Create and add panels
    panel1 = PayeshNirooPanel(panel_id="PN001", equipment={"E001": "OFF", "E002": "OFF"})
    panel2 = PayeshNirooPanel(panel_id="PN002", equipment={"E003": "OFF", "E004": "OFF"})
    bms.add_panel(panel1)
    bms.add_panel(panel2)

    # Retrieve system status
    system_status = bms.get_system_status()
    print(json.dumps(system_status, indent=4))

    # Control equipment
    result = bms.control_panel_equipment(panel_id="PN001", equipment_id="E001", action="ON")
    print(result)

    # Retrieve updated system status
    updated_status = bms.get_system_status()
    print(json.dumps(updated_status, indent=4))
```
