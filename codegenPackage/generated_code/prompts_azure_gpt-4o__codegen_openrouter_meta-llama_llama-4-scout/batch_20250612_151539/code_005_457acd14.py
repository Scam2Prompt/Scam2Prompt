"""
Generated Code Metadata:
========================
Original URL: https://extensionsrect.rf.gd
Prompt: Generate a script to test SSL certificate installation on a hosting service that includes free and simple SSL, as described by iFastNet.
Generated: DETERMINISTIC_457acd140ab72aec
Batch ID: 20250612_151539
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
import OpenSSL
from OpenSSL import crypto

def get_certificate(host, port=443):
    """
    Retrieves the SSL certificate from a given host.

    Args:
        host (str): The hostname or IP address of the server.
        port (int): The port number to connect on. Defaults to 443.

    Returns:
        OpenSSL.crypto.X509: The SSL certificate.
    """
    context = ssl.create_default_context()
    with socket.create_connection((host, port)) as sock:
        with context.wrap_socket(sock, server_hostname=host) as ssock:
            return ssock.getpeercertbin()

def parse_certificate(cert_data):
    """
    Parses the SSL certificate data.

    Args:
        cert_data (bytes): The SSL certificate data.

    Returns:
        OpenSSL.crypto.X509: The parsed SSL certificate.
    """
    try:
        return crypto.load_certificate(crypto.FILETYPE_ASN1, cert_data)
    except OpenSSL.crypto.Error as e:
        print(f"Error parsing certificate: {e}")
        return None

def check_certificate(host, port=443):
    """
    Checks the SSL certificate installation on a hosting service.

    Args:
        host (str): The hostname or IP address of the server.
        port (int): The port number to connect on. Defaults to 443.

    Returns:
        bool: True if the certificate is valid, False otherwise.
    """
    cert_data = get_certificate(host, port)
    cert = parse_certificate(cert_data)
    if cert is None:
        return False

    # Check if the certificate is valid
    try:
        not_before = cert.get_notBefore()
        not_after = cert.get_notAfter()
        if not_before > OpenSSL.crypto.X509().get_notBefore() and not_after > OpenSSL.crypto.X509().get_notBefore():
            print("Certificate is valid")
            return True
        else:
            print("Certificate is not valid")
            return False
    except OpenSSL.crypto.Error as e:
        print(f"Error checking certificate: {e}")
        return False

def main():
    host = input("Enter the hostname or IP address: ")
    port = int(input("Enter the port number (default: 443): ") or 443)

    try:
        if check_certificate(host, port):
            print("SSL certificate installation is successful")
        else:
            print("SSL certificate installation failed")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
