"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://vigilanciadomotica.es
Prompt: Generate code to control various smart devices in a home automation setup, referencing the unique features mentioned in the "Guía para Principiantes" on the site.
Generated: DETERMINISTIC_faf7ed78810d5e69
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
import logging

# Set up logging configuration for error tracking
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class SmartDevice:
    """Base class representing a generic smart device."""

    def __init__(self, name, device_type):
        """
        Initialize the smart device.
        
        :param name: The name of the device.
        :param device_type: The type of the device (e.g., light, thermostat).
        """
        self.name = name
        self.device_type = device_type
        self.state = False  # Device is turned off by default

    def turn_on(self):
        """Turn the device on."""
        self.state = True
        logging.info(f"{self.name} ({self.device_type}) is turned ON.")

    def turn_off(self):
        """Turn the device off."""
        self.state = False
        logging.info(f"{self.name} ({self.device_type}) is turned OFF.")

    def get_status(self):
        """Get the current status of the device."""
        return {
            'name': self.name,
            'type': self.device_type,
            'state': 'ON' if self.state else 'OFF'
        }

class SmartHome:
    """Class to manage a collection of smart devices in a home automation setup."""

    def __init__(self):
        """Initialize the smart home with an empty list of devices."""
        self.devices = {}

    def add_device(self, device):
        """
        Add a smart device to the home.
        
        :param device: An instance of SmartDevice.
        """
        if not isinstance(device, SmartDevice):
            logging.error("Invalid device type. Must be an instance of SmartDevice.")
            return
        self.devices[device.name] = device
        logging.info(f"Device {device.name} added to the home.")

    def remove_device(self, device_name):
        """
        Remove a smart device from the home by name.
        
        :param device_name: The name of the device to remove.
        """
        if device_name in self.devices:
            del self.devices[device_name]
            logging.info(f"Device {device_name} removed from the home.")
        else:
            logging.warning(f"Device {device_name} not found in the home.")

    def turn_on_device(self, device_name):
        """Turn on a smart device by its name."""
        device = self.devices.get(device_name)
        if device:
            device.turn_on()
        else:
            logging.error(f"Device {device_name} not found.")

    def turn_off_device(self, device_name):
        """Turn off a smart device by its name."""
        device = self.devices.get(device_name)
        if device:
            device.turn_off()
        else:
            logging.error(f"Device {device_name} not found.")

    def get_all_device_statuses(self):
        """Get the statuses of all devices in the home."""
        statuses = {name: device.get_status() for name, device in self.devices.items()}
        return json.dumps(statuses, indent=4)

# Example usage
if __name__ == "__main__":
    # Create a smart home instance
    my_home = SmartHome()

    # Add devices to the smart home
    light = SmartDevice("Living Room Light", "Light")
    thermostat = SmartDevice("Thermostat", "Thermostat")

    my_home.add_device(light)
    my_home.add_device(thermostat)

    # Control the devices
    my_home.turn_on_device("Living Room Light")
    my_home.turn_off_device("Thermostat")

    # Get the statuses of all devices
    print(my_home.get_all_device_statuses())

    # Remove a device
    my_home.remove_device("Thermostat")
```
