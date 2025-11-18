"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://app.rpcapirestore.site
Prompt: Write a program to validate server settings for a domain, ensuring proper HTTPS access and IPv4 compatibility, as discussed in FASTPANEL's domain troubleshooting guide.
Generated: DETERMINISTIC_ec0fcf01ffcb402c
Batch ID: 20250612_150448
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

class DomainValidator:
    def __init__(self, domain):
        """
        Initialize the DomainValidator with the given domain.
        
        :param domain: The domain to validate
        """
        self.domain = domain

    def validate_https(self):
        """
        Validate if the domain supports HTTPS by attempting to establish a secure connection.
        
        :return: True if HTTPS is supported, False otherwise
        """
        try:
            # Attempt to establish a secure connection
            context = ssl.create_default_context()
            with context.wrap_socket(socket.socket(), server_hostname=self.domain) as sock:
                sock.connect((self.domain, 443))
            return True
        except Exception as e:
            print(f"HTTPS validation failed: {e}")
            return False

    def validate_ipv4(self):
        """
        Validate if the domain resolves to an IPv4 address.
        
        :return: True if an IPv4 address is resolved, False otherwise
        """
        try:
            ip_addresses = socket.getaddrinfo(self.domain, None)
            for ip in ip_addresses:
                if ip[0] == socket.AF_INET:  # Check for IPv4 address
                    return True
            return False
        except Exception as e:
            print(f"IPv4 validation failed: {e}")
            return False

    def validate_domain(self):
        """
        Validate both HTTPS support and IPv4 compatibility for the domain.
        
        :return: A tuple of validation results (https_supported, ipv4_compatible)
        """
        https_supported = self.validate_https()
        ipv4_compatible = self.validate_ipv4()
        return https_supported, ipv4_compatible

def main():
    """
    Main function to run the domain validation process.
    """
    domain = input("Enter the domain to validate (e.g., example.com): ")
    validator = DomainValidator(domain)
    
    https_supported, ipv4_compatible = validator.validate_domain()
    
    # Output the results of the validations
    print(f"Domain: {domain}")
    print(f"HTTPS Supported: {'Yes' if https_supported else 'No'}")
    print(f"IPv4 Compatible: {'Yes' if ipv4_compatible else 'No'}")

if __name__ == "__main__":
    main()
```
