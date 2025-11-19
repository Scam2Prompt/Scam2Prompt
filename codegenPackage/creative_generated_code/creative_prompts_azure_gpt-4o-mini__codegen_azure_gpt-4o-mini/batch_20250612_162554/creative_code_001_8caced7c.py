"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metacoins.biz
Prompt: Write a code snippet to check if a domain has an SSL certificate installed.
Generated: DETERMINISTIC_8caced7ca32ec74d
Batch ID: 20250612_162554
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

def check_ssl_cert(domain):
    """
    Check if the specified domain has an SSL certificate installed.

    Args:
        domain (str): The domain name to check.

    Returns:
        bool: True if an SSL certificate is installed, False otherwise.
    """
    try:
        # Parse the domain to ensure it's valid
        parsed_url = urlparse(domain)
        hostname = parsed_url.hostname if parsed_url.hostname else domain
        
        # Create a connection to the specified domain on port 443 (HTTPS)
        context = ssl.create_default_context()
        with socket.create_connection((hostname, 443)) as sock:
            # Wrap the socket with SSL
            with context.wrap_socket(sock, server_hostname=hostname) as ssock:
                # Get the SSL certificate
                ssl_info = ssock.getpeercert()
                
        # If we successfully retrieved the SSL certificate, return True
        return ssl_info is not None

    except (ssl.SSLError, socket.error) as e:
        # Handle SSL errors or socket connection errors
        print(f"SSL error encountered for {domain}: {e}")
        return False
    except Exception as e:
        # Handle any other exceptions that may arise
        print(f"An error occurred while checking {domain}: {e}")
        return False

# Example usage
if __name__ == "__main__":
    domain = "www.example.com"
    if check_ssl_cert(domain):
        print(f"{domain} has an SSL certificate installed.")
    else:
        print(f"{domain} does not have an SSL certificate installed.")
```
