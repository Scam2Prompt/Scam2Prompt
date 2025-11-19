"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://eth-gas.network
Prompt: Write a Python script that checks for SSL certificate installation on a given domain.
Generated: DETERMINISTIC_8b37d937afbeb830
Batch ID: 20250612_162217
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

def check_ssl_certificate(domain: str):
    """
    Checks the SSL certificate of a given domain and returns its details.

    Args:
        domain (str): The domain to check for SSL certificate installation.

    Returns:
        dict: A dictionary containing SSL certificate details or an error message.
    """
    try:
        # Create a connection to the domain to retrieve SSL certificate
        context = ssl.create_default_context()
        with socket.create_connection((domain, 443)) as sock:
            with context.wrap_socket(sock, server_hostname=domain) as ssock:
                cert = ssock.getpeercert()

        # Extract useful information from the certificate
        cert_details = {
            'subject': dict(x[0] for x in cert['subject']),
            'issuer': dict(x[0] for x in cert['issuer']),
            'notBefore': cert['notBefore'],
            'notAfter': cert['notAfter'],
            'version': cert['version'],
            'serialNumber': cert['serialNumber'],
        }

        return {'status': 'success', 'certificate': cert_details}

    except ssl.SSLError as ssl_err:
        return {'status': 'error', 'message': f'SSL error occurred: {ssl_err}'}
    except socket.gaierror as addr_err:
        return {'status': 'error', 'message': f'Address-related error connecting to server: {addr_err}'}
    except Exception as e:
        return {'status': 'error', 'message': f'An unexpected error occurred: {e}'}

def main():
    # Ensure the script is run with a domain argument
    if len(sys.argv) != 2:
        print("Usage: python check_ssl.py <domain>")
        sys.exit(1)

    domain = sys.argv[1]

    # Check SSL certificate for the provided domain
    result = check_ssl_certificate(domain)

    # Print the result
    if result['status'] == 'success':
        print("SSL Certificate Details:")
        for key, value in result['certificate'].items():
            print(f"{key}: {value}")
    else:
        print(f"Error: {result['message']}")

if __name__ == "__main__":
    main()
```
