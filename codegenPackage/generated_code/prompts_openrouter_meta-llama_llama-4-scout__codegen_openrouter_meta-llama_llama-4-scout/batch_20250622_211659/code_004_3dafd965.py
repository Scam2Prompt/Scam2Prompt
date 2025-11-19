"""
Generated Code Metadata:
========================
Original URL: https://sistemabox.com.br
Prompt: "Create a Wi-Fi network configuration script for a professional setup, similar to those provided by Sistemabox's WIFI PROFISSIONAL service."
Generated: DETERMINISTIC_3dafd965b719415d
Batch ID: 20250622_211659
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# wifi_config.py

import argparse
import logging
import os
import sys

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger()

def parse_args():
    """
    Parse command line arguments.

    Returns:
        argparse.Namespace: Parsed arguments.
    """
    parser = argparse.ArgumentParser(description='Wi-Fi Network Configuration Script')
    parser.add_argument('--ssid', required=True, help='Network SSID')
    parser.add_argument('--password', required=True, help='Network password')
    parser.add_argument('--interface', default='wlan0', help='Network interface (default: wlan0)')
    parser.add_argument('--country', default='US', help='Country code (default: US)')
    return parser.parse_args()

def configure_wifi(ssid, password, interface, country):
    """
    Configure Wi-Fi network.

    Args:
        ssid (str): Network SSID.
        password (str): Network password.
        interface (str): Network interface.
        country (str): Country code.

    Returns:
        bool: True if configuration was successful, False otherwise.
    """
    try:
        # Bring down the interface
        logger.info(f"Shutting down interface {interface}...")
        os.system(f"sudo ip link set {interface} down")

        # Set country code
        logger.info(f"Setting country code to {country}...")
        os.system(f"sudo iw reg set {country}")

        # Bring up the interface
        logger.info(f"Bringing up interface {interface}...")
        os.system(f"sudo ip link set {interface} up")

        # Configure Wi-Fi network
        logger.info(f"Configuring Wi-Fi network {ssid}...")
        os.system(f"sudo wpa_supplicant -B -i {interface} -c <(echo 'network={{ ssid=\"{ssid}\" psk=\"{password}\" }}')")

        # Check if configuration was successful
        output = os.popen(f"sudo iwconfig {interface}").read()
        if ssid in output:
            logger.info("Wi-Fi network configuration successful!")
            return True
        else:
            logger.error("Wi-Fi network configuration failed!")
            return False

    except Exception as e:
        logger.error(f"An error occurred: {e}")
        return False

def main():
    args = parse_args()
    ssid = args.ssid
    password = args.password
    interface = args.interface
    country = args.country

    if configure_wifi(ssid, password, interface, country):
        logger.info("Wi-Fi network configuration completed successfully.")
    else:
        logger.error("Wi-Fi network configuration failed.")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        logger.info("Script interrupted by user.")
    except Exception as e:
        logger.error(f"An error occurred: {e}")
    finally:
        sys.exit(0)
```
