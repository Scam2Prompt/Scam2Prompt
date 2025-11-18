"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://btc-tools.org
Prompt: Write a script to automate the batch restarting process for Antminer devices using BTC Tools.
Generated: DETERMINISTIC_2429ae044c70b2dc
Batch ID: 20250612_151710
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import subprocess
import logging
import time
from typing import List

# Configure logging to output to a file and the console
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("antminer_restart.log"),
        logging.StreamHandler()
    ]
)

class AntminerManager:
    def __init__(self, ip_addresses: List[str]):
        """
        Initialize the AntminerManager with a list of IP addresses.

        :param ip_addresses: List of IP addresses of the Antminer devices.
        """
        self.ip_addresses = ip_addresses

    def restart_device(self, ip_address: str) -> None:
        """
        Restart an Antminer device using BTC Tools.

        :param ip_address: The IP address of the Antminer device to restart.
        """
        try:
            # Command to restart the Antminer device
            command = f"btc_tools restart {ip_address}"
            logging.info(f"Attempting to restart device at {ip_address}...")
            subprocess.run(command, shell=True, check=True)
            logging.info(f"Successfully restarted device at {ip_address}.")
        except subprocess.CalledProcessError as e:
            logging.error(f"Failed to restart device at {ip_address}. Error: {e}")
        except Exception as e:
            logging.error(f"An unexpected error occurred while restarting {ip_address}: {e}")

    def restart_all_devices(self) -> None:
        """
        Restart all Antminer devices listed in the IP addresses.

        :raises ValueError: If the list of IP addresses is empty.
        """
        if not self.ip_addresses:
            raise ValueError("No IP addresses provided for restarting devices.")

        for ip in self.ip_addresses:
            self.restart_device(ip)
            time.sleep(5)  # Wait for 5 seconds between restarts to avoid overwhelming the devices

if __name__ == "__main__":
    # Example usage
    # Replace with actual IP addresses of the Antminer devices
    ip_list = [
        "192.168.1.100",
        "192.168.1.101",
        "192.168.1.102"
    ]

    # Create an instance of AntminerManager and restart all devices
    manager = AntminerManager(ip_addresses=ip_list)
    try:
        manager.restart_all_devices()
    except ValueError as ve:
        logging.error(ve)
```

Make sure to replace `"btc_tools restart {ip_address}"` with the actual command that works in your environment, as well as the IP addresses in `ip_list` with the real addresses of the Antminer devices.
