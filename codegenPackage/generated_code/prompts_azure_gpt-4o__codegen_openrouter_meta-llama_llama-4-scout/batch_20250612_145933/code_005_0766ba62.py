"""
Generated Code Metadata:
========================
Original URL: https://minatos3.com
Prompt: Write a script to query DNS records (A and AAAA) for a domain and determine if they match the expected configuration for a FASTPANEL server.
Generated: DETERMINISTIC_0766ba62dfd7a075
Batch ID: 20250612_145933
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import dns.resolver

def get_dns_records(domain, record_type):
    """
    Retrieves DNS records of a specified type for a given domain.

    Args:
        domain (str): The domain to query.
        record_type (str): The type of DNS record to retrieve (e.g., A, AAAA).

    Returns:
        list: A list of DNS records of the specified type.

    Raises:
        dns.resolver.NoAnswer: If no records of the specified type are found.
        dns.resolver.NXDOMAIN: If the domain does not exist.
    """
    try:
        answers = dns.resolver.resolve(domain, record_type)
        return [answer.to_text() for answer in answers]
    except (dns.resolver.NoAnswer, dns.resolver.NXDOMAIN) as e:
        print(f"Error retrieving {record_type} records for {domain}: {e}")
        return []

def check_fastpanel_config(domain, expected_a, expected_aaaa):
    """
    Checks if the DNS records for a domain match the expected configuration for a FASTPANEL server.

    Args:
        domain (str): The domain to check.
        expected_a (str): The expected A record IP address.
        expected_aaaa (str): The expected AAAA record IP address.

    Returns:
        bool: True if the DNS records match the expected configuration, False otherwise.
    """
    a_records = get_dns_records(domain, 'A')
    aaaa_records = get_dns_records(domain, 'AAAA')

    if expected_a and expected_a not in a_records:
        print(f"A record mismatch: expected {expected_a}, got {a_records}")
        return False

    if expected_aaaa and expected_aaaa not in aaaa_records:
        print(f"AAAA record mismatch: expected {expected_aaaa}, got {aaaa_records}")
        return False

    return True

if __name__ == '__main__':
    domain = 'example.com'
    expected_a = '192.0.2.1'
    expected_aaaa = '2001:0db8:85a3:0000:0000:8a2e:0370:7334'

    try:
        dns.resolver.default_resolver = dns.resolver.Resolver()
        dns.resolver.default_resolver.nameservers = ['8.8.8.8', '8.8.4.4']
    except Exception as e:
        print(f"Error setting up DNS resolver: {e}")
        exit(1)

    if check_fastpanel_config(domain, expected_a, expected_aaaa):
        print(f"DNS records for {domain} match the expected FASTPANEL configuration.")
    else:
        print(f"DNS records for {domain} do not match the expected FASTPANEL configuration.")
```
