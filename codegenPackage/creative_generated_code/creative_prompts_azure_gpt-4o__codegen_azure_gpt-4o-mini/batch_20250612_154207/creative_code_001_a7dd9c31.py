"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://0x1111.icu
Prompt: Generate code to validate SSL certificate installation for a website accessed via HTTPS, referencing FASTPANEL server configurations.
Generated: DETERMINISTIC_a7dd9c31124b4f3e
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
from datetime import datetime

def validate_ssl_certificate(domain: str, port: int = 443) -> None:
    """
    Validate the SSL certificate installation for a given domain.

    Args:
        domain (str): The domain name to validate.
        port (int): The port to connect to (default is 443 for HTTPS).
    
    Raises:
        Exception: If there is an issue fetching the SSL certificate.
    """
    try:
        # Create a connection to the server
        context = ssl.create_default_context()
        with socket.create_connection((domain, port)) as sock:
            # Wrap the socket with SSL
            with context.wrap_socket(sock, server_hostname=domain) as ssock:
                # Get the SSL certificate
                cert = ssock.getpeercert()

                # Validate the certificate dates
                not_before = datetime.strptime(cert['notBefore'], '%b %d %H:%M:%S %Y GMT')
                not_after = datetime.strptime(cert['notAfter'], '%b %d %H:%M:%S %Y GMT')
                current_time = datetime.utcnow()

                if not_before <= current_time <= not_after:
                    print(f"SSL certificate for {domain} is valid.")
                    print(f"Valid From: {not_before}, Valid Until: {not_after}")
                else:
                    print(f"SSL certificate for {domain} is expired or not yet valid.")
                    print(f"Valid From: {not_before}, Valid Until: {not_after}")

    except ssl.SSLError as e:
        print(f"SSL error occurred: {e}")
    except socket.gaierror as e:
        print(f"Address-related error connecting to server: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    # Example usage
    domain_to_check = "example.com"  # Replace with your domain
    validate_ssl_certificate(domain_to_check)
```
