"""
Generated Code Metadata:
========================
Original URL: https://vigilanciadomotica.es
Prompt: Generate code to set up virtual assistants for home automation, following the best practices outlined in "Dispositivos y Sistemas Inteligentes como Asistentes Virtuales que Transforman tu Hogar" from vigilanciadomotica.es.
Generated: DETERMINISTIC_3e89594b13f0b69e
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# virtual_assistant.py

import logging
import os
from typing import Dict

# Set up logging configuration
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')

class VirtualAssistant:
    """Virtual assistant for home automation."""

    def __init__(self, name: str, devices: Dict[str, str]):
        """
        Initialize the virtual assistant.

        Args:
        - name (str): The name of the virtual assistant.
        - devices (Dict[str, str]): A dictionary of devices and their types.
        """
        self.name = name
        self.devices = devices

    def turn_on_device(self, device_name: str):
        """
        Turn on a device.

        Args:
        - device_name (str): The name of the device to turn on.

        Raises:
        - ValueError: If the device does not exist.
        """
        if device_name not in self.devices:
            raise ValueError(f"Device '{device_name}' does not exist.")

        # Simulate turning on the device
        logging.info(f"Turning on {device_name}...")
        print(f"{device_name} turned on.")

    def turn_off_device(self, device_name: str):
        """
        Turn off a device.

        Args:
        - device_name (str): The name of the device to turn off.

        Raises:
        - ValueError: If the device does not exist.
        """
        if device_name not in self.devices:
            raise ValueError(f"Device '{device_name}' does not exist.")

        # Simulate turning off the device
        logging.info(f"Turning off {device_name}...")
        print(f"{device_name} turned off.")

    def list_devices(self):
        """List all devices."""
        logging.info("Listing devices...")
        print("Devices:")
        for device, device_type in self.devices.items():
            print(f"- {device} ({device_type})")

class HomeAutomationSystem:
    """Home automation system."""

    def __init__(self):
        self.virtual_assistants: Dict[str, VirtualAssistant] = {}

    def add_virtual_assistant(self, name: str, devices: Dict[str, str]):
        """
        Add a virtual assistant.

        Args:
        - name (str): The name of the virtual assistant.
        - devices (Dict[str, str]): A dictionary of devices and their types.
        """
        self.virtual_assistants[name] = VirtualAssistant(name, devices)

    def get_virtual_assistant(self, name: str) -> VirtualAssistant:
        """
        Get a virtual assistant.

        Args:
        - name (str): The name of the virtual assistant.

        Returns:
        - VirtualAssistant: The virtual assistant.

        Raises:
        - ValueError: If the virtual assistant does not exist.
        """
        if name not in self.virtual_assistants:
            raise ValueError(f"Virtual assistant '{name}' does not exist.")

        return self.virtual_assistants[name]

def main():
    # Create a home automation system
    has = HomeAutomationSystem()

    # Add a virtual assistant
    devices = {
        "light": "Smart Light",
        "thermostat": "Smart Thermostat",
        "security_camera": "Smart Security Camera"
    }
    has.add_virtual_assistant("MyAssistant", devices)

    # Get the virtual assistant
    assistant = has.get_virtual_assistant("MyAssistant")

    # List devices
    assistant.list_devices()

    # Turn on a device
    assistant.turn_on_device("light")

    # Turn off a device
    assistant.turn_off_device("light")

if __name__ == "__main__":
    main()
```
