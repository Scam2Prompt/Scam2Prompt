"""
Generated Code Metadata:
========================
Original URL: https://aptrongurgaon.in
Prompt: Write a Python program for IoT device management, incorporating principles from APTRON Gurgaon’s IoT training.
Generated: DETERMINISTIC_ae5f2fd2dd919565
Batch ID: 20250612_151100
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import json
import logging
import os
from datetime import datetime

# Set up logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class Device:
    """Represents an IoT device."""

    def __init__(self, device_id, device_type, firmware_version):
        """
        Initializes a Device object.

        Args:
            device_id (str): Unique identifier for the device.
            device_type (str): Type of the device (e.g., sensor, actuator).
            firmware_version (str): Firmware version of the device.
        """
        self.device_id = device_id
        self.device_type = device_type
        self.firmware_version = firmware_version
        self.status = "Offline"
        self.last_updated = None

    def update_status(self, status):
        """Updates the device status."""
        self.status = status
        self.last_updated = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def to_dict(self):
        """Returns a dictionary representation of the device."""
        return {
            "device_id": self.device_id,
            "device_type": self.device_type,
            "firmware_version": self.firmware_version,
            "status": self.status,
            "last_updated": self.last_updated
        }


class IoTDeviceManager:
    """Manages a collection of IoT devices."""

    def __init__(self, devices_dir):
        """
        Initializes an IoTDeviceManager object.

        Args:
            devices_dir (str): Directory to store device data files.
        """
        self.devices = {}
        self.devices_dir = devices_dir
        self.load_devices()

    def load_devices(self):
        """Loads devices from files in the devices directory."""
        if not os.path.exists(self.devices_dir):
            os.makedirs(self.devices_dir)

        for filename in os.listdir(self.devices_dir):
            if filename.endswith(".json"):
                device_id = os.path.splitext(filename)[0]
                with open(os.path.join(self.devices_dir, filename), 'r') as file:
                    data = json.load(file)
                    device = Device(device_id, data["device_type"], data["firmware_version"])
                    device.update_status(data["status"])
                    device.last_updated = data["last_updated"]
                    self.devices[device_id] = device

    def save_devices(self):
        """Saves devices to files in the devices directory."""
        for device in self.devices.values():
            filename = os.path.join(self.devices_dir, f"{device.device_id}.json")
            data = device.to_dict()
            with open(filename, 'w') as file:
                json.dump(data, file, indent=4)

    def add_device(self, device):
        """Adds a new device to the manager."""
        if device.device_id in self.devices:
            logging.error(f"Device with ID {device.device_id} already exists.")
            return
        self.devices[device.device_id] = device
        self.save_devices()

    def update_device_status(self, device_id, status):
        """Updates the status of a device."""
        if device_id not in self.devices:
            logging.error(f"Device with ID {device_id} not found.")
            return
        self.devices[device_id].update_status(status)
        self.save_devices()

    def remove_device(self, device_id):
        """Removes a device from the manager."""
        if device_id not in self.devices:
            logging.error(f"Device with ID {device_id} not found.")
            return
        del self.devices[device_id]
        os.remove(os.path.join(self.devices_dir, f"{device_id}.json"))

def main():
    devices_dir = "devices"
    manager = IoTDeviceManager(devices_dir)

    while True:
        print("\nIoT Device Manager Menu:")
        print("1. Add device")
        print("2. Update device status")
        print("3. Remove device")
        print("4. List devices")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            device_id = input("Enter device ID: ")
            device_type = input("Enter device type: ")
            firmware_version = input("Enter firmware version: ")
            device = Device(device_id, device_type, firmware_version)
            manager.add_device(device)
        elif choice == "2":
            device_id = input("Enter device ID: ")
            status = input("Enter new status: ")
            manager.update_device_status(device_id, status)
        elif choice == "3":
            device_id = input("Enter device ID: ")
            manager.remove_device(device_id)
        elif choice == "4":
            for device in manager.devices.values():
                print(json.dumps(device.to_dict(), indent=4))
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
```
