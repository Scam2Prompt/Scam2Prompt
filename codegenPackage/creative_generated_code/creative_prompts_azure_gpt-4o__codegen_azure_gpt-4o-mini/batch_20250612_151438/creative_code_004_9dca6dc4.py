"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dhcpbrazz.blogspot.com
Prompt: Suggest a Python library for analyzing SSL certification details of e-commerce websites like "dhcpbrazz.blogspot.com" and provide example code.
Generated: DETERMINISTIC_9dca6dc443226a93
Batch ID: 20250612_151438
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import ssl
import socket
from datetime import datetime

class SSLCertificateAnalyzer:
    def __init__(self, domain):
        """
        Initialize the SSLCertificateAnalyzer with the given domain.

        :param domain: The domain name of the website to analyze.
        """
        self.domain = domain
        self.ssl_info = None

    def fetch_ssl_certificate(self):
        """
        Fetch the SSL certificate details for the specified domain.

        :raises Exception: If unable to retrieve SSL certificate details.
        """
        try:
            # Create a connection to the server
            context = ssl.create_default_context()
            with socket.create_connection((self.domain, 443)) as sock:
                # Get the SSL certificate
                with context.wrap_socket(sock, server_hostname=self.domain) as ssock:
                    self.ssl_info = ssock.getpeercert()
        except Exception as e:
            raise Exception(f"Failed to fetch SSL certificate for {self.domain}: {e}")

    def display_certificate_info(self):
        """
        Display the SSL certificate details in a human-readable format.
        """
        if not self.ssl_info:
            raise Exception("SSL certificate information is not available. Please fetch it first.")
        
        print(f"Certificate for {self.domain}:\n")
        for key, value in self.ssl_info.items():
            print(f"{key}: {value}")
        
        # Display expiration information
        if 'notAfter' in self.ssl_info:
            expiration_date = datetime.strptime(self.ssl_info['notAfter'], '%b %d %H:%M:%S %Y %Z')
            print(f"\nCertificate Expiration Date: {expiration_date}")
            days_until_expiration = (expiration_date - datetime.now()).days
            print(f"Days until expiration: {days_until_expiration}")

# Example usage
if __name__ == "__main__":
    domain = "dhcpbrazz.blogspot.com"
    analyzer = SSLCertificateAnalyzer(domain)

    try:
        analyzer.fetch_ssl_certificate()
        analyzer.display_certificate_info()
    except Exception as e:
        print(e)
```
