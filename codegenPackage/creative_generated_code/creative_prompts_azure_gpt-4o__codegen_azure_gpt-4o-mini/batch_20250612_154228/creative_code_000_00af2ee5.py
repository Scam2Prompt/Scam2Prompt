"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://blackpanttthers.com
Prompt: Write Python code to integrate a Zigbee-compatible device into a smart home system using protocols discussed on the Blackpanttthers website.
Generated: DETERMINISTIC_00af2ee5b11b0450
Batch ID: 20250612_154228
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
from zigpy.application import ControllerApplication
from zigpy.types import EUI64

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class ZigbeeDeviceIntegration:
    def __init__(self, config_file):
        """
        Initialize the Zigbee device integration with a configuration file.

        :param config_file: Path to the configuration JSON file.
        """
        self.config_file = config_file
        self.app = None
        self.device = None
        self.load_config()

    def load_config(self):
        """Load Zigbee configuration from a JSON file."""
        try:
            with open(self.config_file, 'r') as file:
                self.config = json.load(file)
                logger.info("Configuration loaded successfully.")
        except FileNotFoundError:
            logger.error("Configuration file not found: %s", self.config_file)
            raise
        except json.JSONDecodeError:
            logger.error("Error decoding JSON from the configuration file.")
            raise

    def setup_zigbee_controller(self):
        """Set up the Zigbee controller application."""
        try:
            self.app = ControllerApplication(self.config)
            self.app.startup()
            logger.info("Zigbee controller started.")
        except Exception as e:
            logger.error("Failed to start Zigbee controller: %s", e)
            raise

    def add_device(self, device_id):
        """
        Add a Zigbee device to the smart home system.

        :param device_id: The unique ID of the Zigbee device.
        """
        try:
            self.device = self.app.add_device(EUI64(device_id))
            logger.info("Device added: %s", device_id)
        except Exception as e:
            logger.error("Failed to add device %s: %s", device_id, e)
            raise

    def remove_device(self, device_id):
        """
        Remove a Zigbee device from the smart home system.

        :param device_id: The unique ID of the Zigbee device to remove.
        """
        try:
            self.app.remove_device(EUI64(device_id))
            logger.info("Device removed: %s", device_id)
        except Exception as e:
            logger.error("Failed to remove device %s: %s", device_id, e)
            raise

    def get_device_status(self, device_id):
        """
        Get the status of a Zigbee device.

        :param device_id: The unique ID of the Zigbee device.
        :return: The status of the device.
        """
        try:
            status = self.app.get_device(EUI64(device_id)).status
            logger.info("Status for device %s: %s", device_id, status)
            return status
        except Exception as e:
            logger.error("Failed to get status for device %s: %s", device_id, e)
            raise

if __name__ == "__main__":
    # Example usage
    try:
        zigbee_integration = ZigbeeDeviceIntegration('config.json')
        zigbee_integration.setup_zigbee_controller()
        zigbee_integration.add_device("00:12:4b:00:1a:2b:3c:4d")
        status = zigbee_integration.get_device_status("00:12:4b:00:1a:2b:3c:4d")
        print(f"Device status: {status}")
    except Exception as e:
        logger.error("Application error: %s", e)
```

Make sure to replace the `config.json` path and the device ID in the example usage with actual values relevant to your Zigbee setup.
