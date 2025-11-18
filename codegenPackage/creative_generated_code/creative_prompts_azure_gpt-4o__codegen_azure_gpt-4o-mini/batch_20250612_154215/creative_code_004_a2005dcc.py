"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://876981455175.icu
Prompt: Write a diagnostic tool in Python to identify why a FASTPANEL-hosted website is inaccessible, considering domain pointing, SSL installation, and IPv4/IPv6 compatibility.
Generated: DETERMINISTIC_a2005dcccc1c7c9f
Batch ID: 20250612_154215
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

class DiagnosticTool:
    def __init__(self, domain):
        """
        Initializes the DiagnosticTool with the specified domain.

        :param domain: The domain to be diagnosed.
        """
        self.domain = domain

    def check_domain_resolution(self):
        """
        Checks if the domain resolves to an IP address.

        :return: The resolved IP address or an error message.
        """
        try:
            ip_address = socket.gethostbyname(self.domain)
            return f"Domain {self.domain} resolves to IP: {ip_address}"
        except socket.gaierror:
            return f"Error: Domain {self.domain} could not be resolved."

    def check_ssl_cert(self):
        """
        Checks if an SSL certificate is installed for the domain.

        :return: SSL certificate status message.
        """
        try:
            # Establish a connection to the server to retrieve the SSL certificate
            hostname = self.domain
            port = 443
            context = ssl.create_default_context()
            with context.wrap_socket(socket.socket(socket.AF_INET), server_hostname=hostname) as s:
                s.connect((hostname, port))
                ssl_info = s.getpeercert()
            return f"SSL Certificate is installed for {self.domain}."
        except Exception as e:
            return f"Error: SSL Certificate could not be verified for {self.domain}. Details: {str(e)}"

    def check_ipv4_ipv6(self):
        """
        Checks if the domain is accessible via IPv4 and IPv6.

        :return: Availability status for IPv4 and IPv6.
        """
        results = {}
        for family in [socket.AF_INET, socket.AF_INET6]:
            try:
                ip_address = socket.getaddrinfo(self.domain, None, family)
                results[socket.AddressFamily(family).name] = f"Domain {self.domain} is accessible via {socket.AddressFamily(family).name}."
            except socket.gaierror:
                results[socket.AddressFamily(family).name] = f"Error: Domain {self.domain} is not accessible via {socket.AddressFamily(family).name}."
        return results

    def run_diagnostics(self):
        """
        Runs all diagnostic checks for the specified domain.

        :return: A dictionary containing the results of the diagnostic checks.
        """
        diagnostics = {
            "Domain Resolution": self.check_domain_resolution(),
            "SSL Certificate": self.check_ssl_cert(),
            "IPv4/IPv6 Compatibility": self.check_ipv4_ipv6()
        }
        return diagnostics

if __name__ == "__main__":
    # Replace 'example.com' with the domain you wish to check
    domain_to_check = 'example.com'
    diagnostic_tool = DiagnosticTool(domain_to_check)
    results = diagnostic_tool.run_diagnostics()

    # Print the results of the diagnostics
    for check, result in results.items():
        print(f"{check}: {result}")
```
