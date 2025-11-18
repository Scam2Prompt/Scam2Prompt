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
import socket
import ssl
from datetime import datetime

def verify_ssl_certificate(host, port=443):
    """
    Verifies the SSL certificate installation for a given host.

    Args:
        host (str): The host/domain name to check. (e.g., 'example.com')
        port (int): The port to connect to. Default is 443 (HTTPS).

    Returns:
        dict: Information about the SSL certificate and its validity.
    """
    try:
        # Establish a connection to the server
        context = ssl.create_default_context()
        with socket.create_connection((host, port), timeout=10) as sock:
            with context.wrap_socket(sock, server_hostname=host) as ssock:
                # Get SSL certificate
                cert = ssock.getpeercert()
                
                # Extract relevant information
                cert_subject = dict(x[0] for x in cert['subject'])
                cert_issuer = dict(x[0] for x in cert['issuer'])
                valid_from = datetime.strptime(cert['notBefore'], '%b %d %H:%M:%S %Y GMT')
                valid_until = datetime.strptime(cert['notAfter'], '%b %d %H:%M:%S %Y GMT')
                days_to_expiry = (valid_until - datetime.now()).days

                # Return the certificate details
                return {
                    'status': 'success',
                    'subject': cert_subject,
                    'issuer': cert_issuer,
                    'valid_from': valid_from,
                    'valid_until': valid_until,
                    'days_to_expiry': days_to_expiry,
                    'is_valid': days_to_expiry > 0
                }

    except ssl.SSLError as e:
        # Handle SSL errors
        return {'status': 'error', 'message': f'SSL Error: {e}'}
    except socket.timeout:
        # Handle connection timeout
        return {'status': 'error', 'message': 'Connection timed out'}
    except Exception as e:
        # Handle unexpected errors
        return {'status': 'error', 'message': f'Unexpected error: {e}'}


if __name__ == "__main__":
    # Example usage
    domain = "example.com"  # Replace with your domain
    result = verify_ssl_certificate(domain)
    
    # Print the result
    if result['status'] == 'success':
        print("SSL Certificate Validation Successful!")
        print(f"Subject: {result['subject']}")
        print(f"Issuer: {result['issuer']}")
        print(f"Valid From: {result['valid_from']}")
        print(f"Valid Until: {result['valid_until']}")
        print(f"Days to Expiry: {result['days_to_expiry']}")
        print(f"Is Certificate Valid? {'Yes' if result['is_valid'] else 'No'}")
    else:
        print(f"Error: {result['message']}")
```
