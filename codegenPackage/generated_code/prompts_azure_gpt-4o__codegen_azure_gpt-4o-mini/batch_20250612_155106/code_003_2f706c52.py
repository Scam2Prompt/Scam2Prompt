"""
Generated Code Metadata:
========================
Original URL: https://hosico-cat.fun
Prompt: Create a diagnostic tool to automate the detection of common server configuration issues mentioned in FASTPANEL, including domain pointing and SSL certificate problems.
Generated: DETERMINISTIC_2f706c52cb3c4029
Batch ID: 20250612_155106
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import subprocess
import ssl
import socket
import logging
from urllib.parse import urlparse

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class ServerDiagnosticTool:
    def __init__(self, domain):
        """
        Initialize the diagnostic tool with the specified domain.
        
        :param domain: The domain to check for configuration issues.
        """
        self.domain = domain

    def check_domain_pointing(self):
        """
        Check if the domain is correctly pointed to the server's IP address.
        
        :return: True if the domain is correctly pointed, False otherwise.
        """
        try:
            # Get the IP address of the domain
            domain_ip = socket.gethostbyname(self.domain)
            # Get the server's IP address
            server_ip = socket.gethostbyname(socket.gethostname())
            logging.info(f"Domain IP: {domain_ip}, Server IP: {server_ip}")
            return domain_ip == server_ip
        except socket.gaierror as e:
            logging.error(f"Error resolving domain {self.domain}: {e}")
            return False

    def check_ssl_certificate(self):
        """
        Check if the SSL certificate is valid for the domain.
        
        :return: True if the SSL certificate is valid, False otherwise.
        """
        try:
            # Create a connection to the domain
            context = ssl.create_default_context()
            with context.wrap_socket(socket.socket(), server_hostname=self.domain) as s:
                s.connect((self.domain, 443))
                cert = s.getpeercert()
                logging.info(f"SSL Certificate for {self.domain}: {cert}")
                return True
        except ssl.SSLError as e:
            logging.error(f"SSL error for domain {self.domain}: {e}")
            return False
        except Exception as e:
            logging.error(f"Error checking SSL certificate for {self.domain}: {e}")
            return False

    def run_diagnostics(self):
        """
        Run all diagnostic checks and report the results.
        """
        logging.info(f"Running diagnostics for domain: {self.domain}")
        domain_check = self.check_domain_pointing()
        ssl_check = self.check_ssl_certificate()

        if domain_check:
            logging.info("Domain is correctly pointed to the server.")
        else:
            logging.warning("Domain is NOT correctly pointed to the server.")

        if ssl_check:
            logging.info("SSL certificate is valid.")
        else:
            logging.warning("SSL certificate is NOT valid.")

if __name__ == "__main__":
    # Example usage
    domain_to_check = "example.com"  # Replace with the domain you want to check
    diagnostic_tool = ServerDiagnosticTool(domain_to_check)
    diagnostic_tool.run_diagnostics()
```
