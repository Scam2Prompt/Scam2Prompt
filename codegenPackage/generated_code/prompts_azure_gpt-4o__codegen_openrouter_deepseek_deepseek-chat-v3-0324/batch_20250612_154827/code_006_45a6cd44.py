"""
Generated Code Metadata:
========================
Original URL: https://poocoin.rf.gd
Prompt: Generate a Python script to test SSL certificate installation on a hosting platform that supports Python apps and offers free SSL, as mentioned on iFastNet hosting.
Generated: DETERMINISTIC_45a6cd44445f1e68
Batch ID: 20250612_154827
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
        hostname (str): The hostname to check (e.g., 'example.com')
        port (int): The port number (default: 443)
    
    Returns:
        dict: Certificate details including issuer, expiry, and validity
    """
    context = ssl.create_default_context()
    
    try:
        with socket.create_connection((hostname, port)) as sock:
            with context.wrap_socket(sock, server_hostname=hostname) as ssock:
                cert = ssock.getpeercert()
                
                # Parse certificate information
                issuer = dict(x[0] for x in cert['issuer'])
                subject = dict(x[0] for x in cert['subject'])
                not_before = datetime.strptime(cert['notBefore'], '%b %d %H:%M:%S %Y %Z')
                not_after = datetime.strptime(cert['notAfter'], '%b %d %H:%M:%S %Y %Z')
                
                return {
                    'hostname': hostname,
                    'port': port,
                    'issuer': issuer.get('organizationName', 'Unknown'),
                    'common_name': subject.get('commonName', 'Unknown'),
                    'valid_from': not_before,
                    'valid_until': not_after,
                    'is_valid': datetime.now() < not_after,
                    'days_remaining': (not_after - datetime.now()).days
                }
    
    except socket.gaierror:
        raise ValueError(f"Could not resolve hostname: {hostname}")
    except ConnectionRefusedError:
        raise ConnectionError(f"Connection refused to {hostname}:{port}")
    except ssl.SSLError as e:
        raise ssl.SSLError(f"SSL error occurred: {str(e)}")
    except Exception as e:
        raise Exception(f"An unexpected error occurred: {str(e)}")

def main():
    parser = argparse.ArgumentParser(description='SSL Certificate Checker')
    parser.add_argument('hostname', help='Hostname to check SSL certificate for')
    parser.add_argument('--port', type=int, default=443, help='Port number (default: 443)')
    
    args = parser.parse_args()
    
    try:
        cert_info = check_ssl_certificate(args.hostname, args.port)
        
        print("\nSSL Certificate Information:")
        print(f"Hostname: {cert_info['hostname']}")
        print(f"Port: {cert_info['port']}")
        print(f"Issuer: {cert_info['issuer']}")
        print(f"Common Name: {cert_info['common_name']}")
        print(f"Valid From: {cert_info['valid_from']}")
        print(f"Valid Until: {cert_info['valid_until']}")
        print(f"Days Remaining: {cert_info['days_remaining']}")
        print(f"Certificate is {'valid' if cert_info['is_valid'] else 'expired'}")
        
    except Exception as e:
        print(f"\nError: {str(e)}")
        exit(1)

if __name__ == "__main__":
    main()
```
