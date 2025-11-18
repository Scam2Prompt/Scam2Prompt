"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://okxaltdrive.com
Prompt: Generate code to verify if an SSL certificate is installed and valid for a domain accessed via HTTPS, referencing FASTPANEL's error scenarios.
Generated: DETERMINISTIC_2991e04f5b7c983e
Batch ID: 20250612_152240
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

def check_ssl_cert(domain, port=443):
    """
    Check if an SSL certificate is installed and valid for the given domain.
    
    Args:
        domain (str): The domain name to check (e.g., 'example.com').
        port (int): The port to connect to (default is 443 for HTTPS).

    Returns:
        dict: A dictionary containing certificate details or error information.
    """
    result = {
        'domain': domain,
        'valid': False,
        'error': None,
        'cert_details': None
    }

    try:
        # Create a connection to the specified domain and port
        context = ssl.create_default_context()
        with socket.create_connection((domain, port)) as sock:
            with context.wrap_socket(sock, server_hostname=domain) as ssock:
                # Get the server's certificate
                cert = ssock.getpeercert()

                # Check if the certificate is valid
                result['cert_details'] = cert
                result['valid'] = True
                
                # Validate the certificate expiration dates
                cert_not_before = datetime.strptime(cert['notBefore'], '%b %d %H:%M:%S %Y GMT')
                cert_not_after = datetime.strptime(cert['notAfter'], '%b %d %H:%M:%S %Y GMT')
                
                if cert_not_before < datetime.utcnow() < cert_not_after:
                    result['valid'] = True
                else:
                    result['valid'] = False
                    result['error'] = "Certificate is expired or not yet valid."

    except ssl.SSLError as ssl_error:
        result['error'] = f"SSL error occurred: {ssl_error}"
    except socket.gaierror:
        result['error'] = "Domain name could not be resolved."
    except ConnectionRefusedError:
        result['error'] = "Connection was refused by the server."
    except Exception as e:
        result['error'] = f"An unexpected error occurred: {e}"

    return result

# Example usage
if __name__ == "__main__":
    domain_to_check = "example.com"
    ssl_check_result = check_ssl_cert(domain_to_check)

    if ssl_check_result['valid']:
        print(f"SSL certificate is valid for {domain_to_check}.")
        print(f"Certificate details: {ssl_check_result['cert_details']}")
    else:
        print(f"SSL certificate is NOT valid for {domain_to_check}.")
        if ssl_check_result['error']:
            print(f"Error: {ssl_check_result['error']}")
```
