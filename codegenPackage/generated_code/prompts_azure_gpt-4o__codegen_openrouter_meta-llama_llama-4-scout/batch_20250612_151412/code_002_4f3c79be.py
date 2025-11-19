"""
Generated Code Metadata:
========================
Original URL: https://nabberx.com
Prompt: Generate code to implement a network security firewall configuration inspired by NabberX's network solutions.
Generated: DETERMINISTIC_4f3c79be42e436f3
Batch ID: 20250612_151412
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# firewall_config.py

import logging
import ipaddress

# Set up logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class FirewallRule:
    """Represents a single firewall rule."""

    def __init__(self, protocol, src_ip, dst_ip, src_port, dst_port, allow):
        """
        Initializes a FirewallRule object.

        Args:
            protocol (str): The protocol of the rule (e.g., TCP, UDP).
            src_ip (str): The source IP address of the rule.
            dst_ip (str): The destination IP address of the rule.
            src_port (int): The source port of the rule.
            dst_port (int): The destination port of the rule.
            allow (bool): Whether the rule allows or blocks traffic.
        """
        self.protocol = protocol
        self.src_ip = ipaddress.ip_address(src_ip)
        self.dst_ip = ipaddress.ip_address(dst_ip)
        self.src_port = src_port
        self.dst_port = dst_port
        self.allow = allow

    def __str__(self):
        """Returns a string representation of the rule."""
        action = "allow" if self.allow else "block"
        return f"{action} {self.protocol} from {self.src_ip} to {self.dst_ip} on ports {self.src_port} -> {self.dst_port}"

class FirewallConfig:
    """Represents a firewall configuration."""

    def __init__(self):
        """Initializes an empty firewall configuration."""
        self.rules = []

    def add_rule(self, rule):
        """
        Adds a rule to the firewall configuration.

        Args:
            rule (FirewallRule): The rule to add.
        """
        self.rules.append(rule)

    def remove_rule(self, rule):
        """
        Removes a rule from the firewall configuration.

        Args:
            rule (FirewallRule): The rule to remove.
        """
        self.rules.remove(rule)

    def evaluate_traffic(self, protocol, src_ip, dst_ip, src_port, dst_port):
        """
        Evaluates incoming traffic against the firewall configuration.

        Args:
            protocol (str): The protocol of the traffic.
            src_ip (str): The source IP address of the traffic.
            dst_ip (str): The destination IP address of the traffic.
            src_port (int): The source port of the traffic.
            dst_port (int): The destination port of the traffic.

        Returns:
            bool: Whether the traffic is allowed or blocked.
        """
        src_ip = ipaddress.ip_address(src_ip)
        dst_ip = ipaddress.ip_address(dst_ip)

        for rule in self.rules:
            if (rule.protocol == protocol and
                    rule.src_ip == src_ip and
                    rule.dst_ip == dst_ip and
                    rule.src_port == src_port and
                    rule.dst_port == dst_port):
                return rule.allow

        # Default to block if no matching rule is found
        return False

def main():
    # Create a sample firewall configuration
    config = FirewallConfig()

    # Add some sample rules
    config.add_rule(FirewallRule("TCP", "192.168.1.100", "8.8.8.8", 1234, 80, True))
    config.add_rule(FirewallRule("UDP", "192.168.1.200", "8.8.4.4", 5678, 53, False))

    # Evaluate some sample traffic
    traffic1_allowed = config.evaluate_traffic("TCP", "192.168.1.100", "8.8.8.8", 1234, 80)
    traffic2_blocked = config.evaluate_traffic("UDP", "192.168.1.200", "8.8.4.4", 5678, 53)
    traffic3_blocked = config.evaluate_traffic("ICMP", "192.168.1.50", "8.8.8.8", 0, 0)

    logging.info(f"Traffic 1 allowed: {traffic1_allowed}")
    logging.info(f"Traffic 2 blocked: {traffic2_blocked}")
    logging.info(f"Traffic 3 blocked: {traffic3_blocked}")

if __name__ == "__main__":
    main()
```
