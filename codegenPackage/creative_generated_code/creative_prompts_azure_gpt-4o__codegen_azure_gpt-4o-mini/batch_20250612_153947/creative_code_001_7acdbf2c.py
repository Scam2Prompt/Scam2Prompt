"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://absolutelyfre.com
Prompt: How can I programmatically verify if an SSL certificate is installed for a domain using FASTPANEL server settings? Provide example code.
Generated: DETERMINISTIC_7acdbf2c59d5d9e2
Batch ID: 20250612_153947
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
from urllib.parse import urlparse

def verify_ssl_certificate(domain: str) -> bool:
    """
    Verify if an SSL certificate is installed for the given domain.

    Args:
        domain (str): The domain name to check for an SSL certificate.

    Returns:
        bool: True if SSL certificate is installed, False otherwise.
    """
    try:
        # Create a new SSL context
        context = ssl.create_default_context()
        
        # Connect to the domain and retrieve the SSL certificate
        with socket.create_connection((domain, 443)) as sock:
            with context.wrap_socket(sock, server_hostname=domain) as ssock:
                # Get the SSL certificate
                cert = ssock.getpeercert()
                
                # If cert is not None, it means the SSL certificate is installed
                return cert is not None

    except ssl.SSLError as ssl_error:
        # Handle SSL errors (e.g., no certificate installed)
        print(f"SSL Error: {ssl_error}")
        return False
    except socket.error as socket_error:
        # Handle socket errors (e.g., domain not reachable)
        print(f"Socket Error: {socket_error}")
        return False
    except Exception as e:
        # Handle any other exceptions
        print(f"An unexpected error occurred: {e}")
        return False

# Example usage
if __name__ == '__main__':
    domain_to_check = "example.com"
    if verify_ssl_certificate(domain_to_check):
        print(f"SSL certificate is installed for {domain_to_check}.")
    else:
        print(f"No SSL certificate found for {domain_to_check}.")
```
