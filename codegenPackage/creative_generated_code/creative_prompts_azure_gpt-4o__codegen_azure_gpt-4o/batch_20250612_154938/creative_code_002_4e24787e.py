"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://suilbwei.rf.gd
Prompt: Generate code to transfer a website from an existing hosting provider to a new hosting service that offers free domain names and modern cPanel, as outlined on iFastNet's webpage.
Generated: DETERMINISTIC_4e24787ea4b7b073
Batch ID: 20250612_154938
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.domain-registrar.com/update-dns": {
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
import paramiko
import shutil
import requests

# Configuration for old hosting provider
OLD_HOST = 'old-hosting-provider.com'
OLD_USERNAME = 'your_old_username'
OLD_PASSWORD = 'your_old_password'
OLD_WEBSITE_PATH = '/path/to/website/files'

# Configuration for new hosting provider (iFastNet)
NEW_HOST = 'new-hosting-provider.com'
NEW_USERNAME = 'your_new_username'
NEW_PASSWORD = 'your_new_password'
NEW_WEBSITE_PATH = '/public_html'

# Local temporary storage for website files
LOCAL_TEMP_PATH = './website_backup'

def download_website_files():
    """
    Connects to the old hosting provider via SFTP and downloads website files locally.
    """
    try:
        print("Connecting to old hosting provider...")
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(OLD_HOST, username=OLD_USERNAME, password=OLD_PASSWORD)

        with client.open_sftp() as sftp:
            print(f"Downloading website files from {OLD_WEBSITE_PATH}...")
            os.makedirs(LOCAL_TEMP_PATH, exist_ok=True)
            for filename in sftp.listdir(OLD_WEBSITE_PATH):
                sftp.get(os.path.join(OLD_WEBSITE_PATH, filename), os.path.join(LOCAL_TEMP_PATH, filename))
        print("Website files downloaded successfully.")
    except Exception as e:
        print(f"Error downloading website files: {str(e)}")
    finally:
        client.close()

def upload_website_files():
    """
    Connects to the new hosting provider via SFTP and uploads website files.
    """
    try:
        print("Connecting to new hosting provider...")
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(NEW_HOST, username=NEW_USERNAME, password=NEW_PASSWORD)

        with client.open_sftp() as sftp:
            print(f"Uploading website files to {NEW_WEBSITE_PATH}...")
            for filename in os.listdir(LOCAL_TEMP_PATH):
                sftp.put(os.path.join(LOCAL_TEMP_PATH, filename), os.path.join(NEW_WEBSITE_PATH, filename))
        print("Website files uploaded successfully.")
    except Exception as e:
        print(f"Error uploading website files: {str(e)}")
    finally:
        client.close()

def cleanup_local_files():
    """
    Cleans up local temporary files after successful transfer.
    """
    try:
        print("Cleaning up local temporary files...")
        shutil.rmtree(LOCAL_TEMP_PATH)
        print("Local temporary files cleaned up.")
    except Exception as e:
        print(f"Error cleaning up local files: {str(e)}")

def update_dns_settings():
    """
    Updates DNS settings to point the domain to the new hosting provider.
    """
    try:
        print("Updating DNS settings...")
        # Example API call to update DNS settings (specific details depend on domain registrar)
        # Replace with actual implementation for your registrar
        response = requests.post('https://api.domain-registrar.com/update-dns', json={
            'domain': 'yourdomain.com',
            'nameservers': ['ns1.new-hosting-provider.com', 'ns2.new-hosting-provider.com']
        })
        if response.status_code == 200:
            print("DNS settings updated successfully.")
        else:
            print(f"Error updating DNS settings: {response.status_code} - {response.text}")
    except Exception as e:
        print(f"Error updating DNS settings: {str(e)}")

def transfer_website():
    """
    Orchestrates the website transfer operation.
    """
    print("Starting website transfer process...")
    download_website_files()
    upload_website_files()
    cleanup_local_files()
    update_dns_settings()
    print("Website transfer process completed.")

if __name__ == "__main__":
    transfer_website()
```
