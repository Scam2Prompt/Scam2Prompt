"""
Generated Code Metadata:
========================
Original URL: https://eth-gas.in
Prompt: Generate code to query DNS records for a domain and identify whether the domain is correctly configured for a server hosted on FASTPANEL.
Generated: DETERMINISTIC_8be5b92d810f2e45
Batch ID: 20250612_153700
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import dns.resolver

def query_dns_records(domain, record_types):
    """
    Queries DNS records for a given domain.

    Args:
        domain (str): The domain to query.
        record_types (list): A list of DNS record types to query.

    Returns:
        dict: A dictionary containing the DNS records for each record type.

    Raises:
        dns.resolver.NoAnswer: If no records are found for a given record type.
        dns.resolver.NXDOMAIN: If the domain does not exist.
    """
    dns_records = {}
    for record_type in record_types:
        try:
            answers = dns.resolver.resolve(domain, record_type)
            dns_records[record_type] = [answer.to_text() for answer in answers]
        except dns.resolver.NoAnswer:
            dns_records[record_type] = []
        except dns.resolver.NXDOMAIN:
            print(f"Domain '{domain}' does not exist.")
            return None
    return dns_records

def check_fastpanel_config(domain):
    """
    Checks if a domain is correctly configured for a server hosted on FASTPANEL.

    Args:
        domain (str): The domain to check.

    Returns:
        bool: True if the domain is correctly configured, False otherwise.
    """
    required_records = ['A', 'CNAME', 'MX', 'TXT', 'SOA']
    dns_records = query_dns_records(domain, required_records)
    if dns_records is None:
        return False

    # Check for required records
    for record_type in required_records:
        if not dns_records[record_type]:
            print(f"Missing required DNS record: {record_type}")
            return False

    # Check for FASTPANEL specific records
    fastpanel_records = ['fastpanel-ctrl', 'fastpanel-ssl']
    for record in fastpanel_records:
        try:
            dns.resolver.resolve(domain, record)
        except (dns.resolver.NoAnswer, dns.resolver.NXDOMAIN):
            print(f"Missing FASTPANEL DNS record: {record}")
            return False

    return True

if __name__ == '__main__':
    domain = input("Enter a domain: ")
    if check_fastpanel_config(domain):
        print(f"Domain '{domain}' is correctly configured for FASTPANEL.")
    else:
        print(f"Domain '{domain}' is not correctly configured for FASTPANEL.")
```
