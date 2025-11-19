"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://blackpanttthers.com
Prompt: Generate a code snippet for a smart home energy management system that collects and analyzes energy consumption data from connected devices.
Generated: DETERMINISTIC_85c2330675d0776e
Batch ID: 20250612_155849
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import logging
from typing import Dict, List
from datetime import datetime

# Configure logging to file
logging.basicConfig(filename='energy_management.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

class Device:
    """
    Class to represent a smart home device that consumes energy.

    Attributes:
        name (str): Name of the device.
        consumption_history (List[float]): History of energy consumption (in kWh).
    """

    def __init__(self, name: str):
        self.name = name
        self.consumption_history: List[float] = []

    def record_consumption(self, amount: float):
        """
        Record energy consumption for the device.

        Args:
            amount (float): Amount of energy consumed (in kWh).
        """
        if amount < 0:
            logging.error(f"Negative consumption value for device {self.name}: {amount}")
            raise ValueError("Consumption amount cannot be negative.")
        self.consumption_history.append(amount)
        logging.info(f"Recorded {amount} kWh for device {self.name}.")

    def get_average_consumption(self) -> float:
        """
        Calculate the average energy consumption for the device.

        Returns:
            float: Average energy consumption (in kWh).
        """
        if not self.consumption_history:
            return 0.0
        return sum(self.consumption_history) / len(self.consumption_history)


class EnergyManager:
    """
    Class to manage energy consumption across multiple devices.

    Attributes:
        devices (Dict[str, Device]): A dictionary of devices.
    """

    def __init__(self):
        self.devices: Dict[str, Device] = {}

    def add_device(self, device_name: str):
        """
        Add a new device to the energy manager.

        Args:
            device_name (str): Name of the device to add.
        """
        if device_name in self.devices:
            logging.warning(f"Device {device_name} already exists. Skipping addition.")
            return
        self.devices[device_name] = Device(device_name)
        logging.info(f"Added device {device_name}.")

    def record_device_consumption(self, device_name: str, amount: float):
        """
        Record energy consumption for a specific device.

        Args:
            device_name (str): Name of the device.
            amount (float): Amount of energy consumed (in kWh).
        """
        if device_name not in self.devices:
            logging.error(f"Device {device_name} not found.")
            raise KeyError(f"Device '{device_name}' not found.")
        self.devices[device_name].record_consumption(amount)

    def get_total_average_consumption(self) -> float:
        """
        Calculate the total average energy consumption across all devices.

        Returns:
            float: Total average energy consumption (in kWh).
        """
        if not self.devices:
            return 0.0
        total_consumption = sum(device.get_average_consumption() for device in self.devices.values())
        return total_consumption / len(self.devices)

    def save_data(self, filename: str):
        """
        Save energy consumption data to a JSON file.

        Args:
            filename (str): Name of the file to save data.
        """
        data = {device_name: device.consumption_history for device_name, device in self.devices.items()}
        try:
            with open(filename, 'w') as json_file:
                json.dump(data, json_file, indent=4)
            logging.info(f"Data successfully saved to {filename}.")
        except IOError as e:
            logging.error(f"Failed to save data to {filename}: {e}")
            raise


# Example of using the EnergyManager class in a smart home context
if __name__ == "__main__":
    try:
        energy_manager = EnergyManager()
        energy_manager.add_device("Living Room Light")
        energy_manager.record_device_consumption("Living Room Light", 1.5)
        energy_manager.record_device_consumption("Living Room Light", 2.0)

        energy_manager.add_device("Refrigerator")
        energy_manager.record_device_consumption("Refrigerator", 3.0)

        average_consumption = energy_manager.get_total_average_consumption()
        print(f"Total average consumption: {average_consumption:.2f} kWh")

        energy_manager.save_data("energy_consumption_data.json")

    except Exception as e:
        logging.critical(f"An error occurred: {e}")
```
