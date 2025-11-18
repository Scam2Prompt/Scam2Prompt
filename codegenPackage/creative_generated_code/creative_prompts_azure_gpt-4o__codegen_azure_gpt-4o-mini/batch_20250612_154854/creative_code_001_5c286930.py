"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mrspongy.com
Prompt: Recommend an API or library to integrate Cloudflare's 1.1.1.1 DNS resolver into a Python application for improved security and performance.
Generated: DETERMINISTIC_5c286930c839be7d
Batch ID: 20250612_154854
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import dns.resolver
import dns.exception

class DNSResolver:
    """
    A class to interface with Cloudflare's 1.1.1.1 DNS resolver.
    """

    def __init__(self, resolver_ip='1.1.1.1'):
        """
        Initializes the DNSResolver with a specified resolver IP.

        :param resolver_ip: The IP address of the DNS resolver (default: 1.1.1.1).
        """
        self.resolver = dns.resolver.Resolver()
        self.resolver.nameservers = [resolver_ip]

    def resolve(self, domain):
        """
        Resolves a domain name to its IP address using the specified DNS resolver.

        :param domain: The domain name to resolve.
        :return: A list of IP addresses associated with the domain.
        :raises ValueError: If the domain name is invalid.
        :raises Exception: If there is an error during the DNS resolution.
        """
        if not isinstance(domain, str):
            raise ValueError("Domain must be a string.")

        try:
            # Query the DNS records for the domain
            answers = self.resolver.resolve(domain)
            return [answer.to_text() for answer in answers]
        except dns.resolver.NoAnswer:
            raise Exception(f"No answer for the domain: {domain}")
        except dns.resolver.NXDOMAIN:
            raise Exception(f"The domain {domain} does not exist.")
        except dns.exception.Timeout:
            raise Exception("DNS query timed out.")
        except Exception as e:
            raise Exception(f"An error occurred while resolving the domain: {e}")

if __name__ == "__main__":
    # Example usage of the DNSResolver class
    dns_resolver = DNSResolver()
    domain_to_resolve = "example.com"

    try:
        ip_addresses = dns_resolver.resolve(domain_to_resolve)
        print(f"IP addresses for {domain_to_resolve}: {ip_addresses}")
    except Exception as e:
        print(f"Error: {e}")
```
