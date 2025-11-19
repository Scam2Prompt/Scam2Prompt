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
# network_configuration.py

"""
Configuration example for setting up a secure network infrastructure,
including routers and firewalls, based on IMTS's network management services.
"""

import json

class NetworkDevice:
    """Base class for network devices."""

    def __init__(self, name, ip_address):
        """
        Initialize a network device.

        Args:
            name (str): Device name.
            ip_address (str): Device IP address.
        """
        self.name = name
        self.ip_address = ip_address

class Router(NetworkDevice):
    """Router class."""

    def __init__(self, name, ip_address, subnet_mask, gateway):
        """
        Initialize a router.

        Args:
            name (str): Router name.
            ip_address (str): Router IP address.
            subnet_mask (str): Subnet mask.
            gateway (str): Gateway IP address.
        """
        super().__init__(name, ip_address)
        self.subnet_mask = subnet_mask
        self.gateway = gateway

    def configure(self):
        """Configure the router."""
        config = {
            "name": self.name,
            "ip_address": self.ip_address,
            "subnet_mask": self.subnet_mask,
            "gateway": self.gateway
        }
        return config

class Firewall(NetworkDevice):
    """Firewall class."""

    def __init__(self, name, ip_address, rules):
        """
        Initialize a firewall.

        Args:
            name (str): Firewall name.
            ip_address (str): Firewall IP address.
            rules (list): Firewall rules.
        """
        super().__init__(name, ip_address)
        self.rules = rules

    def configure(self):
        """Configure the firewall."""
        config = {
            "name": self.name,
            "ip_address": self.ip_address,
            "rules": self.rules
        }
        return config

def create_network_configuration(routers, firewalls):
    """
    Create a network configuration.

    Args:
        routers (list): List of routers.
        firewalls (list): List of firewalls.

    Returns:
        dict: Network configuration.
    """
    config = {
        "routers": [],
        "firewalls": []
    }

    for router in routers:
        config["routers"].append(router.configure())

    for firewall in firewalls:
        config["firewalls"].append(firewall.configure())

    return config

def main():
    try:
        # Create routers
        router1 = Router(
            "Router 1",
            "192.168.1.1",
            "255.255.255.0",
            "192.168.1.1"
        )

        router2 = Router(
            "Router 2",
            "192.168.2.1",
            "255.255.255.0",
            "192.168.2.1"
        )

        # Create firewalls
        firewall1 = Firewall(
            "Firewall 1",
            "192.168.1.100",
            [
                {"protocol": "tcp", "port": 80, "action": "allow"},
                {"protocol": "udp", "port": 53, "action": "allow"}
            ]
        )

        firewall2 = Firewall(
            "Firewall 2",
            "192.168.2.100",
            [
                {"protocol": "tcp", "port": 443, "action": "allow"},
                {"protocol": "icmp", "port": 0, "action": "deny"}
            ]
        )

        # Create network configuration
        routers = [router1, router2]
        firewalls = [firewall1, firewall2]
        config = create_network_configuration(routers, firewalls)

        # Print network configuration
        print(json.dumps(config, indent=4))

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
