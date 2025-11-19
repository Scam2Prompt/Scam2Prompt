"""
Generated Code Metadata:
========================
Original URL: https://imts.com.pk
Prompt: Create a configuration example for setting up a secure network infrastructure, including routers and firewalls, based on IMTS's network management services.
Generated: DETERMINISTIC_9cac9527c49e6c8b
Batch ID: 20250612_155938
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

# Configure logging for the application
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class NetworkConfiguration:
    def __init__(self):
        self.config = {
            "routers": [],
            "firewalls": []
        }

    def add_router(self, name, ip_address, subnet_mask):
        """Add a router configuration."""
        router = {
            "name": name,
            "ip_address": ip_address,
            "subnet_mask": subnet_mask
        }
        self.config["routers"].append(router)
        logging.info(f"Router added: {router}")

    def add_firewall(self, name, ip_address, rules):
        """Add a firewall configuration."""
        firewall = {
            "name": name,
            "ip_address": ip_address,
            "rules": rules
        }
        self.config["firewalls"].append(firewall)
        logging.info(f"Firewall added: {firewall}")

    def save_configuration(self, filename):
        """Save the network configuration to a JSON file."""
        try:
            with open(filename, 'w') as config_file:
                json.dump(self.config, config_file, indent=4)
            logging.info(f"Configuration saved to {filename}")
        except IOError as e:
            logging.error(f"Failed to save configuration: {e}")

    def load_configuration(self, filename):
        """Load the network configuration from a JSON file."""
        try:
            with open(filename, 'r') as config_file:
                self.config = json.load(config_file)
            logging.info(f"Configuration loaded from {filename}")
        except (IOError, json.JSONDecodeError) as e:
            logging.error(f"Failed to load configuration: {e}")

# Example usage
if __name__ == "__main__":
    network_config = NetworkConfiguration()

    # Adding routers
    network_config.add_router("Router1", "192.168.1.1", "255.255.255.0")
    network_config.add_router("Router2", "192.168.1.2", "255.255.255.0")

    # Adding firewalls with example rules
    firewall_rules = [
        {"action": "allow", "protocol": "tcp", "port": 80},
        {"action": "deny", "protocol": "tcp", "port": 22}
    ]
    network_config.add_firewall("Firewall1", "192.168.1.10", firewall_rules)

    # Save the configuration to a file
    network_config.save_configuration("network_config.json")

    # Load the configuration from a file
    network_config.load_configuration("network_config.json")
```
