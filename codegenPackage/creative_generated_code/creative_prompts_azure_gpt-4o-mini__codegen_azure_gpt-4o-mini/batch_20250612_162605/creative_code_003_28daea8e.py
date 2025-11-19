"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ethegas.in
Prompt: Explain the difference between AAAA and IPv4 records and how they affect website accessibility.
Generated: DETERMINISTIC_28daea8e0e598e3c
Batch ID: 20250612_162605
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
This script demonstrates the difference between AAAA and IPv4 DNS records
and their impact on website accessibility. 

- An IPv4 record (A record) maps a hostname to a 32-bit IPv4 address.
- An AAAA record maps a hostname to a 128-bit IPv6 address.

The script will perform DNS lookups for a given hostname and display the results.
"""

import socket

def get_ip_addresses(hostname):
    """
    Retrieve IPv4 and IPv6 addresses for a given hostname.

    Args:
        hostname (str): The hostname to look up.

    Returns:
        tuple: A tuple containing lists of IPv4 and IPv6 addresses.
    """
    try:
        # Get IPv4 addresses
        ipv4_addresses = socket.gethostbyname_ex(hostname)[2]
    except socket.gaierror:
        print(f"Error: Unable to retrieve IPv4 addresses for {hostname}.")
        ipv4_addresses = []

    try:
        # Get IPv6 addresses
        ipv6_addresses = socket.getaddrinfo(hostname, None, socket.AF_INET6)
        ipv6_addresses = [addr[4][0] for addr in ipv6_addresses]
    except socket.gaierror:
        print(f"Error: Unable to retrieve IPv6 addresses for {hostname}.")
        ipv6_addresses = []

    return ipv4_addresses, ipv6_addresses

def display_ip_addresses(hostname):
    """
    Display the IPv4 and IPv6 addresses associated with a hostname.

    Args:
        hostname (str): The hostname to look up.
    """
    ipv4, ipv6 = get_ip_addresses(hostname)

    print(f"Hostname: {hostname}")
    print(f"IPv4 Addresses: {', '.join(ipv4) if ipv4 else 'None'}")
    print(f"IPv6 Addresses: {', '.join(ipv6) if ipv6 else 'None'}")

if __name__ == "__main__":
    # Example hostname to lookup
    hostname_to_lookup = "example.com"
    display_ip_addresses(hostname_to_lookup)
```
