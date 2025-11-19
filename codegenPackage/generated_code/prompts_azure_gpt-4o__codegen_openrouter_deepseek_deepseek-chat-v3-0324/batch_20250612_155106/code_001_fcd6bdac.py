"""
Generated Code Metadata:
========================
Original URL: https://metacoins.in
Prompt: Generate a script to verify if an SSL certificate is installed for a domain using OpenSSL or a similar library, referencing FASTPANEL's HTTPS-related troubleshooting.
Generated: DETERMINISTIC_fcd6bdac6745c9d6
Batch ID: 20250612_155106
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
#!/usr/bin/env python3
import socket
import ssl
import argparse
from datetime import datetime

def verify_ssl_certificate(domain, port=443, timeout=10):
    """
    Verify SSL certificate for a given domain and port.
    
    Args:
        domain (str): Domain name to check.
        port (int, optional): Port number. Defaults to 443.
        timeout (int, optional): Connection timeout in seconds. Defaults to 10.
    
    Returns:
        dict: Dictionary containing certificate details and verification status.
    """
    context = ssl.create_default_context()
    context.check_hostname = True
    context.verify_mode = ssl.CERT_REQUIRED
    
    try:
        with socket.create_connection((domain, port), timeout=timeout) as sock:
            with context.wrap_socket(sock, server_hostname=domain) as ssock:
                cert = ssock.getpeercert()
                
                # Parse certificate details
                issuer = dict(x[0] for x in cert['issuer'])
                subject = dict(x[0] for x in cert['subject'])
                not_before = datetime.strptime(cert['notBefore'], '%b %d %H:%M:%S %Y %Z')
                not_after = datetime.strptime(cert['notAfter'], '%b %d %H:%M:%S %Y %Z')
                
                return {
                    'domain': domain,
                    'status': 'valid',
                    'issuer': issuer.get('organizationName', 'Unknown'),
                    'subject': subject.get('commonName', 'Unknown'),
                    'valid_from': not_before,
                    'valid_until': not_after,
                    'days_remaining': (not_after - datetime.now()).days,
                    'errors': None
                }
    
    except socket.timeout:
        return {
            'domain': domain,
            'status': 'error',
            'errors': 'Connection timeout'
        }
    except ssl.SSLError as e:
        return {
            'domain': domain,
            'status': 'error',
            'errors': f'SSL Error: {str(e)}'
        }
    except socket.gaierror:
        return {
            'domain': domain,
            'status': 'error',
            'errors': 'DNS resolution failed'
        }
    except Exception as e:
        return {
            'domain': domain,
            'status': 'error',
            'errors': f'Unexpected error: {str(e)}'
        }

def main():
    parser = argparse.ArgumentParser(description='Verify SSL certificate for a domain')
    parser.add_argument('domain', help='Domain name to check')
    parser.add_argument('--port', type=int, default=443, help='Port number (default: 443)')
    parser.add_argument('--timeout', type=int, default=10, help='Connection timeout in seconds (default: 10)')
    args = parser.parse_args()
    
    result = verify_ssl_certificate(args.domain, args.port, args.timeout)
    
    if result['status'] == 'valid':
        print(f"SSL Certificate for {result['domain']} is VALID")
        print(f"Issuer: {result['issuer']}")
        print(f"Subject: {result['subject']}")
        print(f"Valid From: {result['valid_from']}")
        print(f"Valid Until: {result['valid_until']}")
        print(f"Days Remaining: {result['days_remaining']}")
    else:
        print(f"SSL Certificate verification FAILED for {result['domain']}")
        print(f"Error: {result['errors']}")

if __name__ == '__main__':
    main()
```
