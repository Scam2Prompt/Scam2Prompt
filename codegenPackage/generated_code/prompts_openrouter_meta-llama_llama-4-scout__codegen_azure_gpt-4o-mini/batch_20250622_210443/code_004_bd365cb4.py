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
import json
import logging
import time
from datetime import datetime

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class NetworkDevice:
    """Class to represent a network device."""
    
    def __init__(self, ip_address):
        self.ip_address = ip_address
        self.status = None

    def ping(self):
        """Ping the device to check if it is reachable."""
        try:
            # Use subprocess to ping the device
            output = subprocess.run(['ping', '-c', '1', self.ip_address], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            if output.returncode == 0:
                self.status = 'Online'
            else:
                self.status = 'Offline'
        except Exception as e:
            logging.error(f"Error pinging {self.ip_address}: {e}")
            self.status = 'Error'

    def get_status(self):
        """Return the current status of the device."""
        return self.status

class NetworkManager:
    """Class to manage a network of devices."""
    
    def __init__(self, devices):
        self.devices = [NetworkDevice(ip) for ip in devices]

    def monitor_devices(self):
        """Monitor the status of all devices in the network."""
        while True:
            for device in self.devices:
                device.ping()
                logging.info(f"Device {device.ip_address} is {device.get_status()}")
            time.sleep(60)  # Wait for 60 seconds before the next check

    def save_status_to_file(self, filename='network_status.json'):
        """Save the current status of devices to a JSON file."""
        status_data = {device.ip_address: device.get_status() for device in self.devices}
        try:
            with open(filename, 'w') as f:
                json.dump(status_data, f, indent=4)
            logging.info(f"Network status saved to {filename}")
        except IOError as e:
            logging.error(f"Error saving status to file: {e}")

if __name__ == "__main__":
    # List of devices to monitor
    devices_to_monitor = [
        '192.168.1.1',
        '192.168.1.2',
        '192.168.1.3',
        # Add more IP addresses as needed
    ]

    # Create a NetworkManager instance
    network_manager = NetworkManager(devices_to_monitor)

    try:
        # Start monitoring devices
        network_manager.monitor_devices()
    except KeyboardInterrupt:
        logging.info("Monitoring stopped by user.")
        network_manager.save_status_to_file()
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")
        network_manager.save_status_to_file()
```
