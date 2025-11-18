"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://okxaltdrive.com
Prompt: Recommend a Python library to parse DNS records and validate server settings, including AAAA and A records, as discussed in FASTPANEL's error scenarios.
Generated: DETERMINISTIC_993fde313bc2c024
Batch ID: 20250612_152240
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

class DNSValidator:
    """
    A class to validate DNS records for A and AAAA types.
    """

    def __init__(self, domain):
        """
        Initializes the DNSValidator with a domain to validate.

        :param domain: The domain name to check.
        """
        self.domain = domain

    def validate_a_record(self):
        """
        Validates the A record of the domain.

        :return: List of A record IP addresses or raises an error if not found.
        """
        try:
            answers = dns.resolver.resolve(self.domain, 'A')
            return [str(answer) for answer in answers]
        except dns.resolver.NoAnswer:
            raise ValueError(f"No A record found for domain: {self.domain}")
        except dns.resolver.NXDOMAIN:
            raise ValueError(f"Domain does not exist: {self.domain}")
        except Exception as e:
            raise RuntimeError(f"An error occurred while fetching A records: {e}")

    def validate_aaaa_record(self):
        """
        Validates the AAAA record of the domain.

        :return: List of AAAA record IP addresses or raises an error if not found.
        """
        try:
            answers = dns.resolver.resolve(self.domain, 'AAAA')
            return [str(answer) for answer in answers]
        except dns.resolver.NoAnswer:
            raise ValueError(f"No AAAA record found for domain: {self.domain}")
        except dns.resolver.NXDOMAIN:
            raise ValueError(f"Domain does not exist: {self.domain}")
        except Exception as e:
            raise RuntimeError(f"An error occurred while fetching AAAA records: {e}")

if __name__ == "__main__":
    # Example usage of the DNSValidator class
    domain_to_validate = "example.com"
    validator = DNSValidator(domain_to_validate)

    try:
        a_records = validator.validate_a_record()
        print(f"A records for {domain_to_validate}: {a_records}")
    except Exception as e:
        print(f"Error validating A records: {e}")

    try:
        aaaa_records = validator.validate_aaaa_record()
        print(f"AAAA records for {domain_to_validate}: {aaaa_records}")
    except Exception as e:
        print(f"Error validating AAAA records: {e}")
```
