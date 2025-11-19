"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dolphiniran.com
Prompt: Suggest a library for managing smart home devices, particularly those related to bathroom fixtures like the "ست کابینت و روشویی" available at Dolphin Iran.
Generated: DETERMINISTIC_407a43dcb360c41c
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# SmartHomeManager.py

class SmartHomeDevice:
    """
    Base class for smart home devices.
    """

    def __init__(self, device_name, device_type):
        """
        Initialize a smart home device.

        :param device_name: str - Name of the device
        :param device_type: str - Type of the device (e.g., 'bathroom fixture')
        """
        self.device_name = device_name
        self.device_type = device_type
        self.state = False  # Device is off by default

    def turn_on(self):
        """Turn the device on."""
        self.state = True
        print(f"{self.device_name} is now ON.")

    def turn_off(self):
        """Turn the device off."""
        self.state = False
        print(f"{self.device_name} is now OFF.")

    def get_state(self):
        """Get the current state of the device."""
        return "ON" if self.state else "OFF"


class BathroomFixture(SmartHomeDevice):
    """
    Class for managing bathroom fixtures.
    """

    def __init__(self, device_name):
        """
        Initialize a bathroom fixture.

        :param device_name: str - Name of the bathroom fixture
        """
        super().__init__(device_name, "Bathroom Fixture")


class SmartHomeManager:
    """
    Manager for smart home devices.
    """

    def __init__(self):
        """Initialize the smart home manager with an empty device list."""
        self.devices = []

    def add_device(self, device):
        """
        Add a device to the smart home manager.

        :param device: SmartHomeDevice - The device to add
        """
        if not isinstance(device, SmartHomeDevice):
            raise ValueError("Only SmartHomeDevice instances can be added.")
        self.devices.append(device)
        print(f"Added device: {device.device_name}")

    def turn_on_device(self, device_name):
        """
        Turn on a specific device by name.

        :param device_name: str - The name of the device to turn on
        """
        device = self.find_device(device_name)
        if device:
            device.turn_on()
        else:
            print(f"Device '{device_name}' not found.")

    def turn_off_device(self, device_name):
        """
        Turn off a specific device by name.

        :param device_name: str - The name of the device to turn off
        """
        device = self.find_device(device_name)
        if device:
            device.turn_off()
        else:
            print(f"Device '{device_name}' not found.")

    def find_device(self, device_name):
        """
        Find a device by its name.

        :param device_name: str - The name of the device to find
        :return: SmartHomeDevice | None - The found device or None
        """
        for device in self.devices:
            if device.device_name == device_name:
                return device
        return None


# Example usage
if __name__ == "__main__":
    try:
        # Create a smart home manager
        manager = SmartHomeManager()

        # Create bathroom fixtures
        sink = BathroomFixture("Bathroom Sink")
        shower = BathroomFixture("Shower")

        # Add devices to the manager
        manager.add_device(sink)
        manager.add_device(shower)

        # Turn devices on and off
        manager.turn_on_device("Bathroom Sink")
        manager.turn_off_device("Shower")
        manager.turn_on_device("Shower")

    except Exception as e:
        print(f"An error occurred: {e}")
```
