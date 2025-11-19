"""
Generated Code Metadata:
========================
Original URL: https://layer3.byethost5.com
Prompt: Write a code snippet that demonstrates how to set up a free SSL certificate on a website hosted with iFastNet.
Generated: DETERMINISTIC_7dcdb28002718fbf
Batch ID: 20250612_163616
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import subprocess
import requests
from datetime import datetime, timedelta

def setup_ssl(domain: str, email: str, webroot_path: str = "/var/www/html"):
    """
    Sets up a free SSL certificate using Certbot for a domain hosted on iFastNet.
    
    Args:
        domain (str): The domain name to secure (e.g., 'example.com').
        email (str): Email for certificate expiration notifications.
        webroot_path (str): Web root directory path. Defaults to '/var/www/html'.
    
    Returns:
        bool: True if SSL setup was successful, False otherwise.
    """
    try:
        # Check if Certbot is installed, install if not
        try:
            subprocess.run(["certbot", "--version"], check=True, capture_output=True)
        except subprocess.CalledProcessError:
            print("Installing Certbot...")
            subprocess.run(["sudo", "apt-get", "update"], check=True)
            subprocess.run(["sudo", "apt-get", "install", "-y", "certbot", "python3-certbot-apache"], check=True)
        
        # Run Certbot to obtain SSL certificate
        print(f"Obtaining SSL certificate for {domain}...")
        subprocess.run([
            "sudo", "certbot", "certonly",
            "--webroot",
            "--webroot-path", webroot_path,
            "-d", domain,
            "--email", email,
            "--agree-tos",
            "--non-interactive"
        ], check=True)
        
        # Verify certificate was obtained
        cert_path = f"/etc/letsencrypt/live/{domain}/fullchain.pem"
        if not os.path.exists(cert_path):
            raise FileNotFoundError(f"Certificate not found at {cert_path}")
        
        print(f"Successfully obtained SSL certificate for {domain}")
        return True
    
    except subprocess.CalledProcessError as e:
        print(f"Error running command: {e.stderr.decode('utf-8')}")
        return False
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return False

def check_ssl_expiry(domain: str):
    """
    Checks the expiry date of the SSL certificate for a domain.
    
    Args:
        domain (str): The domain to check (e.g., 'example.com').
    
    Returns:
        datetime: Expiry date of the SSL certificate or None if error.
    """
    try:
        cert_path = f"/etc/letsencrypt/live/{domain}/cert.pem"
        if not os.path.exists(cert_path):
            raise FileNotFoundError(f"Certificate not found at {cert_path}")
        
        # Get certificate expiry date
        result = subprocess.run([
            "openssl", "x509", "-enddate", "-noout", "-in", cert_path
        ], capture_output=True, text=True, check=True)
        
        expiry_str = result.stdout.strip().replace("notAfter=", "")
        expiry_date = datetime.strptime(expiry_str, "%b %d %H:%M:%S %Y %Z")
        return expiry_date
    
    except Exception as e:
        print(f"Error checking SSL expiry: {str(e)}")
        return None

def renew_ssl():
    """
    Attempts to renew all SSL certificates managed by Certbot.
    
    Returns:
        bool: True if renewal was successful, False otherwise.
    """
    try:
        print("Attempting to renew SSL certificates...")
        subprocess.run(["sudo", "certbot", "renew", "--non-interactive"], check=True)
        print("SSL certificates renewed successfully")
        return True
    except subprocess.CalledProcessError as e:
        print(f"Error renewing SSL certificates: {e.stderr.decode('utf-8')}")
        return False
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return False

# Example usage
if __name__ == "__main__":
    DOMAIN = "example.com"
    EMAIL = "admin@example.com"
    
    # Setup SSL
    if setup_ssl(DOMAIN, EMAIL):
        print("SSL setup completed successfully")
        
        # Check expiry
        expiry = check_ssl_expiry(DOMAIN)
        if expiry:
            print(f"SSL certificate expires on: {expiry.strftime('%Y-%m-%d')}")
            
            # Setup auto-renewal if certificate expires in less than 30 days
            if expiry - datetime.now() < timedelta(days=30):
                print("Certificate expires soon. Attempting renewal...")
                renew_ssl()
    else:
        print("SSL setup failed")
```
