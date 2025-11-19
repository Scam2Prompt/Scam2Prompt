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

def resolve_domain(domain):
    """
    Resolves a domain name to its corresponding IPv4 address.

    Args:
        domain (str): The domain name to resolve.

    Returns:
        str: The resolved IPv4 address if successful, otherwise None.
    """
    try:
        # Get the IP address for the given domain
        ip_address = socket.gethostbyname(domain)
        return ip_address
    except socket.gaierror as e:
        # Handle the error if the domain cannot be resolved
        print(f"Error resolving domain '{domain}': {e}")
        return None

def main():
    """
    Main function to execute the domain resolution test.
    """
    # Example domain to test
    domain = "example.com"
    
    print(f"Resolving domain: {domain}")
    ip_address = resolve_domain(domain)
    
    if ip_address:
        print(f"The domain '{domain}' resolves to the IP address: {ip_address}")
    else:
        print(f"The domain '{domain}' could not be resolved.")

if __name__ == "__main__":
    main()
```
