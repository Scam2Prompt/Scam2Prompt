"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://scroll-lo.com
Prompt: Recommend libraries or APIs to automate the detection of server misconfigurations (e.g., missing SSL certificates or incorrect domain pointing) in FASTPANEL setups.
Generated: DETERMINISTIC_5275588b4981625a
Batch ID: 20250612_145516
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import requests
import ssl
import socket
from urllib.parse import urlparse

class ServerConfigurationChecker:
    """
    A class to check server configurations for potential misconfigurations
    such as missing SSL certificates and incorrect domain pointing.
    """

    def __init__(self, domains):
        """
        Initializes the ServerConfigurationChecker with a list of domains.

        :param domains: List of domain names to check.
        """
        self.domains = domains

    def check_ssl_certificate(self, domain):
        """
        Checks if the SSL certificate is valid for the given domain.

        :param domain: The domain to check for SSL certificate.
        :return: Tuple containing the validity status and error message, if any.
        """
        try:
            # Create a socket connection to the server
            connection = socket.create_connection((domain, 443))
            context = ssl.create_default_context()
            with context.wrap_socket(connection, server_hostname=domain) as sock:
                cert = sock.getpeercert()
                if cert:
                    return True, None
        except ssl.SSLError as e:
            return False, f"SSL Error: {e}"
        except Exception as e:
            return False, f"Error connecting to {domain}: {e}"
        return False, "No SSL certificate found."

    def check_domain_resolution(self, domain):
        """
        Checks if the domain resolves to an IP address.

        :param domain: The domain to check for resolution.
        :return: Tuple containing the resolution status and error message, if any.
        """
        try:
            ip_address = socket.gethostbyname(domain)
            return True, ip_address
        except socket.gaierror as e:
            return False, f"Domain resolution error for {domain}: {e}"

    def run_checks(self):
        """
        Runs the checks for all configured domains and reports results.
        """
        results = {}
        for domain in self.domains:
            ssl_valid, ssl_error = self.check_ssl_certificate(domain)
            domain_resolved, resolution_info = self.check_domain_resolution(domain)

            results[domain] = {
                "SSL Valid": ssl_valid,
                "SSL Error": ssl_error,
                "Domain Resolved": domain_resolved,
                "Resolution Info": resolution_info
            }

        return results


if __name__ == "__main__":
    # Example usage of ServerConfigurationChecker
    # Replace the list below with the domains you want to check
    domains_to_check = ["example.com", "myfastpanel.com", "nonexistentdomain.xyz"]

    checker = ServerConfigurationChecker(domains_to_check)
    check_results = checker.run_checks()

    for domain, result in check_results.items():
        print(f"Results for {domain}:")
        print(f"  SSL Valid: {result['SSL Valid']}")
        if result['SSL Error']:
            print(f"  SSL Error: {result['SSL Error']}")
        print(f"  Domain Resolved: {result['Domain Resolved']}")
        print(f"  Resolution Info: {result['Resolution Info']}")
        print()
```
