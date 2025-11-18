"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metacoins.in
Prompt: Provide a Python script to detect whether a server supports IPv4 or IPv6, and explain how this aligns with FASTPANEL's domain configuration issues.
Generated: DETERMINISTIC_ad9e3c58bfc91e24
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

def check_ip_support(server_address):
    """
    Check if the given server address supports IPv4 or IPv6.

    Args:
        server_address (str): The domain name or IP address of the server.

    Returns:
        dict: A dictionary indicating support for 'IPv4' and 'IPv6'.
    """
    results = {
        'IPv4': False,
        'IPv6': False
    }

    # Check for IPv4 support
    try:
        # Attempt to resolve the server address to an IPv4 address
        socket.getaddrinfo(server_address, None, socket.AF_INET)
        results['IPv4'] = True
    except socket.gaierror:
        pass  # IPv4 address resolution failed

    # Check for IPv6 support
    try:
        # Attempt to resolve the server address to an IPv6 address
        socket.getaddrinfo(server_address, None, socket.AF_INET6)
        results['IPv6'] = True
    except socket.gaierror:
        pass  # IPv6 address resolution failed

    return results

def main():
    """
    Main function to execute the IP support check.
    """
    # Example server address (replace with your target server)
    server_address = 'example.com'

    # Check IP support
    ip_support = check_ip_support(server_address)

    # Output the results
    print(f"Server '{server_address}' supports:")
    print(f"  IPv4: {ip_support['IPv4']}")
    print(f"  IPv6: {ip_support['IPv6']}")

if __name__ == "__main__":
    main()
```
