"""
Generated Code Metadata:
========================
Original URL: https://dappsconnect.42web.io
Prompt: Generate a script to verify SSL installation on a hosting service that provides free and simple SSL, as described on iFastNet hosting.
Generated: DETERMINISTIC_a731c68819bf7957
Batch ID: 20250612_154740
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
import sys
from datetime import datetime

def get_ssl_cert_info(hostname, port=443):
    """
    Retrieve SSL certificate information for a given hostname and port.

    :param hostname: The hostname to check for SSL certificate.
    :param port: The port to connect to (default is 443 for HTTPS).
    :return: A dictionary containing certificate details or None if an error occurs.
    """
    try:
        # Create a socket connection to the server
        context = ssl.create_default_context()
        with socket.create_connection((hostname, port)) as sock:
            # Wrap the socket with SSL
            with context.wrap_socket(sock, server_hostname=hostname) as ssock:
                # Get the certificate
                cert = ssock.getpeercert()
                return cert
    except Exception as e:
        print(f"Error retrieving SSL certificate: {e}")
        return None

def check_ssl_expiration(cert):
    """
    Check the expiration date of the SSL certificate.

    :param cert: The SSL certificate dictionary.
    :return: A string indicating the expiration status.
    """
    if cert:
        # Extract the expiration date from the certificate
        expiration_date = cert['notAfter']
        expiration_datetime = datetime.strptime(expiration_date, '%b %d %H:%M:%S %Y %Z')
        current_datetime = datetime.utcnow()

        # Check if the certificate is expired
        if expiration_datetime < current_datetime:
            return "The SSL certificate has expired."
        else:
            return f"The SSL certificate is valid until {expiration_datetime}."
    return "No certificate information available."

def main():
    """
    Main function to verify SSL installation on a specified hostname.
    """
    # Define the hostname to check
    hostname = "example.com"  # Replace with the actual hostname

    # Get SSL certificate information
    cert_info = get_ssl_cert_info(hostname)

    # Check the SSL certificate expiration status
    expiration_status = check_ssl_expiration(cert_info)

    # Print the results
    print(f"SSL Certificate Information for {hostname}:")
    print(expiration_status)

if __name__ == "__main__":
    main()
```
