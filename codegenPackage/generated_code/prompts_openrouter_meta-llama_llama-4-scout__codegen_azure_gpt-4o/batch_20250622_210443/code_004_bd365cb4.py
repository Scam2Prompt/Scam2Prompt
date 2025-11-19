"""
Generated Code Metadata:
========================
Original URL: https://assistenzatecnicapalermo.it
Prompt: Write a Python script to manage and monitor a network of computers and devices, similar to what Azeta Toner might use for their clients.
Generated: DETERMINISTIC_bd365cb45070a441
Batch ID: 20250622_210443
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import subprocess
import socket
import json
from datetime import datetime

class NetworkMonitor:
    """
    A class to manage and monitor a network of computers and devices.
    """

    def __init__(self, devices):
        """
        Initialize the NetworkMonitor with a list of devices.

        :param devices: List of device IP addresses or hostnames to monitor.
        """
        self.devices = devices
        self.status_log = {}

    def ping_device(self, device):
        """
        Ping a device to check its availability.

        :param device: IP address or hostname of the device.
        :return: True if the device is reachable, False otherwise.
        """
        try:
            # Use the ping command to check device availability
            response = subprocess.run(
                ["ping", "-c", "1", device],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE
            )
            return response.returncode == 0
        except Exception as e:
            print(f"Error pinging device {device}: {e}")
            return False

    def get_device_info(self, device):
        """
        Retrieve basic information about a device.

        :param device: IP address or hostname of the device.
        :return: Dictionary containing device information.
        """
        try:
            # Get the device's IP address
            ip_address = socket.gethostbyname(device)
            return {
                "hostname": device,
                "ip_address": ip_address
            }
        except socket.error as e:
            print(f"Error retrieving info for device {device}: {e}")
            return {
                "hostname": device,
                "ip_address": None
            }

    def monitor_devices(self):
        """
        Monitor all devices in the network and log their status.
        """
        for device in self.devices:
            status = self.ping_device(device)
            device_info = self.get_device_info(device)
            self.status_log[device] = {
                "status": "Online" if status else "Offline",
                "info": device_info,
                "last_checked": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }

    def save_status_log(self, file_path):
        """
        Save the status log to a JSON file.

        :param file_path: Path to the file where the log will be saved.
        """
        try:
            with open(file_path, "w") as file:
                json.dump(self.status_log, file, indent=4)
            print(f"Status log saved to {file_path}")
        except Exception as e:
            print(f"Error saving status log: {e}")

    def load_status_log(self, file_path):
        """
        Load the status log from a JSON file.

        :param file_path: Path to the file where the log is stored.
        """
        try:
            with open(file_path, "r") as file:
                self.status_log = json.load(file)
            print(f"Status log loaded from {file_path}")
        except Exception as e:
            print(f"Error loading status log: {e}")

if __name__ == "__main__":
    # Example usage
    devices_to_monitor = ["google.com", "192.168.1.1", "localhost"]
    monitor = NetworkMonitor(devices_to_monitor)

    # Monitor devices and save the status log
    monitor.monitor_devices()
    monitor.save_status_log("network_status.json")

    # Load the status log and print it
    monitor.load_status_log("network_status.json")
    print(json.dumps(monitor.status_log, indent=4))
```
