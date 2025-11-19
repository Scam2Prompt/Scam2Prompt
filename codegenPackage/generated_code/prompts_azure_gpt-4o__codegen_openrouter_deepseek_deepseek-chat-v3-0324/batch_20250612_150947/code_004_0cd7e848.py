"""
Generated Code Metadata:
========================
Original URL: https://community-forum.42web.io
Prompt: Create a script to test and verify SSL installation on a hosting service that offers free and simple SSL, as mentioned in iFastNet hosting features.
Generated: DETERMINISTIC_0cd7e848bb070ab7
Batch ID: 20250612_150947
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

def verify_ssl(hostname, port=443):
    """
    Verify SSL certificate installation for a given hostname and port.
    
    Args:
        hostname (str): The domain name to check.
        port (int, optional): The port to check. Defaults to 443.
    
    Returns:
        dict: Dictionary containing verification results.
    """
    context = ssl.create_default_context()
    
    try:
        with socket.create_connection((hostname, port)) as sock:
            with context.wrap_socket(sock, server_hostname=hostname) as ssock:
                cert = ssock.getpeercert()
                
                # Extract certificate information
                issuer = dict(x[0] for x in cert['issuer'])
                subject = dict(x[0] for x in cert['subject'])
                valid_from = datetime.strptime(cert['notBefore'], '%b %d %H:%M:%S %Y %Z')
                valid_to = datetime.strptime(cert['notAfter'], '%b %d %H:%M:%S %Y %Z')
                
                return {
                    'status': 'success',
                    'hostname': hostname,
                    'port': port,
                    'issuer': issuer.get('organizationName', 'Unknown'),
                    'subject': subject.get('commonName', 'Unknown'),
                    'valid_from': valid_from,
                    'valid_to': valid_to,
                    'days_remaining': (valid_to - datetime.now()).days,
                    'protocol': ssock.version(),
                    'certificate': cert
                }
    
    except socket.gaierror:
        return {'status': 'error', 'message': f'Hostname {hostname} could not be resolved'}
    except ssl.SSLError as e:
        return {'status': 'error', 'message': f'SSL error: {str(e)}'}
    except Exception as e:
        return {'status': 'error', 'message': f'Unexpected error: {str(e)}'}

def print_results(results):
    """Print verification results in a human-readable format."""
    if results['status'] == 'success':
        print(f"\nSSL Verification Successful for {results['hostname']}:{results['port']}")
        print("=" * 50)
        print(f"Issuer: {results['issuer']}")
        print(f"Subject: {results['subject']}")
        print(f"Valid From: {results['valid_from']}")
        print(f"Valid To: {results['valid_to']}")
        print(f"Days Remaining: {results['days_remaining']}")
        print(f"Protocol: {results['protocol']}")
        print("=" * 50)
    else:
        print(f"\nSSL Verification Failed for {results.get('hostname', 'unknown')}")
        print("=" * 50)
        print(f"Error: {results['message']}")
        print("=" * 50)

def main():
    parser = argparse.ArgumentParser(description='Verify SSL certificate installation for a domain.')
    parser.add_argument('hostname', help='Domain name to check (e.g., example.com)')
    parser.add_argument('-p', '--port', type=int, default=443, help='Port to check (default: 443)')
    
    args = parser.parse_args()
    
    results = verify_ssl(args.hostname, args.port)
    print_results(results)

if __name__ == '__main__':
    main()
```
