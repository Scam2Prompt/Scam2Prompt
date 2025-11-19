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

def check_ssl_certificate(domain: str, port: int = 443) -> bool:
    """
    Check if a domain has an SSL certificate installed.

    Args:
        domain (str): The domain name to check.
        port (int): The port to check on (default is 443).

    Returns:
        bool: True if the domain has an SSL certificate installed, False otherwise.
    """
    try:
        # Create a socket connection
        context = ssl.create_default_context()  # Use default SSL context
        with socket.create_connection((domain, port), timeout=10) as sock:
            # Wrap the socket with SSL
            with context.wrap_socket(sock, server_hostname=domain) as ssock:
                # Attempt to retrieve the certificate
                certificate = ssock.getpeercert()
                # Return True if a certificate is found
                return bool(certificate)
    except ssl.SSLError:
        # Handle SSL errors (e.g., no certificate found)
        return False
    except socket.error:
        # Handle socket errors (e.g., unable to connect to the domain)
        return False

# Example usage
if __name__ == "__main__":
    domain_to_check = "example.com"
    if check_ssl_certificate(domain_to_check):
        print(f"{domain_to_check} has an SSL certificate installed.")
    else:
        print(f"{domain_to_check} does not have an SSL certificate installed.")
```
