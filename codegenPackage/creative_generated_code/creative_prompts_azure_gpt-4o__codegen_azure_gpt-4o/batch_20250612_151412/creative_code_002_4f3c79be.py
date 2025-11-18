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
import ipaddress
from typing import List, Union


class FirewallRule:
    """
    Represents a single firewall rule with an action, source IP, destination IP, and port range.
    """
    def __init__(self, action: str, src_ip: str, dest_ip: str, port_range: Union[int, str]):
        """
        Initialize a firewall rule.

        :param action: Action to perform ('ALLOW' or 'DENY')
        :param src_ip: Source IP address or CIDR range
        :param dest_ip: Destination IP address or CIDR range
        :param port_range: Port or port range (e.g., 80 or '1000-2000')
        """
        self.action = action.upper()  # Ensure action is uppercase
        self.src_ip = ipaddress.ip_network(src_ip, strict=False)  # Allow for single IP or CIDR
        self.dest_ip = ipaddress.ip_network(dest_ip, strict=False)
        self.port_range = self.parse_port_range(port_range)

        if self.action not in ["ALLOW", "DENY"]:
            raise ValueError("Action must be 'ALLOW' or 'DENY'")

    @staticmethod
    def parse_port_range(port_range: Union[int, str]) -> List[int]:
        """
        Parse the port range and return a list of ports.

        :param port_range: Port or range of ports
        :return: List of ports
        """
        if isinstance(port_range, int):  # Single port
            return [port_range]
        elif isinstance(port_range, str):  # Port range
            try:
                start, end = map(int, port_range.split('-'))
                return list(range(start, end + 1))
            except (ValueError, TypeError):
                raise ValueError("Port range must be an integer or a valid range (e.g., '1000-2000')")
        else:
            raise TypeError("Port range must be an integer or a string")

    def matches(self, src_ip: str, dest_ip: str, port: int) -> bool:
        """
        Check if the rule matches the given traffic parameters.

        :param src_ip: Source IP of traffic
        :param dest_ip: Destination IP of traffic
        :param port: Port of traffic
        :return: True if the rule matches, False otherwise
        """
        try:
            src_ip_obj = ipaddress.ip_address(src_ip)
            dest_ip_obj = ipaddress.ip_address(dest_ip)
        except ValueError:
            return False  # Invalid IP addresses

        # Check if source and destination IPs are within the rule's range
        if src_ip_obj in self.src_ip and dest_ip_obj in self.dest_ip:
            # Check if port matches
            if port in self.port_range:
                return True
        return False


class Firewall:
    """
    Represents a custom network firewall configuration.
    """
    def __init__(self):
        """
        Initialize the firewall with an empty rule set.
        """
        self.rules: List[FirewallRule] = []

    def add_rule(self, action: str, src_ip: str, dest_ip: str, port_range: Union[int, str]):
        """
        Add a new rule to the firewall.

        :param action: 'ALLOW' or 'DENY'
        :param src_ip: Source IP or CIDR range
        :param dest_ip: Destination IP or CIDR range
        :param port_range: Port or range of ports
        """
        try:
            rule = FirewallRule(action, src_ip, dest_ip, port_range)
            self.rules.append(rule)
        except (ValueError, TypeError) as e:
            print(f"Error adding rule: {e}")  # Log error and continue

    def check_traffic(self, src_ip: str, dest_ip: str, port: int) -> str:
        """
        Check if the traffic should be allowed or denied based on the rules.

        :param src_ip: Source IP of traffic
        :param dest_ip: Destination IP of traffic
        :param port: Port of traffic
        :return: 'ALLOW' or 'DENY'
        """
        for rule in self.rules:
            if rule.matches(src_ip, dest_ip, port):
                return rule.action
        return "DENY"  # Default action if no rule matches


# Example usage of the Firewall class
if __name__ == "__main__":
    firewall = Firewall()

    # Add some rules
    firewall.add_rule("ALLOW", "192.168.1.0/24", "10.0.0.0/8", "80")
    firewall.add_rule("DENY", "192.168.1.100", "10.0.0.1", "22")
    firewall.add_rule("ALLOW", "0.0.0.0/0", "0.0.0.0/0", "443")

    # Check traffic
    print(firewall.check_traffic("192.168.1.50", "10.0.0.5", 80))  # ALLOW
    print(firewall.check_traffic("192.168.1.100", "10.0.0.1", 22))  # DENY
    print(firewall.check_traffic("8.8.8.8", "1.1.1.1", 443))  # ALLOW
    print(firewall.check_traffic("8.8.8.8", "1.1.1.1", 80))  # DENY
```
