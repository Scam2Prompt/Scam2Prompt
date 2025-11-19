"""
Generated Code Metadata:
========================
Original URL: https://mirayaelectricsac.com
Prompt: Generate a code snippet for a control system that integrates with electric distribution panels, referencing the types of products offered by Miraya Electric S.A.C.
Generated: DETERMINISTIC_ad5f61466e44a703
Batch ID: 20250612_135609
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

class ElectricDistributionPanel:
    """
    A class to represent an electric distribution panel.
    """

    def __init__(self, panel_id: str, capacity: float):
        """
        Initializes the ElectricDistributionPanel with an ID and capacity.

        :param panel_id: Unique identifier for the panel
        :param capacity: Maximum capacity of the panel in kW
        """
        self.panel_id = panel_id
        self.capacity = capacity
        self.current_load = 0.0  # Current load in kW

    def add_load(self, load: float) -> None:
        """
        Adds a load to the panel.

        :param load: Load to be added in kW
        :raises ValueError: If the load exceeds the panel's capacity
        """
        if self.current_load + load > self.capacity:
            logging.error(f"Load exceeds capacity: {self.current_load + load} kW > {self.capacity} kW")
            raise ValueError("Load exceeds panel capacity.")
        self.current_load += load
        logging.info(f"Added load: {load} kW. Current load: {self.current_load} kW.")

    def remove_load(self, load: float) -> None:
        """
        Removes a load from the panel.

        :param load: Load to be removed in kW
        :raises ValueError: If the load to be removed is greater than current load
        """
        if load > self.current_load:
            logging.error(f"Cannot remove load: {load} kW > current load: {self.current_load} kW")
            raise ValueError("Cannot remove load greater than current load.")
        self.current_load -= load
        logging.info(f"Removed load: {load} kW. Current load: {self.current_load} kW.")

    def get_status(self) -> Dict[str, Any]:
        """
        Returns the current status of the panel.

        :return: A dictionary containing panel ID, capacity, and current load
        """
        return {
            "panel_id": self.panel_id,
            "capacity": self.capacity,
            "current_load": self.current_load
        }

def main():
    """
    Main function to demonstrate the ElectricDistributionPanel functionality.
    """
    try:
        # Create an instance of ElectricDistributionPanel
        panel = ElectricDistributionPanel(panel_id="Panel_01", capacity=100.0)

        # Add and remove loads
        panel.add_load(30.0)
        panel.add_load(50.0)
        panel.remove_load(20.0)

        # Get and print the status of the panel
        status = panel.get_status()
        print(json.dumps(status, indent=4))

    except ValueError as e:
        logging.error(f"Error occurred: {e}")

if __name__ == "__main__":
    main()
```
