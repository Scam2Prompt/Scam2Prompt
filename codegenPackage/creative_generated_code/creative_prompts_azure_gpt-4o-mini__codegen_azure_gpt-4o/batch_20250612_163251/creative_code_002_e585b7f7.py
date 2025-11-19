"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://paxfiul.epizy.com
Prompt: Create a guide for transferring an existing website to iFastNet, including steps for utilizing their free domain and SSL features.
Generated: DETERMINISTIC_e585b7f7a400dd1e
Batch ID: 20250612_163251
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://your-ifastnet-domain:2083/json-api/": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

Certainly! Below is a Python script that acts as a guide/tool to help users transfer an existing website to iFastNet. It includes steps for utilizing their free domain and SSL features. This script assumes the use of cPanel API for uploading files, setting up SSL, and managing domains. The user needs their iFastNet cPanel credentials.

```python
import requests
import os
import zipfile
from pathlib import Path

# Constants
CPANEL_API_URL = "https://your-ifastnet-domain:2083/json-api/"
UPLOAD_ENDPOINT = "filemanager_upload"
SSL_INSTALL_ENDPOINT = "installssl"
DOMAIN_ADD_ENDPOINT = "addaddondomain"
CPANEL_USERNAME = "your_cpanel_username"
CPANEL_PASSWORD = "your_cpanel_password"

# Paths
LOCAL_WEBSITE_FILES_PATH = "/path/to/your/website_files"
WEBSITE_ZIP_PATH = "/path/to/your/website_files.zip"
REMOTE_WEBSITE_DIRECTORY = "/public_html"  # Default site directory in iFastNet

def zip_local_files(source_dir, output_zip_path):
    """
    Compress all files in the source directory into a single ZIP file.
    """
    try:
        with zipfile.ZipFile(output_zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
            for root, _, files in os.walk(source_dir):
                for file in files:
                    file_path = Path(root) / file
                    zipf.write(file_path, arcname=file_path.relative_to(source_dir))
        print(f"Website files successfully compressed to {output_zip_path}")
    except Exception as e:
        print(f"Error compressing website files: {e}")
        raise

def upload_website_to_ifastnet(zip_path, remote_path):
    """
    Upload the website ZIP file to iFastNet using cPanel API.
    """
    try:
        files = {'file': open(zip_path, 'rb')}
        data = {
            'cpanel_jsonapi_user': CPANEL_USERNAME,
            'cpanel_jsonapi_apiversion': 2,
            'cpanel_jsonapi_module': 'Fileman',
            'cpanel_jsonapi_func': UPLOAD_ENDPOINT,
            'path': remote_path
        }
        response = requests.post(CPANEL_API_URL + UPLOAD_ENDPOINT, files=files, data=data, auth=(CPANEL_USERNAME, CPANEL_PASSWORD))
        if response.status_code == 200:
            print("Website files uploaded successfully.")
        else:
            print(f"Failed to upload website files. Response: {response.text}")
    except Exception as e:
        print(f"Error uploading website files: {e}")
        raise

def add_domain_to_ifastnet(domain_name):
    """
    Add a free domain to iFastNet via cPanel API.
    """
    try:
        data = {
            'cpanel_jsonapi_user': CPANEL_USERNAME,
            'cpanel_jsonapi_apiversion': 2,
            'cpanel_jsonapi_module': 'AddonDomain',
            'cpanel_jsonapi_func': DOMAIN_ADD_ENDPOINT,
            'newdomain': domain_name,
            'subdomain': domain_name.split('.')[0],
            'dir': f"/public_html/{domain_name}"
        }
        response = requests.post(CPANEL_API_URL + DOMAIN_ADD_ENDPOINT, data=data, auth=(CPANEL_USERNAME, CPANEL_PASSWORD))
        if response.status_code == 200:
            print(f"Domain {domain_name} added successfully.")
        else:
            print(f"Failed to add domain. Response: {response.text}")
    except Exception as e:
        print(f"Error adding domain: {e}")
        raise

def install_ssl(domain_name):
    """
    Install free SSL for the given domain via iFastNet.
    """
    try:
        data = {
            'cpanel_jsonapi_user': CPANEL_USERNAME,
            'cpanel_jsonapi_apiversion': 2,
            'cpanel_jsonapi_module': 'SSL',
            'cpanel_jsonapi_func': SSL_INSTALL_ENDPOINT,
            'domain': domain_name
        }
        response = requests.post(CPANEL_API_URL + SSL_INSTALL_ENDPOINT, data=data, auth=(CPANEL_USERNAME, CPANEL_PASSWORD))
        if response.status_code == 200:
            print(f"SSL installed successfully for {domain_name}.")
        else:
            print(f"Failed to install SSL. Response: {response.text}")
    except Exception as e:
        print(f"Error installing SSL: {e}")
        raise

def main():
    """
    Main function to guide the user through the website transfer process.
    """
    print("Starting website transfer process...")
    
    # Step 1: Compress website files
    zip_local_files(LOCAL_WEBSITE_FILES_PATH, WEBSITE_ZIP_PATH)

    # Step 2: Upload website files to iFastNet
    upload_website_to_ifastnet(WEBSITE_ZIP_PATH, REMOTE_WEBSITE_DIRECTORY)
    
    # Step 3: Add free domain
    domain_name = input("Enter your free domain name (e.g., example.free-domain.net): ")
    add_domain_to_ifastnet(domain_name)

    # Step 4: Install free SSL for the domain
    install_ssl(domain_name)

    print("Website transfer process completed successfully!")

if __name__ == "__main__":
    main()
```
