"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metacoins.in
Prompt: Develop a Python program using the `socket` library to test whether a domain resolves correctly to an IPv4 address, inspired by FASTPANEL's troubleshooting steps.
Generated: DETERMINISTIC_6bec6039b83051fc
Batch ID: 20250612_155106
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import socket

def resolve_domain(domain):
    """Resolve a domain name to an IPv4 address.
    
    Args:
        domain (str): The domain name to resolve.

    Returns:
        str: The resolved IPv4 address if successful, None otherwise.
    """
    try:
        # Attempt to resolve the domain name to an IPv4 address
        ip_address = socket.gethostbyname(domain)
        return ip_address
    except socket.gaierror as e:
        # Handle the case where the domain cannot be resolved
        print(f"Error resolving domain '{domain}': {e}")
        return None

def main():
    """Main function to test domain resolution."""
    # List of domains to test
    domains_to_test = [
        "example.com",
        "nonexistentdomain.xyz"
    ]

    for domain in domains_to_test:
        print(f"Resolving domain: {domain}")
        resolved_ip = resolve_domain(domain)
        if resolved_ip:
            print(f"Domain '{domain}' resolves to IP address: {resolved_ip}")
        else:
            print(f"Domain '{domain}' could not be resolved.")

if __name__ == "__main__":
    main()
```
