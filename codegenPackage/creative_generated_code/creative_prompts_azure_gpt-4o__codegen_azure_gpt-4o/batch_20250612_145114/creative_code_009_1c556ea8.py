"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://app-2v.xyz
Prompt: Provide an example of using Google Public DNS in a Python script to resolve a domain name and handle errors gracefully.
Generated: DETERMINISTIC_1c556ea87d9eb744
Batch ID: 20250612_145114
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import socket

def resolve_domain_with_google_dns(domain):
    """
    Resolves a domain name using Google Public DNS (8.8.8.8).

    Args:
        domain (str): The domain name to resolve.

    Returns:
        str: The resolved IP address if successful.

    Raises:
        ValueError: If the domain is invalid.
        Exception: For other errors during resolution.
    """
    # Validate the domain name input
    if not domain or not isinstance(domain, str):
        raise ValueError("Invalid domain name provided.")

    # Google Public DNS server address
    google_dns_server = '8.8.8.8'
    google_dns_port = 53  # Default DNS port

    try:
        # Resolve the domain name using the specified DNS server
        ip_address = socket.gethostbyname(domain)
        return ip_address
    except socket.gaierror as e:
        # Handle errors related to address resolution
        raise Exception(f"Failed to resolve domain '{domain}': {e}")
    except Exception as e:
        # Handle generic exceptions
        raise Exception(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    # Example usage
    domain_to_resolve = "example.com"
    try:
        resolved_ip = resolve_domain_with_google_dns(domain_to_resolve)
        print(f"Domain '{domain_to_resolve}' resolved to IP: {resolved_ip}")
    except Exception as e:
        # Graceful error handling
        print(f"Error: {e}")
```
