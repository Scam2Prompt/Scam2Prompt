"""
Generated Code Metadata:
========================
Original URL: https://connectprotocol.42web.io
Prompt: Create a Python script for SSL certificate validation and explain how to use it on a hosting platform that offers free and simple SSL, as described by iFastNet.
Generated: DETERMINISTIC_23dbcc21721dfa7c
Batch ID: 20250612_145238
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import ssl
import socket
from datetime import datetime

def validate_ssl_certificate(hostname, port=443):
    """
    Validate SSL certificate for a given hostname.

    Args:
        hostname (str): Hostname to validate SSL certificate for.
        port (int): Port number to use for validation (default: 443).

    Returns:
        bool: True if SSL certificate is valid, False otherwise.
    """

    # Create a socket object
    context = ssl.create_default_context()
    with socket.create_connection((hostname, port)) as sock:
        with context.wrap_socket(sock, server_hostname=hostname) as ssock:
            # Get SSL certificate information
            ssl_info = ssock.getpeercert()

            # Check certificate expiration
            not_after = ssl_info['notAfter']
            not_after_date = datetime.strptime(not_after, '%b %d %H:%M:%S %Y %Z')
            if not_after_date < datetime.now():
                print(f"Certificate for {hostname} has expired.")
                return False

            # Check certificate subject and hostname
            subject = ssl_info['subject']
            if hostname not in subject[0][1]:
                print(f"Certificate subject mismatch for {hostname}.")
                return False

            print(f"SSL certificate for {hostname} is valid.")
            return True

def main():
    try:
        hostname = input("Enter hostname (e.g., example.com): ")
        port = int(input("Enter port number (default: 443): ") or 443)
        validate_ssl_certificate(hostname, port)
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
