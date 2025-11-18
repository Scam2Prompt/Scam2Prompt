"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jiotv.infinityfreeapp.com
Prompt: Write a script to verify SSL certificate installation on a hosting platform that offers free and simple SSL.
Generated: DETERMINISTIC_b9a2af53a86828d2
Batch ID: 20250612_154657
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

def get_ssl_certificate(hostname, port=443):
    """
    Retrieve the SSL certificate for a given hostname and port.
    
    Args:
        hostname (str): The hostname to check.
        port (int): The port number for the SSL connection. Default is 443.
        
    Returns:
        ssl.SSLCertInfo: The SSL certificate information.
    """
    context = ssl.create_default_context()
    with socket.create_connection((hostname, port)) as sock:
        with context.wrap_socket(sock, server_hostname=hostname) as ssock:
            return ssock.getpeercert()


def verify_ssl_certificate(cert):
    """
    Verify the SSL certificate for expiration and validity.
    
    Args:
        cert (dict): The SSL certificate information.

    Returns:
        dict: A dictionary with verification results.
    """
    current_time = datetime.utcnow()
    cert_not_before = datetime.strptime(cert['notBefore'], '%b %d %H:%M:%S %Y GMT')
    cert_not_after = datetime.strptime(cert['notAfter'], '%b %d %H:%M:%S %Y GMT')

    is_valid = cert_not_before <= current_time <= cert_not_after
    
    return {
        'issuer': cert['issuer'],
        'not_before': cert_not_before,
        'not_after': cert_not_after,
        'is_valid': is_valid
    }


def main():
    """
    Main function to verify the SSL certificate of a hosting platform.
    """
    hostname = input("Enter the hostname to verify SSL certificate: ")

    try:
        # Retrieve SSL certificate
        cert = get_ssl_certificate(hostname)
        # Verify SSL certificate
        verification_result = verify_ssl_certificate(cert)

        # Display verification results
        print(f"Issuer: {verification_result['issuer']}")
        print(f"Valid From: {verification_result['not_before']}")
        print(f"Valid Until: {verification_result['not_after']}")
        print(f"Is Valid: {verification_result['is_valid']}")
        
    except ssl.SSLError as ssl_error:
        print(f"SSL error occurred: {ssl_error}")
    except socket.error as sock_error:
        print(f"Socket error occurred: {sock_error}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
