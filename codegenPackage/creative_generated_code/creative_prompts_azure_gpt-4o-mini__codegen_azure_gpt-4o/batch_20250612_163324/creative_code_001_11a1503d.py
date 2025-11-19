"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://doubleway.rf.gd
Prompt: Write a Python script that utilizes the free SSL feature offered by iFastNet for a web application hosted on their platform.
Generated: DETERMINISTIC_11a1503d767b1079
Batch ID: 20250612_163324
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.ifastnet.com/ssl/free": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```python
"""
Script to utilize free SSL from iFastNet for a web application hosted on their platform.
This script automates the process of ensuring SSL integration and renewal using the iFastNet service.
Tested on Python 3.7+.

Note: Ensure that requests and OpenSSL are installed in your environment before running this script.
      Use `pip install requests pyopenssl` to install them.
"""

import requests
import os
import subprocess
from datetime import datetime, timedelta

# Constants
IFASTNET_API_URL = "https://api.ifastnet.com/ssl/free"
YOUR_DOMAIN = "yourdomain.com"  # Replace with your domain
API_KEY = "your_api_key"  # Replace with your iFastNet API key
CERT_FOLDER = "./certificates"  # Folder to store SSL certificates

# Ensure the certificates folder exists
os.makedirs(CERT_FOLDER, exist_ok=True)

def fetch_free_ssl(domain, api_key):
    """
    Fetch a free SSL certificate from iFastNet API.
    
    :param domain: The domain name for which SSL is requested.
    :param api_key: API key to authenticate with the iFastNet API.
    :return: Dictionary containing the certificate details or None if the request fails.
    """
    try:
        response = requests.post(IFASTNET_API_URL, data={"domain": domain, "api_key": api_key})
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"Error fetching SSL certificate: {e}")
        return None

def save_certificate(cert_data):
    """
    Save certificate data to files for use by your web server.
    
    :param cert_data: Dictionary containing certificate and key data.
    """
    try:
        cert_path = os.path.join(CERT_FOLDER, "certificate.crt")
        key_path = os.path.join(CERT_FOLDER, "private.key")

        with open(cert_path, "w") as cert_file:
            cert_file.write(cert_data["certificate"])
        
        with open(key_path, "w") as key_file:
            key_file.write(cert_data["private_key"])
        
        print(f"Certificate saved at: {cert_path}")
        print(f"Private key saved at: {key_path}")
    except KeyError as e:
        print(f"Missing data in certificate response: {e}")
    except OSError as e:
        print(f"Error saving certificate files: {e}")

def check_certificate_expiry(cert_path):
    """
    Check if the SSL certificate is close to its expiry date.
    
    :param cert_path: Path to the certificate file.
    :return: Boolean indicating whether the certificate is near expiry.
    """
    try:
        result = subprocess.run(["openssl", "x509", "-in", cert_path, "-noout", "-dates"], capture_output=True, text=True)
        if result.returncode != 0:
            print(f"Error reading certificate: {result.stderr}")
            return False
        
        output = result.stdout
        start_date = datetime.strptime(output.split("notBefore=")[1].split("\n")[0], "%b %d %H:%M:%S %Y %Z")
        expiry_date = datetime.strptime(output.split("notAfter=")[1].split("\n")[0], "%b %d %H:%M:%S %Y %Z")
        
        # Check if the certificate is close to expiry (e.g., within 10 days)
        if expiry_date - datetime.utcnow() <= timedelta(days=10):
            return True
        return False
    except Exception as e:
        print(f"Error checking certificate expiry: {e}")
        return False

def main():
    """
    Main function to handle SSL integration and renewal.
    """
    cert_path = os.path.join(CERT_FOLDER, "certificate.crt")
    
    # Check if the certificate already exists and is valid
    if os.path.exists(cert_path) and not check_certificate_expiry(cert_path):
        print("SSL certificate is valid and not close to expiry.")
        return
    
    # Fetch a new SSL certificate
    print("Fetching a new SSL certificate...")
    cert_data = fetch_free_ssl(YOUR_DOMAIN, API_KEY)
    
    if cert_data:
        save_certificate(cert_data)
    else:
        print("Failed to fetch SSL certificate.")

if __name__ == "__main__":
    main()
```
