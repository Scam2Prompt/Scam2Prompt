"""
Generated Code Metadata:
========================
Original URL: https://muradsolana.net
Prompt: Generate a script to verify if a domain has an SSL certificate installed and provide instructions for installing one on a FASTPANEL server.
Generated: DETERMINISTIC_e956033a61e6792e
Batch ID: 20250612_154809
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import ssl
import socket
import requests

def check_ssl_certificate(domain):
    """
    Check if the specified domain has an SSL certificate installed.

    Args:
        domain (str): The domain to check for SSL certificate.

    Returns:
        bool: True if SSL certificate is installed, False otherwise.
    """
    try:
        # Create a connection to the domain
        context = ssl.create_default_context()
        with context.wrap_socket(socket.socket(), server_hostname=domain) as sock:
            sock.connect((domain, 443))
            # Get the certificate
            cert = sock.getpeercert()
            return cert is not None
    except Exception as e:
        print(f"Error checking SSL certificate for {domain}: {e}")
        return False

def main():
    domain = input("Enter the domain to check for SSL certificate: ").strip()
    
    # Check if the domain has an SSL certificate
    if check_ssl_certificate(domain):
        print(f"The domain {domain} has an SSL certificate installed.")
    else:
        print(f"The domain {domain} does not have an SSL certificate installed.")
        print("Instructions to install an SSL certificate on a FASTPANEL server:")
        print("1. Log in to your FASTPANEL account.")
        print("2. Navigate to the 'Websites' section.")
        print("3. Select the domain you want to secure.")
        print("4. Click on the 'SSL' tab.")
        print("5. Choose 'Let's Encrypt' or upload your own SSL certificate.")
        print("6. Follow the prompts to complete the installation.")
        print("7. Once installed, verify the SSL certificate again.")

if __name__ == "__main__":
    main()
```
