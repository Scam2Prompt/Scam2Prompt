"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://uniswap.sihigo.infwww.vpn.osnovanie-osman.ru
Prompt: Write a Python script that checks for both AAAA and A records of a domain to ensure compatibility with IPv4.
Generated: DETERMINISTIC_8e23b630f2da1555
Batch ID: 20250612_160507
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import socket
import sys

def check_domain_records(domain):
    """
    Check for A and AAAA records of a given domain.

    Args:
        domain (str): The domain name to check.

    Returns:
        dict: A dictionary containing A and AAAA records.
    """
    records = {
        'A': None,
        'AAAA': None
    }

    try:
        # Retrieve A records (IPv4)
        a_records = socket.getaddrinfo(domain, None, socket.AF_INET)
        records['A'] = [record[4][0] for record in a_records]
    except socket.gaierror as e:
        print(f"Error retrieving A records for {domain}: {e}")

    try:
        # Retrieve AAAA records (IPv6)
        aaaa_records = socket.getaddrinfo(domain, None, socket.AF_INET6)
        records['AAAA'] = [record[4][0] for record in aaaa_records]
    except socket.gaierror as e:
        print(f"Error retrieving AAAA records for {domain}: {e}")

    return records

def main():
    """
    Main function to execute the domain record check.
    """
    if len(sys.argv) != 2:
        print("Usage: python check_domain.py <domain>")
        sys.exit(1)

    domain = sys.argv[1]
    records = check_domain_records(domain)

    print(f"Domain: {domain}")
    print(f"A Records (IPv4): {records['A']}")
    print(f"AAAA Records (IPv6): {records['AAAA']}")

if __name__ == "__main__":
    main()
```

Make sure to run this script from the command line, passing the domain as an argument. For example:

```bash
python check_domain.py example.com
```
