"""
Generated Code Metadata:
========================
Original URL: https://dapp-webnode.rf.gd
Prompt: Generate a script to check SSL certificate installation on a hosting service that provides free and simple SSL, similar to iFastNet hosting.
Generated: DETERMINISTIC_6ad81665bb6d086d
Batch ID: 20250612_154502
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
import datetime

def check_ssl_certificate(hostname, port=443):
    """
    Check the SSL certificate for a given hostname and port.

    Args:
        hostname (str): The hostname to check.
        port (int): The port to connect to (default is 443 for HTTPS).

    Returns:
        dict: A dictionary containing certificate details or an error message.
    """
    try:
        # Create a socket connection to the server
        context = ssl.create_default_context()
        with socket.create_connection((hostname, port)) as sock:
            # Wrap the socket with SSL
            with context.wrap_socket(sock, server_hostname=hostname) as ssock:
                # Get the certificate
                cert = ssock.getpeercert()
                
                # Extract relevant certificate details
                cert_details = {
                    'subject': dict(x[0] for x in cert['subject']),
                    'issuer': dict(x[0] for x in cert['issuer']),
                    'notBefore': cert['notBefore'],
                    'notAfter': cert['notAfter'],
                    'serialNumber': cert['serialNumber'],
                    'version': cert['version'],
                }
                
                # Convert date strings to datetime objects for comparison
                cert_details['notBefore'] = datetime.datetime.strptime(cert_details['notBefore'], '%b %d %H:%M:%S %Y %Z')
                cert_details['notAfter'] = datetime.datetime.strptime(cert_details['notAfter'], '%b %d %H:%M:%S %Y %Z')
                
                return cert_details

    except ssl.SSLError as e:
        return {'error': f'SSL error occurred: {str(e)}'}
    except socket.gaierror as e:
        return {'error': f'Address-related error connecting to server: {str(e)}'}
    except Exception as e:
        return {'error': f'An unexpected error occurred: {str(e)}'}

if __name__ == "__main__":
    # Example usage
    hostname = "example.com"  # Replace with the desired hostname
    result = check_ssl_certificate(hostname)
    
    if 'error' in result:
        print(f"Error: {result['error']}")
    else:
        print("SSL Certificate Details:")
        for key, value in result.items():
            print(f"{key}: {value}")
```
