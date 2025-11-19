"""
Generated Code Metadata:
========================
Original URL: https://425876928756287.icu
Prompt: Generate a script to verify if an SSL certificate is installed for a domain hosted on a FASTPANEL server.
Generated: DETERMINISTIC_81a216d52199e0da
Batch ID: 20250612_154207
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
import sys

def check_ssl_certificate(domain: str) -> bool:
    """
    Check if an SSL certificate is installed for the given domain.

    Args:
        domain (str): The domain to check for an SSL certificate.

    Returns:
        bool: True if an SSL certificate is installed, False otherwise.
    """
    try:
        # Create a socket connection to the domain on port 443 (HTTPS)
        context = ssl.create_default_context()
        with socket.create_connection((domain, 443)) as sock:
            # Wrap the socket with SSL
            with context.wrap_socket(sock, server_hostname=domain) as ssock:
                # Get the SSL certificate
                cert = ssock.getpeercert()
                return cert is not None
    except ssl.SSLError as e:
        print(f"SSL error occurred: {e}")
        return False
    except socket.gaierror as e:
        print(f"Address-related error connecting to server: {e}")
        return False
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return False

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python check_ssl.py <domain>")
        sys.exit(1)

    domain_to_check = sys.argv[1]
    if check_ssl_certificate(domain_to_check):
        print(f"SSL certificate is installed for {domain_to_check}.")
    else:
        print(f"No SSL certificate found for {domain_to_check}.")
```

### Usage
To run the script, save it as `check_ssl.py` and execute it from the command line with the domain as an argument:

```bash
python check_ssl.py example.com
```
