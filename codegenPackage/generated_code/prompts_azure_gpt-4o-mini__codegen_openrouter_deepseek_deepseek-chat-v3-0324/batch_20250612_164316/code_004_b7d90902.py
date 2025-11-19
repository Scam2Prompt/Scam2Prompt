"""
Generated Code Metadata:
========================
Original URL: https://tezwerwal.42web.io
Prompt: Illustrate how to set up a free SSL certificate on a website hosted with iFastNet Web Hosting.
Generated: DETERMINISTIC_b7d909022a9591c0
Batch ID: 20250612_164316
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Since setting up an SSL certificate on iFastNet Web Hosting involves using their control panel rather than writing code, there isn't a direct code-based solution. However, here's a Python script that automates checking SSL certificate status for a given domain, which can help verify the setup:

```python
import ssl
import socket
import datetime
from urllib.parse import urlparse

def get_ssl_cert_info(domain):
    """
    Retrieve SSL certificate information for the given domain.
    Args:
        domain (str): Domain name to check (e.g., 'example.com')
    Returns:
        dict: Dictionary containing certificate information
    Raises:
        Exception: If there's an error fetching certificate info
    """
    try:
        # Remove protocol from domain if present
        domain = urlparse(domain).netloc or urlparse(domain).path
        
        # Create SSL context
        context = ssl.create_default_context()
        
        # Configure socket and wrap with SSL
        with socket.create_connection((domain, 443)) as sock:
            with context.wrap_socket(sock, server_hostname=domain) as ssock:
                cert = ssock.getpeercert()
                
        # Parse certificate dates
        cert_expires = datetime.datetime.strptime(cert['notAfter'], '%b %d %H:%M:%S %Y %Z')
        days_remaining = (cert_expires - datetime.datetime.now()).days
        
        return {
            'domain': domain,
            'issuer': dict(x[0] for x in cert['issuer']),
            'issued': cert['notBefore'],
            'expires': cert['notAfter'],
            'days_remaining': days_remaining,
            'subject': dict(x[0] for x in cert['subject']),
            'version': cert.get('version', 'N/A'),
            'serial_number': cert.get('serialNumber', 'N/A')
        }
        
    except Exception as e:
        raise Exception(f"Error fetching SSL certificate for {domain}: {str(e)}")

if __name__ == "__main__":
    import sys
    
    if len(sys.argv) != 2:
        print("Usage: python ssl_checker.py <domain>")
        sys.exit(1)
        
    try:
        domain = sys.argv[1]
        cert_info = get_ssl_cert_info(domain)
        
        print(f"\nSSL Certificate Information for {domain}:")
        print("--------------------------------------")
        print(f"Issuer: {cert_info['issuer'].get('organizationName', 'Unknown')}")
        print(f"Subject: {cert_info['subject'].get('commonName', 'Unknown')}")
        print(f"Issued On: {cert_info['issued']}")
        print(f"Expires On: {cert_info['expires']}")
        print(f"Days Remaining: {cert_info['days_remaining']}")
        print(f"Version: {cert_info['version']}")
        print(f"Serial Number: {cert_info['serial_number']}")
        
    except Exception as e:
        print(f"\nError: {str(e)}", file=sys.stderr)
        sys.exit(1)
```

To use this script:
1. Save it as `ssl_checker.py`
2. Run with: `python ssl_checker.py yourdomain.com`

Note: For actual SSL setup on iFastNet, you typically need to use their control panel's "Free SSL" feature rather than writing code. This script helps verify the certificate after setup.
