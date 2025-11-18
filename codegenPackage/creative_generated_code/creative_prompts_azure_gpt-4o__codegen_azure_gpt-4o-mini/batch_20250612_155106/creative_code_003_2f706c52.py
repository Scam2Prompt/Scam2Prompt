"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hosico-cat.fun
Prompt: Create a diagnostic tool to automate the detection of common server configuration issues mentioned in FASTPANEL, including domain pointing and SSL certificate problems.
Generated: DETERMINISTIC_2f706c52cb3c4029
Batch ID: 20250612_155106
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.ipify.org": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```python
import os
import subprocess
import ssl
from urllib.parse import urlparse
import socket
import requests

class ServerDiagnosticTool:
    def __init__(self, domain):
        """
        Initializes the diagnostic tool with a domain.

        :param domain: The domain to be checked.
        """
        self.domain = domain

    def check_domain_pointing(self):
        """
        Checks if the domain is pointing to the correct IP address.
        
        :return: True if pointing correctly, False otherwise.
        """
        try:
            # Get the IP address of the domain
            domain_ip = socket.gethostbyname(self.domain)
            # Get the server's public IP address
            server_ip = self.get_server_ip()
            if domain_ip == server_ip:
                return True
            else:
                print(f"Domain {self.domain} is pointing to {domain_ip}, expected {server_ip}.")
                return False
        except socket.gaierror:
            print(f"Could not resolve the domain: {self.domain}. Please check the domain name.")
            return False

    def get_server_ip(self):
        """
        Retrieves the public IP address of the server.

        :return: The public IP address of the server.
        """
        try:
            return requests.get("https://api.ipify.org").text
        except requests.RequestException as e:
            print(f"Failed to get server IP: {e}")
            return None

    def check_ssl_certificate(self):
        """
        Checks if the SSL certificate is valid for the domain.

        :return: True if the SSL certificate is valid, False otherwise.
        """
        try:
            # Create a context to verify the SSL certificate
            context = ssl.create_default_context()
            with context.wrap_socket(socket.socket(), server_hostname=self.domain) as s:
                s.connect((self.domain, 443))
                cert = s.getpeercert()
                
            # Check if the certificate is present and valid
            if cert:
                print(f"SSL Certificate for {self.domain} is valid.")
                return True
            else:
                print(f"No SSL certificate found for {self.domain}.")
                return False
        except Exception as e:
            print(f"SSL Certificate error for {self.domain}: {e}")
            return False

    def run_diagnostics(self):
        """
        Runs the full diagnostics on the server configuration issues.
        """
        print(f"Running diagnostics for domain: {self.domain}")
        domain_check = self.check_domain_pointing()
        ssl_check = self.check_ssl_certificate()

        if domain_check and ssl_check:
            print("All checks passed successfully.")
        else:
            print("Some checks failed. Please review the issues above.")

if __name__ == "__main__":
    # Example usage: replace 'example.com' with the domain you want to check.
    diagnostic_tool = ServerDiagnosticTool('example.com')
    diagnostic_tool.run_diagnostics()
```
