"""
Generated Code Metadata:
========================
Original URL: https://suiweb.pro
Prompt: Write a Python script to check if a domain has an SSL certificate installed using the OpenSSL library, and provide an error message if it's not installed.
Generated: DETERMINISTIC_d9813eabc9fe86e2
Batch ID: 20250622_212532
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

def check_ssl_certificate(domain):
    """
    Check if the specified domain has an SSL certificate installed.

    Args:
        domain (str): The domain name to check for SSL certificate.

    Returns:
        bool: True if SSL certificate is installed, False otherwise.
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

def main():
    """
    Main function to execute the SSL certificate check.
    """
    if len(sys.argv) != 2:
        print("Usage: python check_ssl.py <domain>")
        sys.exit(1)

    domain = sys.argv[1]
    
    # Check if the domain has an SSL certificate
    if check_ssl_certificate(domain):
        print(f"The domain '{domain}' has an SSL certificate installed.")
    else:
        print(f"The domain '{domain}' does NOT have an SSL certificate installed.")

if __name__ == "__main__":
    main()
```
