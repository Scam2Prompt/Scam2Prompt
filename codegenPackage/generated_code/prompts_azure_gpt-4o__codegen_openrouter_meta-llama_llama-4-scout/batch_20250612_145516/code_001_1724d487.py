"""
Generated Code Metadata:
========================
Original URL: https://scroll-lo.com
Prompt: Generate a script to verify if an SSL certificate is installed for a domain accessed via HTTPS, referencing FASTPANEL server settings.
Generated: DETERMINISTIC_1724d487d2da1660
Batch ID: 20250612_145516
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
from typing import Tuple

def get_ssl_certificate(domain: str, port: int = 443) -> Tuple[ssl.SSLSocket, str]:
    """
    Retrieves the SSL certificate for a given domain.

    Args:
    - domain (str): The domain to retrieve the SSL certificate for.
    - port (int): The port to use for the connection. Defaults to 443.

    Returns:
    - A tuple containing the SSL socket and the SSL certificate in PEM format.
    """
    context = ssl.create_default_context()
    with socket.create_connection((domain, port)) as sock:
        with context.wrap_socket(sock, server_hostname=domain) as ssock:
            # Get the SSL certificate
            der_cert = ssock.getpeercert(binary_form=True)
            # Convert DER to PEM
            import base64
            import OpenSSL
            pem_cert = OpenSSL.crypto.dump_certificate(OpenSSL.crypto.FILETYPE_PEM, der_cert)
            return ssock, pem_cert.decode('utf-8')

def verify_ssl_certificate(domain: str, expected_issuer: str = None, expected_subject: str = None, port: int = 443) -> bool:
    """
    Verifies if an SSL certificate is installed for a domain.

    Args:
    - domain (str): The domain to verify the SSL certificate for.
    - expected_issuer (str): The expected issuer of the SSL certificate. Defaults to None.
    - expected_subject (str): The expected subject of the SSL certificate. Defaults to None.
    - port (int): The port to use for the connection. Defaults to 443.

    Returns:
    - True if the SSL certificate is valid, False otherwise.
    """
    try:
        ssock, pem_cert = get_ssl_certificate(domain, port)
        ssock.close()

        import OpenSSL
        x509 = OpenSSL.crypto.load_certificate(OpenSSL.crypto.FILETYPE_PEM, pem_cert)

        if expected_issuer and x509.get_issuer().CN != expected_issuer:
            print(f"Issuer mismatch: expected {expected_issuer}, got {x509.get_issuer().CN}")
            return False

        if expected_subject and x509.get_subject().CN != expected_subject:
            print(f"Subject mismatch: expected {expected_subject}, got {x509.get_subject().CN}")
            return False

        # Additional verification steps can be added here

        return True

    except ssl.SSLError as e:
        print(f"SSL error: {e}")
        return False
    except socket.error as e:
        print(f"Socket error: {e}")
        return False
    except Exception as e:
        print(f"An error occurred: {e}")
        return False

def check_fastpanel_ssl(FASTPANEL_DOMAIN: str, FASTPANEL_HTTPS_PORT: int) -> bool:
    """
    Checks if an SSL certificate is installed for the FASTPANEL server.

    Args:
    - FASTPANEL_DOMAIN (str): The domain of the FASTPANEL server.
    - FASTPANEL_HTTPS_PORT (int): The HTTPS port of the FASTPANEL server.

    Returns:
    - True if the SSL certificate is valid, False otherwise.
    """
    return verify_ssl_certificate(FASTPANEL_DOMAIN, port=FASTPANEL_HTTPS_PORT)

if __name__ == "__main__":
    FASTPANEL_DOMAIN = "your_fastpanel_domain.com"
    FASTPANEL_HTTPS_PORT = 443

    if check_fastpanel_ssl(FASTPANEL_DOMAIN, FASTPANEL_HTTPS_PORT):
        print("SSL certificate is valid")
    else:
        print("SSL certificate is not valid")
```
