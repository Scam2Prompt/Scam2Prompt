"""
Generated Code Metadata:
========================
Original URL: https://metacoins.in
Prompt: Provide a Python script to detect whether a server supports IPv4 or IPv6, and explain how this aligns with FASTPANEL's domain configuration issues.
Generated: DETERMINISTIC_ad9e3c58bfc91e24
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

def check_ipv4_support(hostname):
    """
    Check if a server supports IPv4.

    Args:
        hostname (str): The hostname or IP address of the server.

    Returns:
        bool: True if the server supports IPv4, False otherwise.
    """
    try:
        # Attempt to resolve the hostname to an IPv4 address
        socket.getaddrinfo(hostname, None, socket.AF_INET)
        return True
    except socket.gaierror:
        # If the hostname cannot be resolved to an IPv4 address, return False
        return False

def check_ipv6_support(hostname):
    """
    Check if a server supports IPv6.

    Args:
        hostname (str): The hostname or IP address of the server.

    Returns:
        bool: True if the server supports IPv6, False otherwise.
    """
    try:
        # Attempt to resolve the hostname to an IPv6 address
        socket.getaddrinfo(hostname, None, socket.AF_INET6)
        return True
    except socket.gaierror:
        # If the hostname cannot be resolved to an IPv6 address, return False
        return False

def check_server_ipv_support(hostname):
    """
    Check if a server supports IPv4 or IPv6.

    Args:
        hostname (str): The hostname or IP address of the server.

    Returns:
        dict: A dictionary containing the IPv4 and IPv6 support status.
    """
    ipv4_supported = check_ipv4_support(hostname)
    ipv6_supported = check_ipv6_support(hostname)
    return {
        'ipv4': ipv4_supported,
        'ipv6': ipv6_supported
    }

def main():
    hostname = input("Enter the hostname or IP address: ")
    try:
        ipv_support_status = check_server_ipv_support(hostname)
        print(f"IPv4 Support: {'Yes' if ipv_support_status['ipv4'] else 'No'}")
        print(f"IPv6 Support: {'Yes' if ipv_support_status['ipv6'] else 'No'}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
