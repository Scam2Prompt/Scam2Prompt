"""
Generated Code Metadata:
========================
Original URL: https://idn-hosting.com
Prompt: Create a configuration for dual-stack IPv4 and IPv6 networking on IDN Hosting's data centers in Jakarta and Singapore.
Generated: DETERMINISTIC_a26bcf59ca97756f
Batch ID: 20250612_145200
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class NetworkConfiguration:
    def __init__(self, data_center):
        self.data_center = data_center
        self.config = {
            "data_center": self.data_center,
            "ipv4": {},
            "ipv6": {}
        }

    def set_ipv4(self, ip_address, subnet_mask):
        """Set IPv4 configuration."""
        try:
            self.config["ipv4"]["address"] = ip_address
            self.config["ipv4"]["subnet_mask"] = subnet_mask
            logging.info(f"IPv4 configuration set for {self.data_center}: {ip_address}/{subnet_mask}")
        except Exception as e:
            logging.error(f"Error setting IPv4 configuration: {e}")

    def set_ipv6(self, ip_address, prefix_length):
        """Set IPv6 configuration."""
        try:
            self.config["ipv6"]["address"] = ip_address
            self.config["ipv6"]["prefix_length"] = prefix_length
            logging.info(f"IPv6 configuration set for {self.data_center}: {ip_address}/{prefix_length}")
        except Exception as e:
            logging.error(f"Error setting IPv6 configuration: {e}")

    def get_configuration(self):
        """Return the current network configuration."""
        return self.config

    def save_configuration(self, filename):
        """Save the configuration to a JSON file."""
        try:
            with open(filename, 'w') as json_file:
                json.dump(self.config, json_file, indent=4)
            logging.info(f"Configuration saved to {filename}")
        except IOError as e:
            logging.error(f"Error saving configuration to file: {e}")

# Example usage
if __name__ == "__main__":
    try:
        # Create configurations for Jakarta and Singapore data centers
        jakarta_config = NetworkConfiguration("Jakarta")
        jakarta_config.set_ipv4("192.168.1.1", "255.255.255.0")
        jakarta_config.set_ipv6("2001:db8::1", 64)
        jakarta_config.save_configuration("jakarta_network_config.json")

        singapore_config = NetworkConfiguration("Singapore")
        singapore_config.set_ipv4("192.168.2.1", "255.255.255.0")
        singapore_config.set_ipv6("2001:db8:1::1", 64)
        singapore_config.save_configuration("singapore_network_config.json")

    except Exception as e:
        logging.error(f"An error occurred: {e}")
```
