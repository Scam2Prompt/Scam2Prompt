"""
Generated Code Metadata:
========================
Original URL: https://minipepe.digital
Prompt: Provide code to query and validate DNS settings for a domain hosted on FASTPANEL, including checks for AAAA and A records.
Generated: DETERMINISTIC_08ea4c672424150c
Batch ID: 20250612_145913
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import dns.resolver
import dns.exception

def query_dns_records(domain):
    """
    Queries DNS records for the specified domain and validates the presence of A and AAAA records.

    Args:
        domain (str): The domain name to query.

    Returns:
        dict: A dictionary containing A and AAAA records if found, otherwise empty lists.
    """
    records = {
        'A': [],
        'AAAA': []
    }

    try:
        # Query A records
        a_records = dns.resolver.resolve(domain, 'A')
        records['A'] = [str(record) for record in a_records]
    except dns.resolver.NoAnswer:
        print(f"No A records found for {domain}.")
    except dns.resolver.NXDOMAIN:
        print(f"The domain {domain} does not exist.")
    except dns.exception.DNSException as e:
        print(f"An error occurred while querying A records: {e}")

    try:
        # Query AAAA records
        aaaa_records = dns.resolver.resolve(domain, 'AAAA')
        records['AAAA'] = [str(record) for record in aaaa_records]
    except dns.resolver.NoAnswer:
        print(f"No AAAA records found for {domain}.")
    except dns.resolver.NXDOMAIN:
        print(f"The domain {domain} does not exist.")
    except dns.exception.DNSException as e:
        print(f"An error occurred while querying AAAA records: {e}")

    return records

if __name__ == "__main__":
    # Example usage
    domain_to_check = "example.com"  # Replace with the domain you want to check
    dns_records = query_dns_records(domain_to_check)
    
    print(f"DNS records for {domain_to_check}:")
    print(f"A records: {dns_records['A']}")
    print(f"AAAA records: {dns_records['AAAA']}")
```

Make sure to install the `dnspython` library if you haven't already:

```bash
pip install dnspython
```
