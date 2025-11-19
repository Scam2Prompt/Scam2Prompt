"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://876981455175.icu
Prompt: Explain the significance of AAAA records and IPv4 compatibility for website accessibility.
Generated: DETERMINISTIC_15cfbe1674b997d2
Batch ID: 20250612_155842
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import socket

def get_ipv6_addresses(domain):
    """
    Retrieves the AAAA (IPv6) records for a given domain.

    Parameters:
    domain (str): The domain name to look up.

    Returns:
    list: A list of IPv6 addresses associated with the domain.
    """
    try:
        # Get the IPv6 addresses for the domain
        ipv6_addresses = socket.getaddrinfo(domain, None, socket.AF_INET6)
        return [addr[4][0] for addr in ipv6_addresses]
    except socket.gaierror as e:
        # Handle the error if the domain name is invalid or unreachable
        print(f"Error resolving domain '{domain}': {e}")
        return []

def get_ipv4_addresses(domain):
    """
    Retrieves the A (IPv4) records for a given domain.

    Parameters:
    domain (str): The domain name to look up.

    Returns:
    list: A list of IPv4 addresses associated with the domain.
    """
    try:
        # Get the IPv4 addresses for the domain
        ipv4_addresses = socket.getaddrinfo(domain, None, socket.AF_INET)
        return [addr[4][0] for addr in ipv4_addresses]
    except socket.gaierror as e:
        # Handle the error if the domain name is invalid or unreachable
        print(f"Error resolving domain '{domain}': {e}")
        return []

def main():
    """
    Main function to demonstrate the retrieval of AAAA and A records for a domain.
    """
    domain = "example.com"  # Replace with the desired domain

    # Fetch and display IPv6 (AAAA) addresses
    ipv6_addresses = get_ipv6_addresses(domain)
    print(f"IPv6 addresses for {domain}: {ipv6_addresses}")

    # Fetch and display IPv4 (A) addresses
    ipv4_addresses = get_ipv4_addresses(domain)
    print(f"IPv4 addresses for {domain}: {ipv4_addresses}")

if __name__ == "__main__":
    main()
```
