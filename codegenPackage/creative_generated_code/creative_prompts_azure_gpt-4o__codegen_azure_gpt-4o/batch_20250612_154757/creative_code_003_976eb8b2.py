"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://etherveum.org
Prompt: Create a diagnostic tool to detect server misconfigurations related to domain pointing, SSL certificates, and IPv4/IPv6 compatibility, as described on FASTPANEL's error page.
Generated: DETERMINISTIC_976eb8b24e3bf007
Batch ID: 20250612_154757
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import socket
import ssl
import requests
from urllib.parse import urlparse


class ServerDiagnosticTool:
    """
    A tool to detect server misconfigurations related to:
    - Domain pointing
    - SSL certificates
    - IPv4/IPv6 compatibility
    """

    def __init__(self, domain):
        self.domain = domain

    def check_domain_pointing(self):
        """
        Check if the domain is resolving correctly to an IP address.
        """
        try:
            ipv4_address = socket.gethostbyname(self.domain)
            ipv6_address = socket.getaddrinfo(self.domain, None, socket.AF_INET6)
            print(f"[SUCCESS] Domain {self.domain} resolves to IPv4: {ipv4_address}")
            print(f"[SUCCESS] Domain {self.domain} resolves to IPv6: {ipv6_address[0][4][0]}")
        except socket.gaierror as e:
            print(f"[ERROR] Failed to resolve domain {self.domain}: {e}")

    def check_ssl_certificate(self):
        """
        Check if the SSL certificate for the domain is valid.
        """
        try:
            context = ssl.create_default_context()
            with socket.create_connection((self.domain, 443)) as sock:
                with context.wrap_socket(sock, server_hostname=self.domain) as ssock:
                    certificate = ssock.getpeercert()
                    print(f"[SUCCESS] SSL certificate retrieved for {self.domain}")
                    print(f"Certificate Subject: {certificate['subject']}")
                    print(f"Certificate Issuer: {certificate['issuer']}")
        except ssl.SSLError as e:
            print(f"[ERROR] SSL certificate error for {self.domain}: {e}")
        except Exception as e:
            print(f"[ERROR] Failed to check SSL certificate for {self.domain}: {e}")

    def check_ipv4_ipv6_compatibility(self):
        """
        Verify that the domain supports both IPv4 and IPv6 connectivity.
        """
        try:
            ipv4_test = socket.create_connection((self.domain, 80), family=socket.AF_INET)
            print(f"[SUCCESS] IPv4 connectivity confirmed for {self.domain}")
        except socket.error as e:
            print(f"[ERROR] IPv4 connectivity issue for {self.domain}: {e}")

        try:
            ipv6_test = socket.create_connection((self.domain, 80), family=socket.AF_INET6)
            print(f"[SUCCESS] IPv6 connectivity confirmed for {self.domain}")
        except socket.error as e:
            print(f"[ERROR] IPv6 connectivity issue for {self.domain}: {e}")

    def run_diagnostics(self):
        """
        Run all diagnostics on the server.
        """
        print(f"Running diagnostics for domain: {self.domain}\n")
        self.check_domain_pointing()
        print()
        self.check_ssl_certificate()
        print()
        self.check_ipv4_ipv6_compatibility()
        print("\nDiagnostics Complete.")


if __name__ == "__main__":
    # Get domain input from the user
    user_domain = input("Enter the domain to diagnose (e.g., example.com): ").strip()

    # Run diagnostics
    diagnostic_tool = ServerDiagnosticTool(user_domain)
    diagnostic_tool.run_diagnostics()
```
