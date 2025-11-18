"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claim-resolv.digital
Prompt: Write a script to check if a domain has an AAAA record and verify whether the server supports IPv6.
Generated: DETERMINISTIC_87d5b7122d5beae4
Batch ID: 20250612_153832
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import socket

def check_ipv6_support(domain):
    """
    Check if a domain has an AAAA record and whether the server supports IPv6.

    Parameters:
    domain (str): The domain name to check.

    Returns:
    bool: True if the domain has an AAAA record; False otherwise.
    bool: True if the server supports IPv6; False otherwise.
    """
    try:
        # Attempt to retrieve AAAA records for the domain
        ipv6_addresses = socket.getaddrinfo(domain, None, socket.AF_INET6)
        
        # If we receive any IPv6 addresses, the domain has an AAAA record
        has_aaaa_record = len(ipv6_addresses) > 0
        
        # Check if the server can establish a connection over IPv6
        for addrinfo in ipv6_addresses:
            try:
                # Create a socket and attempt to connect to the IPv6 address
                with socket.socket(socket.AF_INET6) as s:
                    # Set a timeout for the connection attempt
                    s.settimeout(5)
                    s.connect(addrinfo[4])  # addrinfo[4] contains the address tuple
                    supports_ipv6 = True
                    break
            except (socket.error, socket.timeout):
                supports_ipv6 = False
        
        return has_aaaa_record, supports_ipv6

    except socket.gaierror as e:
        # Handle the exception for failed DNS resolution
        print(f"Error resolving domain '{domain}': {e}")
        return False, False

if __name__ == "__main__":
    # Example usage of the check_ipv6_support function
    domain_name = "example.com"  # Replace with the desired domain
    has_aaaa, supports_ipv6 = check_ipv6_support(domain_name)

    print(f"Domain: {domain_name}")
    print(f"Has AAAA record: {has_aaaa}")
    print(f"Supports IPv6: {supports_ipv6}")
```
