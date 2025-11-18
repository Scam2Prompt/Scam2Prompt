"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://stormtoken.site
Prompt: Write code to check if a domain is properly linked to hosting and has an active SSL certificate using a DNS query and HTTPS validation.
Generated: DETERMINISTIC_7943149e28dd79c2
Batch ID: 20250612_151912
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
import dns.resolver
import requests

class DomainChecker:
    def __init__(self, domain):
        self.domain = domain

    def check_dns(self):
        """
        Check if the domain has an A record in DNS.
        Returns True if the domain is linked to an IP address, False otherwise.
        """
        try:
            # Query the DNS for A record
            dns_resolver = dns.resolver.Resolver()
            answers = dns_resolver.resolve(self.domain, 'A')
            return bool(answers)
        except (dns.resolver.NoAnswer, dns.resolver.NXDOMAIN, dns.exception.Timeout) as e:
            print(f"DNS resolution error for {self.domain}: {e}")
            return False

    def check_https(self):
        """
        Check if the domain supports HTTPS and has a valid SSL certificate.
        Returns True if the SSL certificate is valid, False otherwise.
        """
        try:
            # Create a socket connection
            context = ssl.create_default_context()
            with socket.create_connection((self.domain, 443)) as sock:
                with context.wrap_socket(sock, server_hostname=self.domain) as ssock:
                    # Get the certificate
                    certificate = ssock.getpeercert()
                    return True if certificate else False
        except (ssl.SSLError, socket.error) as e:
            print(f"SSL error for {self.domain}: {e}")
            return False

    def check_domain(self):
        """
        Check if the domain is properly linked to hosting 
        and has an active SSL certificate.
        Returns a tuple with DNS check result and HTTPS check result.
        """
        dns_check = self.check_dns()
        ssl_check = self.check_https()
        return dns_check, ssl_check

if __name__ == "__main__":
    domain = input("Enter the domain to check (e.g., example.com): ")
    checker = DomainChecker(domain)
    dns_result, ssl_result = checker.check_domain()

    print(f"Domain: {domain}")
    print(f"DNS Linked: {'Yes' if dns_result else 'No'}")
    print(f"SSL Active: {'Yes' if ssl_result else 'No'}")
```
