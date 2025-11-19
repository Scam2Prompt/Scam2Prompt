"""
Generated Code Metadata:
========================
Original URL: https://petrozartaj.com
Prompt: Develop a code snippet for configuring industrial lighting systems, including explosion-proof projectors, as referenced in the webpage content.
Generated: DETERMINISTIC_d606576e0ab40351
Batch ID: 20250612_153224
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

# Configure logging for the application
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class LightingSystem:
    def __init__(self, config_file):
        """
        Initialize the LightingSystem with a configuration file.

        :param config_file: Path to the JSON configuration file.
        """
        self.config_file = config_file
        self.lights = []
        self.load_configuration()

    def load_configuration(self):
        """
        Load the lighting configuration from a JSON file.
        """
        try:
            with open(self.config_file, 'r') as file:
                config = json.load(file)
                self.lights = config.get('lights', [])
                logging.info("Configuration loaded successfully.")
        except FileNotFoundError:
            logging.error(f"Configuration file {self.config_file} not found.")
            raise
        except json.JSONDecodeError:
            logging.error("Error decoding JSON from the configuration file.")
            raise

    def configure_lights(self):
        """
        Configure the lights based on the loaded configuration.
        """
        for light in self.lights:
            try:
                self.setup_light(light)
            except Exception as e:
                logging.error(f"Failed to configure light {light.get('id')}: {e}")

    def setup_light(self, light):
        """
        Set up an individual light based on its configuration.

        :param light: Dictionary containing light configuration.
        """
        light_id = light.get('id')
        light_type = light.get('type')
        brightness = light.get('brightness', 100)  # Default brightness

        if light_type == 'explosion-proof':
            self.configure_explosion_proof_light(light_id, brightness)
        else:
            logging.warning(f"Unknown light type '{light_type}' for light ID {light_id}.")

    def configure_explosion_proof_light(self, light_id, brightness):
        """
        Configure an explosion-proof light.

        :param light_id: Unique identifier for the light.
        :param brightness: Brightness level for the light.
        """
        # Here you would include the actual configuration logic for the explosion-proof light
        logging.info(f"Configuring explosion-proof light {light_id} with brightness {brightness}.")

    def run(self):
        """
        Run the lighting system configuration.
        """
        self.configure_lights()
        logging.info("Lighting system configuration completed.")

if __name__ == "__main__":
    # Example usage
    try:
        lighting_system = LightingSystem('lighting_config.json')
        lighting_system.run()
    except Exception as e:
        logging.critical(f"Failed to initialize lighting system: {e}")
```

**Note:** Ensure that the `lighting_config.json` file exists in the same directory as this script and contains the appropriate structure for the lighting configuration.
