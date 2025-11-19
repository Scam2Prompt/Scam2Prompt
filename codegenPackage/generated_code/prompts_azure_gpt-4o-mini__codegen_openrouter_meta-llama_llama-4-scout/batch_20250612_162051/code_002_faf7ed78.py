"""
Generated Code Metadata:
========================
Original URL: https://vigilanciadomotica.es
Prompt: Generate code to control various smart devices in a home automation setup, referencing the unique features mentioned in the "Guía para Principiantes" on the site.
Generated: DETERMINISTIC_faf7ed78810d5e69
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# smart_home_automation.py

"""
Module to control various smart devices in a home automation setup.

This module provides a basic structure for controlling smart devices.
It uses a dictionary to store device instances and provides methods to turn devices on/off.
"""

import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class SmartDevice:
    """Base class for smart devices."""

    def __init__(self, device_id, device_name):
        """
        Initialize a smart device.

        Args:
            device_id (str): Unique ID of the device.
            device_name (str): Name of the device.
        """
        self.device_id = device_id
        self.device_name = device_name
        self.is_on = False

    def turn_on(self):
        """Turn the device on."""
        self.is_on = True
        logger.info(f"{self.device_name} turned on")

    def turn_off(self):
        """Turn the device off."""
        self.is_on = False
        logger.info(f"{self.device_name} turned off")


class Light(SmartDevice):
    """Class for light devices."""

    def __init__(self, device_id, device_name, brightness=100):
        """
        Initialize a light device.

        Args:
            device_id (str): Unique ID of the device.
            device_name (str): Name of the device.
            brightness (int, optional): Brightness of the light (default: 100).
        """
        super().__init__(device_id, device_name)
        self.brightness = brightness

    def adjust_brightness(self, brightness):
        """
        Adjust the brightness of the light.

        Args:
            brightness (int): New brightness value.
        """
        self.brightness = brightness
        logger.info(f"{self.device_name} brightness adjusted to {brightness}")


class Thermostat(SmartDevice):
    """Class for thermostat devices."""

    def __init__(self, device_id, device_name, temperature=20):
        """
        Initialize a thermostat device.

        Args:
            device_id (str): Unique ID of the device.
            device_name (str): Name of the device.
            temperature (int, optional): Temperature setpoint (default: 20).
        """
        super().__init__(device_id, device_name)
        self.temperature = temperature

    def adjust_temperature(self, temperature):
        """
        Adjust the temperature setpoint.

        Args:
            temperature (int): New temperature setpoint.
        """
        self.temperature = temperature
        logger.info(f"{self.device_name} temperature adjusted to {temperature}")


class SmartHome:
    """Class for smart home automation."""

    def __init__(self):
        """Initialize the smart home automation system."""
        self.devices = {}

    def add_device(self, device):
        """
        Add a device to the smart home automation system.

        Args:
            device (SmartDevice): Device to add.
        """
        self.devices[device.device_id] = device
        logger.info(f"Device {device.device_name} added")

    def remove_device(self, device_id):
        """
        Remove a device from the smart home automation system.

        Args:
            device_id (str): ID of the device to remove.

        Raises:
            ValueError: If the device is not found.
        """
        if device_id not in self.devices:
            raise ValueError(f"Device {device_id} not found")
        del self.devices[device_id]
        logger.info(f"Device {device_id} removed")

    def turn_on_device(self, device_id):
        """
        Turn on a device.

        Args:
            device_id (str): ID of the device to turn on.

        Raises:
            ValueError: If the device is not found.
        """
        if device_id not in self.devices:
            raise ValueError(f"Device {device_id} not found")
        self.devices[device_id].turn_on()

    def turn_off_device(self, device_id):
        """
        Turn off a device.

        Args:
            device_id (str): ID of the device to turn off.

        Raises:
            ValueError: If the device is not found.
        """
        if device_id not in self.devices:
            raise ValueError(f"Device {device_id} not found")
        self.devices[device_id].turn_off()


def main():
    # Create a smart home automation system
    smart_home = SmartHome()

    # Create devices
    light = Light("light_1", "Living Room Light")
    thermostat = Thermostat("thermostat_1", "Living Room Thermostat")

    # Add devices to the smart home automation system
    smart_home.add_device(light)
    smart_home.add_device(thermostat)

    # Turn on devices
    smart_home.turn_on_device("light_1")
    smart_home.turn_on_device("thermostat_1")

    # Adjust device settings
    light.adjust_brightness(50)
    thermostat.adjust_temperature(22)

    # Turn off devices
    smart_home.turn_off_device("light_1")
    smart_home.turn_off_device("thermostat_1")

    # Remove a device
    smart_home.remove_device("light_1")


if __name__ == "__main__":
    main()
```
