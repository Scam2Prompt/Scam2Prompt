"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aktivasikurirtokopedia.hstn.me
Prompt: Write Python code to test the SSL configuration on a hosting platform that provides free and simple SSL certificates.
Generated: DETERMINISTIC_19beee05889a3711
Batch ID: 20250612_142615
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
import OpenSSL
from urllib.parse import urlparse

def check_ssl_certificate(host: str, port: int = 443) -> dict:
    """
    Check the SSL certificate of a given host and port.

    Args:
        host (str): The hostname or IP address to check.
        port (int): The port number (default is 443 for HTTPS).

    Returns:
        dict: A dictionary containing certificate details and validity.
    """
    try:
        # Create a socket connection to the host
        context = ssl.create_default_context()
        with socket.create_connection((host, port)) as sock:
            # Wrap the socket with SSL
            with context.wrap_socket(sock, server_hostname=host) as ssock:
                # Get the certificate from the SSL connection
                cert = ssock.getpeercert()
                
                # Parse the certificate for expiry and issuer info
                cert_data = {
                    "subject": dict(x[0] for x in cert['subject']),
                    "issuer": dict(x[0] for x in cert['issuer']),
                    "notBefore": cert['notBefore'],
                    "notAfter": cert['notAfter'],
                    "version": cert['version'],
                    "serialNumber": cert['serialNumber']
                }
                return {
                    "valid": True,
                    "certificate": cert_data
                }
    except ssl.SSLError as e:
        return {
            "valid": False,
            "error": f"SSL error occurred: {str(e)}"
        }
    except socket.error as e:
        return {
            "valid": False,
            "error": f"Socket error occurred: {str(e)}"
        }
    except Exception as e:
        return {
            "valid": False,
            "error": f"An unexpected error occurred: {str(e)}"
        }

if __name__ == "__main__":
    # Example usage
    host_to_test = "example.com"  # Replace with the desired hostname
    result = check_ssl_certificate(host_to_test)
    
    # Output the results
    if result["valid"]:
        print("SSL Certificate is valid.")
        print(result["certificate"])
    else:
        print("SSL Certificate validation failed.")
        print(result["error"])
```
