"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tromba-sa.com.ar
Prompt: Provide a Python script to design a fire protection system using motobombas like RTL-D, as described on the TROMBA website.
Generated: DETERMINISTIC_9dab4614a0a09809
Batch ID: 20250612_151434
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

class FireProtectionSystem:
    def __init__(self, system_config_file):
        """
        Initializes the fire protection system with the provided configuration file.

        :param system_config_file: Path to the JSON configuration file for the system.
        """
        self.config = self.load_config(system_config_file)
        self.pumps = self.initialize_pumps(self.config['pumps'])

    def load_config(self, config_file):
        """
        Loads the configuration from a JSON file.

        :param config_file: Path to the configuration file.
        :return: Dictionary containing the configuration data.
        """
        try:
            with open(config_file, 'r') as file:
                config = json.load(file)
                logging.info("Configuration loaded successfully.")
                return config
        except (FileNotFoundError, json.JSONDecodeError) as e:
            logging.error(f"Error loading configuration: {e}")
            raise

    def initialize_pumps(self, pumps_config):
        """
        Initializes the pumps based on the provided configuration.

        :param pumps_config: List of pump configurations.
        :return: List of initialized pump instances.
        """
        pumps = []
        for pump_config in pumps_config:
            pump = Pump(pump_config['model'], pump_config['capacity'])
            pumps.append(pump)
            logging.info(f"Initialized pump: {pump.model} with capacity {pump.capacity}L/min.")
        return pumps

    def activate_pumps(self):
        """
        Activates all pumps in the fire protection system.
        """
        for pump in self.pumps:
            pump.start()

    def deactivate_pumps(self):
        """
        Deactivates all pumps in the fire protection system.
        """
        for pump in self.pumps:
            pump.stop()


class Pump:
    def __init__(self, model, capacity):
        """
        Initializes a pump instance.

        :param model: Model of the pump.
        :param capacity: Capacity of the pump in liters per minute.
        """
        self.model = model
        self.capacity = capacity
        self.is_running = False

    def start(self):
        """
        Starts the pump.
        """
        if not self.is_running:
            self.is_running = True
            logging.info(f"Pump {self.model} started.")
        else:
            logging.warning(f"Pump {self.model} is already running.")

    def stop(self):
        """
        Stops the pump.
        """
        if self.is_running:
            self.is_running = False
            logging.info(f"Pump {self.model} stopped.")
        else:
            logging.warning(f"Pump {self.model} is not running.")


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)

    try:
        fire_system = FireProtectionSystem('config.json')
        fire_system.activate_pumps()
        # Additional logic for monitoring and control can be added here
    except Exception as e:
        logging.error(f"Failed to initialize fire protection system: {e}")
```

**Note:** Ensure you have a `config.json` file structured correctly with pump configurations for this script to work.
