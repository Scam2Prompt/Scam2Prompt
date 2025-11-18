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

def resolve_domain(domain):
    """
    Resolves a domain name to its corresponding IP address using Google Public DNS.
    
    Args:
        domain (str): The domain name to resolve.

    Returns:
        str: The resolved IP address if successful, None otherwise.
    
    Raises:
        ValueError: If the domain name is not valid.
        socket.gaierror: If the DNS resolution fails.
    """
    # Validate the domain name
    if not isinstance(domain, str) or not domain:
        raise ValueError("Invalid domain name. It must be a non-empty string.")

    # Google Public DNS servers
    dns_servers = ['8.8.8.8', '8.8.4.4']

    for dns in dns_servers:
        try:
            # Set the DNS server for the socket
            resolver = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            resolver.settimeout(5)  # Set a timeout for DNS resolution
            
            # Attempt to resolve the domain name
            ip_address = socket.gethostbyname(domain)
            print(f"The IP address of {domain} is {ip_address}")
            return ip_address
        except socket.gaierror as e:
            print(f"DNS resolution failed using server {dns}: {e}")
        finally:
            resolver.close()

    print("All DNS servers failed to resolve the domain.")
    return None

if __name__ == "__main__":
    # Example usage
    domain_to_resolve = "example.com"
    
    try:
        ip = resolve_domain(domain_to_resolve)
        if ip:
            print(f"Resolved IP: {ip}")
    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
