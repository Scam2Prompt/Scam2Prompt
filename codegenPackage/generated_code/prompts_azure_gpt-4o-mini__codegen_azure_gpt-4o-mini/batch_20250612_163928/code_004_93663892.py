"""
Generated Code Metadata:
========================
Original URL: https://nabberx.com
Prompt: Illustrate how to implement network security measures and firewalls in a business environment, using the guidelines from NabberX’s offerings.
Generated: DETERMINISTIC_936638924d006ef0
Batch ID: 20250612_163928
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
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class FirewallManager:
    """
    A class to manage firewall rules and network security measures.
    """

    def __init__(self):
        """
        Initializes the FirewallManager.
        """
        self.firewall_rules = []

    def add_rule(self, rule):
        """
        Adds a firewall rule to the list.

        :param rule: A string representing the firewall rule.
        """
        self.firewall_rules.append(rule)
        logging.info(f"Rule added: {rule}")

    def remove_rule(self, rule):
        """
        Removes a firewall rule from the list.

        :param rule: A string representing the firewall rule.
        """
        try:
            self.firewall_rules.remove(rule)
            logging.info(f"Rule removed: {rule}")
        except ValueError:
            logging.error(f"Rule not found: {rule}")

    def apply_rules(self):
        """
        Applies all firewall rules to the system.
        """
        for rule in self.firewall_rules:
            try:
                # This is a placeholder for the actual command to apply the rule
                subprocess.run(['iptables', rule], check=True)
                logging.info(f"Applied rule: {rule}")
            except subprocess.CalledProcessError as e:
                logging.error(f"Failed to apply rule '{rule}': {e}")

    def show_rules(self):
        """
        Displays the current firewall rules.
        """
        logging.info("Current firewall rules:")
        for rule in self.firewall_rules:
            print(rule)

def main():
    """
    Main function to demonstrate the FirewallManager functionality.
    """
    firewall_manager = FirewallManager()

    # Example rules (these should be replaced with actual iptables rules)
    example_rules = [
        '-A INPUT -p tcp --dport 22 -j ACCEPT',  # Allow SSH
        '-A INPUT -p tcp --dport 80 -j ACCEPT',  # Allow HTTP
        '-A INPUT -p tcp --dport 443 -j ACCEPT', # Allow HTTPS
        '-A INPUT -j DROP'                       # Drop all other traffic
    ]

    # Adding rules
    for rule in example_rules:
        firewall_manager.add_rule(rule)

    # Show current rules
    firewall_manager.show_rules()

    # Apply rules
    firewall_manager.apply_rules()

if __name__ == "__main__":
    main()
```
