"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nabberx.com
Prompt: Illustrate how to implement network security measures and firewalls in a business environment, using the guidelines from NabberX’s offerings.
Generated: DETERMINISTIC_936638924d006ef0
Batch ID: 20250612_163928
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import subprocess
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class FirewallManager:
    def __init__(self):
        """Initialize the FirewallManager class."""
        self.firewall_rules = []

    def add_rule(self, rule):
        """
        Add a firewall rule to the list.
        
        :param rule: A string representing the firewall rule.
        """
        self.firewall_rules.append(rule)
        logging.info(f"Rule added: {rule}")

    def remove_rule(self, rule):
        """
        Remove a firewall rule from the list.
        
        :param rule: A string representing the firewall rule to remove.
        """
        try:
            self.firewall_rules.remove(rule)
            logging.info(f"Rule removed: {rule}")
        except ValueError:
            logging.error(f"Attempted to remove a non-existent rule: {rule}")

    def apply_rules(self):
        """Apply all firewall rules to the system."""
        for rule in self.firewall_rules:
            try:
                subprocess.run(rule, shell=True, check=True)
                logging.info(f"Successfully applied rule: {rule}")
            except subprocess.CalledProcessError as e:
                logging.error(f"Failed to apply rule: {rule}. Error: {e}")

    def clear_rules(self):
        """Clear all firewall rules."""
        self.firewall_rules.clear()
        logging.info("All firewall rules have been cleared.")

def main():
    """Run the firewall manager."""
    firewall_manager = FirewallManager()

    # Example rules based on NabberX offerings
    example_rules = [
        "iptables -A INPUT -p tcp --dport 22 -j ACCEPT",   # Allow SSH
        "iptables -A INPUT -p tcp --dport 80 -j ACCEPT",   # Allow HTTP
        "iptables -A INPUT -p tcp --dport 443 -j ACCEPT",  # Allow HTTPS
        "iptables -A INPUT -j DROP"                         # Drop all other traffic
    ]

    # Adding rules
    for rule in example_rules:
        firewall_manager.add_rule(rule)

    # Applying firewall rules
    firewall_manager.apply_rules()

    # For demonstration, let's clear rules after application
    firewall_manager.clear_rules()

if __name__ == "__main__":
    main()
```
