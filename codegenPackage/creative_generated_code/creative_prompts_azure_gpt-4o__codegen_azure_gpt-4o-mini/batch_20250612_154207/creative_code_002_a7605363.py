"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://425876928756287.icu
Prompt: Provide a Python function to identify whether a domain has an AAAA record and suggest a fallback to IPv4 for FASTPANEL compatibility.
Generated: DETERMINISTIC_a76053634abb8a7c
Batch ID: 20250612_154207
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import socket

def check_domain_ipv6(domain):
    """
    Check if a domain has an AAAA record (IPv6 address) and suggest a fallback to IPv4 if not.

    Args:
        domain (str): The domain name to check.

    Returns:
        dict: A dictionary containing the status and IP addresses.
              Example: {'has_ipv6': True, 'ipv6': '::1', 'ipv4': '127.0.0.1'}
    """
    result = {
        'has_ipv6': False,
        'ipv6': None,
        'ipv4': None
    }

    try:
        # Attempt to get the IPv6 address (AAAA record)
        ipv6_addresses = socket.getaddrinfo(domain, None, socket.AF_INET6)
        if ipv6_addresses:
            result['has_ipv6'] = True
            result['ipv6'] = ipv6_addresses[0][4][0]  # Get the first IPv6 address

    except socket.gaierror as e:
        print(f"Error retrieving IPv6 address for domain '{domain}': {e}")

    if not result['has_ipv6']:
        try:
            # Fallback to get the IPv4 address if no IPv6 address is found
            ipv4_addresses = socket.getaddrinfo(domain, None, socket.AF_INET)
            if ipv4_addresses:
                result['ipv4'] = ipv4_addresses[0][4][0]  # Get the first IPv4 address
        except socket.gaierror as e:
            print(f"Error retrieving IPv4 address for domain '{domain}': {e}")

    return result

# Example usage:
if __name__ == "__main__":
    domain_name = "example.com"
    ip_info = check_domain_ipv6(domain_name)
    print(ip_info)
```
