"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://eth-gas.network
Prompt: Generate code to verify if an SSL certificate is installed and valid for a given domain using Python libraries like `ssl` or `cryptography`.
Generated: DETERMINISTIC_c7e7657a76b6307e
Batch ID: 20250612_155006
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
from datetime import datetime


def verify_ssl_certificate(domain: str) -> dict:
    """
    Verifies if an SSL certificate is installed and valid for a given domain.

    Args:
        domain (str): The domain to check the SSL certificate for.

    Returns:
        dict: A dictionary containing the SSL certificate details and validity status.
              - 'valid' (bool): True if the certificate is valid, False otherwise.
              - 'expiration_date' (str): Expiration date of the certificate.
              - 'error' (str): Error message if any issues occur during verification.
    """
    cert_info = {
        'valid': False,
        'expiration_date': None,
        'error': None
    }

    try:
        # Create an SSL context
        context = ssl.create_default_context()

        # Retrieve the certificate from the domain
        with socket.create_connection((domain, 443)) as sock:
            # Wrap the socket for SSL
            with context.wrap_socket(sock, server_hostname=domain) as ssock:
                # Get the certificate
                cert = ssock.getpeercert()

        # Check the expiration date of the certificate
        expiration_date = cert['notAfter']
        cert_info['expiration_date'] = expiration_date

        # Convert the expiration date string to a datetime object
        expiration_datetime = datetime.strptime(expiration_date, '%b %d %H:%M:%S %Y %Z')

        # Set validity to True if the certificate is still valid
        cert_info['valid'] = expiration_datetime > datetime.utcnow()

    except ssl.SSLError as ssl_error:
        cert_info['error'] = f"SSL error occurred: {ssl_error}"
    except socket.error as socket_error:
        cert_info['error'] = f"Socket error occurred: {socket_error}"
    except Exception as e:
        cert_info['error'] = f"An unexpected error occurred: {e}"

    return cert_info


if __name__ == "__main__":
    # Example usage
    domain_to_check = "example.com"
    result = verify_ssl_certificate(domain_to_check)
    print(f"SSL Certificate verification for {domain_to_check}:")
    print(result)
```
