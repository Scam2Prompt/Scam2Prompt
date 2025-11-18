"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://0x000000000000000.icu
Prompt: Generate code to verify if an SSL certificate is installed for a domain accessed via HTTPS in a FASTPANEL-managed server.
Generated: DETERMINISTIC_5e6828507541ab6b
Batch ID: 20250612_154207
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

def check_ssl_certificate(domain: str) -> bool:
    """
    Check if an SSL certificate is installed for the given domain.

    Parameters:
        domain (str): The domain to check for an SSL certificate.

    Returns:
        bool: True if SSL certificate is installed, False otherwise.

    Raises:
        ValueError: If the domain is invalid or cannot be resolved.
        Exception: For general exceptions, including connection issues.
    """
    # Validate the input domain
    parsed_url = urlparse(domain)
    domain = parsed_url.netloc if parsed_url.netloc else parsed_url.path
    if not domain:
        raise ValueError("Invalid domain provided.")

    try:
        # Create a socket connection to the domain on the HTTPS port
        context = ssl.create_default_context()
        with socket.create_connection((domain, 443)) as sock:
            # Wrap the socket with SSL
            with context.wrap_socket(sock, server_hostname=domain) as ssock:
                # Get the ssl certificate
                cert = ssock.getpeercert()
                # If a certificate was retrieved, return True
                return cert is not None

    except ssl.SSLError as e:
        print(f"SSL error occurred: {e}")
        return False
    except socket.gaierror as e:
        raise ValueError(f"Could not resolve domain {domain}: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return False

if __name__ == "__main__":
    # Example usage
    domain_to_check = "example.com"
    
    try:
        if check_ssl_certificate(domain_to_check):
            print(f"SSL certificate is installed for {domain_to_check}.")
        else:
            print(f"No SSL certificate found for {domain_to_check}.")
    except ValueError as ve:
        print(f"ValueError: {ve}")
    except Exception as ex:
        print(f"An error occurred: {ex}")
```
