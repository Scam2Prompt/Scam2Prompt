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
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def check_ipv6_support(hostname):
    """
    Check if the server supports IPv6 by attempting to resolve its AAAA record.

    Args:
        hostname (str): The hostname of the server to check.

    Returns:
        bool: True if IPv6 is supported, False otherwise.
    """
    try:
        # Attempt to resolve the AAAA record for the hostname
        socket.getaddrinfo(hostname, None, socket.AF_INET6)
        logging.info(f"{hostname} supports IPv6.")
        return True
    except socket.gaierror:
        logging.warning(f"{hostname} does not support IPv6.")
        return False

def resolve_hostname(hostname):
    """
    Resolve the hostname to an IP address, preferring IPv6 and falling back to IPv4.

    Args:
        hostname (str): The hostname to resolve.

    Returns:
        str: The resolved IP address (IPv6 or IPv4).
    """
    # Check for IPv6 support
    if check_ipv6_support(hostname):
        try:
            # Resolve to IPv6
            ipv6_address = socket.getaddrinfo(hostname, None, socket.AF_INET6)[0][4][0]
            return ipv6_address
        except Exception as e:
            logging.error(f"Error resolving IPv6 for {hostname}: {e}")

    # Fallback to IPv4 if IPv6 is not supported or an error occurred
    try:
        ipv4_address = socket.getaddrinfo(hostname, None, socket.AF_INET)[0][4][0]
        return ipv4_address
    except Exception as e:
        logging.error(f"Error resolving IPv4 for {hostname}: {e}")
        return None

if __name__ == "__main__":
    # Example usage
    hostname = "example.com"  # Replace with the desired hostname
    ip_address = resolve_hostname(hostname)
    
    if ip_address:
        logging.info(f"Resolved IP address for {hostname}: {ip_address}")
    else:
        logging.error(f"Failed to resolve IP address for {hostname}.")
```
