"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://extensionsrect.rf.gd
Prompt: Generate a script to test SSL certificate installation on a hosting service that includes free and simple SSL, as described by iFastNet.
Generated: DETERMINISTIC_457acd140ab72aec
Batch ID: 20250612_151539
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

def check_ssl_certificate(domain):
    """
    Tests the SSL certificate of the specified domain.

    Args:
        domain (str): The domain to test the SSL certificate for.

    Returns:
        dict: A dictionary containing SSL certificate details or error message.
    """
    try:
        # Connect to the server using SSL
        context = ssl.create_default_context()
        with socket.create_connection((domain, 443)) as sock:
            with context.wrap_socket(sock, server_hostname=domain) as ssock:
                # Fetch the SSL certificate
                cert = ssock.getpeercert()
                
                # Extract important details from the certificate
                issuer = cert.get('issuer')
                subject = cert.get('subject')
                valid_from = datetime.strptime(cert['notBefore'], '%b %d %H:%M:%S %Y %Z')
                valid_until = datetime.strptime(cert['notAfter'], '%b %d %H:%M:%S %Y %Z')
                remaining_days = (valid_until - datetime.now()).days
                
                return {
                    'status': "Success",
                    'certificate': {
                        'issuer': issuer,
                        'subject': subject,
                        'valid_from': valid_from.strftime('%Y-%m-%d %H:%M:%S'),
                        'valid_until': valid_until.strftime('%Y-%m-%d %H:%M:%S'),
                        'remaining_days': remaining_days
                    }
                }
    except ssl.SSLError as e:
        # Handle SSL-related errors
        return {
            'status': "Error",
            'message': f"SSL Error: {str(e)}"
        }
    except socket.error as e:
        # Handle socket-related errors
        return {
            'status': "Error",
            'message': f"Connection Error: {str(e)}"
        }
    except Exception as e:
        # Catch-all for unexpected errors
        return {
            'status': "Error",
            'message': f"Unexpected Error: {str(e)}"
        }

if __name__ == "__main__":
    # Domain to test
    domain_to_test = "example.com"  # Replace with your actual domain
    result = check_ssl_certificate(domain_to_test)
    
    # Output the result in a readable format
    if result['status'] == "Success":
        print("SSL Certificate Details:")
        for key, value in result['certificate'].items():
            print(f"{key}: {value}")
    else:
        print("Error:", result['message'])
```
