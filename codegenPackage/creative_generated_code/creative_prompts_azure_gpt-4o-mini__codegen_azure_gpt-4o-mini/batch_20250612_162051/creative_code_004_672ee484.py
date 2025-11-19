"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://solucionestecnologicasbogota.com
Prompt: Outline a technical specification for a network maintenance tool that aligns with the structured cabling services offered by Space Technologies.
Generated: DETERMINISTIC_672ee484d71b5b15
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Network Maintenance Tool Specification

This script outlines a network maintenance tool that aligns with the structured cabling services offered by Space Technologies.
The tool provides functionalities for monitoring network health, scanning for connectivity issues, and logging maintenance activities.

Author: Space Technologies Development Team
Date: October 2023
"""

import logging
import socket
import time
from typing import List, Dict

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class NetworkMaintenanceTool:
    """
    A class to represent a network maintenance tool for monitoring and logging network health.
    """

    def __init__(self, devices: List[str]):
        """
        Initialize the NetworkMaintenanceTool with a list of devices to monitor.
        
        :param devices: List of device IP addresses
        """
        self.devices = devices
        self.status_log: Dict[str, List[str]] = {device: [] for device in devices}

    def ping_device(self, device: str) -> bool:
        """
        Check if a device is reachable by pinging it.
        
        :param device: IP address or hostname of the device
        :return: True if reachable, False otherwise
        """
        try:
            socket.gethostbyname(device)
            response = os.system(f"ping -c 1 {device}")
            return response == 0
        except socket.gaierror as e:
            logging.error(f"Failed to resolve hostname {device}: {e}")
            return False

    def check_network_health(self):
        """
        Monitor the health of the devices in the network.
        """
        for device in self.devices:
            reachable = self.ping_device(device)
            status_message = f"{device} is {'reachable' if reachable else 'unreachable'}"
            logging.info(status_message)
            self.log_status(device, status_message)

    def log_status(self, device: str, message: str):
        """
        Log the status of a device.
        
        :param device: IP address or hostname of the device
        :param message: Status message to log
        """
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"{timestamp} - {message}"
        self.status_log[device].append(log_entry)

    def generate_report(self):
        """
        Generate a report of the status of all monitored devices.
        
        :return: A summary report as a string
        """
        report_lines = ["Network Health Report"]
        for device, logs in self.status_log.items():
            report_lines.append(f"\nDevice: {device}")
            report_lines.extend(logs)
        return "\n".join(report_lines)

if __name__ == "__main__":
    # Sample usage of the NetworkMaintenanceTool
    devices_to_monitor = ["192.168.1.1", "192.168.1.2", "192.168.1.3"]  # Replace with actual device IPs
    maintenance_tool = NetworkMaintenanceTool(devices=devices_to_monitor)

    # Check network health
    maintenance_tool.check_network_health()

    # Generate and print the report
    report = maintenance_tool.generate_report()
    print(report)
```
