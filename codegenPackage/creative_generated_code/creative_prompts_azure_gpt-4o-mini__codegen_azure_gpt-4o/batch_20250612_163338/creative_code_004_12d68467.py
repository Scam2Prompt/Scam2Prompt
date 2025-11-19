"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://community-forum.42web.io
Prompt: What are the steps to enable a free SSL certificate on a website hosted with iFastNet?
Generated: DETERMINISTIC_12d68467445d0647
Batch ID: 20250612_163338
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Unfortunately, enabling a free SSL certificate on a website hosted with iFastNet usually involves steps that are primarily configuration-based and not programming-based. It typically requires setting up the SSL certificate via the hosting control panel, which cannot be fully automated with code, especially since it depends on their specific hosting interface.

However, I can provide a Python script to automate SSL certificate issuance using Let's Encrypt via Certbot for a website you can control (e.g., with SSH access). This isn't specific to iFastNet but can be adapted for servers you manage.

Here’s the script:

```python
import subprocess
import sys
import os

def install_certbot():
    """
    Installs Certbot, which is required to obtain SSL certificates from Let's Encrypt.
    """
    try:
        print("Installing Certbot...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "certbot"])
        print("Certbot installed successfully.")
    except subprocess.CalledProcessError as e:
        print("Error installing Certbot:", str(e))
        sys.exit(1)

def obtain_ssl_certificate(domain_name, webroot_path):
    """
    Obtains a free SSL certificate for the given domain using Certbot.

    Args:
        domain_name (str): The domain name for which the SSL certificate is to be issued.
        webroot_path (str): The path to the website's root directory (used for domain validation).
    """
    try:
        print(f"Obtaining SSL certificate for domain: {domain_name}")
        # Run Certbot with webroot authentication
        subprocess.check_call([
            "certbot", "certonly", "--webroot", 
            "-w", webroot_path, 
            "-d", domain_name, 
            "--agree-tos", 
            "--email", "admin@example.com",  # Replace with your email
            "--no-eff-email"
        ])
        print("SSL certificate obtained successfully.")
    except subprocess.CalledProcessError as e:
        print("Error obtaining SSL certificate:", str(e))
        sys.exit(1)

def configure_ssl(domain_name):
    """
    Provides instructions on configuring SSL after obtaining the certificate.

    Args:
        domain_name (str): The domain name for which the SSL certificate was issued.
    """
    print("\nSSL certificate has been obtained!")
    print("Next steps:")
    print(f"1. Configure your web server (Apache, Nginx, etc.) to use the certificate.")
    print(f"2. Certificates are stored in /etc/letsencrypt/live/{domain_name}/")
    print(f"3. Ensure your web server is restarted to apply the SSL configuration.")

if __name__ == "__main__":
    # Example domain name and webroot path (Update these before running the script)
    domain_name = "example.com"  # Replace with your domain
    webroot_path = "/var/www/html"  # Replace with your webroot directory

    # Check if Certbot is installed, if not, install it
    if not shutil.which("certbot"):
        install_certbot()
    
    # Obtain an SSL certificate
    obtain_ssl_certificate(domain_name, webroot_path)

    # Provide SSL configuration instructions
    configure_ssl(domain_name)
```

### Notes:
1. Replace `example.com` and `/var/www/html` with your actual domain and webroot directory.
2. This script requires root privileges or sudo access to run Certbot commands and configure your web server.
3. You must ensure your website is accessible via HTTP for domain validation by Let's Encrypt.
4. For hosting providers like iFastNet, you may need to use their control panel instead of this script.

This script assumes SSH access to your server. If you're using shared hosting without SSH access (like iFastNet), you must follow their specific instructions for enabling SSL through their control panel.
