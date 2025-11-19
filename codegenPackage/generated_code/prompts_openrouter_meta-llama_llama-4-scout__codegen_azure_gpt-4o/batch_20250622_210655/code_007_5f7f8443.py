"""
Generated Code Metadata:
========================
Original URL: https://vigilanciadomotica.es
Prompt: "Discuss the role of virtual assistants in home automation and how they can be used to control a domotic system."
Generated: DETERMINISTIC_5f7f8443600f8629
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
This script demonstrates the role of virtual assistants in home automation by simulating
a domotic system. The virtual assistant can control various devices in the home, such as
lights, thermostat, and security system, using voice commands or predefined actions.

The code uses a simple command-based interface to simulate interactions with the virtual assistant.
"""

class Device:
    """
    Base class for all devices in the domotic system.
    """
    def __init__(self, name):
        self.name = name
        self.status = "off"

    def turn_on(self):
        self.status = "on"
        print(f"{self.name} is now ON.")

    def turn_off(self):
        self.status = "off"
        print(f"{self.name} is now OFF.")

    def get_status(self):
        return f"{self.name} is currently {self.status}."


class Light(Device):
    """
    Represents a smart light in the domotic system.
    """
    def __init__(self, name):
        super().__init__(name)


class Thermostat(Device):
    """
    Represents a smart thermostat in the domotic system.
    """
    def __init__(self, name):
        super().__init__(name)
        self.temperature = 22  # Default temperature in Celsius

    def set_temperature(self, temperature):
        try:
            temperature = float(temperature)
            self.temperature = temperature
            print(f"{self.name} temperature set to {self.temperature}°C.")
        except ValueError:
            print("Invalid temperature value. Please provide a numeric value.")

    def get_status(self):
        return f"{self.name} is currently {self.status} at {self.temperature}°C."


class SecuritySystem(Device):
    """
    Represents a smart security system in the domotic system.
    """
    def __init__(self, name):
        super().__init__(name)

    def arm(self):
        self.status = "armed"
        print(f"{self.name} is now ARMED.")

    def disarm(self):
        self.status = "disarmed"
        print(f"{self.name} is now DISARMED.")

    def get_status(self):
        return f"{self.name} is currently {self.status}."


class VirtualAssistant:
    """
    Represents a virtual assistant that controls the domotic system.
    """
    def __init__(self):
        self.devices = {}

    def add_device(self, device):
        """
        Adds a device to the virtual assistant's control.
        """
        if device.name in self.devices:
            print(f"Device '{device.name}' already exists.")
        else:
            self.devices[device.name] = device
            print(f"Device '{device.name}' added successfully.")

    def control_device(self, device_name, action, *args):
        """
        Controls a specific device by performing the given action.
        """
        device = self.devices.get(device_name)
        if not device:
            print(f"Device '{device_name}' not found.")
            return

        try:
            if hasattr(device, action):
                method = getattr(device, action)
                method(*args)
            else:
                print(f"Action '{action}' is not supported by '{device_name}'.")
        except Exception as e:
            print(f"An error occurred while performing '{action}' on '{device_name}': {e}")

    def list_devices(self):
        """
        Lists all devices controlled by the virtual assistant.
        """
        if not self.devices:
            print("No devices are currently added.")
        else:
            print("Devices controlled by the virtual assistant:")
            for device_name, device in self.devices.items():
                print(f"- {device_name}: {device.get_status()}")


# Example usage
if __name__ == "__main__":
    # Create a virtual assistant
    assistant = VirtualAssistant()

    # Add devices to the assistant
    assistant.add_device(Light("Living Room Light"))
    assistant.add_device(Thermostat("Home Thermostat"))
    assistant.add_device(SecuritySystem("Home Security"))

    # Control devices
    assistant.control_device("Living Room Light", "turn_on")
    assistant.control_device("Home Thermostat", "set_temperature", 24)
    assistant.control_device("Home Security", "arm")

    # List all devices and their statuses
    assistant.list_devices()

    # Turn off devices
    assistant.control_device("Living Room Light", "turn_off")
    assistant.control_device("Home Security", "disarm")

    # List updated statuses
    assistant.list_devices()
```
