"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://msu.best
Prompt: Generate code to verify if an SSL certificate is installed for a domain hosted on FASTPANEL.
Generated: DETERMINISTIC_8f159b1536f4b90d
Batch ID: 20250612_153849
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import socket
import ssl
from urllib.parse import urlparse

def is_ssl_certificate_installed(domain):
    """
    Check if an SSL certificate is installed for the given domain.

    Parameters:
    domain (str): The domain name to check for an SSL certificate.

    Returns:
    bool: True if an SSL certificate is installed, False otherwise.
    """
    try:
        # Parse the domain to handle potential URLs
        parsed_url = urlparse(domain)
        domain_name = parsed_url.netloc if parsed_url.netloc else parsed_url.path

        # Create a socket and wrap it with SSL
        with socket.create_connection((domain_name, 443)) as sock:
            context = ssl.create_default_context()
            with context.wrap_socket(sock, server_hostname=domain_name) as ssock:
                # Get the certificate
                certificate = ssock.getpeercert()
                return certificate is not None

    except ssl.SSLError as e:
        # Handle SSL errors (e.g., no certificate)
        print(f"SSL error occurred: {e}")
        return False
    except socket.gaierror as e:
        # Handle address-related errors (e.g., domain not found)
        print(f"Address-related error occurred: {e}")
        return False
    except Exception as e:
        # Handle any other unforeseen errors
        print(f"An unexpected error occurred: {e}")
        return False

if __name__ == "__main__":
    # Example usage
    domain_to_check = "example.com"
    if is_ssl_certificate_installed(domain_to_check):
        print(f"An SSL certificate is installed for {domain_to_check}.")
    else:
        print(f"No SSL certificate is installed for {domain_to_check}.")
```
