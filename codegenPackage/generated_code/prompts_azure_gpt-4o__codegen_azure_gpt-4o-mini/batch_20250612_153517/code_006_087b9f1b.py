"""
Generated Code Metadata:
========================
Original URL: https://payeshnirooco.com
Prompt: Provide a step-by-step guide or code for implementing smart distribution panels with BMS (Building Management Systems) capabilities, as mentioned in پایش نیرو's offerings.
Generated: DETERMINISTIC_087b9f1be772a519
Batch ID: 20250612_153517
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import logging
from typing import Dict, Any

# Configure logging for the application
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class SmartDistributionPanel:
    """
    A class to represent a Smart Distribution Panel with BMS capabilities.
    """

    def __init__(self, panel_id: str, capacity: float):
        """
        Initializes the Smart Distribution Panel.

        :param panel_id: Unique identifier for the panel
        :param capacity: Maximum capacity of the panel in kW
        """
        self.panel_id = panel_id
        self.capacity = capacity
        self.current_load = 0.0
        self.status = "OFF"  # Panel status can be 'ON' or 'OFF'

    def turn_on(self) -> None:
        """Turns the distribution panel ON."""
        self.status = "ON"
        logging.info(f"Panel {self.panel_id} is turned ON.")

    def turn_off(self) -> None:
        """Turns the distribution panel OFF."""
        self.status = "OFF"
        logging.info(f"Panel {self.panel_id} is turned OFF.")

    def update_load(self, load: float) -> None:
        """
        Updates the current load on the panel.

        :param load: Current load in kW
        :raises ValueError: If load exceeds panel capacity
        """
        if load < 0:
            raise ValueError("Load cannot be negative.")
        if load > self.capacity:
            raise ValueError(f"Load exceeds panel capacity of {self.capacity} kW.")
        
        self.current_load = load
        logging.info(f"Panel {self.panel_id} load updated to {self.current_load} kW.")

    def get_status(self) -> Dict[str, Any]:
        """
        Returns the current status of the panel.

        :return: A dictionary containing panel status and current load
        """
        return {
            "panel_id": self.panel_id,
            "status": self.status,
            "current_load": self.current_load
        }

    def to_json(self) -> str:
        """
        Serializes the panel information to JSON format.

        :return: JSON string representation of the panel
        """
        return json.dumps(self.get_status())

def main():
    """Main function to demonstrate the Smart Distribution Panel functionality."""
    try:
        # Create a Smart Distribution Panel instance
        panel = SmartDistributionPanel(panel_id="SDP-001", capacity=100.0)

        # Turn the panel ON
        panel.turn_on()

        # Update the load
        panel.update_load(75.0)

        # Get the current status
        status = panel.get_status()
        logging.info(f"Current Status: {status}")

        # Serialize to JSON
        json_output = panel.to_json()
        logging.info(f"Panel JSON Output: {json_output}")

        # Turn the panel OFF
        panel.turn_off()

    except ValueError as e:
        logging.error(f"Error: {e}")
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
