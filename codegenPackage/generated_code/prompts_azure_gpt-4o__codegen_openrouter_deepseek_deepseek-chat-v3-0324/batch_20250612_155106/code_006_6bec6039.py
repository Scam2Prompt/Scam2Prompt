"""
Generated Code Metadata:
========================
Original URL: https://metacoins.in
Prompt: Develop a Python program using the `socket` library to test whether a domain resolves correctly to an IPv4 address, inspired by FASTPANEL's troubleshooting steps.
Generated: DETERMINISTIC_6bec6039b83051fc
Batch ID: 20250612_155106
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import socket
import sys

def resolve_domain_to_ipv4(domain):
    """
    Resolve a domain name to its IPv4 address.

    Args:
        domain (str): The domain name to resolve.

    Returns:
        str: The resolved IPv4 address or None if resolution fails.
    """
    try:
        # Get address information for the domain (IPv4 only)
        addr_info = socket.getaddrinfo(domain, None, socket.AF_INET)
        if not addr_info:
            return None
        
        # Extract the first IPv4 address from the address info
        ipv4_address = addr_info[0][4][0]
        return ipv4_address
    except socket.gaierror as e:
        print(f"Error resolving domain '{domain}': {e}", file=sys.stderr)
        return None
    except Exception as e:
        print(f"Unexpected error while resolving domain '{domain}': {e}", file=sys.stderr)
        return None

def main():
    """
    Main function to test domain resolution to IPv4.
    """
    if len(sys.argv) != 2:
        print("Usage: python domain_resolver.py <domain>", file=sys.stderr)
        sys.exit(1)

    domain = sys.argv[1]
    ipv4_address = resolve_domain_to_ipv4(domain)

    if ipv4_address:
        print(f"Domain '{domain}' resolves to IPv4 address: {ipv4_address}")
    else:
        print(f"Domain '{domain}' could not be resolved to an IPv4 address.")
        sys.exit(1)

if __name__ == "__main__":
    main()
```
