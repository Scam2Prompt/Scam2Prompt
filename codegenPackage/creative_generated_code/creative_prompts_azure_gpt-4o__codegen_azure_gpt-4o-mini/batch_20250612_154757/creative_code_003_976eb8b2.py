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
import ipaddress
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class ServerDiagnosticTool:
    def __init__(self, domain):
        self.domain = domain
    
    def check_domain_resolution(self):
        """Check if the domain resolves to an IP address."""
        try:
            ip = socket.gethostbyname(self.domain)
            logging.info(f"Domain {self.domain} resolves to IP: {ip}")
            return ip
        except socket.gaierror as e:
            logging.error(f"Domain resolution failed for {self.domain}: {e}")
            return None

    def check_ssl_certificate(self):
        """Check if the SSL certificate is present and valid."""
        try:
            # Get the SSL certificate
            cert = ssl.get_server_certificate((self.domain, 443))
            logging.info(f"SSL certificate retrieved for {self.domain}.")
            return cert
        except Exception as e:
            logging.error(f"SSL certificate retrieval failed for {self.domain}: {e}")
            return None

    def check_ipv4_ipv6_compatibility(self):
        """Check if the server supports both IPv4 and IPv6."""
        try:
            # Check for IPv4
            ipv4 = socket.gethostbyname(self.domain)
            logging.info(f"IPv4 address for {self.domain}: {ipv4}")

            # Check for IPv6
            ipv6 = socket.getaddrinfo(self.domain, None, socket.AF_INET6)
            logging.info(f"IPv6 address for {self.domain}: {ipv6[0][4][0]}")  # First IPv6 entry
            return True
        except socket.gaierror:
            logging.warning(f"IPv6 not supported for {self.domain}.")
            return False
            
    def run_diagnostics(self):
        """Run all diagnostic checks."""
        logging.info(f"Running diagnostics for {self.domain}...")
        domain_ip = self.check_domain_resolution()
        ssl_cert = self.check_ssl_certificate()
        ipv6_supported = self.check_ipv4_ipv6_compatibility()

        logging.info("Diagnostics completed.")
        return {
            'domain_ip': domain_ip,
            'ssl_cert': ssl_cert,
            'ipv6_supported': ipv6_supported
        }

if __name__ == "__main__":
    # Example usage
    domain_to_check = "example.com"  # Replace with your domain
    diagnostic_tool = ServerDiagnosticTool(domain_to_check)
    results = diagnostic_tool.run_diagnostics()
    print("Diagnostic Results:")
    print(results)
```
