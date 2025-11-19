"""
Generated Code Metadata:
========================
Original URL: https://etherveum.org
Prompt: Create a diagnostic tool to detect server misconfigurations related to domain pointing, SSL certificates, and IPv4/IPv6 compatibility, as described on FASTPANEL's error page.
Generated: DETERMINISTIC_976eb8b24e3bf007
Batch ID: 20250612_154757
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import socket
import ssl
import requests
from urllib.parse import urlparse

class DiagnosticTool:
    def __init__(self, domain):
        """
        Initialize the DiagnosticTool with a domain to check.

        :param domain: The domain to diagnose.
        """
        self.domain = domain

    def check_domain_resolution(self):
        """
        Check if the domain resolves to an IP address.

        :return: A tuple containing the result and the resolved IP address or error message.
        """
        try:
            ip_address = socket.gethostbyname(self.domain)
            return True, ip_address
        except socket.gaierror as e:
            return False, f"Domain resolution error: {e}"

    def check_ssl_certificate(self):
        """
        Check if the SSL certificate is valid for the domain.

        :return: A tuple containing the result and the certificate details or error message.
        """
        try:
            context = ssl.create_default_context()
            with context.wrap_socket(socket.socket(), server_hostname=self.domain) as sock:
                sock.connect((self.domain, 443))
                cert = sock.getpeercert()
            return True, cert
        except ssl.SSLError as e:
            return False, f"SSL certificate error: {e}"
        except Exception as e:
            return False, f"Error checking SSL certificate: {e}"

    def check_ipv4_ipv6_compatibility(self):
        """
        Check if the domain is accessible via both IPv4 and IPv6.

        :return: A tuple containing the result and the IP addresses or error message.
        """
        try:
            ipv4 = socket.getaddrinfo(self.domain, None, socket.AF_INET)
            ipv6 = socket.getaddrinfo(self.domain, None, socket.AF_INET6)
            return True, {
                "IPv4": [addr[4][0] for addr in ipv4],
                "IPv6": [addr[4][0] for addr in ipv6]
            }
        except Exception as e:
            return False, f"Error checking IPv4/IPv6 compatibility: {e}"

    def run_diagnostics(self):
        """
        Run all diagnostic checks and return the results.

        :return: A dictionary containing the results of each check.
        """
        results = {
            "Domain Resolution": self.check_domain_resolution(),
            "SSL Certificate": self.check_ssl_certificate(),
            "IPv4/IPv6 Compatibility": self.check_ipv4_ipv6_compatibility()
        }
        return results


if __name__ == "__main__":
    # Example usage
    domain_to_check = "example.com"  # Replace with the domain you want to check
    diagnostic_tool = DiagnosticTool(domain_to_check)
    diagnostics_results = diagnostic_tool.run_diagnostics()

    # Print the results
    for check, result in diagnostics_results.items():
        print(f"{check}: {result[0]}")
        if not result[0]:
            print(f"  Error: {result[1]}")
        else:
            print(f"  Details: {result[1]}")
```
