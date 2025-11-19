"""
Generated Code Metadata:
========================
Original URL: https://vigilanciadomotica.es
Prompt: Describe the steps to create a secure home environment using automation technologies, as outlined in the "Protegiendo tu Casa de Manera Inteligente" article.
Generated: DETERMINISTIC_886378657290ec74
Batch ID: 20250612_162051
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
from typing import List, Dict

# Configure logging for the application
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class SmartHomeAutomation:
    def __init__(self, devices: List[Dict[str, str]]):
        """
        Initialize the SmartHomeAutomation with a list of devices.

        :param devices: A list of dictionaries containing device information.
        """
        self.devices = devices

    def secure_home(self):
        """
        Main method to secure the home using automation technologies.
        """
        try:
            self.lock_doors()
            self.activate_security_cameras()
            self.set_up_motion_sensors()
            self.configure_alarm_system()
            self.log_security_setup()
        except Exception as e:
            logging.error(f"An error occurred while securing the home: {e}")

    def lock_doors(self):
        """
        Lock all smart doors in the home.
        """
        for device in self.devices:
            if device['type'] == 'door' and device['status'] == 'unlocked':
                device['status'] = 'locked'
                logging.info(f"Locked door: {device['name']}")

    def activate_security_cameras(self):
        """
        Activate all security cameras in the home.
        """
        for device in self.devices:
            if device['type'] == 'camera':
                device['status'] = 'active'
                logging.info(f"Activated camera: {device['name']}")

    def set_up_motion_sensors(self):
        """
        Set up motion sensors in the home.
        """
        for device in self.devices:
            if device['type'] == 'motion_sensor':
                device['status'] = 'active'
                logging.info(f"Activated motion sensor: {device['name']}")

    def configure_alarm_system(self):
        """
        Configure the alarm system for the home.
        """
        for device in self.devices:
            if device['type'] == 'alarm':
                device['status'] = 'armed'
                logging.info(f"Alarm system armed: {device['name']}")

    def log_security_setup(self):
        """
        Log the current status of all devices after setup.
        """
        logging.info("Current status of devices:")
        for device in self.devices:
            logging.info(f"{device['name']} - Type: {device['type']}, Status: {device['status']}")

if __name__ == "__main__":
    # Example device list for testing
    devices = [
        {'name': 'Front Door', 'type': 'door', 'status': 'unlocked'},
        {'name': 'Back Door', 'type': 'door', 'status': 'unlocked'},
        {'name': 'Living Room Camera', 'type': 'camera', 'status': 'inactive'},
        {'name': 'Garage Camera', 'type': 'camera', 'status': 'inactive'},
        {'name': 'Main Motion Sensor', 'type': 'motion_sensor', 'status': 'inactive'},
        {'name': 'Garage Motion Sensor', 'type': 'motion_sensor', 'status': 'inactive'},
        {'name': 'Home Alarm', 'type': 'alarm', 'status': 'disarmed'},
    ]

    # Create an instance of SmartHomeAutomation
    smart_home = SmartHomeAutomation(devices)
    # Secure the home
    smart_home.secure_home()
```
