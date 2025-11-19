"""
Generated Code Metadata:
========================
Original URL: https://tezwerwal.42web.io
Prompt: Write a Python script to test SSL functionality on a hosting platform that offers free and simple SSL, as described by iFastNet.
Generated: DETERMINISTIC_e56e0960296a0d4c
Batch ID: 20250612_151525
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

def test_ssl(hostname, port=443):
    """
    Test SSL functionality for a given hostname and port.
    
    Args:
        hostname (str): The hostname to test (e.g., example.com)
        port (int): The port to connect to (default: 443)
    
    Returns:
        dict: A dictionary containing SSL test results
    """
    result = {
        'hostname': hostname,
        'port': port,
        'success': False,
        'error': None,
        'cert_info': None,
        'protocol': None,
        'ciphers': None
    }
    
    try:
        # Create a socket and wrap it with SSL
        context = ssl.create_default_context()
        context.check_hostname = True
        context.verify_mode = ssl.CERT_REQUIRED
        
        with socket.create_connection((hostname, port)) as sock:
            with context.wrap_socket(sock, server_hostname=hostname) as ssock:
                result['success'] = True
                result['protocol'] = ssock.version()
                
                # Get certificate details
                cert = ssock.getpeercert()
                if cert:
                    result['cert_info'] = {
                        'issuer': dict(x[0] for x in cert['issuer']),
                        'subject': dict(x[0] for x in cert['subject']),
                        'valid_from': datetime.strptime(cert['notBefore'], '%b %d %H:%M:%S %Y %Z'),
                        'valid_to': datetime.strptime(cert['notAfter'], '%b %d %H:%M:%S %Y %Z'),
                        'serial_number': cert.get('serialNumber'),
                        'version': cert.get('version')
                    }
                
                # Get supported ciphers
                result['ciphers'] = ssock.shared_ciphers()
    
    except ssl.SSLError as e:
        result['error'] = f"SSL Error: {str(e)}"
    except socket.gaierror as e:
        result['error'] = f"Hostname resolution error: {str(e)}"
    except socket.timeout as e:
        result['error'] = f"Connection timeout: {str(e)}"
    except Exception as e:
        result['error'] = f"Unexpected error: {str(e)}"
    
    return result

def print_results(results):
    """Print the SSL test results in a readable format."""
    print(f"\nSSL Test Results for {results['hostname']}:{results['port']}")
    print("=" * 50)
    
    if results['success']:
        print("✅ SSL connection successful")
        print(f"🔒 Protocol: {results['protocol']}")
        
        if results['cert_info']:
            cert = results['cert_info']
            print("\n📜 Certificate Details:")
            print(f"  Issuer: {cert['issuer']}")
            print(f"  Subject: {cert['subject']}")
            print(f"  Valid From: {cert['valid_from']}")
            print(f"  Valid To: {cert['valid_to']}")
            print(f"  Serial Number: {cert['serial_number']}")
            print(f"  Version: {cert['version']}")
        
        if results['ciphers']:
            print("\n🔐 Supported Ciphers:")
            for cipher in results['ciphers']:
                print(f"  - {cipher[0]}")
    else:
        print(f"❌ SSL connection failed: {results['error']}")

def main():
    parser = argparse.ArgumentParser(description='Test SSL functionality for a given hostname.')
    parser.add_argument('hostname', help='The hostname to test (e.g., example.com)')
    parser.add_argument('-p', '--port', type=int, default=443, help='Port to connect to (default: 443)')
    
    args = parser.parse_args()
    results = test_ssl(args.hostname, args.port)
    print_results(results)

if __name__ == '__main__':
    main()
```
