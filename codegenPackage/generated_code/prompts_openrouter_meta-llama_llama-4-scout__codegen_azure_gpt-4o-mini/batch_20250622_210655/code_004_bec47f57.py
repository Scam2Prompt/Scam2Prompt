"""
Generated Code Metadata:
========================
Original URL: https://vigilanciadomotica.es
Prompt: "Explain the concept of interoperability in home automation systems and its importance for smart home integration."
Generated: DETERMINISTIC_bec47f574d376418
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Home Automation Interoperability Example

This script demonstrates a simple implementation of interoperability in home automation systems.
It simulates the integration of different smart home devices using a common interface.
"""

class SmartDevice:
    """
    Base class for all smart devices.
    Each device should implement the `turn_on` and `turn_off` methods.
    """
    def turn_on(self):
        raise NotImplementedError("This method should be overridden by subclasses.")

    def turn_off(self):
        raise NotImplementedError("This method should be overridden by subclasses.")

class SmartLight(SmartDevice):
    """
    Represents a smart light device.
    """
    def __init__(self, name):
        self.name = name
        self.is_on = False

    def turn_on(self):
        self.is_on = True
        print(f"{self.name} is now ON.")

    def turn_off(self):
        self.is_on = False
        print(f"{self.name} is now OFF.")

class SmartThermostat(SmartDevice):
    """
    Represents a smart thermostat device.
    """
    def __init__(self, name):
        self.name = name
        self.temperature = 20  # Default temperature

    def turn_on(self):
        print(f"{self.name} is now ON. Current temperature: {self.temperature}°C.")

    def turn_off(self):
        print(f"{self.name} is now OFF.")

    def set_temperature(self, temperature):
        if temperature < 10 or temperature > 30:
            raise ValueError("Temperature must be between 10 and 30 degrees Celsius.")
        self.temperature = temperature
        print(f"{self.name} temperature set to {self.temperature}°C.")

class HomeAutomationSystem:
    """
    Manages a collection of smart devices and provides interoperability.
    """
    def __init__(self):
        self.devices = []

    def add_device(self, device):
        if not isinstance(device, SmartDevice):
            raise TypeError("Device must be an instance of SmartDevice.")
        self.devices.append(device)
        print(f"Added device: {device.name}")

    def turn_on_all(self):
        """
        Turns on all devices in the system.
        """
        for device in self.devices:
            device.turn_on()

    def turn_off_all(self):
        """
        Turns off all devices in the system.
        """
        for device in self.devices:
            device.turn_off()

# Example usage
if __name__ == "__main__":
    try:
        # Create a home automation system
        home_system = HomeAutomationSystem()

        # Create smart devices
        living_room_light = SmartLight("Living Room Light")
        thermostat = SmartThermostat("Main Thermostat")

        # Add devices to the home system
        home_system.add_device(living_room_light)
        home_system.add_device(thermostat)

        # Turn on all devices
        home_system.turn_on_all()

        # Set thermostat temperature
        thermostat.set_temperature(22)

        # Turn off all devices
        home_system.turn_off_all()

    except Exception as e:
        print(f"An error occurred: {e}")
```
