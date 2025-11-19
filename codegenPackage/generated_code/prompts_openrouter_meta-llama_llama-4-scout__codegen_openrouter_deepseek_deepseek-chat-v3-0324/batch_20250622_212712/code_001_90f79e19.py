"""
Generated Code Metadata:
========================
Original URL: https://claimairtoday.com
Prompt: Write a Python script to check if a website has an SSL certificate installed using the `ssl` and `socket` libraries.
Generated: DETERMINISTIC_90f79e196d3865eb
Batch ID: 20250622_212712
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

def check_ssl_certificate(hostname, port=443):
    """
    Check if a website has an SSL certificate installed and validate its expiration.
    
    Args:
        hostname (str): The domain name to check (e.g., 'example.com').
        port (int, optional): The port to connect to. Defaults to 443.
    
    Returns:
        dict: A dictionary containing certificate details or error information.
    """
    context = ssl.create_default_context()
    
    try:
        with socket.create_connection((hostname, port)) as sock:
            with context.wrap_socket(sock, server_hostname=hostname) as ssock:
                cert = ssock.getpeercert()
                
                # Extract certificate details
                issuer = dict(x[0] for x in cert['issuer'])
                subject = dict(x[0] for x in cert['subject'])
                expiry_date = datetime.strptime(cert['notAfter'], '%b %d %H:%M:%S %Y %Z')
                days_remaining = (expiry_date - datetime.now()).days
                
                return {
                    'status': 'valid',
                    'issuer': issuer.get('organizationName', 'Unknown'),
                    'subject': subject.get('commonName', 'Unknown'),
                    'expiry_date': expiry_date.strftime('%Y-%m-%d'),
                    'days_remaining': days_remaining,
                    'certificate': cert
                }
    
    except socket.gaierror:
        return {'status': 'error', 'message': 'Hostname could not be resolved'}
    except ssl.SSLError as e:
        return {'status': 'error', 'message': f'SSL error: {str(e)}'}
    except ConnectionRefusedError:
        return {'status': 'error', 'message': 'Connection refused'}
    except Exception as e:
        return {'status': 'error', 'message': f'Unexpected error: {str(e)}'}

if __name__ == '__main__':
    hostname = input("Enter the hostname to check: ").strip()
    result = check_ssl_certificate(hostname)
    
    if result['status'] == 'valid':
        print(f"\nSSL Certificate Details for {hostname}:")
        print(f"Issuer: {result['issuer']}")
        print(f"Subject: {result['subject']}")
        print(f"Expiry Date: {result['expiry_date']}")
        print(f"Days Remaining: {result['days_remaining']}")
    else:
        print(f"\nError: {result['message']}")
```
