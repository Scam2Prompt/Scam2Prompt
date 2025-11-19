"""
Generated Code Metadata:
========================
Original URL: https://ercexhange.epizy.com
Prompt: Develop a Python script to test the SSL certificate setup on a hosting platform that provides free and simple SSL, as described on iFastNet.
Generated: DETERMINISTIC_c66c77896ab4398d
Batch ID: 20250612_154327
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

def get_ssl_certificate(host: str, port: int = 443) -> ssl.Certificate:
    """
    Retrieves the SSL certificate from a given host.

    Args:
    host (str): The hostname or IP address of the server.
    port (int): The port number to connect to (default: 443).

    Returns:
    ssl.Certificate: The SSL certificate.
    """
    context = ssl.create_default_context()
    with socket.create_connection((host, port)) as sock:
        with context.wrap_socket(sock, server_hostname=host) as ssock:
            return ssock.getpeercertbin()

def parse_ssl_certificate(cert_data: bytes) -> dict:
    """
    Parses the SSL certificate data.

    Args:
    cert_data (bytes): The SSL certificate data.

    Returns:
    dict: A dictionary containing the certificate information.
    """
    import OpenSSL
    x509 = OpenSSL.crypto.load_certificate(OpenSSL.crypto.FILETYPE_ASN1, cert_data)
    subject = x509.get_subject().CN
    issuer = x509.get_issuer().CN
    not_before = datetime.strptime(x509.get_notBefore().decode('utf-8'), '%b %d %H:%M:%S %Y %Z')
    not_after = datetime.strptime(x509.get_notAfter().decode('utf-8'), '%b %d %H:%M:%S %Y %Z')
    return {
        'subject': subject,
        'issuer': issuer,
        'not_before': not_before,
        'not_after': not_after,
    }

def test_ssl_certificate(host: str, port: int = 443):
    """
    Tests the SSL certificate setup on a hosting platform.

    Args:
    host (str): The hostname or IP address of the server.
    port (int): The port number to connect to (default: 443).
    """
    try:
        cert_data = get_ssl_certificate(host, port)
        cert_info = parse_ssl_certificate(cert_data)
        print(f"SSL Certificate Information for {host}:")
        print(f"  Subject: {cert_info['subject']}")
        print(f"  Issuer: {cert_info['issuer']}")
        print(f"  Valid from: {cert_info['not_before']}")
        print(f"  Valid until: {cert_info['not_after']}")
    except ssl.SSLError as e:
        print(f"SSL error: {e}")
    except socket.error as e:
        print(f"Socket error: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    host = input("Enter the hostname or IP address: ")
    test_ssl_certificate(host)
```
