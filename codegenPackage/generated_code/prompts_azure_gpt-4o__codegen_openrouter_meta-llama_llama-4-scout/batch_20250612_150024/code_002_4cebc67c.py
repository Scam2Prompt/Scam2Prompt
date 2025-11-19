"""
Generated Code Metadata:
========================
Original URL: https://bid-notification.bet
Prompt: Provide a Python script that detects whether a server supports IPv6 and falls back to IPv4 if necessary, based on FASTPANEL's explanation of AAAA record issues.
Generated: DETERMINISTIC_4cebc67c23a978c4
Batch ID: 20250612_150024
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import socket

def check_ipv6_support(hostname):
    """
    Checks if a server supports IPv6 by attempting to resolve its AAAA record.

    Args:
        hostname (str): The hostname of the server to check.

    Returns:
        bool: True if the server supports IPv6, False otherwise.
    """
    try:
        # Attempt to resolve the AAAA record for the given hostname
        socket.getaddrinfo(hostname, None, family=socket.AF_INET6)
        return True
    except socket.gaierror:
        # If the AAAA record cannot be resolved, assume IPv6 is not supported
        return False

def get_server_address(hostname, prefer_ipv6=True):
    """
    Retrieves the address of a server, falling back to IPv4 if IPv6 is not supported.

    Args:
        hostname (str): The hostname of the server to retrieve the address for.
        prefer_ipv6 (bool): Whether to prefer IPv6 addresses if available. Defaults to True.

    Returns:
        str: The address of the server.
    """
    if prefer_ipv6 and check_ipv6_support(hostname):
        try:
            # Attempt to resolve the AAAA record for the given hostname
            return socket.getaddrinfo(hostname, None, family=socket.AF_INET6)[0][4][0]
        except socket.gaierror:
            pass  # Fall back to IPv4 if AAAA record cannot be resolved

    # Attempt to resolve the A record for the given hostname
    try:
        return socket.getaddrinfo(hostname, None, family=socket.AF_INET)[0][4][0]
    except socket.gaierror as e:
        raise Exception(f"Failed to resolve hostname {hostname}: {e}")

def main():
    hostname = "example.com"  # Replace with the desired hostname
    try:
        address = get_server_address(hostname)
        print(f"The address of {hostname} is: {address}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
