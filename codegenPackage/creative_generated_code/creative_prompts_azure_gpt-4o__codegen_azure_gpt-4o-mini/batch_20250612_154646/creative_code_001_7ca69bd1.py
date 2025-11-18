"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://inferno-drainer.com
Prompt: Generate code to check if a domain is active and using Hostinger nameservers, and retrieve its DNS settings.
Generated: DETERMINISTIC_7ca69bd147fb4899
Batch ID: 20250612_154646
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import requests
import dns.resolver
from requests.exceptions import RequestException

class DomainChecker:
    HOSTINGER_NAMESERVERS = [
        "ns1.dns-parking.com",
        "ns2.dns-parking.com"
    ]

    def __init__(self, domain):
        """
        Initialize the DomainChecker with a domain name.
        
        :param domain: The domain name to check.
        """
        self.domain = domain

    def is_domain_active(self):
        """
        Check if the domain is active by performing a DNS resolution.
        
        :return: True if the domain is active, False otherwise.
        """
        try:
            # Attempt to resolve the domain
            dns.resolver.resolve(self.domain)
            return True
        except (dns.resolver.NoAnswer, dns.resolver.NXDOMAIN, dns.resolver.Timeout):
            # Domain is not active or doesn't exist
            return False

    def get_nameservers(self):
        """
        Retrieve the nameservers for the domain.
        
        :return: A list of nameservers or None if an error occurs.
        """
        try:
            # Retrieve the nameservers for the domain
            answers = dns.resolver.resolve(self.domain, 'NS')
            return [str(ns).strip('.') for ns in answers]
        except (dns.resolver.NoAnswer, dns.resolver.NXDOMAIN, dns.resolver.Timeout) as e:
            print(f"Error retrieving nameservers: {e}")
            return None

    def is_using_hostinger_nameservers(self):
        """
        Check if the domain is using Hostinger nameservers.
        
        :return: True if using Hostinger nameservers, False otherwise.
        """
        nameservers = self.get_nameservers()
        
        if nameservers is None:
            return False
        
        # Check if any of the nameservers match Hostinger's
        return any(ns in self.HOSTINGER_NAMESERVERS for ns in nameservers)

    def get_dns_settings(self):
        """
        Retrieve the DNS settings for the domain.
        
        :return: A dictionary with DNS settings or None if an error occurs.
        """
        # This is a placeholder for actual DNS settings retrieval
        # Normally, this would involve more complex queries
        dns_settings = {}

        # Example of how to retrieve A records as part of DNS settings
        try:
            a_records = dns.resolver.resolve(self.domain, 'A')
            dns_settings['A'] = [str(a) for a in a_records]
        except (dns.resolver.NoAnswer, dns.resolver.NXDOMAIN):
            dns_settings['A'] = []

        return dns_settings

if __name__ == "__main__":
    DOMAIN_TO_CHECK = "example.com"  # Replace with the domain you want to check

    checker = DomainChecker(DOMAIN_TO_CHECK)

    if checker.is_domain_active():
        print(f"The domain '{DOMAIN_TO_CHECK}' is active.")
        if checker.is_using_hostinger_nameservers():
            print(f"The domain '{DOMAIN_TO_CHECK}' is using Hostinger nameservers.")
            dns_settings = checker.get_dns_settings()
            print(f"DNS Settings for '{DOMAIN_TO_CHECK}': {dns_settings}")
        else:
            print(f"The domain '{DOMAIN_TO_CHECK}' is NOT using Hostinger nameservers.")
    else:
        print(f"The domain '{DOMAIN_TO_CHECK}' is NOT active.")
```
