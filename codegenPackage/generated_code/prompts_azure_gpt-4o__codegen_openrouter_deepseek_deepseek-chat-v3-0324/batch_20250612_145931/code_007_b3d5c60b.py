"""
Generated Code Metadata:
========================
Original URL: https://walletsignpage.rf.gd
Prompt: Create a Python script to test SSL certificates on a hosting service that provides free and simple SSL, as highlighted by iFastNet.
Generated: DETERMINISTIC_b3d5c60b6ad81e4b
Batch ID: 20250612_145931
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
    Check the SSL certificate of a given hostname and port.
    
    Args:
        hostname (str): The hostname to check.
        port (int, optional): The port to check. Defaults to 443.
    
    Returns:
        dict: A dictionary containing certificate details or error information.
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
                    'serial_number': cert.get('serialNumber', 'Unknown')
                }
    
    except socket.gaierror:
        return {'status': 'error', 'message': f'Hostname resolution failed for {hostname}'}
    except ssl.SSLError as e:
        return {'status': 'error', 'message': f'SSL error occurred: {str(e)}'}
    except socket.timeout:
        return {'status': 'error', 'message': 'Connection timed out'}
    except Exception as e:
        return {'status': 'error', 'message': f'Unexpected error: {str(e)}'}

def print_results(result):
    """Print the results of the SSL check in a readable format."""
    if result['status'] == 'valid':
        print(f"\nSSL Certificate Details for {result['hostname']}:")
        print(f"  - Issuer: {result['issuer']}")
        print(f"  - Subject: {result['subject']}")
        print(f"  - Valid From: {result['valid_from']}")
        print(f"  - Valid Until: {result['valid_until']}")
        print(f"  - Days Remaining: {result['days_remaining']}")
        print(f"  - Serial Number: {result['serial_number']}\n")
    else:
        print(f"\nError checking SSL certificate: {result['message']}\n")

def main():
    parser = argparse.ArgumentParser(description='Check SSL certificate details for a given hostname.')
    parser.add_argument('hostname', help='The hostname to check')
    parser.add_argument('-p', '--port', type=int, default=443, help='Port number (default: 443)')
    
    args = parser.parse_args()
    
    result = check_ssl_certificate(args.hostname, args.port)
    print_results(result)

if __name__ == '__main__':
    main()
```
