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
"""
Home Automation System
This script controls various smart devices in a home automation setup.
It follows a modular approach to handle different types of devices such as lights, thermostats, and security cameras.

Requirements:
- Each device has a unique ID.
- Devices can perform specific actions based on their type.
- Error handling ensures robust operation.

Best Practices:
- Clean and readable code using Python conventions.
- Comprehensive comments for maintainability.
"""

import logging

# Configure logging for debugging and error tracking
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")


class SmartDevice:
    """
    Base class for all smart devices.
    """
    def __init__(self, device_id, device_name):
        self.device_id = device_id
        self.device_name = device_name

    def perform_action(self, action, **kwargs):
        """
        Perform a generic action. Should be overridden in child classes.
        """
        raise NotImplementedError("Subclasses must implement 'perform_action' method.")


class SmartLight(SmartDevice):
    """
    Class for smart lights.
    """
    def perform_action(self, action, **kwargs):
        try:
            if action == "turn_on":
                logging.info(f"Turning on light '{self.device_name}' (ID: {self.device_id})")
            elif action == "turn_off":
                logging.info(f"Turning off light '{self.device_name}' (ID: {self.device_id})")
            elif action == "set_brightness":
                brightness = kwargs.get("brightness", 100)
                logging.info(f"Setting brightness of '{self.device_name}' (ID: {self.device_id}) to {brightness}%")
            else:
                logging.error(f"Invalid action '{action}' for light '{self.device_name}'")
        except Exception as e:
            logging.error(f"Error while performing action '{action}' on light '{self.device_name}': {e}")


class SmartThermostat(SmartDevice):
    """
    Class for smart thermostats.
    """
    def perform_action(self, action, **kwargs):
        try:
            if action == "set_temperature":
                temperature = kwargs.get("temperature", 22)
                logging.info(f"Setting temperature of thermostat '{self.device_name}' (ID: {self.device_id}) to {temperature}°C")
            elif action == "turn_off":
                logging.info(f"Turning off thermostat '{self.device_name}' (ID: {self.device_id})")
            else:
                logging.error(f"Invalid action '{action}' for thermostat '{self.device_name}'")
        except Exception as e:
            logging.error(f"Error while performing action '{action}' on thermostat '{self.device_name}': {e}")


class SmartCamera(SmartDevice):
    """
    Class for smart security cameras.
    """
    def perform_action(self, action, **kwargs):
        try:
            if action == "start_recording":
                logging.info(f"Starting recording on camera '{self.device_name}' (ID: {self.device_id})")
            elif action == "stop_recording":
                logging.info(f"Stopping recording on camera '{self.device_name}' (ID: {self.device_id})")
            elif action == "capture_image":
                logging.info(f"Capturing image from camera '{self.device_name}' (ID: {self.device_id})")
            else:
                logging.error(f"Invalid action '{action}' for camera '{self.device_name}'")
        except Exception as e:
            logging.error(f"Error while performing action '{action}' on camera '{self.device_name}': {e}")


# Helper function to control devices
def control_device(device, action, **kwargs):
    """
    Controls a specific device by performing an action.
    :param device: Instance of SmartDevice (or subclass).
    :param action: Action string (e.g., "turn_on", "set_temperature").
    :param kwargs: Additional parameters for the action.
    """
    try:
        device.perform_action(action, **kwargs)
    except Exception as e:
        logging.error(f"Failed to control device '{device.device_name}': {e}")


# Example usage
if __name__ == "__main__":
    # Create instances of smart devices
    living_room_light = SmartLight(device_id="light_001", device_name="Living Room Light")
    bedroom_thermostat = SmartThermostat(device_id="thermo_001", device_name="Bedroom Thermostat")
    front_door_camera = SmartCamera(device_id="camera_001", device_name="Front Door Camera")

    # Control devices
    control_device(living_room_light, "turn_on")
    control_device(living_room_light, "set_brightness", brightness=75)
    control_device(bedroom_thermostat, "set_temperature", temperature=20)
    control_device(front_door_camera, "capture_image")
```
