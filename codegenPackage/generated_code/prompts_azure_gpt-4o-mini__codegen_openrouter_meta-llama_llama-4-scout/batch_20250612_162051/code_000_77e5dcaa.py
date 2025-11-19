"""
Generated Code Metadata:
========================
Original URL: https://vigilanciadomotica.es
Prompt: Write a Python script that integrates smart home devices for enhanced security and automation, as discussed in the "Dispositivos de Hogar Inteligente" section.
Generated: DETERMINISTIC_77e5dcaae3ff164c
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# smart_home_integration.py

import logging
import time
from typing import Dict, List

# Set up logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class SmartDevice:
    """Base class for smart home devices."""

    def __init__(self, device_id: str, device_name: str):
        """
        Initialize a smart device.

        Args:
        - device_id (str): Unique identifier for the device.
        - device_name (str): Human-readable name for the device.
        """
        self.device_id = device_id
        self.device_name = device_name

    def turn_on(self):
        """Turn on the device."""
        logging.info(f"Turning on {self.device_name} ({self.device_id})")

    def turn_off(self):
        """Turn off the device."""
        logging.info(f"Turning off {self.device_name} ({self.device_id})")


class SecurityCamera(SmartDevice):
    """Class for security cameras."""

    def __init__(self, device_id: str, device_name: str, resolution: str):
        """
        Initialize a security camera.

        Args:
        - device_id (str): Unique identifier for the camera.
        - device_name (str): Human-readable name for the camera.
        - resolution (str): Camera resolution (e.g., 1080p, 4K).
        """
        super().__init__(device_id, device_name)
        self.resolution = resolution

    def start_recording(self):
        """Start recording video."""
        logging.info(f"Starting recording on {self.device_name} ({self.device_id}) at {self.resolution}")

    def stop_recording(self):
        """Stop recording video."""
        logging.info(f"Stopping recording on {self.device_name} ({self.device_id})")


class SmartLock(SmartDevice):
    """Class for smart locks."""

    def __init__(self, device_id: str, device_name: str, lock_status: bool = False):
        """
        Initialize a smart lock.

        Args:
        - device_id (str): Unique identifier for the lock.
        - device_name (str): Human-readable name for the lock.
        - lock_status (bool): Initial lock status (default: False, i.e., unlocked).
        """
        super().__init__(device_id, device_name)
        self.lock_status = lock_status

    def lock(self):
        """Lock the door."""
        if not self.lock_status:
            self.lock_status = True
            logging.info(f"Locking {self.device_name} ({self.device_id})")
        else:
            logging.info(f"{self.device_name} ({self.device_id}) is already locked")

    def unlock(self):
        """Unlock the door."""
        if self.lock_status:
            self.lock_status = False
            logging.info(f"Unlocking {self.device_name} ({self.device_id})")
        else:
            logging.info(f"{self.device_name} ({self.device_id}) is already unlocked")


class SmartHomeSystem:
    """Class for integrating smart home devices."""

    def __init__(self):
        self.devices: Dict[str, SmartDevice] = {}

    def add_device(self, device: SmartDevice):
        """
        Add a smart device to the system.

        Args:
        - device (SmartDevice): Device to add.
        """
        self.devices[device.device_id] = device
        logging.info(f"Added {device.device_name} ({device.device_id}) to the smart home system")

    def remove_device(self, device_id: str):
        """
        Remove a smart device from the system.

        Args:
        - device_id (str): ID of the device to remove.
        """
        if device_id in self.devices:
            del self.devices[device_id]
            logging.info(f"Removed device with ID {device_id} from the smart home system")
        else:
            logging.warning(f"Device with ID {device_id} not found in the smart home system")

    def turn_on_all_devices(self):
        """Turn on all devices in the system."""
        for device in self.devices.values():
            device.turn_on()

    def turn_off_all_devices(self):
        """Turn off all devices in the system."""
        for device in self.devices.values():
            device.turn_off()


def main():
    # Create smart home system
    smart_home = SmartHomeSystem()

    # Create devices
    camera = SecurityCamera("CAM-001", "Living Room Camera", "1080p")
    lock = SmartLock("LCK-001", "Front Door Lock")

    # Add devices to the system
    smart_home.add_device(camera)
    smart_home.add_device(lock)

    # Turn on all devices
    smart_home.turn_on_all_devices()

    # Start recording on camera
    camera.start_recording()

    # Lock the door
    lock.lock()

    # Wait for 5 seconds
    time.sleep(5)

    # Stop recording on camera
    camera.stop_recording()

    # Unlock the door
    lock.unlock()

    # Turn off all devices
    smart_home.turn_off_all_devices()

    # Remove devices from the system
    smart_home.remove_device("CAM-001")
    smart_home.remove_device("LCK-001")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        logging.error(f"An error occurred: {e}")
```
