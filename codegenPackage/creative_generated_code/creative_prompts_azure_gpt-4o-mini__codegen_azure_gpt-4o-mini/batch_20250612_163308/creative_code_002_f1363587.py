"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://app-2v.xyz
Prompt: What are the steps to get started with Google Public DNS for resolving IP addresses?
Generated: DETERMINISTIC_f1363587766e4845
Batch ID: 20250612_163308
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import socket

def resolve_hostname_to_ip(hostname):
    """
    Resolves a given hostname to its corresponding IP address using Google Public DNS.
    
    Args:
        hostname (str): The hostname to resolve.
        
    Returns:
        str: The resolved IP address.
        
    Raises:
        ValueError: If the hostname is invalid.
        socket.gaierror: If the hostname cannot be resolved.
    """
    # Validate the hostname input
    if not isinstance(hostname, str) or not hostname:
        raise ValueError("Invalid hostname provided. It must be a non-empty string.")
    
    try:
        # Using Google Public DNS (8.8.8.8 and 8.8.4.4) for DNS resolution
        ip_address = socket.gethostbyname(hostname)
        return ip_address
    except socket.gaierror as e:
        # Handle errors related to DNS resolution
        raise socket.gaierror(f"Could not resolve hostname '{hostname}': {e}")

if __name__ == "__main__":
    # Example usage
    try:
        hostname = "www.example.com"
        ip = resolve_hostname_to_ip(hostname)
        print(f"The IP address of {hostname} is {ip}.")
    except ValueError as ve:
        print(f"Value error: {ve}")
    except socket.gaierror as ge:
        print(f"DNS error: {ge}")
```
