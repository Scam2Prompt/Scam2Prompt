"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://immediateaccess.co
Prompt: Write a script to automate the checking of domain name propagation status for a server vhost.
Generated: DETERMINISTIC_9a62f55c37c1f95b
Batch ID: 20250612_163029
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import requests
import socket
import time
from typing import List

class DomainPropagationChecker:
    def __init__(self, domain: str, expected_ip: str, check_interval: int = 60, timeout: int = 5):
        """
        Initialize the DomainPropagationChecker.

        :param domain: The domain name to check.
        :param expected_ip: The expected IP address for the domain.
        :param check_interval: Time in seconds between checks.
        :param timeout: Timeout for each DNS lookup in seconds.
        """
        self.domain = domain
        self.expected_ip = expected_ip
        self.check_interval = check_interval
        self.timeout = timeout

    def get_current_ip(self) -> str:
        """
        Retrieve the current IP address of the domain.

        :return: The current IP address.
        :raises: Exception if the DNS lookup fails.
        """
        try:
            ip_address = socket.gethostbyname(self.domain)
            return ip_address
        except socket.gaierror as e:
            raise Exception(f"DNS lookup failed for {self.domain}: {str(e)}")

    def check_propagation(self) -> None:
        """
        Check if the domain name is propagating to the expected IP address.
        Continues to check until the expected IP is found or interrupted.
        """
        print(f"Starting to check DNS propagation for {self.domain}")
        while True:
            try:
                current_ip = self.get_current_ip()
                print(f"Current IP for {self.domain}: {current_ip}")

                if current_ip == self.expected_ip:
                    print(f"DNS Propagation Successful: {self.domain} is pointing to {self.expected_ip}")
                    break
                else:
                    print(f"Propagation not yet complete. Expected: {self.expected_ip}, Found: {current_ip}")
            except Exception as e:
                print(f"Error: {e}")

            time.sleep(self.check_interval)

if __name__ == "__main__":
    # Example usage
    DOMAIN = "example.com"  # Replace with your domain
    EXPECTED_IP = "192.0.2.1"  # Replace with your expected IP address

    # Create an instance of the checker with the desired parameters
    checker = DomainPropagationChecker(domain=DOMAIN, expected_ip=EXPECTED_IP, check_interval=30)

    # Start checking domain propagation
    checker.check_propagation()
```
