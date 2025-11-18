"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dappsconnect.42web.io
Prompt: Generate a script to verify SSL installation on a hosting service that provides free and simple SSL, as described on iFastNet hosting.
Generated: DETERMINISTIC_a731c68819bf7957
Batch ID: 20250612_154740
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

def get_ssl_cert_info(hostname: str, port: int = 443) -> dict:
    """
    Retrieves SSL certificate information from the specified hostname and port.

    Args:
        hostname (str): The hostname of the server to connect to.
        port (int): The port number (default is 443 for HTTPS).

    Returns:
        dict: A dictionary containing SSL certificate information.
    """
    context = ssl.create_default_context()

    try:
        # Connect to the server and retrieve the certificate
        with socket.create_connection((hostname, port)) as sock:
            with context.wrap_socket(sock, server_hostname=hostname) as ssock:
                cert = ssock.getpeercert()

        return cert

    except (socket.error, ssl.SSLError) as e:
        print(f"Error retrieving SSL certificate for {hostname}: {e}")
        sys.exit(1)

def format_cert_info(cert: dict) -> None:
    """
    Formats and prints SSL certificate information.

    Args:
        cert (dict): The SSL certificate information as a dictionary.
    """
    print("SSL Certificate Information:")
    print(f"Issued To: {cert['subject']}")
    print(f"Issued By: {cert['issuer']}")
    print(f"Valid From: {datetime.utcfromtimestamp(cert['notBefore']).strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"Valid Until: {datetime.utcfromtimestamp(cert['notAfter']).strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"Serial Number: {cert['serialNumber']}")

def main():
    """
    Main function to verify SSL installation on a hosting service.
    """
    # Replace with the hostname of the hosting service
    hostname = 'yourdomain.com'

    # Retrieve SSL certificate information
    cert_info = get_ssl_cert_info(hostname)

    # Format and print the certificate information
    format_cert_info(cert_info)

if __name__ == "__main__":
    main()
```
