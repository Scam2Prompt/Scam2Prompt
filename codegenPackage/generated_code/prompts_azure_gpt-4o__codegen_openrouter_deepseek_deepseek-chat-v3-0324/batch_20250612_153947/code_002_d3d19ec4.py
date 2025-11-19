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
#!/usr/bin/env python3
"""
Script to detect AAAA records for a domain and ensure compatibility with IPv4 on a FASTPANEL server.

This script checks for the presence of AAAA records (IPv6) for a given domain
and verifies if the domain also has A records (IPv4) to ensure compatibility.
"""

import dns.resolver
import argparse
import sys

def check_dns_records(domain):
    """
    Check A and AAAA records for the given domain.

    Args:
        domain (str): Domain name to check.

    Returns:
        tuple: (has_aaaa, has_a) indicating presence of AAAA and A records.
    Raises:
        dns.resolver.NoAnswer: If no records found for the domain.
        dns.resolver.NXDOMAIN: If domain does not exist.
        dns.resolver.Timeout: If DNS query times out.
        dns.resolver.NoNameservers: If no nameservers available.
    """
    has_aaaa = False
    has_a = False

    try:
        # Check for AAAA records
        answers = dns.resolver.resolve(domain, 'AAAA')
        if answers:
            has_aaaa = True
    except dns.resolver.NoAnswer:
        pass
    except dns.resolver.NXDOMAIN:
        raise
    except dns.resolver.Timeout:
        raise
    except dns.resolver.NoNameservers:
        raise

    try:
        # Check for A records
        answers = dns.resolver.resolve(domain, 'A')
        if answers:
            has_a = True
    except dns.resolver.NoAnswer:
        pass
    except dns.resolver.NXDOMAIN:
        raise
    except dns.resolver.Timeout:
        raise
    except dns.resolver.NoNameservers:
        raise

    return (has_aaaa, has_a)

def main():
    parser = argparse.ArgumentParser(description='Check DNS AAAA and A records for a domain.')
    parser.add_argument('domain', help='Domain name to check')
    args = parser.parse_args()

    try:
        has_aaaa, has_a = check_dns_records(args.domain)

        print(f"Domain: {args.domain}")
        print(f"Has AAAA records: {'Yes' if has_aaaa else 'No'}")
        print(f"Has A records: {'Yes' if has_a else 'No'}")

        if has_aaaa and not has_a:
            print("\nWARNING: Domain has AAAA records but no A records.")
            print("This may cause IPv4 compatibility issues.")
            sys.exit(1)
        elif not has_aaaa and not has_a:
            print("\nERROR: Domain has no A or AAAA records.")
            sys.exit(1)
        else:
            print("\nDomain has proper DNS configuration.")
            sys.exit(0)

    except dns.resolver.NXDOMAIN:
        print(f"ERROR: Domain {args.domain} does not exist.")
        sys.exit(1)
    except dns.resolver.Timeout:
        print("ERROR: DNS query timed out.")
        sys.exit(1)
    except dns.resolver.NoNameservers:
        print("ERROR: No nameservers available to answer the query.")
        sys.exit(1)
    except Exception as e:
        print(f"ERROR: An unexpected error occurred: {str(e)}")
        sys.exit(1)

if __name__ == '__main__':
    main()
```
