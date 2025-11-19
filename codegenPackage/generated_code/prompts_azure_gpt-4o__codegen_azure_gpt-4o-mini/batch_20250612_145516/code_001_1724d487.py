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
import argparse
from datetime import datetime

def check_ssl_certificate(domain):
    """
    Check if an SSL certificate is installed for the given domain.

    Args:
        domain (str): The domain to check for SSL certificate.

    Returns:
        dict: A dictionary containing certificate details or an error message.
    """
    try:
        # Create a connection to the domain on port 443 (HTTPS)
        context = ssl.create_default_context()
        with socket.create_connection((domain, 443)) as sock:
            # Wrap the socket with SSL
            with context.wrap_socket(sock, server_hostname=domain) as ssock:
                # Get the certificate
                cert = ssock.getpeercert()
                return {
                    'subject': dict(x[0] for x in cert['subject']),
                    'issuer': dict(x[0] for x in cert['issuer']),
                    'notBefore': cert['notBefore'],
                    'notAfter': cert['notAfter'],
                    'version': cert['version'],
                }
    except ssl.SSLError as e:
        return {'error': f'SSL error: {str(e)}'}
    except socket.gaierror as e:
        return {'error': f'Address-related error: {str(e)}'}
    except Exception as e:
        return {'error': f'An unexpected error occurred: {str(e)}'}

def format_certificate_info(cert_info):
    """
    Format the SSL certificate information for display.

    Args:
        cert_info (dict): The certificate information.

    Returns:
        str: Formatted string of certificate information.
    """
    if 'error' in cert_info:
        return cert_info['error']
    
    return (
        f"Subject: {cert_info['subject']}\n"
        f"Issuer: {cert_info['issuer']}\n"
        f"Valid From: {cert_info['notBefore']}\n"
        f"Valid Until: {cert_info['notAfter']}\n"
        f"Version: {cert_info['version']}\n"
    )

def main():
    # Set up argument parsing
    parser = argparse.ArgumentParser(description='Check SSL certificate for a domain.')
    parser.add_argument('domain', type=str, help='The domain to check (e.g., example.com)')
    args = parser.parse_args()

    # Check the SSL certificate
    cert_info = check_ssl_certificate(args.domain)

    # Display the certificate information
    print(format_certificate_info(cert_info))

if __name__ == '__main__':
    main()
```
