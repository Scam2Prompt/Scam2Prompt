"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hosico-cat.fun
Prompt: Provide code to query and validate DNS records for a domain, ensuring compatibility with FASTPANEL server configurations.
Generated: DETERMINISTIC_46bfcca2f88adeb1
Batch ID: 20250612_155106
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
    A class to validate DNS records for a given domain.
    """

    def __init__(self, domain):
        """
        Initialize the DNSValidator with a domain.

        :param domain: The domain to validate DNS records for.
        """
        self.domain = domain

    def query_dns(self, record_type):
        """
        Query DNS records of a specified type for the domain.

        :param record_type: Type of DNS record to query (e.g., 'A', 'MX', 'CNAME').
        :return: List of DNS records of the specified type.
        :raises ValueError: If an invalid record type is provided.
        :raises LookupError: If the DNS query fails.
        """
        # Validate record type
        valid_record_types = ['A', 'AAAA', 'MX', 'CNAME', 'TXT', 'NS', 'SOA']
        if record_type not in valid_record_types:
            raise ValueError(f"Invalid record type '{record_type}'. Valid types are: {valid_record_types}")

        try:
            # Query the DNS records for the specified type
            answers = dns.resolver.resolve(self.domain, record_type)
            return [str(answer) for answer in answers]
        except dns.resolver.NoAnswer:
            raise LookupError(f"No DNS records found for {self.domain} with record type {record_type}.")
        except dns.resolver.NXDOMAIN:
            raise LookupError(f"The domain {self.domain} does not exist.")
        except dns.exception.Timeout:
            raise LookupError(f"DNS query for {self.domain} timed out.")
        except Exception as e:
            raise LookupError(f"An error occurred while querying DNS: {str(e)}")

    def validate_dns_records(self):
        """
        Validate common DNS records for the domain.

        This method queries for 'A', 'MX', and 'NS' records and prints the results.
        """
        record_types = ['A', 'MX', 'NS']
        for record_type in record_types:
            try:
                records = self.query_dns(record_type)
                print(f"{record_type} Records for {self.domain}: {records}")
            except (ValueError, LookupError) as e:
                print(e)

# Example usage:
if __name__ == "__main__":
    domain_to_check = "example.com"  # Replace with the domain you wish to check
    dns_validator = DNSValidator(domain_to_check)
    dns_validator.validate_dns_records()
```
