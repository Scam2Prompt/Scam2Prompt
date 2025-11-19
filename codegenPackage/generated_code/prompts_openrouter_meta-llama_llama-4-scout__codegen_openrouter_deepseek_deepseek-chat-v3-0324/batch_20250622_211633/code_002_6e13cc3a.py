"""
Generated Code Metadata:
========================
Original URL: https://4de192bb.d6c1924f22b82c8daa243716.workers.dev
Prompt: Generate a script to monitor and review the security of a website's connection, similar to the one described on this page.
Generated: DETERMINISTIC_6e13cc3ab54e9c7a
Batch ID: 20250622_211633
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import requests
import socket
import ssl
import datetime
from urllib.parse import urlparse
import argparse
import json
import sys

def check_ssl_certificate(hostname):
    """
    Check the SSL certificate details of the given hostname.
    
    Args:
        hostname (str): The hostname to check the SSL certificate for.
    
    Returns:
        dict: A dictionary containing SSL certificate details.
    """
    context = ssl.create_default_context()
    conn = context.wrap_socket(socket.socket(), server_hostname=hostname)
    conn.settimeout(10.0)
    
    try:
        conn.connect((hostname, 443))
        cert = conn.getpeercert()
        
        # Convert dates to readable format
        not_before = datetime.datetime.strptime(cert['notBefore'], '%b %d %H:%M:%S %Y %Z')
        not_after = datetime.datetime.strptime(cert['notAfter'], '%b %d %H:%M:%S %Y %Z')
        
        return {
            'issuer': dict(x[0] for x in cert['issuer']),
            'subject': dict(x[0] for x in cert['subject']),
            'version': cert.get('version', 'N/A'),
            'serialNumber': cert.get('serialNumber', 'N/A'),
            'notBefore': not_before.isoformat(),
            'notAfter': not_after.isoformat(),
            'expires_in_days': (not_after - datetime.datetime.now()).days,
            'signatureAlgorithm': cert.get('signatureAlgorithm', 'N/A'),
            'valid': True
        }
    except Exception as e:
        return {
            'error': str(e),
            'valid': False
        }
    finally:
        conn.close()

def check_http_headers(url):
    """
    Check HTTP security headers for the given URL.
    
    Args:
        url (str): The URL to check headers for.
    
    Returns:
        dict: A dictionary containing security headers and their values.
    """
    try:
        response = requests.get(url, timeout=10.0)
        headers = response.headers
        
        security_headers = {
            'Strict-Transport-Security': headers.get('Strict-Transport-Security', 'Not Present'),
            'Content-Security-Policy': headers.get('Content-Security-Policy', 'Not Present'),
            'X-Frame-Options': headers.get('X-Frame-Options', 'Not Present'),
            'X-Content-Type-Options': headers.get('X-Content-Type-Options', 'Not Present'),
            'Referrer-Policy': headers.get('Referrer-Policy', 'Not Present'),
            'Permissions-Policy': headers.get('Permissions-Policy', 'Not Present'),
            'X-XSS-Protection': headers.get('X-XSS-Protection', 'Not Present')
        }
        
        return security_headers
    except requests.exceptions.RequestException as e:
        return {
            'error': str(e)
        }

def check_website_security(url):
    """
    Perform a comprehensive security check for a website.
    
    Args:
        url (str): The URL to check.
    
    Returns:
        dict: A dictionary containing all security check results.
    """
    parsed_url = urlparse(url)
    hostname = parsed_url.hostname
    
    if not hostname:
        return {
            'error': 'Invalid URL provided'
        }
    
    ssl_info = check_ssl_certificate(hostname)
    headers_info = check_http_headers(url)
    
    return {
        'url': url,
        'hostname': hostname,
        'ssl_certificate': ssl_info,
        'security_headers': headers_info
    }

def main():
    parser = argparse.ArgumentParser(description='Website Security Checker')
    parser.add_argument('url', help='The URL to check')
    parser.add_argument('--output', help='Output file (JSON format)', default=None)
    args = parser.parse_args()
    
    try:
        result = check_website_security(args.url)
        
        if args.output:
            with open(args.output, 'w') as f:
                json.dump(result, f, indent=2)
            print(f"Results saved to {args.output}")
        else:
            print(json.dumps(result, indent=2))
    except Exception as e:
        print(f"An error occurred: {str(e)}", file=sys.stderr)
        sys.exit(1)

if __name__ == '__main__':
    main()
```
