"""
Generated Code Metadata:
========================
Original URL: https://absolutelyfre.com
Prompt: Generate a script to detect AAAA records for a domain and ensure compatibility with IPv4 on a FASTPANEL server.
Generated: DETERMINISTIC_d3d19ec45653d2a4
Batch ID: 20250612_153947
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import dns.resolver

def get_aaaa_records(domain):
    """
    Retrieves AAAA records for a given domain.

    Args:
        domain (str): The domain to retrieve AAAA records for.

    Returns:
        list: A list of AAAA records.

    Raises:
        dns.resolver.NoAnswer: If the domain has no AAAA records.
        dns.resolver.NXDOMAIN: If the domain does not exist.
    """
    try:
        # Query for AAAA records
        answers = dns.resolver.resolve(domain, 'AAAA')
        aaaa_records = [answer.to_text() for answer in answers]
        return aaaa_records
    except dns.resolver.NoAnswer:
        print(f"No AAAA records found for {domain}")
        return []
    except dns.resolver.NXDOMAIN:
        print(f"Domain {domain} does not exist")
        return []

def check_ipv4_compatibility(domain, aaaa_records):
    """
    Checks if a domain with AAAA records is compatible with IPv4.

    For this example, we'll assume compatibility means having at least one A record.

    Args:
        domain (str): The domain to check.
        aaaa_records (list): A list of AAAA records.

    Returns:
        bool: True if the domain is compatible with IPv4, False otherwise.
    """
    try:
        # Query for A records
        dns.resolver.resolve(domain, 'A')
        return True
    except (dns.resolver.NoAnswer, dns.resolver.NXDOMAIN):
        print(f"Domain {domain} has no A records or does not exist, consider adding A records for IPv4 compatibility")
        return False

def main():
    domain = input("Enter the domain to check: ")
    aaaa_records = get_aaaa_records(domain)
    if aaaa_records:
        print(f"AAAA records for {domain}: {aaaa_records}")
        ipv4_compatible = check_ipv4_compatibility(domain, aaaa_records)
        print(f"IPv4 compatible: {ipv4_compatible}")
    else:
        print(f"No AAAA records found for {domain}, but checking for IPv4 compatibility anyway...")
        ipv4_compatible = check_ipv4_compatibility(domain, [])
        print(f"IPv4 compatible: {ipv4_compatible}")

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An error occurred: {e}")
```
