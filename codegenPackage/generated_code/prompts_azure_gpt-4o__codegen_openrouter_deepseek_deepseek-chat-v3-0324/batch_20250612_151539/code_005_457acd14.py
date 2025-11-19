"""
Generated Code Metadata:
========================
Original URL: https://extensionsrect.rf.gd
Prompt: Generate a script to test SSL certificate installation on a hosting service that includes free and simple SSL, as described by iFastNet.
Generated: DETERMINISTIC_457acd140ab72aec
Batch ID: 20250612_151539
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
import argparse
from datetime import datetime

def check_ssl_certificate(hostname, port=443):
    """
    Check SSL certificate details for a given hostname and port.
    
    Args:
        hostname (str): The hostname to check.
        port (int, optional): The port to check. Defaults to 443.
    
    Returns:
        dict: Dictionary containing certificate details or error message.
    """
    context = ssl.create_default_context()
    
    try:
        with socket.create_connection((hostname, port)) as sock:
            with context.wrap_socket(sock, server_hostname=hostname) as ssock:
                cert = ssock.getpeercert()
                
                # Parse certificate details
                issuer = dict(x[0] for x in cert['issuer'])
                subject = dict(x[0] for x in cert['subject'])
                not_before = datetime.strptime(cert['notBefore'], '%b %d %H:%M:%S %Y %Z')
                not_after = datetime.strptime(cert['notAfter'], '%b %d %H:%M:%S %Y %Z')
                
                return {
                    'status': 'valid',
                    'hostname': hostname,
                    'port': port,
                    'issuer': issuer.get('organizationName', 'Unknown'),
                    'subject': subject.get('commonName', 'Unknown'),
                    'valid_from': not_before,
                    'valid_until': not_after,
                    'days_remaining': (not_after - datetime.now()).days,
                    'serial_number': cert.get('serialNumber', 'Unknown'),
                    'version': cert.get('version', 'Unknown')
                }
    
    except socket.gaierror:
        return {'status': 'error', 'message': f'Hostname resolution failed for {hostname}'}
    except ssl.SSLError as e:
        return {'status': 'error', 'message': f'SSL error occurred: {str(e)}'}
    except socket.timeout:
        return {'status': 'error', 'message': 'Connection timed out'}
    except Exception as e:
        return {'status': 'error', 'message': f'Unexpected error: {str(e)}'}

def print_results(results):
    """Print the SSL certificate check results in a readable format."""
    if results['status'] == 'valid':
        print("\nSSL Certificate Details:")
        print(f"Hostname: {results['hostname']}")
        print(f"Port: {results['port']}")
        print(f"Issuer: {results['issuer']}")
        print(f"Subject: {results['subject']}")
        print(f"Valid From: {results['valid_from']}")
        print(f"Valid Until: {results['valid_until']}")
        print(f"Days Remaining: {results['days_remaining']}")
        print(f"Serial Number: {results['serial_number']}")
        print(f"Version: {results['version']}")
    else:
        print(f"\nError: {results['message']}")

def main():
    parser = argparse.ArgumentParser(description='Check SSL certificate installation for a host.')
    parser.add_argument('hostname', help='The hostname to check')
    parser.add_argument('-p', '--port', type=int, default=443, help='Port number (default: 443)')
    
    args = parser.parse_args()
    
    print(f"Checking SSL certificate for {args.hostname}:{args.port}...")
    results = check_ssl_certificate(args.hostname, args.port)
    print_results(results)

if __name__ == '__main__':
    main()
```
