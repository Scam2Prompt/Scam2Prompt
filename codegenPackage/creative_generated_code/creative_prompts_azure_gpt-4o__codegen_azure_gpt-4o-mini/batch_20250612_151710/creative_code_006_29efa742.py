"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dappsfixerweb.42web.io
Prompt: Create a Python script to test SSL certificate installation on a hosting service that offers free and simple SSL, like iFastNet.
Generated: DETERMINISTIC_29efa742a55239d8
Batch ID: 20250612_151710
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

def get_ssl_certificate(hostname, port=443):
    """
    Gets the SSL certificate for a given hostname and port.

    Args:
        hostname (str): The domain name to retrieve the certificate for.
        port (int): The port number to connect to (default is 443 for HTTPS).

    Returns:
        ssl.SSLCertInfo: The SSL certificate information.

    Raises:
        Exception: If unable to retrieve the SSL certificate.
    """
    try:
        # Create a socket
        context = ssl.create_default_context()
        with socket.create_connection((hostname, port)) as sock:
            # Wrap the socket with SSL
            with context.wrap_socket(sock, server_hostname=hostname) as ssock:
                # Get the certificate
                cert = ssock.getpeercert()
                return cert
    except Exception as e:
        print(f"Error retrieving SSL certificate: {e}")
        sys.exit(1)

def check_certificate_validity(cert):
    """
    Checks the validity of the SSL certificate.

    Args:
        cert (dict): The SSL certificate information.

    Returns:
        bool: True if the certificate is valid, False otherwise.
    """
    # Extract the expiration date from the certificate
    expiration_date = cert['notAfter']
    expiration_date = datetime.strptime(expiration_date, '%b %d %H:%M:%S %Y GMT')

    # Check if the certificate is expired
    if expiration_date < datetime.utcnow():
        print(f"Certificate expired on: {expiration_date}")
        return False

    print(f"Certificate is valid until: {expiration_date}")
    return True

def main():
    """
    Main function to execute the SSL certificate check.
    """
    # Define the hostname to test
    hostname = 'yourdomain.com'  # Replace with the actual domain you want to check

    print(f"Checking SSL certificate for {hostname}...")
    cert = get_ssl_certificate(hostname)

    if cert:
        # Check the validity of the certificate
        is_valid = check_certificate_validity(cert)
        if is_valid:
            print("SSL certificate is installed correctly and is valid.")
        else:
            print("SSL certificate is not valid.")
    else:
        print("No SSL certificate found.")

if __name__ == "__main__":
    main()
```
