"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://payeshnirooco.com
Prompt: Provide a step-by-step guide or code for implementing smart distribution panels with BMS (Building Management Systems) capabilities, as mentioned in پایش نیرو's offerings.
Generated: DETERMINISTIC_087b9f1be772a519
Batch ID: 20250612_153517
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is Python code for implementing a basic simulation of smart distribution panels with Building Management System (BMS) capabilities. This code focuses on monitoring energy consumption, controlling connected devices, and reporting status via logging.

```python
import logging
from datetime import datetime
import random

# Configure logging for monitoring system events
logging.basicConfig(
    filename="smart_panel.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

class SmartDistributionPanel:
    """
    A class that represents a Smart Distribution Panel with BMS capabilities.
    """

    def __init__(self):
        """
        Initialize the Smart Distribution Panel with connected devices and default settings.
        """
        self.devices = {}  # Stores devices and their statuses
        self.energy_consumption_logs = {}  # Stores energy consumption data by device

    def add_device(self, device_name: str, max_power: float):
        """
        Add a device to the panel.

        Args:
            device_name (str): Name of the device.
            max_power (float): Maximum power the device can consume in kW.

        Raises:
            ValueError: If the device name already exists.
        """
        if device_name in self.devices:
            raise ValueError(f"Device '{device_name}' already exists in the panel.")
        
        self.devices[device_name] = {
            "status": "OFF",  # Status can be 'ON' or 'OFF'
            "max_power": max_power,  # Maximum power consumption in kW
            "current_power": 0.0,  # Current power consumption in kW
        }
        self.energy_consumption_logs[device_name] = []
        logging.info(f"Device '{device_name}' added to panel.")

    def control_device(self, device_name: str, action: str):
        """
        Control a device by turning it ON or OFF.

        Args:
            device_name (str): Name of the device.
            action (str): Action to perform ('ON' or 'OFF').

        Raises:
            ValueError: If the device does not exist or the action is invalid.
        """
        if device_name not in self.devices:
            raise ValueError(f"Device '{device_name}' is not found in the panel.")
        if action not in ["ON", "OFF"]:
            raise ValueError("Action must be 'ON' or 'OFF'.")
        
        self.devices[device_name]["status"] = action

        if action == "ON":
            # Simulate random power usage for the device within its max range
            power_usage = round(random.uniform(0.1, self.devices[device_name]["max_power"]), 2)
            self.devices[device_name]["current_power"] = power_usage
            self.log_energy_consumption(device_name, power_usage)
            logging.info(f"Device '{device_name}' turned ON. Power usage: {power_usage} kW.")
        else:
            self.devices[device_name]["current_power"] = 0.0
            logging.info(f"Device '{device_name}' turned OFF.")

    def log_energy_consumption(self, device_name: str, power_usage: float):
        """
        Log energy consumption for a device.

        Args:
            device_name (str): Name of the device.
            power_usage (float): Power consumed in kW.
        """
        timestamp = datetime.now().isoformat()
        self.energy_consumption_logs[device_name].append({"timestamp": timestamp, "power_usage": power_usage})
    
    def generate_report(self):
        """
        Generate a report of the energy usage for all devices.

        Returns:
            dict: Energy usage data for all devices.
        """
        report = {}
        for device, logs in self.energy_consumption_logs.items():
            total_energy = sum(log["power_usage"] for log in logs)
            report[device] = {"total_energy_kWh": round(total_energy, 2), "usage_logs": logs}
        return report

    def print_status(self):
        """
        Print the current status of all connected devices.
        """
        for device_name, status in self.devices.items():
            print(f"Device: {device_name}, Status: {status['status']}, Current Power: {status['current_power']} kW")

# Example usage
if __name__ == "__main__":
    try:
        # Initialize the smart distribution panel
        panel = SmartDistributionPanel()

        # Add devices to the panel
        panel.add_device("HVAC System", 15.0)
        panel.add_device("Lighting System", 5.0)
        panel.add_device("Elevator System", 20.0)

        # Control devices
        panel.control_device("HVAC System", "ON")
        panel.control_device("Lighting System", "ON")
        panel.control_device("Elevator System", "OFF")

        # Print current status
        panel.print_status()

        # Generate and print energy usage report
        report = panel.generate_report()
        for device, data in report.items():
            print(f"Device: {device}, Total Energy Usage: {data['total_energy_kWh']} kWh")

    except Exception as e:
        logging.error(f"Error occurred: {e}")
        print(f"An error occurred: {e}")
```
This script simulates basic BMS functions in a smart distribution panel. It includes device management, energy monitoring, error handling, and logging capabilities.
