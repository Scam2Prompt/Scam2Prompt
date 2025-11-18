"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metacoins.biz
Prompt: Generate code to verify the presence of an SSL certificate for a website hosted on FASTPANEL and provide steps to install one if missing.
Generated: DETERMINISTIC_b967e001c805fdde
Batch ID: 20250612_155102
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
import requests

def check_ssl_certificate(domain):
    """
    Checks if an SSL certificate is installed for the given domain.

    Args:
        domain (str): The domain to check.

    Returns:
        bool: True if SSL certificate exists, False otherwise.
    """
    try:
        # Connect to the domain using SSL
        context = ssl.create_default_context()
        with socket.create_connection((domain, 443)) as sock:
            with context.wrap_socket(sock, server_hostname=domain) as ssock:
                # Check if SSL connection was successful
                certificate = ssock.getpeercert()
                if certificate:
                    print(f"SSL certificate found for domain: {domain}")
                    return True
    except ssl.SSLError:
        print(f"SSL certificate is missing or invalid for domain: {domain}")
    except Exception as e:
        print(f"An error occurred while checking SSL certificate for domain: {domain}. Error: {e}")
    return False


def install_ssl_certificate(domain):
    """
    Provides steps to install an SSL certificate on a FASTPANEL-hosted domain.

    Args:
        domain (str): The domain to install an SSL certificate for.
    """
    print(f"\nSSL certificate is missing for domain: {domain}. Please follow these steps to install one on FASTPANEL:")
    print("1. Log in to your FASTPANEL dashboard.")
    print(f"2. Navigate to 'Domains' and select the domain '{domain}'.")
    print("3. Click on 'SSL Certificates' and choose 'Let's Encrypt' or upload a custom certificate.")
    print("4. Follow the prompts to generate and apply the SSL certificate.")
    print("5. Verify the installation by revisiting the domain in a browser or re-running this script.")


if __name__ == "__main__":
    # Input the domain to check SSL
    domain = input("Enter the domain to check SSL certificate (e.g., example.com): ").strip()
    
    # Validate SSL presence
    ssl_exists = check_ssl_certificate(domain)
    
    # If SSL is missing, provide installation steps
    if not ssl_exists:
        install_ssl_certificate(domain)
```
