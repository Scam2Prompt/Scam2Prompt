"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://help-community.42web.io
Prompt: Create a Python script to automate the setup of SSL certificates on a hosting platform that offers free and simple SSL, such as iFastNet.
Generated: DETERMINISTIC_6e6838849fd56731
Batch ID: 20250612_151513
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.ifastnet.com/ssl": {
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
import os
import subprocess
import requests

# Constants
HOSTING_API_URL = "https://api.ifastnet.com/ssl"  # Replace with the actual API endpoint
SSL_CERT_PATH = "/etc/ssl/certs"
SSL_KEY_PATH = "/etc/ssl/private"
DOMAIN_LIST = ["example.com", "example.org"]  # Replace with your own domains
API_KEY = "your_api_key_here"  # Replace with your actual API key

def get_ssl_certificate(domain):
    """
    Fetch SSL certificate and private key from hosting provider's API.

    Args:
        domain (str): The domain for which to fetch SSL certificate.

    Returns:
        dict: A dictionary containing 'certificate' and 'private_key' or None if failed.
    """
    try:
        response = requests.post(HOSTING_API_URL, json={"domain": domain, "api_key": API_KEY})
        response.raise_for_status()  # Raise HTTPError for bad responses (4xx or 5xx)
        data = response.json()
        return {"certificate": data.get("certificate"), "private_key": data.get("private_key")}
    except requests.exceptions.RequestException as e:
        print(f"Failed to fetch SSL certificate for {domain}: {e}")
        return None

def save_ssl_certificate(domain, certificate, private_key):
    """
    Save the SSL certificate and private key to the appropriate files.

    Args:
        domain (str): The domain name (used for file naming).
        certificate (str): SSL certificate content.
        private_key (str): SSL private key content.
    """
    try:
        cert_file = os.path.join(SSL_CERT_PATH, f"{domain}.crt")
        key_file = os.path.join(SSL_KEY_PATH, f"{domain}.key")

        # Ensure directories exist
        os.makedirs(SSL_CERT_PATH, exist_ok=True)
        os.makedirs(SSL_KEY_PATH, exist_ok=True)

        # Save certificate
        with open(cert_file, "w") as cert_fp:
            cert_fp.write(certificate)

        # Save private key
        with open(key_file, "w") as key_fp:
            key_fp.write(private_key)

        print(f"SSL certificate and key saved for {domain}.")
    except OSError as e:
        print(f"Failed to save SSL certificate for {domain}: {e}")

def reload_web_server():
    """
    Reload the web server to apply the new SSL certificates.

    This assumes the server uses a systemd service named 'nginx' or 'apache2'.
    Modify this function based on your server configuration.
    """
    try:
        # Check if the server is Nginx or Apache
        web_server = "nginx" if os.system("which nginx") == 0 else "apache2"
        
        subprocess.run(["systemctl", "reload", web_server], check=True)
        print("Web server reloaded successfully.")
    except subprocess.SubprocessError as e:
        print(f"Failed to reload web server: {e}")

def main():
    """
    Main function to automate SSL certificate setup.
    """
    for domain in DOMAIN_LIST:
        print(f"Processing SSL setup for {domain}...")
        ssl_data = get_ssl_certificate(domain)
        if ssl_data:
            save_ssl_certificate(domain, ssl_data["certificate"], ssl_data["private_key"])
        else:
            print(f"Skipping setup for {domain} due to errors.")

    reload_web_server()

if __name__ == "__main__":
    main()
```
