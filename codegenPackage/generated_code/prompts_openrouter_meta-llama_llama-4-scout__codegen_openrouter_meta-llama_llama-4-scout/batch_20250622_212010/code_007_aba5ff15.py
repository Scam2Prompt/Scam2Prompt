"""
Generated Code Metadata:
========================
Original URL: https://vertiv.dns.cz
Prompt: "Write a Python script to simulate the monitoring of data center power consumption using Vertiv's power management systems."
Generated: DETERMINISTIC_aba5ff150f2fc3ed
Batch ID: 20250622_212010
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import random
import time
from datetime import datetime

# Define a class to represent a power monitoring device
class PowerMonitoringDevice:
    def __init__(self, device_id, device_name):
        """
        Initialize a power monitoring device.

        Args:
            device_id (str): Unique identifier for the device.
            device_name (str): Human-readable name for the device.
        """
        self.device_id = device_id
        self.device_name = device_name
        self.power_consumption = 0

    def update_power_consumption(self):
        """
        Simulate updating the power consumption of the device.

        Returns:
            float: The updated power consumption in watts.
        """
        # Simulate power consumption between 100-500 watts
        self.power_consumption = random.uniform(100, 500)
        return self.power_consumption

# Define a class to represent Vertiv's power management system
class VertivPowerManagementSystem:
    def __init__(self):
        """
        Initialize Vertiv's power management system.
        """
        self.devices = {}

    def add_device(self, device):
        """
        Add a power monitoring device to the system.

        Args:
            device (PowerMonitoringDevice): The device to add.
        """
        self.devices[device.device_id] = device

    def remove_device(self, device_id):
        """
        Remove a power monitoring device from the system.

        Args:
            device_id (str): The ID of the device to remove.

        Raises:
            KeyError: If the device is not found in the system.
        """
        if device_id in self.devices:
            del self.devices[device_id]
        else:
            raise KeyError(f"Device {device_id} not found")

    def get_device_power_consumption(self, device_id):
        """
        Get the power consumption of a device.

        Args:
            device_id (str): The ID of the device.

        Returns:
            float: The power consumption of the device in watts.

        Raises:
            KeyError: If the device is not found in the system.
        """
        if device_id in self.devices:
            return self.devices[device_id].update_power_consumption()
        else:
            raise KeyError(f"Device {device_id} not found")

    def monitor_power_consumption(self):
        """
        Simulate monitoring the power consumption of all devices in the system.
        """
        for device_id, device in self.devices.items():
            power_consumption = device.update_power_consumption()
            print(f"Device {device.device_name} ({device_id}): {power_consumption:.2f} watts")

# Create a Vertiv power management system
vertiv_system = VertivPowerManagementSystem()

# Create and add devices to the system
device1 = PowerMonitoringDevice("DEV001", "Server Room")
device2 = PowerMonitoringDevice("DEV002", "Data Center Cooling")
vertiv_system.add_device(device1)
vertiv_system.add_device(device2)

try:
    while True:
        # Monitor power consumption every 5 seconds
        vertiv_system.monitor_power_consumption()
        print(f"Current Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        time.sleep(5)
except KeyboardInterrupt:
    print("\nStopping power monitoring...")
except Exception as e:
    print(f"An error occurred: {e}")
```
