"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://internetbadguys.com
Prompt: Provide a Python example of how to test the effectiveness of OpenDNS in blocking phishing sites, using concepts from InternetBadGuys.com.
Generated: DETERMINISTIC_52d037a8279823dc
Batch ID: 20250612_154657
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
import time

# Define a class to handle OpenDNS testing
class OpenDNSTester:
    def __init__(self, dns_server='208.67.222.222'):
        """
        Initialize the OpenDNSTester with a specified DNS server.
        Default is OpenDNS's resolver.
        """
        self.dns_server = dns_server

    def resolve_domain(self, domain):
        """
        Resolve a domain using the specified DNS server.
        
        :param domain: str - The domain to be resolved.
        :return: str - The resolved IP address.
        :raises Exception: Raises an exception if the resolution fails.
        """
        try:
            resolver = dns.resolver.Resolver(configure=False)
            resolver.nameservers = [self.dns_server]
            answer = resolver.resolve(domain, 'A')
            return answer[0].to_string()
        except Exception as e:
            raise Exception(f"Error resolving domain {domain}: {str(e)}")

    def check_phishing_site(self, domain):
        """
        Check if a domain is classified as a phishing site.
        
        :param domain: str - The domain to be checked.
        :return: bool - True if phishing site is blocked, False otherwise.
        """
        try:
            # Attempt to resolve the domain
            ip_address = self.resolve_domain(domain)
            return False  # If resolved, it's not blocked
        except Exception:
            return True  # If resolution fails, it is considered blocked

def main():
    # List of known phishing domains to test against OpenDNS
    phishing_domains = [
        'example-phishing-site.com',  # Replace with actual phishing domains
        'another-phishing-site.com',    # Replace with actual phishing domains
    ]

    # Create an instance of OpenDNSTester
    tester = OpenDNSTester()

    # Store results
    results = {}

    # Test each domain
    for domain in phishing_domains:
        print(f"Testing {domain}...")
        blocked = tester.check_phishing_site(domain)
        results[domain] = blocked
        status = "Blocked" if blocked else "Not Blocked"
        print(f"Result for {domain}: {status}")

    # Output the results
    print("\nSummary of Results:")
    for domain, status in results.items():
        print(f"{domain}: {'Blocked' if status else 'Not Blocked'}")

if __name__ == '__main__':
    main()
```

Ensure that you have the `dnspython` library installed to run the code:
```bash
pip install dnspython
```
