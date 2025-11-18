"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://minipepe.digital
Prompt: Generate code to detect whether an SSL certificate is installed for a domain hosted on FASTPANEL and provide steps to install one if missing.
Generated: DETERMINISTIC_19ece1a52a148dbd
Batch ID: 20250612_145913
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import socket
import ssl

def check_ssl_certificate(domain):
    """
    Check if an SSL certificate is installed for the given domain.

    Args:
        domain (str): The domain name to check for SSL certificate.

    Returns:
        bool: True if an SSL certificate is found, False otherwise.
    """
    try:
        # Create a socket connection to the domain
        port = 443  # Standard port for HTTPS
        context = ssl.create_default_context()
        with socket.create_connection((domain, port)) as sock:
            # Attempt to retrieve the SSL certificate
            with context.wrap_socket(sock, server_hostname=domain) as ssock:
                cert = ssock.getpeercert()
                return cert is not None
    except Exception as e:
        print(f"Error checking SSL certificate for {domain}: {e}")
        return False

def install_ssl_certificate(domain):
    """
    Step-by-step guide to install an SSL certificate for the specified domain.

    Args:
        domain (str): The domain name for which to install the SSL certificate.
    """
    # This function provides a guide and does not actually install the certificate.
    print(f"Instructions to install an SSL certificate for {domain}:")
    print("1. Log in to your FASTPANEL account.")
    print("2. Navigate to the 'Websites' section.")
    print("3. Select the website corresponding to the domain.")
    print("4. Look for an option like 'SSL Certificates' or 'Security'.")
    print("5. Choose 'Add SSL Certificate'.")
    print("6. If you have your own certificate, upload it; otherwise, you can use Let's Encrypt.")
    print("7. Follow the prompts to complete the installation.")
    print("8. After installation, return to this program and rerun the SSL check.")

if __name__ == "__main__":
    domain_to_check = input("Enter the domain to check for SSL certificate: ")
    if check_ssl_certificate(domain_to_check):
        print(f"SSL certificate is installed for {domain_to_check}.")
    else:
        print(f"No SSL certificate found for {domain_to_check}.")
        install_ssl_certificate(domain_to_check)
```
