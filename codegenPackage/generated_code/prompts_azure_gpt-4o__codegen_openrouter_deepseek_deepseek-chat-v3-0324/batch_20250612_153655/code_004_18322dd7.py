"""
Generated Code Metadata:
========================
Original URL: https://wallstreetpepe.club
Prompt: Provide a step-by-step guide to programmatically resolve a domain name using Google Public DNS, including IPv4 and IPv6 addresses.
Generated: DETERMINISTIC_18322dd743d1b515
Batch ID: 20250612_153655
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
import dns.exception

def resolve_domain(domain_name):
    """
    Resolve a domain name to its IPv4 and IPv6 addresses using Google Public DNS.
    
    Args:
        domain_name (str): The domain name to resolve.
    
    Returns:
        dict: A dictionary containing 'ipv4' and 'ipv6' lists of addresses.
    
    Raises:
        ValueError: If the domain_name is empty or invalid.
        dns.exception.DNSException: If DNS resolution fails.
    """
    if not domain_name or not isinstance(domain_name, str):
        raise ValueError("Invalid domain name provided.")
    
    # Configure resolver to use Google Public DNS
    resolver = dns.resolver.Resolver()
    resolver.nameservers = ['8.8.8.8', '8.8.4.4']  # Google Public DNS IPv4
    resolver.nameservers.extend(['2001:4860:4860::8888', '2001:4860:4860::8844'])  # Google Public DNS IPv6
    
    result = {'ipv4': [], 'ipv6': []}
    
    try:
        # Resolve IPv4 addresses (A records)
        answers = resolver.resolve(domain_name, 'A')
        result['ipv4'] = [str(r) for r in answers]
    except (dns.resolver.NoAnswer, dns.resolver.NXDOMAIN):
        pass  # No IPv4 records found
    except dns.exception.DNSException as e:
        raise dns.exception.DNSException(f"IPv4 resolution failed: {e}")
    
    try:
        # Resolve IPv6 addresses (AAAA records)
        answers = resolver.resolve(domain_name, 'AAAA')
        result['ipv6'] = [str(r) for r in answers]
    except (dns.resolver.NoAnswer, dns.resolver.NXDOMAIN):
        pass  # No IPv6 records found
    except dns.exception.DNSException as e:
        raise dns.exception.DNSException(f"IPv6 resolution failed: {e}")
    
    return result

def main():
    """Example usage of the resolve_domain function."""
    try:
        domain = input("Enter domain name to resolve: ")
        result = resolve_domain(domain)
        
        print(f"\nResolution results for {domain}:")
        print("IPv4 Addresses:", result['ipv4'] or "None found")
        print("IPv6 Addresses:", result['ipv6'] or "None found")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
