"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bid-notification.bet
Prompt: Can you explain the significance of AAAA records and IPv4 compatibility in website accessibility, as mentioned on the bid-notification.bet page?
Generated: DETERMINISTIC_81f82b8ccc345102
Batch ID: 20250612_160129
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import socket

def check_ip_version(domain):
    """
    Checks the IP addresses associated with a domain for both IPv4 and IPv6.
    
    Args:
        domain (str): The domain name to check.
        
    Returns:
        dict: A dictionary containing lists of IPv4 and IPv6 addresses.
        
    Raises:
        ValueError: If the provided domain is invalid or unreachable.
    """
    if not isinstance(domain, str) or not domain:
        raise ValueError("Invalid domain name provided.")

    ip_addresses = {
        'IPv4': [],
        'IPv6': []
    }

    try:
        # Get the IPv4 addresses
        ipv4_addresses = socket.getaddrinfo(domain, None, socket.AF_INET)
        ip_addresses['IPv4'] = [addr[4][0] for addr in ipv4_addresses]

        # Get the IPv6 addresses
        ipv6_addresses = socket.getaddrinfo(domain, None, socket.AF_INET6)
        ip_addresses['IPv6'] = [addr[4][0] for addr in ipv6_addresses]

    except socket.gaierror as e:
        raise ValueError(f"Could not resolve domain '{domain}': {e}")

    return ip_addresses


def main():
    """
    Main function to demonstrate the checking of AAAA records for a given domain.
    """
    domain = "bid-notification.bet"  # Example domain
    try:
        ip_info = check_ip_version(domain)
        print(f"Domain: {domain}")
        print("IPv4 Addresses:", ip_info['IPv4'])
        print("IPv6 Addresses:", ip_info['IPv6'])
        
        if not ip_info['IPv6']:
            print("Note: This domain does not have AAAA records, which may affect accessibility over IPv6.")
        
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
