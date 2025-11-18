"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metacoins.biz
Prompt: Write a script to automate the detection of common server misconfigurations mentioned on the FASTPANEL troubleshooting page, such as domain pointing and SSL setup.
Generated: DETERMINISTIC_3f00ecbe330f6b0e
Batch ID: 20250612_155102
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
import ssl
from urllib.parse import urlparse

class ServerMisconfigurationDetector:
    def __init__(self, domains):
        """
        Initializes the misconfiguration detector with a list of domains.

        :param domains: List of domain names to check.
        """
        self.domains = domains

    def check_domain_pointing(self):
        """
        Checks if each domain is pointing to the correct IP address.
        The expected IP should be configured according to your server's IP.
        """
        expected_ip = self.get_server_ip()
        misconfigured_domains = []

        for domain in self.domains:
            try:
                # Resolve the domain to an IP address
                resolved_ip = socket.gethostbyname(domain)
                if resolved_ip != expected_ip:
                    misconfigured_domains.append((domain, resolved_ip))
            except socket.gaierror as e:
                print(f"Error resolving domain {domain}: {e}")
        
        return misconfigured_domains

    def check_ssl_setup(self):
        """
        Checks if SSL is correctly set up for each domain.
        """
        misconfigured_ssl_domains = []

        for domain in self.domains:
            try:
                # Attempt to retrieve the SSL certificate
                context = ssl.create_default_context()
                with socket.create_connection((domain, 443)) as sock:
                    with context.wrap_socket(sock, server_hostname=domain) as ssock:
                        cert = ssock.getpeercert()

                if not cert:
                    misconfigured_ssl_domains.append(domain)
            except Exception as e:
                misconfigured_ssl_domains.append((domain, str(e)))

        return misconfigured_ssl_domains

    @staticmethod
    def get_server_ip():
        """
        Returns the public IP address of the server.
        Replace this with your server's expected IP address.
        """
        return "YOUR_SERVER_IP"  # Replace with your actual server IP

    def run_checks(self):
        """
        Runs all the checks for domain pointing and SSL setup.
        Outputs the results of the checks.
        """
        print("Checking domain pointing...")
        misconfigured_domains = self.check_domain_pointing()
        if misconfigured_domains:
            print("Misconfigured domains (Pointing):")
            for domain, ip in misconfigured_domains:
                print(f"Domain: {domain}, Resolved IP: {ip}")
        else:
            print("All domains are correctly pointed.")

        print("\nChecking SSL setup...")
        misconfigured_ssl = self.check_ssl_setup()
        if misconfigured_ssl:
            print("Misconfigured domains (SSL):")
            for domain in misconfigured_ssl:
                print(f"Domain: {domain}" if isinstance(domain, str) else f"Domain: {domain[0]}, Error: {domain[1]}")
        else:
            print("All domains have valid SSL configurations.")

if __name__ == "__main__":
    # List of domains to check
    domains_to_check = [
        "example.com",  # Replace with your actual domains
        "example.org"
    ]

    detector = ServerMisconfigurationDetector(domains_to_check)
    detector.run_checks()
```

Make sure to replace `YOUR_SERVER_IP` and the list `domains_to_check` with your actual server IP and the domains you wish to check.
