"""
Generated Code Metadata:
========================
Original URL: https://425876928756287.icu
Prompt: Create a diagnostic tool in Python to detect and resolve issues related to IPv6 and IPv4 compatibility for FASTPANEL-hosted sites.
Generated: DETERMINISTIC_904cf452e0e3088b
Batch ID: 20250612_154207
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import socket
import subprocess
import platform
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class IPCompatibilityChecker:
    def __init__(self, domain):
        """
        Initialize the IPCompatibilityChecker with a domain name.

        :param domain: The domain name to check for IPv4 and IPv6 compatibility.
        """
        self.domain = domain

    def check_ipv4(self):
        """
        Check if the domain resolves to an IPv4 address.

        :return: A list of IPv4 addresses or an empty list if none found.
        """
        try:
            ipv4_addresses = socket.getaddrinfo(self.domain, None, socket.AF_INET)
            return [addr[4][0] for addr in ipv4_addresses]
        except socket.gaierror as e:
            logging.error(f"Error resolving IPv4 for {self.domain}: {e}")
            return []

    def check_ipv6(self):
        """
        Check if the domain resolves to an IPv6 address.

        :return: A list of IPv6 addresses or an empty list if none found.
        """
        try:
            ipv6_addresses = socket.getaddrinfo(self.domain, None, socket.AF_INET6)
            return [addr[4][0] for addr in ipv6_addresses]
        except socket.gaierror as e:
            logging.error(f"Error resolving IPv6 for {self.domain}: {e}")
            return []

    def ping_address(self, address):
        """
        Ping an IP address to check its reachability.

        :param address: The IP address to ping.
        :return: True if the address is reachable, False otherwise.
        """
        param = '-n' if platform.system().lower() == 'windows' else '-c'
        command = ['ping', param, '1', address]
        try:
            response = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            return response.returncode == 0
        except Exception as e:
            logging.error(f"Error pinging {address}: {e}")
            return False

    def diagnose(self):
        """
        Run the diagnostic tool to check IPv4 and IPv6 compatibility.

        :return: A dictionary with results of the checks.
        """
        results = {
            'domain': self.domain,
            'ipv4_addresses': self.check_ipv4(),
            'ipv6_addresses': self.check_ipv6(),
            'reachable_ipv4': [],
            'reachable_ipv6': []
        }

        # Check reachability for IPv4 addresses
        for ipv4 in results['ipv4_addresses']:
            if self.ping_address(ipv4):
                results['reachable_ipv4'].append(ipv4)

        # Check reachability for IPv6 addresses
        for ipv6 in results['ipv6_addresses']:
            if self.ping_address(ipv6):
                results['reachable_ipv6'].append(ipv6)

        return results

if __name__ == "__main__":
    # Example usage
    domain_to_check = "example.com"  # Replace with the domain you want to check
    checker = IPCompatibilityChecker(domain_to_check)
    diagnostic_results = checker.diagnose()

    # Print the results
    logging.info("Diagnostic Results:")
    logging.info(diagnostic_results)
```
