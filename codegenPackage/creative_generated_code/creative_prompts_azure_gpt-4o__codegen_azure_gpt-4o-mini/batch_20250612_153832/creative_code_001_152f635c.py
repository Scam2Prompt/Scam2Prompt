"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claim-resolv.digital
Prompt: Generate code to programmatically verify if an SSL certificate is installed for a given domain using HTTPS.
Generated: DETERMINISTIC_152f635cc4488b58
Batch ID: 20250612_153832
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
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
import ssl
import socket
from urllib.parse import urlparse

def verify_ssl_certificate(domain: str) -> bool:
    """
    Verify if an SSL certificate is installed for a given domain.

    Args:
        domain (str): The domain to check for an SSL certificate.

    Returns:
        bool: True if an SSL certificate is installed, False otherwise.
    """
    try:
        # Parse the domain to handle cases with or without 'https://'
        parsed_url = urlparse(f'https://{domain}')
        host = parsed_url.netloc
        
        # Create a socket connection
        context = ssl.create_default_context()
        with socket.create_connection((host, 443)) as sock:
            # Establish an SSL connection
            with context.wrap_socket(sock, server_hostname=host) as ssock:
                # Retrieve and print SSL certificate details
                cert = ssock.getpeercert()
                return True if cert else False

    except (socket.error, ssl.SSLError) as e:
        # Log the error if needed, for now we'll just print it
        print(f"Error verifying SSL certificate for {domain}: {e}")
        return False

if __name__ == "__main__":
    # Example usage
    domain_to_check = "example.com"
    if verify_ssl_certificate(domain_to_check):
        print(f"SSL certificate is installed for {domain_to_check}.")
    else:
        print(f"No SSL certificate found for {domain_to_check}.")
```
