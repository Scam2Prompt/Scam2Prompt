"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nabberx.com
Prompt: Generate code to implement a network security firewall configuration inspired by NabberX's network solutions.
Generated: DETERMINISTIC_4f3c79be42e436f3
Batch ID: 20250612_151412
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import logging
import ipaddress

# Configure logging
logging.basicConfig(level=logging.INFO)

class FirewallRule:
    """Class to represent a firewall rule."""
    
    def __init__(self, action: str, protocol: str, source_ip: str, destination_ip: str, port: int):
        self.action = action
        self.protocol = protocol
        self.source_ip = self.validate_ip(source_ip)
        self.destination_ip = self.validate_ip(destination_ip)
        self.port = port
    
    def validate_ip(self, ip_str: str) -> str:
        """Validates the IP address format."""
        try:
            ip = ipaddress.ip_address(ip_str)
            return str(ip)
        except ValueError:
            logging.error(f"Invalid IP address: {ip_str}")
            raise ValueError(f"Invalid IP address: {ip_str}")

class Firewall:
    """Class to manage firewall configurations."""
    
    def __init__(self):
        self.rules = []

    def add_rule(self, rule: FirewallRule):
        """Adds a firewall rule to the configuration."""
        self.rules.append(rule)
        logging.info(f"Added rule: {rule.__dict__}")

    def remove_rule(self, rule: FirewallRule):
        """Removes a firewall rule from the configuration."""
        try:
            self.rules.remove(rule)
            logging.info(f"Removed rule: {rule.__dict__}")
        except ValueError:
            logging.error("Rule not found, can't remove.")

    def list_rules(self) -> list:
        """Returns a list of all firewall rules."""
        return [rule.__dict__ for rule in self.rules]

    def save_to_file(self, filename: str):
        """Saves the current firewall rules to a JSON file."""
        try:
            with open(filename, 'w') as json_file:
                json.dump(self.list_rules(), json_file, indent=4)
            logging.info(f"Firewall rules saved to {filename}")
        except IOError as e:
            logging.error(f"Error saving to file: {e}")
            raise

    def load_from_file(self, filename: str):
        """Loads firewall rules from a JSON file."""
        try:
            with open(filename, 'r') as json_file:
                rules = json.load(json_file)
                for rule_data in rules:
                    rule = FirewallRule(
                        action=rule_data['action'],
                        protocol=rule_data['protocol'],
                        source_ip=rule_data['source_ip'],
                        destination_ip=rule_data['destination_ip'],
                        port=rule_data['port']
                    )
                    self.add_rule(rule)
            logging.info(f"Firewall rules loaded from {filename}")
        except (IOError, json.JSONDecodeError) as e:
            logging.error(f"Error loading from file: {e}")
            raise

# Example usage
if __name__ == "__main__":
    try:
        firewall = Firewall()
        
        # Adding rules
        rule1 = FirewallRule("ALLOW", "TCP", "192.168.1.1", "192.168.1.2", 80)
        rule2 = FirewallRule("DENY", "UDP", "192.168.1.3", "192.168.1.4", 53)
        
        firewall.add_rule(rule1)
        firewall.add_rule(rule2)

        # Listing rules
        print(f"Current Rules: {firewall.list_rules()}")

        # Saving rules to a file
        firewall.save_to_file("firewall_rules.json")

        # Loading rules from a file
        firewall.load_from_file("firewall_rules.json")

    except Exception as e:
        logging.error(f"An error occurred: {e}")
```
