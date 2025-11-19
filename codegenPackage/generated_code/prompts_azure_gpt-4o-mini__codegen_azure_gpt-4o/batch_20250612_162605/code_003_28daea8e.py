"""
Generated Code Metadata:
========================
Original URL: https://ethegas.in
Prompt: Explain the difference between AAAA and IPv4 records and how they affect website accessibility.
Generated: DETERMINISTIC_28daea8e0e598e3c
Batch ID: 20250612_162605
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
This script demonstrates the difference between AAAA (IPv6) and IPv4 records
and how they affect website accessibility. It queries DNS records for a given
domain and checks for both IPv4 (A) and IPv6 (AAAA) records.

Requirements:
- Install the 'dnspython' library: pip install dnspython
"""

import dns.resolver

def query_dns_records(domain):
    """
    Queries DNS records for the given domain and retrieves both IPv4 (A) and IPv6 (AAAA) records.

    Args:
        domain (str): The domain name to query.

    Returns:
        dict: A dictionary containing IPv4 and IPv6 addresses.
    """
    results = {"IPv4": [], "IPv6": []}

    try:
        # Query IPv4 (A) records
        ipv4_records = dns.resolver.resolve(domain, 'A')
        results["IPv4"] = [record.to_text() for record in ipv4_records]
    except dns.resolver.NoAnswer:
        # No IPv4 records found
        results["IPv4"] = []
    except dns.resolver.NXDOMAIN:
        print(f"Domain '{domain}' does not exist.")
        return None
    except Exception as e:
        print(f"Error querying IPv4 records: {e}")
        return None

    try:
        # Query IPv6 (AAAA) records
        ipv6_records = dns.resolver.resolve(domain, 'AAAA')
        results["IPv6"] = [record.to_text() for record in ipv6_records]
    except dns.resolver.NoAnswer:
        # No IPv6 records found
        results["IPv6"] = []
    except dns.resolver.NXDOMAIN:
        print(f"Domain '{domain}' does not exist.")
        return None
    except Exception as e:
        print(f"Error querying IPv6 records: {e}")
        return None

    return results


def main():
    """
    Main function to demonstrate the difference between AAAA and IPv4 records.
    """
    domain = input("Enter a domain name (e.g., example.com): ").strip()

    # Query DNS records
    dns_records = query_dns_records(domain)

    if dns_records is None:
        print("Failed to retrieve DNS records.")
        return

    # Display results
    print(f"\nDNS Records for '{domain}':")
    print("IPv4 Addresses (A Records):")
    if dns_records["IPv4"]:
        for ip in dns_records["IPv4"]:
            print(f"  - {ip}")
    else:
        print("  No IPv4 addresses found.")

    print("IPv6 Addresses (AAAA Records):")
    if dns_records["IPv6"]:
        for ip in dns_records["IPv6"]:
            print(f"  - {ip}")
    else:
        print("  No IPv6 addresses found.")


if __name__ == "__main__":
    main()
```
