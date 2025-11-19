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

def resolve_domain_to_ipv4(domain: str) -> str:
    """
    Resolves a domain to its IPv4 address.

    Args:
    domain (str): The domain to resolve.

    Returns:
    str: The IPv4 address of the domain.

    Raises:
    socket.gaierror: If the domain cannot be resolved.
    ValueError: If the domain has no IPv4 address.
    """

    try:
        # Get the IP address of the domain
        ip_addresses = socket.getaddrinfo(domain, None, family=socket.AF_INET)
        
        # Check if there are any IPv4 addresses
        if not ip_addresses:
            raise ValueError(f"The domain '{domain}' has no IPv4 address.")

        # Return the first IPv4 address
        return ip_addresses[0][4][0]

    except socket.gaierror as e:
        # Handle DNS lookup errors
        raise socket.gaierror(f"Failed to resolve domain '{domain}': {e}")

def main():
    domain = input("Enter a domain to test: ")

    try:
        ipv4_address = resolve_domain_to_ipv4(domain)
        print(f"The domain '{domain}' resolves to: {ipv4_address}")
    except (socket.gaierror, ValueError) as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
