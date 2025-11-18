"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://scroll-lo.com
Prompt: Generate a script to verify if an SSL certificate is installed for a domain accessed via HTTPS, referencing FASTPANEL server settings.
Generated: DETERMINISTIC_1724d487d2da1660
Batch ID: 20250612_145516
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
import argparse
from datetime import datetime

def check_ssl_certificate(domain):
    """
    Check if an SSL certificate is installed for a given domain.
    
    Args:
        domain (str): The domain to check for its SSL certificate.

    Returns:
        dict: A dictionary containing certificate details if present, otherwise None.
    """
    try:
        # Create a connection to the domain over SSL
        context = ssl.create_default_context()
        with context.wrap_socket(socket.socket(socket.AF_INET), server_hostname=domain) as s:
            # Connect to the server on port 443 (default for HTTPS)
            s.connect((domain, 443))
            # Get the certificate
            certificate = s.getpeercert()
            return certificate
    except ssl.SSLError as e:
        print(f"SSL error occurred: {e}")
    except socket.gaierror as e:
        print(f"Domain resolution error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    return None

def format_certificate_info(cert):
    """
    Format the SSL certificate information for display.

    Args:
        cert (dict): The SSL certificate details.

    Returns:
        str: Formatted certificate information.
    """
    if cert:
        info = (
            f"Subject: {cert['subject']}\n"
            f"Issuer: {cert['issuer']}\n"
            f"Version: {cert['version']}\n"
            f"Serial Number: {cert['serialNumber']}\n"
            f"Valid From: {datetime.utcfromtimestamp(cert['notBefore']).strftime('%Y-%m-%d %H:%M:%S')}\n"
            f"Valid To: {datetime.utcfromtimestamp(cert['notAfter']).strftime('%Y-%m-%d %H:%M:%S')}\n"
        )
        return info
    return "No certificate found."

def main():
    # Set up argument parsing
    parser = argparse.ArgumentParser(description="Check if an SSL certificate is installed for a domain.")
    parser.add_argument("domain", type=str, help="The domain to check for SSL certificate.")
    args = parser.parse_args()

    # Check the SSL certificate
    certificate = check_ssl_certificate(args.domain)

    # Format and display the certificate information
    certificate_info = format_certificate_info(certificate)
    print(certificate_info)

if __name__ == "__main__":
    main()
```
