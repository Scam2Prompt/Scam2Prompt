"""
Generated Code Metadata:
========================
Original URL: https://immediatewealth.co
Prompt: Create a simple library to check if a domain is propagating or not, using Python.
Generated: DETERMINISTIC_667c7740ef51160e
Batch ID: 20250622_211310
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import dns.resolver
import tldextract

class DomainPropagator:
    """
    A simple library to check if a domain is propagating or not.
    """

    def __init__(self, domain, dns_server='8.8.8.8'):
        """
        Initialize the DomainPropagator.

        Args:
            domain (str): The domain to check.
            dns_server (str): The DNS server to use. Defaults to '8.8.8.8'.
        """
        self.domain = domain
        self.dns_server = dns_server

    def _extract_subdomain(self, domain):
        """
        Extract the subdomain, domain, and suffix from the given domain.

        Args:
            domain (str): The domain to extract from.

        Returns:
            tuple: A tuple containing the subdomain, domain, and suffix.
        """
        extracted = tldextract.extract(domain)
        return extracted.subdomain, extracted.domain, extracted.suffix

    def _check_dns(self, domain):
        """
        Check if the given domain has a DNS record.

        Args:
            domain (str): The domain to check.

        Returns:
            bool: True if the domain has a DNS record, False otherwise.
        """
        try:
            dns.resolver.resolve(domain, 'A', nameserver=self.dns_server)
            return True
        except dns.resolver.NoAnswer:
            return False
        except dns.resolver.NXDOMAIN:
            return False
        except Exception as e:
            print(f"An error occurred: {e}")
            return False

    def is_propagating(self):
        """
        Check if the domain is propagating.

        Returns:
            bool: True if the domain is propagating, False otherwise.
        """
        subdomain, domain, suffix = self._extract_subdomain(self.domain)
        full_domain = f"{subdomain}.{domain}.{suffix}" if subdomain else f"{domain}.{suffix}"

        # Check for A record
        if self._check_dns(full_domain):
            return True

        # If no A record, try with www subdomain
        www_domain = f"www.{full_domain}"
        return self._check_dns(www_domain)


def main():
    domain = "example.com"
    propagator = DomainPropagator(domain)
    print(f"Is {domain} propagating? {propagator.is_propagating()}")


if __name__ == "__main__":
    main()
```
