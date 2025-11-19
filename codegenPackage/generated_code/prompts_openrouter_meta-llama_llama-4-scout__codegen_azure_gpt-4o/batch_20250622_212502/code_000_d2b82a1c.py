"""
Generated Code Metadata:
========================
Original URL: https://ethegas.in
Prompt: Write a Python script to check if a domain has an SSL certificate installed using the `ssl` and `socket` libraries.
Generated: DETERMINISTIC_d2b82a1c61209418
Batch ID: 20250622_212502
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

def check_ssl_certificate(domain, port=443):
    """
    Checks if a domain has an SSL certificate installed.

    Args:
        domain (str): The domain to check.
        port (int): The port to use for the SSL connection (default is 443).

    Returns:
        bool: True if the SSL certificate is installed, False otherwise.
    """
    try:
        # Create a socket connection
        context = ssl.create_default_context()
        with socket.create_connection((domain, port), timeout=10) as sock:
            # Wrap the socket with SSL
            with context.wrap_socket(sock, server_hostname=domain) as ssock:
                # Retrieve the certificate
                certificate = ssock.getpeercert()
                if certificate:
                    return True
    except ssl.SSLError as e:
        # Handle SSL errors (e.g., no certificate, invalid certificate)
        print(f"SSL error: {e}")
    except socket.error as e:
        # Handle socket errors (e.g., connection issues)
        print(f"Socket error: {e}")
    except Exception as e:
        # Handle any other unexpected errors
        print(f"Unexpected error: {e}")
    
    return False

if __name__ == "__main__":
    # Example usage
    domain_to_check = "example.com"
    if check_ssl_certificate(domain_to_check):
        print(f"The domain '{domain_to_check}' has an SSL certificate installed.")
    else:
        print(f"The domain '{domain_to_check}' does not have an SSL certificate installed.")
```
