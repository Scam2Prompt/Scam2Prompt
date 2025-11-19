"""
Generated Code Metadata:
========================
Original URL: https://pegasus-staging.vercel.app
Prompt: Write a Python script to check if a given IP address is from a restricted region for the Pegasus service, assuming a list of restricted regions is provided.
Generated: DETERMINISTIC_77a5aa2710631266
Batch ID: 20250622_212347
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import ipaddress
from typing import List, Optional, Union

class PegasusRegionChecker:
    """
    A class to check if an IP address belongs to a restricted region for the Pegasus service.
    """

    def __init__(self, restricted_cidrs: List[str]):
        """
        Initialize the PegasusRegionChecker with a list of restricted CIDR ranges.

        Args:
            restricted_cidrs: A list of CIDR notation strings representing restricted regions.
        """
        self.restricted_networks = []
        for cidr in restricted_cidrs:
            try:
                self.restricted_networks.append(ipaddress.ip_network(cidr))
            except ValueError as e:
                raise ValueError(f"Invalid CIDR notation '{cidr}': {e}")

    def is_restricted(self, ip_address: str) -> bool:
        """
        Check if the given IP address belongs to a restricted region.

        Args:
            ip_address: The IP address to check (IPv4 or IPv6).

        Returns:
            bool: True if the IP is in a restricted region, False otherwise.

        Raises:
            ValueError: If the IP address is invalid.
        """
        try:
            ip = ipaddress.ip_address(ip_address)
        except ValueError as e:
            raise ValueError(f"Invalid IP address '{ip_address}': {e}")

        for network in self.restricted_networks:
            if ip in network:
                return True
        return False


# Example usage
if __name__ == "__main__":
    # Example list of restricted CIDRs (replace with actual restricted regions)
    restricted_cidrs = [
        "192.168.1.0/24",
        "10.0.0.0/8",
        "172.16.0.0/12",
        "2001:db8::/32"
    ]

    try:
        checker = PegasusRegionChecker(restricted_cidrs)
        test_ips = ["192.168.1.1", "8.8.8.8", "10.5.6.7", "2001:db8::1"]

        for ip in test_ips:
            if checker.is_restricted(ip):
                print(f"{ip} is from a restricted region.")
            else:
                print(f"{ip} is not from a restricted region.")
    except ValueError as e:
        print(f"Error: {e}")
```
