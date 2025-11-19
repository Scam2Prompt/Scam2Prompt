"""
Generated Code Metadata:
========================
Original URL: https://ercexhange.epizy.com
Prompt: Develop a Python script to test the SSL certificate setup on a hosting platform that provides free and simple SSL, as described on iFastNet.
Generated: DETERMINISTIC_c66c77896ab4398d
Batch ID: 20250612_154327
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
                    'common_name': subject.get('commonName', 'Unknown'),
                    'not_before': not_before,
                    'not_after': not_after,
                    'expires_in': (not_after - datetime.now()).days,
                    'serial_number': cert.get('serialNumber', 'Unknown'),
                    'version': cert.get('version', 'Unknown')
                }
    
    except socket.gaierror:
        return {'status': 'error', 'message': f'Hostname {hostname} could not be resolved'}
    except ssl.SSLError as e:
        return {'status': 'error', 'message': f'SSL error: {str(e)}'}
    except ConnectionRefusedError:
        return {'status': 'error', 'message': f'Connection refused on port {port}'}
    except Exception as e:
        return {'status': 'error', 'message': f'Unexpected error: {str(e)}'}

def print_results(results):
    """Print the results of the SSL certificate check in a readable format."""
    if results['status'] == 'valid':
        print(f"\nSSL Certificate Details for {results['hostname']}:{results['port']}")
        print("=" * 50)
        print(f"Issuer: {results['issuer']}")
        print(f"Common Name: {results['common_name']}")
        print(f"Valid From: {results['not_before']}")
        print(f"Valid Until: {results['not_after']}")
        print(f"Expires In: {results['expires_in']} days")
        print(f"Serial Number: {results['serial_number']}")
        print(f"Version: {results['version']}")
        print("=" * 50)
    else:
        print(f"\nError: {results['message']}")

def main():
    """Main function to parse arguments and execute the SSL check."""
    parser = argparse.ArgumentParser(description='Check SSL certificate for a given hostname.')
    parser.add_argument('hostname', help='The hostname to check')
    parser.add_argument('-p', '--port', type=int, default=443, help='Port to check (default: 443)')
    
    args = parser.parse_args()
    
    results = check_ssl_certificate(args.hostname, args.port)
    print_results(results)

if __name__ == '__main__':
    main()
```
