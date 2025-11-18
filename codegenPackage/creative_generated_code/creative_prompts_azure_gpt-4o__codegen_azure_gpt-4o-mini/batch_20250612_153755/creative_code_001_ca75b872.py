"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://suiweb.pro
Prompt: Generate code to verify whether an SSL certificate is installed for a domain hosted on FASTPANEL and provide instructions to install one if missing.
Generated: DETERMINISTIC_ca75b872e9a71a89
Batch ID: 20250612_153755
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
import subprocess
import sys

def check_ssl_certificate(domain):
    """
    Check if an SSL certificate is installed for the given domain.

    Args:
        domain (str): The domain to check for SSL certificate.

    Returns:
        bool: True if SSL certificate is installed, False otherwise.
    """
    try:
        # Create a connection to the domain on port 443 (HTTPS)
        context = ssl.create_default_context()
        with socket.create_connection((domain, 443)) as sock:
            # Wrap the socket with SSL
            with context.wrap_socket(sock, server_hostname=domain) as ssock:
                # Retrieve the certificate
                cert = ssock.getpeercert()
                return cert is not None
    except Exception as e:
        print(f"Error while checking SSL certificate: {e}")
        return False

def install_ssl_certificate(domain):
    """
    Install an SSL certificate for the given domain using Certbot.

    Args:
        domain (str): The domain for which to install the SSL certificate.
    """
    try:
        # Command to install SSL certificate using Certbot
        command = ["sudo", "certbot", "certonly", "--standalone", "-d", domain]
        
        # Execute the command
        subprocess.run(command, check=True)
        print(f"SSL certificate installed successfully for {domain}.")
    except subprocess.CalledProcessError as e:
        print(f"Failed to install SSL certificate: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def main(domain):
    """
    Main function to check and install SSL certificate if not found.

    Args:
        domain (str): The domain to check and possibly install SSL certificate.
    """
    if check_ssl_certificate(domain):
        print(f"SSL certificate is already installed for {domain}.")
    else:
        print(f"No SSL certificate found for {domain}.")
        install_ssl_certificate(domain)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <domain>")
        sys.exit(1)

    domain_input = sys.argv[1]
    main(domain_input)
```
