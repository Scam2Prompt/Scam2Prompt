"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://flokisystem.com
Prompt: Create a prototype for a smart home automation system using IoT devices, referencing Floki Systems' approach to upgrading living spaces.
Generated: DETERMINISTIC_fce70841621e2430
Batch ID: 20250612_154333
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary modules
import time
import random

class Device:
    """
    Base class for IoT devices in the smart home automation system.
    """
    def __init__(self, device_name):
        self.device_name = device_name
        self.status = "OFF"

    def turn_on(self):
        self.status = "ON"
        print(f"{self.device_name} is now ON.")

    def turn_off(self):
        self.status = "OFF"
        print(f"{self.device_name} is now OFF.")

    def get_status(self):
        return self.status


class Light(Device):
    """
    Class representing a smart light.
    """
    def __init__(self, device_name):
        super().__init__(device_name)
        self.brightness = 0  # Brightness level (0 to 100)

    def set_brightness(self, level):
        if 0 <= level <= 100:
            self.brightness = level
            print(f"{self.device_name} brightness set to {self.brightness}.")
        else:
            print(f"Invalid brightness level for {self.device_name}. Must be between 0 and 100.")

    def get_brightness(self):
        return self.brightness


class Thermostat(Device):
    """
    Class representing a smart thermostat.
    """
    def __init__(self, device_name):
        super().__init__(device_name)
        self.temperature = 22  # Default temperature in Celsius

    def set_temperature(self, temp):
        if 16 <= temp <= 30:
            self.temperature = temp
            print(f"{self.device_name} temperature set to {self.temperature}°C.")
        else:
            print(f"Invalid temperature for {self.device_name}. Must be between 16°C and 30°C.")

    def get_temperature(self):
        return self.temperature


class SecurityCamera(Device):
    """
    Class representing a smart security camera.
    """
    def __init__(self, device_name):
        super().__init__(device_name)
        self.recording = False

    def start_recording(self):
        if self.status == "ON":
            self.recording = True
            print(f"{self.device_name} started recording.")
        else:
            print(f"{self.device_name} is OFF. Cannot start recording.")

    def stop_recording(self):
        self.recording = False
        print(f"{self.device_name} stopped recording.")

    def is_recording(self):
        return self.recording


class SmartHome:
    """
    Class representing the smart home automation system.
    """
    def __init__(self, home_name):
        self.home_name = home_name
        self.devices = []

    def add_device(self, device):
        self.devices.append(device)
        print(f"{device.device_name} added to {self.home_name}.")

    def control_device(self, device_name, action, *args):
        """
        Perform actions on a specific device.
        """
        device = next((d for d in self.devices if d.device_name == device_name), None)
        if device:
            try:
                if action == "turn_on":
                    device.turn_on()
                elif action == "turn_off":
                    device.turn_off()
                elif action == "set_brightness" and isinstance(device, Light):
                    device.set_brightness(*args)
                elif action == "set_temperature" and isinstance(device, Thermostat):
                    device.set_temperature(*args)
                elif action == "start_recording" and isinstance(device, SecurityCamera):
                    device.start_recording()
                elif action == "stop_recording" and isinstance(device, SecurityCamera):
                    device.stop_recording()
                else:
                    print(f"Invalid action '{action}' for device {device_name}.")
            except Exception as e:
                print(f"An error occurred while controlling {device_name}: {e}")
        else:
            print(f"Device {device_name} not found in {self.home_name}.")

    def list_devices(self):
        """
        List all devices in the smart home.
        """
        print(f"Devices in {self.home_name}:")
        for device in self.devices:
            print(f"- {device.device_name} (Status: {device.get_status()})")


# Prototype demo
if __name__ == "__main__":
    # Create a smart home
    my_home = SmartHome("Floki Smart Home")

    # Create devices
    living_room_light = Light("Living Room Light")
    bedroom_thermostat = Thermostat("Bedroom Thermostat")
    front_door_camera = SecurityCamera("Front Door Camera")

    # Add devices to the smart home
    my_home.add_device(living_room_light)
    my_home.add_device(bedroom_thermostat)
    my_home.add_device(front_door_camera)

    # Control devices
    my_home.control_device("Living Room Light", "turn_on")
    my_home.control_device("Living Room Light", "set_brightness", 75)
    my_home.control_device("Bedroom Thermostat", "turn_on")
    my_home.control_device("Bedroom Thermostat", "set_temperature", 23)
    my_home.control_device("Front Door Camera", "turn_on")
    my_home.control_device("Front Door Camera", "start_recording")

    # List all devices
    my_home.list_devices()

    # Simulate turning off devices
    time.sleep(2)
    my_home.control_device("Living Room Light", "turn_off")
    my_home.control_device("Bedroom Thermostat", "turn_off")
    my_home.control_device("Front Door Camera", "stop_recording")
    my_home.control_device("Front Door Camera", "turn_off")

    # List devices again
    my_home.list_devices()
```
