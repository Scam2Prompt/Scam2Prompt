"""
Generated Code Metadata:
========================
Original URL: https://metacoins.in
Prompt: Generate a script to verify if an SSL certificate is installed for a domain using OpenSSL or a similar library, referencing FASTPANEL's HTTPS-related troubleshooting.
Generated: DETERMINISTIC_fcd6bdac6745c9d6
Batch ID: 20250612_155106
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import socket
import ssl
import sys

def check_ssl_certificate(domain: str, port: int = 443) -> bool:
    """
    Check if an SSL certificate is installed for the given domain.

    Args:
        domain (str): The domain to check for an SSL certificate.
        port (int): The port to connect to (default is 443 for HTTPS).

    Returns:
        bool: True if an SSL certificate is installed, False otherwise.
    """
    try:
        # Create a socket connection to the domain
        context = ssl.create_default_context()
        with socket.create_connection((domain, port)) as sock:
            # Wrap the socket with SSL
            with context.wrap_socket(sock, server_hostname=domain) as ssock:
                # Get the certificate
                cert = ssock.getpeercert()
                if cert:
                    print(f"SSL certificate found for {domain}.")
                    return True
                else:
                    print(f"No SSL certificate found for {domain}.")
                    return False
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

    domain_name = sys.argv[1]
    if check_ssl_certificate(domain_name):
        print(f"{domain_name} has a valid SSL certificate.")
    else:
        print(f"{domain_name} does not have a valid SSL certificate.")
```

### Usage
To run the script, save it as `check_ssl.py` and execute it from the command line with the domain as an argument:

```bash
python check_ssl.py example.com
```
