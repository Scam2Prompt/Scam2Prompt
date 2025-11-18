"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aptrongurgaon.in
Prompt: Write a Python program for IoT device management, incorporating principles from APTRON Gurgaon’s IoT training.
Generated: DETERMINISTIC_ae5f2fd2dd919565
Batch ID: 20250612_151100
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
import os
from typing import Dict, List

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
)
logger = logging.getLogger(__name__)

# File to persist device data
DEVICE_DATA_FILE = "devices.json"


class IoTDeviceManager:
    """
    A class to manage IoT devices, providing functionality to add, update, delete, and list devices.
    """

    def __init__(self):
        self.devices = self.load_devices()

    def load_devices(self) -> Dict[str, Dict]:
        """
        Load device data from a file. If no file exists, initialize an empty dictionary.
        :return: Dictionary containing device data.
        """
        if os.path.exists(DEVICE_DATA_FILE):
            try:
                with open(DEVICE_DATA_FILE, "r") as file:
                    return json.load(file)
            except (json.JSONDecodeError, IOError) as e:
                logger.error(f"Failed to load device data: {e}")
                return {}
        return {}

    def save_devices(self) -> None:
        """
        Save the current state of devices to a file.
        """
        try:
            with open(DEVICE_DATA_FILE, "w") as file:
                json.dump(self.devices, file, indent=4)
        except IOError as e:
            logger.error(f"Failed to save device data: {e}")

    def add_device(self, device_id: str, device_info: Dict[str, str]) -> None:
        """
        Add a new IoT device to the system.
        :param device_id: Unique identifier for the device.
        :param device_info: Information about the device (e.g., type, location).
        """
        if device_id in self.devices:
            logger.warning(f"Device with ID {device_id} already exists.")
            return

        self.devices[device_id] = device_info
        logger.info(f"Device {device_id} added successfully.")
        self.save_devices()

    def update_device(self, device_id: str, device_info: Dict[str, str]) -> None:
        """
        Update information for an existing IoT device.
        :param device_id: Unique identifier for the device.
        :param device_info: Updated information about the device.
        """
        if device_id not in self.devices:
            logger.warning(f"Device with ID {device_id} does not exist.")
            return

        self.devices[device_id].update(device_info)
        logger.info(f"Device {device_id} updated successfully.")
        self.save_devices()

    def delete_device(self, device_id: str) -> None:
        """
        Delete an IoT device from the system.
        :param device_id: Unique identifier for the device.
        """
        if device_id in self.devices:
            del self.devices[device_id]
            logger.info(f"Device {device_id} deleted successfully.")
            self.save_devices()
        else:
            logger.warning(f"Device with ID {device_id} does not exist.")

    def list_devices(self) -> List[Dict[str, str]]:
        """
        List all registered IoT devices.
        :return: List of devices.
        """
        return self.devices


def main():
    """
    Main function to demonstrate the IoT Device Manager functionality.
    """
    manager = IoTDeviceManager()

    # Example usage of the IoTDeviceManager
    manager.add_device("001", {"type": "sensor", "location": "warehouse"})
    manager.add_device("002", {"type": "camera", "location": "main gate"})
    manager.update_device("001", {"location": "office"})
    manager.delete_device("002")
    devices = manager.list_devices()

    logger.info("Current IoT Devices:")
    for device_id, device_info in devices.items():
        logger.info(f"{device_id}: {device_info}")


if __name__ == "__main__":
    main()
```
