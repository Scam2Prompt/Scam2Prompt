"""
Generated Code Metadata:
========================
Original URL: https://bid-notification.bet
Prompt: Write a Python script to check if a domain has an SSL certificate installed using APIs like OpenSSL or Python's ssl library, considering the error message "Your domain has an AAAA record, but the site only works with IPv4 on the server."
Generated: DETERMINISTIC_1411fae5789919c9
Batch ID: 20250622_211811
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
import argparse
import sys

def check_ssl_certificate(domain, port=443):
    """
    Check if a domain has a valid SSL certificate installed.
    
    Args:
        domain (str): The domain to check (e.g., 'example.com').
        port (int): The port to check (default: 443).
    
    Returns:
        dict: A dictionary containing certificate details or error information.
    """
    result = {
        'domain': domain,
        'port': port,
        'has_ssl': False,
        'cert_info': None,
        'error': None
    }

    try:
        # Create a socket connection
        sock = socket.create_connection((domain, port))
        
        # Wrap the socket with SSL context
        context = ssl.create_default_context()
        with context.wrap_socket(sock, server_hostname=domain) as ssock:
            cert = ssock.getpeercert()
            result['has_ssl'] = True
            result['cert_info'] = {
                'issuer': dict(x[0] for x in cert['issuer']),
                'subject': dict(x[0] for x in cert['subject']),
                'version': cert.get('version'),
                'notBefore': cert['notBefore'],
                'notAfter': cert['notAfter'],
                'serialNumber': cert.get('serialNumber'),
            }
    
    except socket.gaierror as e:
        if "AAAA" in str(e) and "IPv4" in str(e):
            result['error'] = "Your domain has an AAAA record, but the site only works with IPv4 on the server."
        else:
            result['error'] = f"DNS resolution failed: {e}"
    except ssl.SSLError as e:
        result['error'] = f"SSL error: {e}"
    except Exception as e:
        result['error'] = f"Unexpected error: {e}"
    
    return result

def main():
    parser = argparse.ArgumentParser(description='Check SSL certificate for a domain.')
    parser.add_argument('domain', help='Domain to check (e.g., example.com)')
    parser.add_argument('--port', type=int, default=443, help='Port to check (default: 443)')
    args = parser.parse_args()

    result = check_ssl_certificate(args.domain, args.port)
    
    if result['error']:
        print(f"Error checking {args.domain}: {result['error']}", file=sys.stderr)
        sys.exit(1)
    
    if result['has_ssl']:
        print(f"SSL certificate found for {args.domain}:")
        for key, value in result['cert_info'].items():
            print(f"{key}: {value}")
    else:
        print(f"No SSL certificate found for {args.domain}")

if __name__ == '__main__':
    main()
```
