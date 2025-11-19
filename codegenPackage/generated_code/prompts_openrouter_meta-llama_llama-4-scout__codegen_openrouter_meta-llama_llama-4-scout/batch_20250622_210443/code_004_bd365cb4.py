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
# network_monitor.py

import os
import socket
import psutil
import logging
from datetime import datetime

# Set up logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class NetworkDevice:
    """Represents a network device with its properties and status."""

    def __init__(self, ip_address):
        self.ip_address = ip_address
        self.hostname = None
        self.os = None
        self.cpu_usage = None
        self.memory_usage = None

    def get_hostname(self):
        """Retrieve the hostname of the device."""
        try:
            self.hostname = socket.gethostname(self.ip_address)
        except socket.error as e:
            logging.error(f"Failed to retrieve hostname for {self.ip_address}: {e}")

    def get_os(self):
        """Retrieve the operating system of the device."""
        try:
            # This is a simple implementation and might not work for all devices
            self.os = self.get_system_info()['platform']
        except Exception as e:
            logging.error(f"Failed to retrieve OS for {self.ip_address}: {e}")

    def get_system_info(self):
        """Retrieve system information using psutil."""
        try:
            # This will only work if the device is accessible via SSH or has psutil installed
            # For simplicity, let's assume we have a way to execute commands remotely
            # For production, consider using a library like paramiko for SSH access
            return psutil.os_info()
        except Exception as e:
            logging.error(f"Failed to retrieve system info for {self.ip_address}: {e}")

    def get_cpu_usage(self):
        """Retrieve the current CPU usage of the device."""
        try:
            # This will only work if the device is accessible via SSH or has psutil installed
            self.cpu_usage = psutil.cpu_percent()
        except Exception as e:
            logging.error(f"Failed to retrieve CPU usage for {self.ip_address}: {e}")

    def get_memory_usage(self):
        """Retrieve the current memory usage of the device."""
        try:
            # This will only work if the device is accessible via SSH or has psutil installed
            self.memory_usage = psutil.virtual_memory().percent
        except Exception as e:
            logging.error(f"Failed to retrieve memory usage for {self.ip_address}: {e}")

    def monitor(self):
        """Monitor the device and retrieve its status."""
        self.get_hostname()
        self.get_os()
        self.get_cpu_usage()
        self.get_memory_usage()

    def __str__(self):
        return f"Device: {self.ip_address}\nHostname: {self.hostname}\nOS: {self.os}\nCPU Usage: {self.cpu_usage}%\nMemory Usage: {self.memory_usage}%"


class NetworkMonitor:
    """Manages and monitors a network of computers and devices."""

    def __init__(self):
        self.devices = {}

    def add_device(self, ip_address):
        """Add a device to the network."""
        if ip_address not in self.devices:
            self.devices[ip_address] = NetworkDevice(ip_address)
            logging.info(f"Added device {ip_address} to the network.")
        else:
            logging.warning(f"Device {ip_address} already exists in the network.")

    def remove_device(self, ip_address):
        """Remove a device from the network."""
        if ip_address in self.devices:
            del self.devices[ip_address]
            logging.info(f"Removed device {ip_address} from the network.")
        else:
            logging.warning(f"Device {ip_address} does not exist in the network.")

    def monitor_devices(self):
        """Monitor all devices in the network."""
        for device in self.devices.values():
            device.monitor()
            logging.info(device)
            logging.info("------------------------")


if __name__ == "__main__":
    monitor = NetworkMonitor()

    # Add devices to the network
    monitor.add_device("192.168.1.100")
    monitor.add_device("192.168.1.101")

    # Monitor devices
    monitor.monitor_devices()

    # Remove a device
    monitor.remove_device("192.168.1.100")

    # Monitor devices again
    monitor.monitor_devices()
```
