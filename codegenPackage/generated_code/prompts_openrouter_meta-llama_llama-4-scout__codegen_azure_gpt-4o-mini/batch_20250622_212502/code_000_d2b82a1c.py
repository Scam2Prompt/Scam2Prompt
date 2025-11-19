"""
Generated Code Metadata:
========================
Original URL: https://ethegas.in
Prompt: Write a Python script to check if a domain has an SSL certificate installed using the `ssl` and `socket` libraries.
Generated: DETERMINISTIC_d2b82a1c61209418
Batch ID: 20250622_212502
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import socket
import ssl
from datetime import datetime

def check_ssl_certificate(domain):
    """
    Check if a domain has an SSL certificate installed and return its details.

    Args:
        domain (str): The domain name to check for SSL certificate.

    Returns:
        dict: A dictionary containing SSL certificate details or an error message.
    """
    try:
        # Create a socket connection to the domain
        port = 443  # Default port for HTTPS
        context = ssl.create_default_context()
        with socket.create_connection((domain, port)) as sock:
            # Wrap the socket with SSL
            with context.wrap_socket(sock, server_hostname=domain) as ssock:
                # Get the SSL certificate
                cert = ssock.getpeercert()
                
                # Extract relevant certificate details
                cert_details = {
                    'subject': dict(x[0] for x in cert['subject']),
                    'issuer': dict(x[0] for x in cert['issuer']),
                    'notBefore': cert['notBefore'],
                    'notAfter': cert['notAfter'],
                    'version': cert['version'],
                }
                
                # Convert date strings to datetime objects for better handling
                cert_details['notBefore'] = datetime.strptime(cert_details['notBefore'], '%b %d %H:%M:%S %Y %Z')
                cert_details['notAfter'] = datetime.strptime(cert_details['notAfter'], '%b %d %H:%M:%S %Y %Z')
                
                return {
                    'status': 'success',
                    'certificate': cert_details
                }
    except ssl.SSLError as e:
        return {
            'status': 'error',
            'message': f'SSL error occurred: {str(e)}'
        }
    except socket.gaierror as e:
        return {
            'status': 'error',
            'message': f'Address-related error connecting to server: {str(e)}'
        }
    except Exception as e:
        return {
            'status': 'error',
            'message': f'An unexpected error occurred: {str(e)}'
        }

if __name__ == "__main__":
    # Example usage
    domain_to_check = "example.com"
    result = check_ssl_certificate(domain_to_check)
    
    if result['status'] == 'success':
        print("SSL Certificate Details:")
        for key, value in result['certificate'].items():
            print(f"{key}: {value}")
    else:
        print(f"Error: {result['message']}")
```
