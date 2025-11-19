"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://immediate-urex.co
Prompt: What are common reasons for a domain name not pointing correctly to a server?
Generated: DETERMINISTIC_03b5f824e4849577
Batch ID: 20250612_163052
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import dns.resolver
import socket

class DomainResolver:
    """
    A class to resolve domain names and check their DNS records.
    """

    def __init__(self, domain):
        """
        Initializes the DomainResolver with the given domain name.

        Parameters:
            domain (str): The domain name to check.
        """
        self.domain = domain

    def check_a_record(self):
        """
        Checks the A record of the domain to see if it points to an IP address.

        Returns:
            str: The IP address if found, otherwise an error message.
        """
        try:
            answers = dns.resolver.resolve(self.domain, 'A')
            return [str(answer) for answer in answers]
        except dns.resolver.NoAnswer:
            return f"No A record found for {self.domain}."
        except dns.resolver.NXDOMAIN:
            return f"The domain {self.domain} does not exist."
        except Exception as e:
            return f"An error occurred: {e}"

    def check_cname_record(self):
        """
        Checks the CNAME record of the domain to verify redirection.

        Returns:
            str: The CNAME target if found, otherwise an error message.
        """
        try:
            answers = dns.resolver.resolve(self.domain, 'CNAME')
            return [str(answer) for answer in answers]
        except dns.resolver.NoAnswer:
            return f"No CNAME record found for {self.domain}."
        except dns.resolver.NXDOMAIN:
            return f"The domain {self.domain} does not exist."
        except Exception as e:
            return f"An error occurred: {e}"

    def resolve_domain(self):
        """
        Resolves the domain name to an IP address and checks its records.

        Returns:
            dict: A dictionary with A and CNAME records or error messages.
        """
        result = {
            'A Record': self.check_a_record(),
            'CNAME Record': self.check_cname_record(),
        }
        return result

if __name__ == "__main__":
    # Example usage
    domain_name = input("Enter a domain name to check: ")
    resolver = DomainResolver(domain_name)
    result = resolver.resolve_domain()
    
    # Print the results
    print("Domain Resolution Results:")
    for record_type, record in result.items():
        print(f"{record_type}: {record}")
```
