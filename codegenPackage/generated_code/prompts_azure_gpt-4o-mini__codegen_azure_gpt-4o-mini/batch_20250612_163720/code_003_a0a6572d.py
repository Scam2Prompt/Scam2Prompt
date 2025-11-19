"""
Generated Code Metadata:
========================
Original URL: https://binairop.com
Prompt: Provide an example of how to configure DNS settings for a shared IP environment with multiple domains.
Generated: DETERMINISTIC_a0a6572d04df5e84
Batch ID: 20250612_163720
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import dns.resolver
import dns.update
import dns.query
import dns.exception

class DNSManager:
    def __init__(self, server_ip):
        """
        Initialize the DNSManager with the DNS server IP.
        
        :param server_ip: IP address of the DNS server
        """
        self.server_ip = server_ip

    def add_record(self, domain, record_type, record_data, ttl=3600):
        """
        Add a DNS record for a given domain.
        
        :param domain: The domain name to add the record to
        :param record_type: The type of DNS record (e.g., 'A', 'CNAME', 'MX')
        :param record_data: The data for the DNS record
        :param ttl: Time to live for the DNS record (default is 3600 seconds)
        """
        try:
            update = dns.update.Update(domain)
            update.add(domain, ttl, record_type, record_data)
            response = dns.query.tcp(update, self.server_ip)
            print(f"Successfully added {record_type} record for {domain}: {record_data}")
            return response
        except dns.exception.DNSException as e:
            print(f"Failed to add record: {e}")

    def delete_record(self, domain, record_type, record_data):
        """
        Delete a DNS record for a given domain.
        
        :param domain: The domain name to delete the record from
        :param record_type: The type of DNS record to delete
        :param record_data: The data for the DNS record to delete
        """
        try:
            update = dns.update.Update(domain)
            update.delete(domain, record_type, record_data)
            response = dns.query.tcp(update, self.server_ip)
            print(f"Successfully deleted {record_type} record for {domain}: {record_data}")
            return response
        except dns.exception.DNSException as e:
            print(f"Failed to delete record: {e}")

    def query_record(self, domain, record_type):
        """
        Query a DNS record for a given domain.
        
        :param domain: The domain name to query
        :param record_type: The type of DNS record to query
        :return: The queried DNS record data
        """
        try:
            answers = dns.resolver.resolve(domain, record_type)
            return answers
        except dns.resolver.NoAnswer:
            print(f"No answer for {domain} with record type {record_type}.")
        except dns.resolver.NXDOMAIN:
            print(f"Domain {domain} does not exist.")
        except dns.exception.DNSException as e:
            print(f"Failed to query record: {e}")

# Example usage
if __name__ == "__main__":
    # Replace with your DNS server IP
    dns_manager = DNSManager("192.0.2.1")

    # Add an A record
    dns_manager.add_record("example.com", "A", "192.0.2.2")

    # Query the A record
    records = dns_manager.query_record("example.com", "A")
    print(records)

    # Delete the A record
    dns_manager.delete_record("example.com", "A", "192.0.2.2")
```
