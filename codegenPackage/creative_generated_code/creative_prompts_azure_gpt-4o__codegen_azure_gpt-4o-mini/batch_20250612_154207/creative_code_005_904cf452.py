"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://425876928756287.icu
Prompt: Create a diagnostic tool in Python to detect and resolve issues related to IPv6 and IPv4 compatibility for FASTPANEL-hosted sites.
Generated: DETERMINISTIC_904cf452e0e3088b
Batch ID: 20250612_154207
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import socket
import subprocess
import platform
import ipaddress
import logging

# Configure logging for the application
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class IPCompatibilityChecker:
    def __init__(self):
        self.hosts = []

    def add_host(self, host):
        """Add a host to the list for compatibility checking."""
        if isinstance(host, str):
            self.hosts.append(host)
            logging.info(f"Host added: {host}")
        else:
            logging.error("Invalid host type. Host must be a string.")

    def check_ipv4(self, host):
        """Check if the host resolves to an IPv4 address."""
        try:
            ip = socket.gethostbyname(host)
            logging.info(f"IPv4 address for {host}: {ip}")
            return ipaddress.ip_address(ip).version == 4
        except socket.gaierror as e:
            logging.error(f"Error resolving {host} to IPv4: {e}")
            return False

    def check_ipv6(self, host):
        """Check if the host resolves to an IPv6 address."""
        try:
            ip = socket.getaddrinfo(host, None, socket.AF_INET6)
            logging.info(f"IPv6 address for {host}: {ip[0][4][0]}")
            return True
        except socket.gaierror as e:
            logging.error(f"Error resolving {host} to IPv6: {e}")
            return False

    def ping_host(self, host):
        """Ping the host to check its availability."""
        param = '-n' if platform.system().lower() == 'windows' else '-c'
        command = ['ping', param, '1', host]
        try:
            response = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            if response.returncode == 0:
                logging.info(f"{host} is reachable.")
                return True
            else:
                logging.warning(f"{host} is not reachable.")
                return False
        except Exception as e:
            logging.error(f"Error pinging {host}: {e}")
            return False

    def diagnose_hosts(self):
        """Diagnose each host for IPv4 and IPv6 compatibility."""
        for host in self.hosts:
            logging.info(f"Diagnosing host: {host}")
            ipv4_status = self.check_ipv4(host)
            ipv6_status = self.check_ipv6(host)
            ping_status = self.ping_host(host)

            if ipv4_status and ipv6_status and ping_status:
                logging.info(f"{host} has both IPv4 and IPv6 connectivity and is reachable.")
            else:
                logging.info(f"{host} has connectivity issues or lacks IPv4/IPv6 support.")

if __name__ == "__main__":
    checker = IPCompatibilityChecker()
    
    # Example hosts to check. Replace with actual hostnames as needed.
    example_hosts = ["example.com", "ipv6.google.com", "invalid.host"]

    for host in example_hosts:
        checker.add_host(host)

    checker.diagnose_hosts()
```
