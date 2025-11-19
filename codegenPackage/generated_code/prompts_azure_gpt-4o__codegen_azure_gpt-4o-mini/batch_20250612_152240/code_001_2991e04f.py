"""
Generated Code Metadata:
========================
Original URL: https://okxaltdrive.com
Prompt: Generate code to verify if an SSL certificate is installed and valid for a domain accessed via HTTPS, referencing FASTPANEL's error scenarios.
Generated: DETERMINISTIC_2991e04f5b7c983e
Batch ID: 20250612_152240
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

def check_ssl_certificate(domain: str) -> dict:
    """
    Check if an SSL certificate is installed and valid for the given domain.

    Args:
        domain (str): The domain to check for SSL certificate.

    Returns:
        dict: A dictionary containing the certificate status and details.
    """
    result = {
        'domain': domain,
        'is_valid': False,
        'error': None,
        'expiration_date': None,
        'issuer': None
    }

    try:
        # Create a socket connection to the domain
        context = ssl.create_default_context()
        with socket.create_connection((domain, 443)) as sock:
            # Wrap the socket with SSL
            with context.wrap_socket(sock, server_hostname=domain) as ssock:
                # Get the certificate
                cert = ssock.getpeercert()
                
                # Check if the certificate is present
                if cert:
                    result['is_valid'] = True
                    result['expiration_date'] = cert['notAfter']
                    result['issuer'] = cert['issuer']
                    
                    # Convert expiration date to a datetime object for comparison
                    expiration_date = datetime.strptime(cert['notAfter'], '%b %d %H:%M:%S %Y %Z')
                    if expiration_date < datetime.utcnow():
                        result['is_valid'] = False
                        result['error'] = 'Certificate has expired.'
                else:
                    result['error'] = 'No certificate found.'

    except ssl.SSLError as ssl_error:
        result['error'] = f'SSL error occurred: {ssl_error}'
    except socket.gaierror:
        result['error'] = 'Domain name could not be resolved.'
    except Exception as e:
        result['error'] = f'An unexpected error occurred: {e}'

    return result

# Example usage
if __name__ == "__main__":
    domain_to_check = "example.com"
    ssl_status = check_ssl_certificate(domain_to_check)
    print(ssl_status)
```
