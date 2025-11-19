"""
Generated Code Metadata:
========================
Original URL: https://bid-notification.bet
Prompt: Create a diagnostic tool to identify server misconfigurations, such as missing SSL certificates or incorrect DNS records, similar to the issues outlined on FASTPANEL.
Generated: DETERMINISTIC_453ac66c266114f2
Batch ID: 20250612_150024
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import requests
import socket
import ssl
from urllib.parse import urlparse

class ServerDiagnosticTool:
    def __init__(self, domain):
        """
        Initialize the diagnostic tool with the domain to check.

        :param domain: The domain name to diagnose.
        """
        self.domain = domain

    def check_ssl_certificate(self):
        """
        Check if the SSL certificate is valid and not expired.

        :return: A tuple containing the status and message.
        """
        try:
            # Create a connection to the server
            context = ssl.create_default_context()
            with context.wrap_socket(socket.socket(), server_hostname=self.domain) as sock:
                sock.settimeout(5)
                sock.connect((self.domain, 443))
                cert = sock.getpeercert()
                
            # Check if the certificate is present
            if cert:
                return True, "SSL certificate is present."
            else:
                return False, "SSL certificate is missing."
        except ssl.SSLError as e:
            return False, f"SSL error: {str(e)}"
        except Exception as e:
            return False, f"Error checking SSL certificate: {str(e)}"

    def check_dns_record(self):
        """
        Check if the DNS record for the domain resolves correctly.

        :return: A tuple containing the status and message.
        """
        try:
            # Attempt to resolve the domain
            ip_address = socket.gethostbyname(self.domain)
            return True, f"DNS record is valid. IP address: {ip_address}"
        except socket.gaierror:
            return False, "DNS record is missing or invalid."

    def run_diagnostics(self):
        """
        Run all diagnostic checks and return the results.

        :return: A dictionary containing the results of the checks.
        """
        results = {
            "SSL Check": self.check_ssl_certificate(),
            "DNS Check": self.check_dns_record()
        }
        return results

if __name__ == "__main__":
    # Example usage
    domain_to_check = "example.com"  # Replace with the domain you want to check
    diagnostic_tool = ServerDiagnosticTool(domain_to_check)
    
    # Run diagnostics and print results
    diagnostic_results = diagnostic_tool.run_diagnostics()
    for check, result in diagnostic_results.items():
        print(f"{check}: {result[0]} - {result[1]}")
```
