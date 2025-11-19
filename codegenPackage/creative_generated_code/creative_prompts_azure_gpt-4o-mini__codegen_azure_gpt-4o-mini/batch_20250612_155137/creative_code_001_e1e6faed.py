"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://checker-ethena.fi
Prompt: How can I troubleshoot SSL certificate issues for my website that is accessed via HTTPS?
Generated: DETERMINISTIC_e1e6faed63a1ac56
Batch ID: 20250612_155137
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import ssl
import socket
import sys
from datetime import datetime

def get_ssl_info(hostname: str, port: int = 443) -> dict:
    """
    Retrieve SSL certificate information for a given hostname.

    :param hostname: The hostname of the website to check.
    :param port: The port (default is 443 for HTTPS).
    :return: A dictionary containing SSL certificate details.
    """
    ssl_info = {}
    
    try:
        # Create a socket connection to the host
        context = ssl.create_default_context()
        with socket.create_connection((hostname, port)) as sock:
            # Wrap the socket with SSL
            with context.wrap_socket(sock, server_hostname=hostname) as ssock:
                # Get the SSL certificate
                cert = ssock.getpeercert()
                ssl_info['subject'] = dict(x[0] for x in cert['subject'])
                ssl_info['issuer'] = dict(x[0] for x in cert['issuer'])
                ssl_info['notBefore'] = cert['notBefore']
                ssl_info['notAfter'] = cert['notAfter']
                ssl_info['version'] = cert['version']
                ssl_info['serialNumber'] = cert['serialNumber']
                
                # Convert date strings to datetime objects for easier handling
                ssl_info['notBefore'] = datetime.strptime(ssl_info['notBefore'], "%b %d %H:%M:%S %Y %Z")
                ssl_info['notAfter'] = datetime.strptime(ssl_info['notAfter'], "%b %d %H:%M:%S %Y %Z")

    except Exception as e:
        print(f"Error retrieving SSL certificate for {hostname}: {e}", file=sys.stderr)
        return {}

    return ssl_info

def print_ssl_info(info: dict):
    """
    Print SSL certificate information in a readable format.

    :param info: A dictionary containing SSL certificate details.
    """
    if not info:
        print("No SSL information available.")
        return

    print("SSL Certificate Information:")
    print(f"  Subject: {info['subject']}")
    print(f"  Issuer: {info['issuer']}")
    print(f"  Valid From: {info['notBefore']}")
    print(f"  Valid Until: {info['notAfter']}")
    print(f"  Version: {info['version']}")
    print(f"  Serial Number: {info['serialNumber']}")

def main():
    # Replace 'example.com' with the desired hostname to check
    hostname = 'example.com'
    ssl_info = get_ssl_info(hostname)
    print_ssl_info(ssl_info)

if __name__ == "__main__":
    main()
```

Make sure to replace `'example.com'` with the hostname of the website you wish to check for SSL certificate issues. This script retrieves and prints SSL certificate details for the specified hostname.
