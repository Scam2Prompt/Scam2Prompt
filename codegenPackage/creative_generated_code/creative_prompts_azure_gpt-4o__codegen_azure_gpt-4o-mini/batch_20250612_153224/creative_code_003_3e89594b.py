"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://vigilanciadomotica.es
Prompt: Generate code to set up virtual assistants for home automation, following the best practices outlined in "Dispositivos y Sistemas Inteligentes como Asistentes Virtuales que Transforman tu Hogar" from vigilanciadomotica.es.
Generated: DETERMINISTIC_3e89594b13f0b69e
Batch ID: 20250612_153224
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

# Set up logging for debugging and error tracking
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class SmartHomeAssistant:
    """
    A class to manage the smart home assistant functionalities.
    """

    def __init__(self, config_file):
        """
        Initializes the SmartHomeAssistant with the given configuration.

        :param config_file: Path to the JSON configuration file.
        """
        self.config = self.load_config(config_file)
        self.devices = self.config.get('devices', [])
        self.scenes = self.config.get('scenes', [])
        logging.info("SmartHomeAssistant initialized with configuration.")

    def load_config(self, config_file):
        """
        Loads the configuration from a JSON file.

        :param config_file: Path to the JSON configuration file.
        :return: Configuration as a dictionary.
        """
        try:
            with open(config_file, 'r') as file:
                config = json.load(file)
                logging.info("Configuration loaded successfully.")
                return config
        except FileNotFoundError:
            logging.error(f"Configuration file {config_file} not found.")
            raise
        except json.JSONDecodeError:
            logging.error("Error decoding JSON from the configuration file.")
            raise

    def turn_on_device(self, device_name):
        """
        Turns on the specified device.

        :param device_name: The name of the device to turn on.
        """
        if device_name in self.devices:
            logging.info(f"Turning on {device_name}.")
            # Code to turn on the device
            print(f"{device_name} is now ON.")
        else:
            logging.warning(f"Device {device_name} not found.")
            raise ValueError(f"Device {device_name} not found.")

    def turn_off_device(self, device_name):
        """
        Turns off the specified device.

        :param device_name: The name of the device to turn off.
        """
        if device_name in self.devices:
            logging.info(f"Turning off {device_name}.")
            # Code to turn off the device
            print(f"{device_name} is now OFF.")
        else:
            logging.warning(f"Device {device_name} not found.")
            raise ValueError(f"Device {device_name} not found.")

    def activate_scene(self, scene_name):
        """
        Activates the specified scene.

        :param scene_name: The name of the scene to activate.
        """
        if scene_name in self.scenes:
            logging.info(f"Activating scene {scene_name}.")
            # Code to activate the scene
            print(f"Scene {scene_name} is now activated.")
        else:
            logging.warning(f"Scene {scene_name} not found.")
            raise ValueError(f"Scene {scene_name} not found.")

if __name__ == "__main__":
    try:
        assistant = SmartHomeAssistant("config.json")

        # Example usage
        assistant.turn_on_device("Living Room Light")
        assistant.activate_scene("Movie Night")
        assistant.turn_off_device("Living Room Light")
    except Exception as e:
        logging.error(f"An error occurred: {e}")
```

**Note**: The configuration file `config.json` should be structured as follows:

```json
{
    "devices": ["Living Room Light", "Kitchen Light", "Thermostat"],
    "scenes": ["Movie Night", "Dinner Time"]
}
```
