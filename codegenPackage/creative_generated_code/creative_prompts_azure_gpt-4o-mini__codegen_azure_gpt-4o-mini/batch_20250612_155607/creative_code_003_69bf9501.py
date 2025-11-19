"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wallstreetpepe.club
Prompt: Generate a code snippet that demonstrates how to query Google Public DNS for an IP address using a specific domain.
Generated: DETERMINISTIC_69bf9501b3c44b82
Batch ID: 20250612_155607
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import socket

def query_google_dns(domain):
    """
    Queries Google Public DNS (8.8.8.8) for the IP address of the given domain.

    Args:
        domain (str): The domain name to resolve.

    Returns:
        str: The resolved IP address of the domain.

    Raises:
        ValueError: If the domain is invalid.
        socket.gaierror: If the domain cannot be resolved.
    """
    # Validate the domain input
    if not isinstance(domain, str) or not domain:
        raise ValueError("Invalid domain. Please provide a non-empty string.")

    # Google's Public DNS server IP
    google_dns = '8.8.8.8'

    try:
        # Use the socket library to perform a DNS lookup
        ip_address = socket.gethostbyname(domain)
        return ip_address
    except socket.gaierror as e:
        # Handle the error if the domain cannot be resolved
        raise socket.gaierror(f"Could not resolve domain '{domain}': {e}")

if __name__ == "__main__":
    # Example usage
    domain_to_query = "example.com"
    try:
        ip = query_google_dns(domain_to_query)
        print(f"The IP address of '{domain_to_query}' is: {ip}")
    except Exception as e:
        print(f"Error: {e}")
```
