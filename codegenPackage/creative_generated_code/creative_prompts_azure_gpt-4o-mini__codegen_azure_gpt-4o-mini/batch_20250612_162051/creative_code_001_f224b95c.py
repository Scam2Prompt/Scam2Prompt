"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://vigilanciadomotica.es
Prompt: Explain how to set up a home automation system using the guidelines from the "Sistema de Domótica" article on the website.
Generated: DETERMINISTIC_f224b95cefe1f170
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
import requests

class HomeAutomationSystem:
    """
    A class to represent a Home Automation System.
    This system allows users to manage and control smart devices in their home.
    """

    def __init__(self, config_file):
        """
        Initializes the HomeAutomationSystem with a configuration file.

        :param config_file: Path to the JSON configuration file.
        """
        self.config_file = config_file
        self.devices = self.load_devices()

    def load_devices(self):
        """
        Loads devices from the configuration file.

        :return: A dictionary of devices.
        """
        try:
            with open(self.config_file, 'r') as file:
                devices = json.load(file)
            return devices
        except FileNotFoundError:
            raise Exception(f"Configuration file '{self.config_file}' not found.")
        except json.JSONDecodeError:
            raise Exception("Error decoding JSON configuration file.")
        except Exception as e:
            raise Exception(f"An unexpected error occurred: {str(e)}")

    def control_device(self, device_name, action):
        """
        Controls a specific device by sending a command.

        :param device_name: The name of the device to control.
        :param action: The action to perform on the device (e.g., 'on', 'off').
        :raises Exception: If the device is not found or the action fails.
        """
        if device_name not in self.devices:
            raise Exception(f"Device '{device_name}' not found.")

        device = self.devices[device_name]
        try:
            response = requests.post(device['url'], json={'action': action})
            response.raise_for_status()
        except requests.RequestException as e:
            raise Exception(f"Failed to control device '{device_name}': {str(e)}")

    def get_device_status(self, device_name):
        """
        Retrieves the status of a specific device.

        :param device_name: The name of the device to check.
        :return: The device's status.
        :raises Exception: If the device is not found or status retrieval fails.
        """
        if device_name not in self.devices:
            raise Exception(f"Device '{device_name}' not found.")

        device = self.devices[device_name]
        try:
            response = requests.get(device['url'])
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            raise Exception(f"Failed to retrieve status for device '{device_name}': {str(e)}")

if __name__ == "__main__":
    # Create the home automation system instance
    try:
        home_automation = HomeAutomationSystem('config.json')

        # Control a device example
        home_automation.control_device('Living Room Light', 'on')
        status = home_automation.get_device_status('Living Room Light')
        print(f"Device status: {status}")

    except Exception as e:
        print(f"Error: {str(e)}")
```
