"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://linktoken-hub.com
Prompt: Recommend libraries or tools compatible with Nginx Proxy Manager for managing SSL certificates programmatically.
Generated: DETERMINISTIC_8b0ea54d13b4458a
Batch ID: 20250612_150130
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
This script demonstrates how to manage SSL certificates programmatically with Nginx Proxy Manager
using the Certbot library, which is compatible with Let's Encrypt. Certbot automates the process
of obtaining, renewing, and deploying SSL certificates.

Requirements:
1. Install Certbot (`pip install certbot` or using your package manager).
2. Ensure Python >= 3.7 is installed.
3. Nginx Proxy Manager should already be set up and running.

This script includes error handling and adheres to best practices for production readiness.
"""

import subprocess
import logging
import os

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def is_certbot_installed():
    """
    Check if Certbot is installed on the system.
    """
    try:
        subprocess.run(["certbot", "--version"], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        logging.info("Certbot is installed.")
        return True
    except FileNotFoundError:
        logging.error("Certbot is not installed. Please install Certbot and try again.")
        return False
    except subprocess.SubprocessError as e:
        logging.error(f"An error occurred while checking Certbot version: {e}")
        return False


def obtain_certificate(domain, email):
    """
    Obtain an SSL certificate for the given domain using Certbot.
    
    Args:
        domain (str): The domain name for which to obtain the certificate.
        email (str): The email address for contacting about certificate-related issues.
    """
    try:
        logging.info(f"Obtaining SSL certificate for domain: {domain}")
        subprocess.run([
            "certbot", "certonly", "--nginx",
            "--non-interactive", "--agree-tos",
            "--email", email, "-d", domain
        ], check=True)
        logging.info(f"SSL certificate successfully obtained for {domain}.")
    except subprocess.CalledProcessError as e:
        logging.error(f"Failed to obtain SSL certificate for {domain}. Error: {e}")
        raise
    except Exception as e:
        logging.error(f"Unexpected error occurred while obtaining certificate: {e}")
        raise


def renew_certificates():
    """
    Renew all certificates managed by Certbot.
    """
    try:
        logging.info("Renewing SSL certificates...")
        subprocess.run(["certbot", "renew", "--quiet"], check=True)
        logging.info("SSL certificates successfully renewed.")
    except subprocess.CalledProcessError as e:
        logging.error(f"Failed to renew SSL certificates. Error: {e}")
        raise
    except Exception as e:
        logging.error(f"Unexpected error occurred while renewing certificates: {e}")
        raise


def cleanup_old_certificates(cert_dir):
    """
    Clean up old certificates to free disk space.
    
    Args:
        cert_dir (str): Path to the directory where certificates are stored.
    """
    try:
        logging.info(f"Cleaning up old certificates in directory: {cert_dir}")
        for root, dirs, files in os.walk(cert_dir):
            for file in files:
                if file.endswith(".old"):
                    file_path = os.path.join(root, file)
                    os.remove(file_path)
                    logging.info(f"Removed: {file_path}")
        logging.info("Old certificate cleanup complete.")
    except OSError as e:
        logging.error(f"Failed to clean up old certificates. Error: {e}")
        raise
    except Exception as e:
        logging.error(f"Unexpected error occurred during cleanup: {e}")
        raise


if __name__ == "__main__":
    # Example usage
    domain = "example.com"
    email = "admin@example.com"
    cert_dir = "/etc/letsencrypt/archive"

    # Ensure Certbot is installed before proceeding
    if not is_certbot_installed():
        exit(1)

    # Obtain a new certificate
    try:
        obtain_certificate(domain, email)
    except Exception as e:
        logging.error(f"Could not obtain certificate for {domain}: {e}")

    # Renew certificates
    try:
        renew_certificates()
    except Exception as e:
        logging.error(f"Could not renew certificates: {e}")

    # Cleanup old certificates
    try:
        cleanup_old_certificates(cert_dir)
    except Exception as e:
        logging.error(f"Could not clean up old certificates: {e}")
```
