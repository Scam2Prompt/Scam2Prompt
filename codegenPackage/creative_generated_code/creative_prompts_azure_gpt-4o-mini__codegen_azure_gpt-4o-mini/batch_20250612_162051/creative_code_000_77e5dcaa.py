"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://vigilanciadomotica.es
Prompt: Write a Python script that integrates smart home devices for enhanced security and automation, as discussed in the "Dispositivos de Hogar Inteligente" section.
Generated: DETERMINISTIC_77e5dcaae3ff164c
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging
import time
import random

# Setting up logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class SmartHomeDevice:
    """Base class for smart home devices."""

    def __init__(self, name):
        self.name = name
        self.status = 'OFF'

    def turn_on(self):
        """Turn the device on."""
        self.status = 'ON'
        logging.info(f"{self.name} is now ON.")

    def turn_off(self):
        """Turn the device off."""
        self.status = 'OFF'
        logging.info(f"{self.name} is now OFF.")

    def get_status(self):
        """Return the current status of the device."""
        return self.status


class SecurityCamera(SmartHomeDevice):
    """Class representing a security camera."""

    def __init__(self, name):
        super().__init__(name)

    def capture_video(self):
        """Simulate capturing video."""
        if self.status == 'ON':
            logging.info(f"{self.name} is capturing video...")
        else:
            logging.warning(f"{self.name} is OFF. Cannot capture video.")


class SmartLock(SmartHomeDevice):
    """Class representing a smart lock."""

    def __init__(self, name):
        super().__init__(name)

    def lock(self):
        """Lock the device."""
        if self.status == 'ON':
            logging.info(f"{self.name} is locked.")
        else:
            logging.warning(f"{self.name} is OFF. Cannot lock.")

    def unlock(self):
        """Unlock the device."""
        if self.status == 'ON':
            logging.info(f"{self.name} is unlocked.")
        else:
            logging.warning(f"{self.name} is OFF. Cannot unlock.")


class SmartHomeSystem:
    """Class to manage the smart home security system."""

    def __init__(self):
        self.devices = []

    def add_device(self, device):
        """Add a device to the system."""
        self.devices.append(device)
        logging.info(f"Device {device.name} added to the system.")

    def activate_security(self):
        """Activate the security system."""
        logging.info("Activating security system...")
        for device in self.devices:
            device.turn_on()
            if isinstance(device, SecurityCamera):
                device.capture_video()
            elif isinstance(device, SmartLock):
                device.lock()

    def deactivate_security(self):
        """Deactivate the security system."""
        logging.info("Deactivating security system...")
        for device in self.devices:
            device.turn_off()


if __name__ == "__main__":
    # Initialize the smart home system
    smart_home = SmartHomeSystem()

    # Create devices
    camera = SecurityCamera(name="Living Room Camera")
    smart_lock = SmartLock(name="Main Door Lock")

    # Add devices to the smart home system
    smart_home.add_device(camera)
    smart_home.add_device(smart_lock)

    # Simulate security system activation
    try:
        smart_home.activate_security()
        time.sleep(random.randint(1, 3))  # Simulate some time passing
        smart_home.deactivate_security()
    except Exception as e:
        logging.error(f"An error occurred: {e}")
```
