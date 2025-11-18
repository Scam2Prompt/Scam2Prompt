"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dapp-webnode.rf.gd
Prompt: Generate a script to check SSL certificate installation on a hosting service that provides free and simple SSL, similar to iFastNet hosting.
Generated: DETERMINISTIC_6ad81665bb6d086d
Batch ID: 20250612_154502
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import ssl
import socket
from datetime import datetime

def check_ssl_certificate(hostname, port=443):
    """
    Check the SSL certificate for a given hostname and port.

    Args:
        hostname (str): The hostname to check for SSL certificate.
        port (int): The port number to connect to (default is 443 for HTTPS).

    Returns:
        dict: A dictionary containing certificate details or an error message.
    """
    try:
        # Create a context for the SSL connection
        context = ssl.create_default_context()

        # Connect to the server and retrieve the certificate
        with socket.create_connection((hostname, port)) as sock:
            with context.wrap_socket(sock, server_hostname=hostname) as ssock:
                cert = ssock.getpeercert()

        # Extract certificate details
        cert_info = {
            'subject': dict(cert['subject']),
            'issuer': dict(cert['issuer']),
            'version': cert['version'],
            'serialNumber': cert['serialNumber'],
            'notBefore': cert['notBefore'],
            'notAfter': cert['notAfter'],
        }

        # Convert 'notBefore' and 'notAfter' from string to datetime
        cert_info['notBefore'] = datetime.strptime(cert_info['notBefore'], '%b %d %H:%M:%S %Y %Z')
        cert_info['notAfter'] = datetime.strptime(cert_info['notAfter'], '%b %d %H:%M:%S %Y %Z')

        return cert_info

    except ssl.SSLError as e:
        return {"error": f"SSL error: {e}"}
    except socket.gaierror as e:
        return {"error": f"Address-related error connecting to server: {e}"}
    except Exception as e:
        return {"error": f"An unexpected error occurred: {e}"}

if __name__ == '__main__':
    # Example usage
    hostname = 'example.com'  # Replace with the desired hostname
    result = check_ssl_certificate(hostname)

    if 'error' in result:
        print(result['error'])  # Print error message if occurs
    else:
        # Print SSL certificate details
        print("SSL Certificate Details:")
        for key, value in result.items():
            print(f"{key}: {value}")
```
