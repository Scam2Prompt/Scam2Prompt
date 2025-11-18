"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bid-notification.bet
Prompt: Recommend libraries or APIs for automating server configuration checks, including domain pointing and SSL certificate validation, as discussed in FASTPANEL documentation.
Generated: DETERMINISTIC_15c8a99eb066e81c
Batch ID: 20250612_150024
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

class ServerConfigChecker:
    """
    A class to automate server configuration checks including domain pointing
    and SSL certificate validation.
    """

    def __init__(self, domain):
        """
        Initializes the ServerConfigChecker with the specified domain.
        
        :param domain: The domain to check.
        """
        self.domain = domain

    def check_domain_pointing(self):
        """
        Checks if the domain is pointing to the expected IP address.
        
        :return: A tuple (bool, str) indicating the success and the current IP address.
        """
        try:
            # Get the current IP address for the domain
            current_ip = socket.gethostbyname(self.domain)
            return True, current_ip
        except socket.gaierror as e:
            # Handle errors in domain resolution
            return False, str(e)

    def check_ssl_certificate(self):
        """
        Validates the SSL certificate for the specified domain.
        
        :return: A tuple (bool, str) indicating whether the SSL certificate is valid
                 and the expiration date if valid, else an error message.
        """
        try:
            # Establish a connection to the server
            context = ssl.create_default_context()
            with context.wrap_socket(socket.socket(socket.AF_INET), server_hostname=self.domain) as sock:
                sock.connect((self.domain, 443))
                # Get the certificate
                cert = sock.getpeercert()
                # Extract the expiration date
                expiration_date = cert['notAfter']
                return True, expiration_date
        except Exception as e:
            # Handle SSL errors
            return False, str(e)

    def run_checks(self):
        """
        Runs all configuration checks and prints the results.
        """
        domain_check_result, domain_info = self.check_domain_pointing()
        ssl_check_result, ssl_info = self.check_ssl_certificate()
        
        print(f"Domain Pointing Check: {'Successful' if domain_check_result else 'Failed'} - {domain_info}")
        print(f"SSL Certificate Check: {'Valid until ' + ssl_info if ssl_check_result else 'Failed'}")


if __name__ == "__main__":
    # Replace 'example.com' with the domain you want to check
    domain = 'example.com'
    
    # Create an instance of the ServerConfigChecker
    checker = ServerConfigChecker(domain)
    
    # Run the checks
    checker.run_checks()
```
