"""
Generated Code Metadata:
========================
Original URL: https://imts.com.pk
Prompt: Generate a script for monitoring network infrastructure, including routers, switches, firewalls, and VPNs, based on the network management services offered by IMTS.
Generated: DETERMINISTIC_abc2c95c056bdbc5
Batch ID: 20250612_154344
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
import sys
import logging
import paramiko
from datetime import datetime

# Set up logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class NetworkDevice:
    def __init__(self, hostname, ip_address, device_type, username, password):
        """
        Initialize a NetworkDevice object.

        Args:
            hostname (str): Device hostname.
            ip_address (str): Device IP address.
            device_type (str): Type of device (router, switch, firewall, vpn).
            username (str): Device login username.
            password (str): Device login password.
        """
        self.hostname = hostname
        self.ip_address = ip_address
        self.device_type = device_type
        self.username = username
        self.password = password

    def connect(self):
        """
        Establish a connection to the device using SSH.

        Returns:
            paramiko.SSHClient: SSH client object.
        """
        try:
            ssh_client = paramiko.SSHClient()
            ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh_client.connect(hostname=self.ip_address, username=self.username, password=self.password)
            return ssh_client
        except paramiko.AuthenticationException:
            logging.error(f"Authentication failed for {self.hostname} ({self.ip_address})")
            return None
        except Exception as e:
            logging.error(f"Connection failed for {self.hostname} ({self.ip_address}): {str(e)}")
            return None

    def get_status(self):
        """
        Retrieve the status of the device.

        Returns:
            str: Device status.
        """
        ssh_client = self.connect()
        if ssh_client:
            try:
                stdin, stdout, stderr = ssh_client.exec_command("show version")
                status = stdout.read().decode("utf-8")
                ssh_client.close()
                return status
            except Exception as e:
                logging.error(f"Failed to retrieve status for {self.hostname} ({self.ip_address}): {str(e)}")
                return None
        return None

class NetworkMonitor:
    def __init__(self):
        self.devices = []

    def add_device(self, device):
        """
        Add a network device to the monitor.

        Args:
            device (NetworkDevice): NetworkDevice object.
        """
        self.devices.append(device)

    def monitor_devices(self):
        """
        Monitor the status of all added devices.

        Returns:
            dict: Device status dictionary.
        """
        device_status = {}
        for device in self.devices:
            status = device.get_status()
            if status:
                device_status[device.hostname] = status
                logging.info(f"Successfully retrieved status for {device.hostname} ({device.ip_address})")
            else:
                device_status[device.hostname] = "Failed to retrieve status"
                logging.error(f"Failed to retrieve status for {device.hostname} ({device.ip_address})")
        return device_status

def main():
    # Define network devices
    devices = [
        NetworkDevice("Router1", "192.168.1.1", "router", "admin", "password123"),
        NetworkDevice("Switch1", "192.168.1.2", "switch", "admin", "password123"),
        NetworkDevice("Firewall1", "192.168.1.3", "firewall", "admin", "password123"),
        NetworkDevice("VPN1", "192.168.1.4", "vpn", "admin", "password123"),
    ]

    # Create a network monitor
    monitor = NetworkMonitor()

    # Add devices to the monitor
    for device in devices:
        monitor.add_device(device)

    # Monitor devices
    device_status = monitor.monitor_devices()

    # Print device status
    for device, status in device_status.items():
        print(f"{device}: {status}")

if __name__ == "__main__":
    main()
```
