"""
Generated Code Metadata:
========================
Original URL: https://vigilanciadomotica.es
Prompt: "Discuss the role of virtual assistants in home automation and how they can be used to control a domotic system."
Generated: DETERMINISTIC_5f7f8443600f8629
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
import json
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class VirtualAssistant:
    """
    A class to represent a virtual assistant for home automation.
    """

    def __init__(self, name):
        """
        Initializes the virtual assistant with a name.

        Args:
            name (str): The name of the virtual assistant.
        """
        self.name = name
        self.domotic_system = {}

    def add_device(self, device_name, device_type):
        """
        Adds a device to the domotic system.

        Args:
            device_name (str): The name of the device.
            device_type (str): The type of the device (e.g., light, thermostat).
        """
        self.domotic_system[device_name] = {
            'type': device_type,
            'status': 'off'
        }
        logging.info(f"Device '{device_name}' of type '{device_type}' added.")

    def control_device(self, device_name, action):
        """
        Controls a device in the domotic system.

        Args:
            device_name (str): The name of the device to control.
            action (str): The action to perform (e.g., 'on', 'off').

        Raises:
            ValueError: If the device does not exist or the action is invalid.
        """
        if device_name not in self.domotic_system:
            logging.error(f"Device '{device_name}' not found.")
            raise ValueError(f"Device '{device_name}' not found.")

        if action not in ['on', 'off']:
            logging.error(f"Invalid action '{action}' for device '{device_name}'.")
            raise ValueError(f"Invalid action '{action}' for device '{device_name}'.")

        self.domotic_system[device_name]['status'] = action
        logging.info(f"Device '{device_name}' turned {action}.")

    def get_device_status(self, device_name):
        """
        Retrieves the status of a device.

        Args:
            device_name (str): The name of the device.

        Returns:
            str: The status of the device.

        Raises:
            ValueError: If the device does not exist.
        """
        if device_name not in self.domotic_system:
            logging.error(f"Device '{device_name}' not found.")
            raise ValueError(f"Device '{device_name}' not found.")

        status = self.domotic_system[device_name]['status']
        logging.info(f"Device '{device_name}' status: {status}")
        return status

    def save_configuration(self, filename):
        """
        Saves the current configuration of the domotic system to a JSON file.

        Args:
            filename (str): The name of the file to save the configuration.
        """
        try:
            with open(filename, 'w') as file:
                json.dump(self.domotic_system, file)
            logging.info(f"Configuration saved to '{filename}'.")
        except IOError as e:
            logging.error(f"Failed to save configuration: {e}")

    def load_configuration(self, filename):
        """
        Loads the configuration of the domotic system from a JSON file.

        Args:
            filename (str): The name of the file to load the configuration.

        Raises:
            IOError: If the file cannot be read.
        """
        try:
            with open(filename, 'r') as file:
                self.domotic_system = json.load(file)
            logging.info(f"Configuration loaded from '{filename}'.")
        except IOError as e:
            logging.error(f"Failed to load configuration: {e}")
            raise

# Example usage
if __name__ == "__main__":
    assistant = VirtualAssistant("HomeAssistant")
    assistant.add_device("LivingRoomLight", "light")
    assistant.control_device("LivingRoomLight", "on")
    print(assistant.get_device_status("LivingRoomLight"))
    assistant.save_configuration("home_config.json")
    assistant.load_configuration("home_config.json")
```
