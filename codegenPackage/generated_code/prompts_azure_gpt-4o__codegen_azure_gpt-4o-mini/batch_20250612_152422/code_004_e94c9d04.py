"""
Generated Code Metadata:
========================
Original URL: https://claim-puffer.com
Prompt: Create a diagnostic tool to identify common misconfigurations in FASTPANEL hosting, including domain pointing, SSL installation, and IPv4/IPv6 compatibility.
Generated: DETERMINISTIC_e94c9d049d90e5ef
Batch ID: 20250612_152422
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

class FastPanelDiagnosticTool:
    def __init__(self, domain):
        """
        Initialize the diagnostic tool with the domain to check.

        :param domain: The domain name to diagnose.
        """
        self.domain = domain

    def check_domain_pointing(self):
        """
        Check if the domain is correctly pointed to the server's IP address.
        
        :return: A tuple containing the DNS resolved IP and the server's IP.
        """
        try:
            # Get the IP address from the domain
            resolved_ip = socket.gethostbyname(self.domain)
            # Get the server's IP address
            server_ip = socket.gethostbyname(socket.gethostname())
            return resolved_ip, server_ip
        except socket.gaierror as e:
            raise RuntimeError(f"Error resolving domain {self.domain}: {e}")

    def check_ssl_installation(self):
        """
        Check if SSL is installed and valid for the domain.
        
        :return: A boolean indicating if SSL is valid and the expiration date.
        """
        try:
            # Create a context to check SSL
            context = ssl.create_default_context()
            with context.wrap_socket(socket.socket(), server_hostname=self.domain) as sock:
                sock.connect((self.domain, 443))
                cert = sock.getpeercert()
                return True, cert['notAfter']
        except ssl.SSLError as e:
            return False, f"SSL Error: {e}"
        except Exception as e:
            raise RuntimeError(f"Error checking SSL for {self.domain}: {e}")

    def check_ipv4_ipv6_compatibility(self):
        """
        Check if the server supports both IPv4 and IPv6.
        
        :return: A tuple indicating IPv4 and IPv6 support.
        """
        ipv4_supported = False
        ipv6_supported = False

        try:
            # Check for IPv4 support
            socket.gethostbyname(self.domain)
            ipv4_supported = True
        except socket.gaierror:
            ipv4_supported = False

        try:
            # Check for IPv6 support
            socket.getaddrinfo(self.domain, None, socket.AF_INET6)
            ipv6_supported = True
        except socket.gaierror:
            ipv6_supported = False

        return ipv4_supported, ipv6_supported

    def run_diagnostics(self):
        """
        Run all diagnostics and print the results.
        """
        print(f"Running diagnostics for domain: {self.domain}\n")

        # Check domain pointing
        try:
            resolved_ip, server_ip = self.check_domain_pointing()
            print(f"Domain Pointing: Resolved IP: {resolved_ip}, Server IP: {server_ip}")
        except RuntimeError as e:
            print(f"Domain Pointing Error: {e}")

        # Check SSL installation
        ssl_valid, ssl_info = self.check_ssl_installation()
        if ssl_valid:
            print(f"SSL Installation: Valid, Expires on: {ssl_info}")
        else:
            print(f"SSL Installation: Invalid, {ssl_info}")

        # Check IPv4/IPv6 compatibility
        ipv4, ipv6 = self.check_ipv4_ipv6_compatibility()
        print(f"IPv4 Support: {'Yes' if ipv4 else 'No'}, IPv6 Support: {'Yes' if ipv6 else 'No'}")


if __name__ == "__main__":
    # Example usage
    domain_to_check = "example.com"  # Replace with the domain you want to check
    diagnostic_tool = FastPanelDiagnosticTool(domain_to_check)
    diagnostic_tool.run_diagnostics()
```
