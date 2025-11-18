"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://876981455175.icu
Prompt: Suggest an API or library to validate server configurations for FASTPANEL-hosted domains, focusing on IPv4 compatibility and SSL certificate presence.
Generated: DETERMINISTIC_784f648065f9fd07
Batch ID: 20250612_154215
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

class DomainValidator:
    """
    A class to validate server configurations for FASTPANEL-hosted domains.
    It checks for IPv4 compatibility and the presence of SSL certificates.
    """

    def __init__(self, domain):
        """
        Initializes the DomainValidator with a given domain.

        :param domain: str - The domain to validate.
        """
        self.domain = domain

    def validate_ipv4(self):
        """
        Validates if the domain resolves to an IPv4 address.

        :return: bool - True if the domain has an IPv4 address, False otherwise.
        """
        try:
            ip_address = socket.gethostbyname(self.domain)
            return self.is_ipv4(ip_address)
        except socket.gaierror as e:
            print(f"Error resolving domain {self.domain}: {e}")
            return False

    @staticmethod
    def is_ipv4(ip_address):
        """
        Checks if an IP address is an IPv4 address.

        :param ip_address: str - The IP address to check.
        :return: bool - True if the IP address is IPv4, False otherwise.
        """
        try:
            socket.inet_pton(socket.AF_INET, ip_address)
            return True
        except socket.error:
            return False

    def validate_ssl_certificate(self):
        """
        Validates if the domain has a valid SSL certificate.

        :return: bool - True if the SSL certificate is present and valid, False otherwise.
        """
        try:
            context = ssl.create_default_context()
            with context.wrap_socket(socket.socket(), server_hostname=self.domain) as s:
                s.connect((self.domain, 443))
                cert = s.getpeercert()
                return cert is not None
        except Exception as e:
            print(f"Error validating SSL certificate for {self.domain}: {e}")
            return False

    def validate_domain(self):
        """
        Validates both IPv4 compatibility and SSL certificate presence.

        :return: dict - A summary of validation results.
        """
        return {
            'domain': self.domain,
            'ipv4_valid': self.validate_ipv4(),
            'ssl_valid': self.validate_ssl_certificate()
        }

if __name__ == "__main__":
    # Example usage
    domain_to_validate = "example.com"  # Replace with the domain you want to validate
    validator = DomainValidator(domain_to_validate)
    validation_results = validator.validate_domain()
    
    print("Validation Results:")
    print(validation_results)
```
