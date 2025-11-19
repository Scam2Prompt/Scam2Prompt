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

I'm happy to provide code, but I must point out that setting up a free SSL certificate on a website hosted with iFastNet Web Hosting involves more than just code. It requires interaction with their control panel, obtaining a certificate from a Certificate Authority like Let's Encrypt, and configuring the server. However, I can provide a Python script that automates obtaining a free SSL certificate using Let's Encrypt and certbot, assuming you have shell access and can manually configure your server.

```python
# Import required libraries
import subprocess
import os

def obtain_ssl_certificate(domain, email):
    """
    Obtain a free SSL certificate using Let's Encrypt and certbot.

    Args:
    - domain (str): The domain name for the certificate.
    - email (str): The email address for the certificate.

    Returns:
    - None
    """

    # Check if certbot is installed
    try:
        subprocess.run(["certbot", "--version"], check=True, stdout=subprocess.DEVNULL)
    except FileNotFoundError:
        print("Certbot is not installed. Please install it first.")
        return

    # Obtain the certificate
    try:
        subprocess.run([
            "certbot", "certonly",
            "--standalone",
            "--preferred-challenges", "http",
            "--email", email,
            "--agree-tos",
            "--non-interactive",
            "--expand",
            "--domain", domain
        ], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Failed to obtain certificate: {e}")
        return

    # Check if certificate is obtained successfully
    cert_path = "/etc/letsencrypt/live/" + domain + "/fullchain.pem"
    if os.path.exists(cert_path):
        print(f"Certificate obtained successfully for {domain}.")
    else:
        print(f"Failed to obtain certificate for {domain}.")

def configure_ssl_certificate(domain):
    """
    Configure the SSL certificate for a website.

    Args:
    - domain (str): The domain name for the certificate.

    Returns:
    - None
    """

    # Assuming Nginx server
    try:
        # Reload Nginx to pick up new certificate
        subprocess.run(["sudo", "nginx", "-t"], check=True)
        subprocess.run(["sudo", "service", "nginx", "reload"], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Failed to reload Nginx: {e}")
        return

    print(f"SSL certificate configured successfully for {domain}.")

if __name__ == "__main__":
    domain = "example.com"  # Replace with your domain
    email = "user@example.com"  # Replace with your email
    obtain_ssl_certificate(domain, email)
    configure_ssl_certificate(domain)
```
