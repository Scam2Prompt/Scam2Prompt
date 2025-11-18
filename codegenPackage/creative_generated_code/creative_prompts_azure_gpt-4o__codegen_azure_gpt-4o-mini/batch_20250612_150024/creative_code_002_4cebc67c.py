"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bid-notification.bet
Prompt: Provide a Python script that detects whether a server supports IPv6 and falls back to IPv4 if necessary, based on FASTPANEL's explanation of AAAA record issues.
Generated: DETERMINISTIC_4cebc67c23a978c4
Batch ID: 20250612_150024
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import socket
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

def check_ipv6_support(hostname):
    """
    Checks if the given hostname supports IPv6 by attempting to resolve its AAAA record.

    Args:
        hostname (str): The hostname to check for IPv6 support.

    Returns:
        bool: True if IPv6 is supported, False otherwise.
    """
    try:
        # Attempt to get the IPv6 address
        ipv6_addresses = socket.getaddrinfo(hostname, None, socket.AF_INET6)
        logging.info(f"IPv6 is supported for {hostname}: {ipv6_addresses}")
        return True
    except socket.gaierror as e:
        logging.error(f"IPv6 resolution failed for {hostname}: {e}")
        return False

def get_ip_address(hostname):
    """
    Retrieves the appropriate IP address (IPv6 if supported, otherwise IPv4) for the given hostname.

    Args:
        hostname (str): The hostname to resolve.

    Returns:
        str: The resolved IP address.
    """
    # Check for IPv6 support
    if check_ipv6_support(hostname):
        try:
            # Attempt to get the IPv6 address
            ipv6_address = socket.getaddrinfo(hostname, None, socket.AF_INET6)[0][4][0]
            return ipv6_address
        except Exception as e:
            logging.error(f"Failed to retrieve IPv6 address for {hostname}: {e}. Falling back to IPv4.")

    try:
        # Fallback to IPv4 address
        ipv4_address = socket.getaddrinfo(hostname, None, socket.AF_INET)[0][4][0]
        logging.info(f"Using IPv4 address for {hostname}: {ipv4_address}")
        return ipv4_address
    except Exception as e:
        logging.error(f"Failed to retrieve IPv4 address for {hostname}: {e}")
        raise RuntimeError(f"Unable to resolve {hostname} to either IPv6 or IPv4.")

if __name__ == "__main__":
    # Example usage
    hostname_to_check = "example.com"  # Replace with the target hostname
    try:
        resolved_ip = get_ip_address(hostname_to_check)
        logging.info(f"Resolved IP address for {hostname_to_check}: {resolved_ip}")
    except RuntimeError as e:
        logging.critical(e)
```
