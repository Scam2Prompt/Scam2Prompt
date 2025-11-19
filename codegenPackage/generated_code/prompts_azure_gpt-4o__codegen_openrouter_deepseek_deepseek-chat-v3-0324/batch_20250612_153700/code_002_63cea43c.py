"""
Generated Code Metadata:
========================
Original URL: https://eth-gas.in
Prompt: Create a Python script that uses a library like `socket` or `dnspython` to test IPv4 and IPv6 compatibility for a given domain.
Generated: DETERMINISTIC_63cea43c5a336d3e
Batch ID: 20250612_153700
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import socket
import dns.resolver
from typing import Tuple, List, Optional

def get_ipv4_addresses(domain: str) -> List[str]:
    """
    Resolve IPv4 addresses for a given domain.
    
    Args:
        domain: Domain name to resolve.
    
    Returns:
        List of IPv4 addresses as strings.
    """
    try:
        return [addr[4][0] for addr in socket.getaddrinfo(domain, None, socket.AF_INET)]
    except (socket.gaierror, socket.herror) as e:
        print(f"Error resolving IPv4 for {domain}: {e}")
        return []

def get_ipv6_addresses(domain: str) -> List[str]:
    """
    Resolve IPv6 addresses for a given domain.
    
    Args:
        domain: Domain name to resolve.
    
    Returns:
        List of IPv6 addresses as strings.
    """
    try:
        return [addr[4][0] for addr in socket.getaddrinfo(domain, None, socket.AF_INET6)]
    except (socket.gaierror, socket.herror) as e:
        print(f"Error resolving IPv6 for {domain}: {e}")
        return []

def check_dns_records(domain: str) -> Tuple[List[str], List[str]]:
    """
    Check DNS records for A (IPv4) and AAAA (IPv6) records.
    
    Args:
        domain: Domain name to check.
    
    Returns:
        Tuple of (IPv4 addresses, IPv6 addresses).
    """
    ipv4_addresses = []
    ipv6_addresses = []
    
    try:
        answers = dns.resolver.resolve(domain, 'A')
        ipv4_addresses = [str(r) for r in answers]
    except (dns.resolver.NoAnswer, dns.resolver.NXDOMAIN, dns.resolver.NoNameservers) as e:
        print(f"DNS query for A records failed: {e}")
    
    try:
        answers = dns.resolver.resolve(domain, 'AAAA')
        ipv6_addresses = [str(r) for r in answers]
    except (dns.resolver.NoAnswer, dns.resolver.NXDOMAIN, dns.resolver.NoNameservers) as e:
        print(f"DNS query for AAAA records failed: {e}")
    
    return ipv4_addresses, ipv6_addresses

def test_ip_compatibility(domain: str) -> None:
    """
    Test IPv4 and IPv6 compatibility for a given domain.
    
    Args:
        domain: Domain name to test.
    """
    print(f"\nTesting IP compatibility for: {domain}")
    
    # Using socket library
    print("\nUsing socket library:")
    ipv4_socket = get_ipv4_addresses(domain)
    ipv6_socket = get_ipv6_addresses(domain)
    
    print(f"IPv4 addresses: {ipv4_socket if ipv4_socket else 'None'}")
    print(f"IPv6 addresses: {ipv6_socket if ipv6_socket else 'None'}")
    
    # Using dnspython library
    print("\nUsing dnspython library:")
    ipv4_dns, ipv6_dns = check_dns_records(domain)
    
    print(f"A records (IPv4): {ipv4_dns if ipv4_dns else 'None'}")
    print(f"AAAA records (IPv6): {ipv6_dns if ipv6_dns else 'None'}")
    
    # Compatibility summary
    print("\nCompatibility Summary:")
    print(f"IPv4 supported: {'Yes' if ipv4_socket or ipv4_dns else 'No'}")
    print(f"IPv6 supported: {'Yes' if ipv6_socket or ipv6_dns else 'No'}")

if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description="Test IPv4 and IPv6 compatibility for a domain.")
    parser.add_argument("domain", help="Domain name to test")
    args = parser.parse_args()
    
    test_ip_compatibility(args.domain)
```
