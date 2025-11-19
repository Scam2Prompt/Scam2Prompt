"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://minipepe.digital
Prompt: What steps should I take if my site is accessible via HTTPS but lacks an SSL certificate in FASTPANEL?
Generated: DETERMINISTIC_1ae2ae6ce3ff029f
Batch ID: 20250612_160044
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import subprocess
import logging

# Configure logging for the script
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def check_ssl_certificate(domain):
    """
    Check if the domain has a valid SSL certificate.
    
    :param domain: The domain name to check
    :return: True if a valid SSL certificate is found, False otherwise
    """
    try:
        result = subprocess.run(
            ['openssl', 's_client', '-connect', f'{domain}:443', '-servername', domain],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            check=True
        )
        cert_info = result.stdout.decode('utf-8')
        if "BEGIN CERTIFICATE" in cert_info:
            logging.info(f"SSL certificate found for {domain}.")
            return True
        else:
            logging.warning(f"No SSL certificate found for {domain}.")
            return False
    except subprocess.CalledProcessError as e:
        logging.error(f"Error occurred while checking SSL certificate: {e}")
        return False

def install_ssl_certificate(domain):
    """
    Install an SSL certificate for the specified domain using FastPanel commands.
    
    :param domain: The domain name for which to install the SSL certificate
    """
    try:
        # Example command to install SSL certificate in FastPanel
        subprocess.run(['fastpanel', 'ssl', 'install', domain], check=True)
        logging.info(f"SSL certificate installation initiated for {domain}.")
    except subprocess.CalledProcessError as e:
        logging.error(f"Error occurred while installing SSL certificate: {e}")

def main():
    """
    Main function to check and install SSL certificate for a domain.
    """
    domain = input("Enter your domain (e.g., example.com): ")
    
    if check_ssl_certificate(domain):
        logging.info("The site already has a valid SSL certificate.")
    else:
        logging.info("No valid SSL certificate found. Initiating installation...")
        install_ssl_certificate(domain)

if __name__ == "__main__":
    main()
```
