"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metacoins.in
Prompt: Generate a script to verify if an SSL certificate is installed for a domain using OpenSSL or a similar library, referencing FASTPANEL's HTTPS-related troubleshooting.
Generated: DETERMINISTIC_fcd6bdac6745c9d6
Batch ID: 20250612_155106
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://{domain": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```python
import socket
import ssl
import sys
from urllib.parse import urlparse

def verify_ssl_certificate(domain):
    """
    Verifies if an SSL certificate is installed for the given domain.

    Args:
    domain (str): The domain to check for an SSL certificate.

    Returns:
    bool: True if the SSL certificate is installed, False otherwise.
    str: The SSL certificate details if installed, else an error message.
    """
    try:
        # Parse the domain to ensure it's formatted correctly
        parsed_domain = urlparse(f"https://{domain}")
        hostname = parsed_domain.hostname

        # Create a socket connection to the domain on port 443 (HTTPS)
        context = ssl.create_default_context()
        with socket.create_connection((hostname, 443)) as sock:
            # Wrap the socket with SSL
            with context.wrap_socket(sock, server_hostname=hostname) as ssock:
                # Get the SSL certificate
                certificate = ssock.getpeercert()
                if certificate:
                    return True, certificate
                else:
                    return False, "No SSL certificate found."
    except ssl.SSLError as ssl_error:
        return False, f"SSL error occurred: {ssl_error}"
    except socket.timeout:
        return False, "Connection timed out."
    except socket.error as socket_error:
        return False, f"Socket error occurred: {socket_error}"
    except Exception as e:
        return False, f"An unexpected error occurred: {e}"

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python verify_ssl.py <domain>")
        sys.exit(1)

    domain = sys.argv[1]
    is_installed, details = verify_ssl_certificate(domain)

    if is_installed:
        print(f"SSL certificate is installed for {domain}.")
        print("Certificate details:", details)
    else:
        print(f"SSL certificate is NOT installed for {domain}.")
        print("Details:", details)
```
