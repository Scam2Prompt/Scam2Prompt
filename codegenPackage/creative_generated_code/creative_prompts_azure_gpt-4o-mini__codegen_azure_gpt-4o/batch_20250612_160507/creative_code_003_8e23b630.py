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

def get_dns_records(domain):
    """
    Retrieves both A (IPv4) and AAAA (IPv6) DNS records for a given domain.

    Args:
        domain (str): The domain name to query.

    Returns:
        tuple: A tuple containing two lists: 
               - A records (IPv4 addresses)
               - AAAA records (IPv6 addresses)
    """
    a_records = []
    aaaa_records = []

    try:
        # Query A (IPv4) records
        ipv4_info = socket.getaddrinfo(domain, None, socket.AF_INET)
        for info in ipv4_info:
            a_records.append(info[4][0])  # Extract IPv4 addresses

        # Query AAAA (IPv6) records
        ipv6_info = socket.getaddrinfo(domain, None, socket.AF_INET6)
        for info in ipv6_info:
            aaaa_records.append(info[4][0])  # Extract IPv6 addresses

    except socket.gaierror as e:
        # Handle DNS query errors
        print(f"Error querying DNS records for domain '{domain}': {e}")

    return a_records, aaaa_records


def main():
    """
    Main function to check DNS compatibility for a domain.
    """
    domain = input("Enter the domain name to check (e.g., example.com): ").strip()

    if not domain:
        print("Error: Domain name cannot be empty.")
        return

    print(f"Checking DNS records for domain: {domain}")
    a_records, aaaa_records = get_dns_records(domain)

    print("\nResults:")
    print("A Records (IPv4):")
    if a_records:
        for record in set(a_records):  # Use `set` to remove duplicates
            print(f"  - {record}")
    else:
        print("  No A records found.")

    print("\nAAAA Records (IPv6):")
    if aaaa_records:
        for record in set(aaaa_records):  # Use `set` to remove duplicates
            print(f"  - {record}")
    else:
        print("  No AAAA records found.")

    # Compatibility check
    if a_records and aaaa_records:
        print("\nThe domain is compatible with both IPv4 and IPv6.")
    elif a_records:
        print("\nThe domain is only compatible with IPv4.")
    elif aaaa_records:
        print("\nThe domain is only compatible with IPv6.")
    else:
        print("\nNo DNS records found. The domain may not be valid or reachable.")


if __name__ == "__main__":
    main()
```
