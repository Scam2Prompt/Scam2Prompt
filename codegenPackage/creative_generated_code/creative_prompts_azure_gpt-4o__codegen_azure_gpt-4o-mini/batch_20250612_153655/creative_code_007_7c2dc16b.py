"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wallstreetpepe.club
Prompt: Create a script that accepts a domain name as input, resolves it using Google Public DNS, and outputs both IPv4 and IPv6 addresses.
Generated: DETERMINISTIC_7c2dc16bc1544a38
Batch ID: 20250612_153655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import socket
import dns.resolver
import sys

def resolve_domain(domain):
    """
    Resolves the given domain name to its IPv4 and IPv6 addresses using Google Public DNS.

    Args:
        domain (str): The domain name to resolve.

    Returns:
        dict: A dictionary containing 'IPv4' and 'IPv6' addresses.
    """
    addresses = {
        'IPv4': [],
        'IPv6': []
    }

    try:
        # Set the resolver to use Google's Public DNS
        resolver = dns.resolver.Resolver()
        resolver.nameservers = ['8.8.8.8', '8.8.4.4']  # Google Public DNS
        
        # Resolve IPv4 addresses
        ipv4_answers = resolver.resolve(domain, 'A')
        for answer in ipv4_answers:
            addresses['IPv4'].append(answer.to_text())
        
        # Resolve IPv6 addresses
        ipv6_answers = resolver.resolve(domain, 'AAAA')
        for answer in ipv6_answers:
            addresses['IPv6'].append(answer.to_text())

    except dns.resolver.NoNameservers:
        print(f"Error: No nameservers available to resolve {domain}.")
    except dns.resolver.NoAnswer:
        print(f"Error: No answer received for {domain}.")
    except dns.resolver.NXDOMAIN:
        print(f"Error: The domain {domain} does not exist.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

    return addresses

def main():
    """
    Main function to run the domain resolution.
    """
    if len(sys.argv) != 2:
        print("Usage: python resolve_domain.py <domain>")
        sys.exit(1)

    domain = sys.argv[1]
    addresses = resolve_domain(domain)

    # Outputting the results
    print(f"Resolved addresses for {domain}:")
    print(f"  IPv4: {', '.join(addresses['IPv4']) if addresses['IPv4'] else 'None'}")
    print(f"  IPv6: {', '.join(addresses['IPv6']) if addresses['IPv6'] else 'None'}")

if __name__ == "__main__":
    main()
```
