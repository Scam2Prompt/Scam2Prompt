"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://etihreum.org
Prompt: Can you provide code examples for checking if a domain has an SSL certificate installed and how to resolve issues related to HTTPS access?
Generated: DETERMINISTIC_441ff58397dd4427
Batch ID: 20250612_162106
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
    Check if a domain has a valid SSL certificate installed.
    
    :param domain: The domain to check.
    :param port: The port to connect to (default is 443 for HTTPS).
    :return: True if SSL certificate is installed, False otherwise.
    """
    try:
        # Create a SSL context
        context = ssl.create_default_context()
        # Establish a connection to the domain over the specified port
        with socket.create_connection((domain, port), timeout=5) as sock:
            with context.wrap_socket(sock, server_hostname=domain) as ssock:
                # SSL certificate is successfully retrieved
                certificate = ssock.getpeercert()
                # Check if certificate is valid
                if certificate:
                    return True
        return False
    except ssl.SSLError as e:
        # SSL-related error
        print(f"SSL Error: {e}")
        return False
    except socket.error as e:
        # Socket connection error
        print(f"Socket Error: {e}")
        return False
    except Exception as e:
        # Catch and print any other unexpected errors
        print(f"Unexpected Error: {e}")
        return False


def resolve_https_access(domain: str) -> None:
    """
    Attempt to resolve issues related to HTTPS access for a domain.
    
    :param domain: The domain to check and troubleshoot.
    """
    has_ssl = check_ssl_certificate(domain)
    if has_ssl:
        print(f"The domain '{domain}' has a valid SSL certificate installed.")
    else:
        print(f"The domain '{domain}' does NOT have a valid SSL certificate installed.")
        print("Steps to resolve:")
        print("1. Ensure the domain's SSL certificate is properly installed.")
        print("2. Verify the certificate is not expired and matches the domain.")
        print("3. If using a self-signed certificate, add it to your trusted store.")
        print("4. Check your web server settings to confirm HTTPS is enabled.")
        print("5. Contact your hosting provider or certificate authority for assistance.")

# Example usage
if __name__ == "__main__":
    domain_name = "example.com"
    resolve_https_access(domain_name)
```
