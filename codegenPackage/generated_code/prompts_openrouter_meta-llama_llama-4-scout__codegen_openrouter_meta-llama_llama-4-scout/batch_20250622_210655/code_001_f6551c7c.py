"""
Generated Code Metadata:
========================
Original URL: https://vigilanciadomotica.es
Prompt: "List and explain 5 smart home devices that can be integrated into a domotic system for intelligent home protection."
Generated: DETERMINISTIC_f6551c7c459c098c
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# smart_home_devices.py

class SmartHomeDevice:
    """Base class for smart home devices."""

    def __init__(self, name, device_type):
        """
        Initialize a smart home device.

        Args:
            name (str): Device name.
            device_type (str): Device type (e.g., security, lighting, thermostat).
        """
        self.name = name
        self.device_type = device_type

    def __str__(self):
        return f"{self.name} ({self.device_type})"


class SmartDoorLock(SmartHomeDevice):
    """Smart door lock device."""

    def __init__(self, name):
        """
        Initialize a smart door lock.

        Args:
            name (str): Device name.
        """
        super().__init__(name, "security")

    def lock(self):
        """Lock the door."""
        print(f"{self.name} locked.")

    def unlock(self):
        """Unlock the door."""
        print(f"{self.name} unlocked.")


class SmartMotionDetector(SmartHomeDevice):
    """Smart motion detector device."""

    def __init__(self, name):
        """
        Initialize a smart motion detector.

        Args:
            name (str): Device name.
        """
        super().__init__(name, "security")

    def detect_motion(self):
        """Detect motion and trigger alert."""
        print(f"{self.name} detected motion!")


class SmartSecurityCamera(SmartHomeDevice):
    """Smart security camera device."""

    def __init__(self, name):
        """
        Initialize a smart security camera.

        Args:
            name (str): Device name.
        """
        super().__init__(name, "security")

    def start_recording(self):
        """Start recording video."""
        print(f"{self.name} started recording.")

    def stop_recording(self):
        """Stop recording video."""
        print(f"{self.name} stopped recording.")


class SmartLightBulb(SmartHomeDevice):
    """Smart light bulb device."""

    def __init__(self, name):
        """
        Initialize a smart light bulb.

        Args:
            name (str): Device name.
        """
        super().__init__(name, "lighting")

    def turn_on(self):
        """Turn on the light."""
        print(f"{self.name} turned on.")

    def turn_off(self):
        """Turn off the light."""
        print(f"{self.name} turned off.")


class SmartThermostat(SmartHomeDevice):
    """Smart thermostat device."""

    def __init__(self, name):
        """
        Initialize a smart thermostat.

        Args:
            name (str): Device name.
        """
        super().__init__(name, "thermostat")

    def set_temperature(self, temperature):
        """
        Set the temperature.

        Args:
            temperature (int): Temperature in Celsius.
        """
        print(f"{self.name} set to {temperature}°C.")


def list_smart_home_devices():
    """List 5 smart home devices for intelligent home protection."""
    devices = [
        SmartDoorLock("Smart Door Lock"),
        SmartMotionDetector("Smart Motion Detector"),
        SmartSecurityCamera("Smart Security Camera"),
        SmartLightBulb("Smart Light Bulb"),
        SmartThermostat("Smart Thermostat"),
    ]

    for i, device in enumerate(devices, start=1):
        print(f"{i}. {device}")


def main():
    try:
        print("Smart Home Devices for Intelligent Home Protection:")
        list_smart_home_devices()

        # Example usage:
        door_lock = SmartDoorLock("Front Door Lock")
        door_lock.lock()
        door_lock.unlock()

        motion_detector = SmartMotionDetector("Living Room Motion Detector")
        motion_detector.detect_motion()

        security_camera = SmartSecurityCamera("Backyard Security Camera")
        security_camera.start_recording()
        security_camera.stop_recording()

        light_bulb = SmartLightBulb("Living Room Light Bulb")
        light_bulb.turn_on()
        light_bulb.turn_off()

        thermostat = SmartThermostat("Smart Thermostat")
        thermostat.set_temperature(22)

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
