"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://binairop.com
Prompt: Provide an example of how to configure DNS settings for a shared IP environment with multiple domains.
Generated: DETERMINISTIC_a0a6572d04df5e84
Batch ID: 20250612_163720
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import dns.resolver
import dns.update
import dns.query
import dns.exception

class DNSManager:
    """A class to manage DNS settings for multiple domains on a shared IP."""

    def __init__(self, server):
        """
        Initialize the DNSManager with the DNS server address.
        
        :param server: The DNS server to update records.
        """
        self.server = server

    def add_record(self, domain, record_type, record_value, ttl=300):
        """
        Add a DNS record for a specific domain.

        :param domain: The domain name to modify.
        :param record_type: The type of DNS record (A, CNAME, etc.).
        :param record_value: The value of the DNS record.
        :param ttl: Time to live for the DNS record (default is 300 seconds).
        """
        update = dns.update.Update(domain)
        update.add(domain, ttl, record_type, record_value)

        try:
            response = dns.query.tcp(update, self.server)
            print(f"Successfully added record: {domain} {record_type} {record_value}")
        except dns.exception.DNSException as e:
            print(f"Failed to add record: {e}")

    def remove_record(self, domain, record_type, record_value):
        """
        Remove a DNS record for a specific domain.

        :param domain: The domain name to modify.
        :param record_type: The type of DNS record (A, CNAME, etc.).
        :param record_value: The value of the DNS record to remove.
        """
        update = dns.update.Update(domain)
        update.remove(domain, record_type, record_value)

        try:
            response = dns.query.tcp(update, self.server)
            print(f"Successfully removed record: {domain} {record_type} {record_value}")
        except dns.exception.DNSException as e:
            print(f"Failed to remove record: {e}")

    def get_records(self, domain, record_type):
        """
        Retrieve DNS records for a specific domain.

        :param domain: The domain name to query.
        :param record_type: The type of DNS record to retrieve.
        :return: List of DNS records.
        """
        try:
            answers = dns.resolver.resolve(domain, record_type)
            return [str(answer) for answer in answers]
        except (dns.resolver.NoAnswer, dns.resolver.NXDOMAIN) as e:
            print(f"No records found for {domain} {record_type}: {e}")
            return []
        except Exception as e:
            print(f"Error querying records for {domain} {record_type}: {e}")
            return []

# Example usage
if __name__ == "__main__":
    dns_manager = DNSManager("8.8.8.8")  # Google Public DNS

    # Add an A record
    dns_manager.add_record("example.com", "A", "192.0.2.1")

    # Retrieve A records
    records = dns_manager.get_records("example.com", "A")
    print(f"A records for example.com: {records}")

    # Remove the A record
    dns_manager.remove_record("example.com", "A", "192.0.2.1")
```
