"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tech-connect.cloud
Prompt: Provide an example of how to integrate Hostinger's hosting services with a website deployment pipeline using Python or Bash scripts.
Generated: DETERMINISTIC_59b2a83fe665fae5
Batch ID: 20250612_145306
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

### Bash Script for Deploying a Website to Hostinger

```bash
#!/bin/bash

# This script automates the deployment of a website to Hostinger via FTP.

# Exit the script if any command fails
set -e

# Configuration variables
FTP_SERVER="ftp.your-hostinger-domain.com"
FTP_USERNAME="your-ftp-username"
FTP_PASSWORD="your-ftp-password"
LOCAL_DIRECTORY="/path/to/your/local/website/files"
REMOTE_DIRECTORY="/path/to/remote/directory"

# Function to print error message and exit
error_exit() {
  echo "Error: $1"
  exit 1
}

# Check if lftp is installed
if ! command -v lftp &> /dev/null; then
  error_exit "lftp is not installed. Please install it to use this script."
fi

# Deploy files using lftp
echo "Starting deployment to Hostinger..."

lftp -e "
open -u $FTP_USERNAME,$FTP_PASSWORD $FTP_SERVER
lcd $LOCAL_DIRECTORY
mirror -R --parallel=4 $LOCAL_DIRECTORY $REMOTE_DIRECTORY
bye
" || error_exit "Deployment failed."

echo "Deployment successful!"
```

---

### Python Script for Deploying a Website to Hostinger via FTP

```python
import os
from ftplib import FTP, error_perm

# Configuration variables
FTP_SERVER = "ftp.your-hostinger-domain.com"
FTP_USERNAME = "your-ftp-username"
FTP_PASSWORD = "your-ftp-password"
LOCAL_DIRECTORY = "/path/to/your/local/website/files"
REMOTE_DIRECTORY = "/path/to/remote/directory"

def upload_directory(ftp, local_dir, remote_dir):
    """
    Recursively upload files and directories to the remote FTP server.
    """
    try:
        # Change to the remote directory
        ftp.cwd(remote_dir)
    except error_perm:
        # If the remote directory does not exist, create it
        ftp.mkd(remote_dir)
        ftp.cwd(remote_dir)
    
    for item in os.listdir(local_dir):
        local_path = os.path.join(local_dir, item)
        if os.path.isfile(local_path):
            # Upload a file
            with open(local_path, "rb") as file:
                ftp.storbinary(f"STOR {item}", file)
            print(f"Uploaded file: {item}")
        elif os.path.isdir(local_path):
            # Recursively upload a directory
            upload_directory(ftp, local_path, os.path.join(remote_dir, item))

def main():
    """
    Main function to connect to the FTP server and deploy the website.
    """
    try:
        print("Connecting to Hostinger FTP server...")
        ftp = FTP(FTP_SERVER)
        ftp.login(FTP_USERNAME, FTP_PASSWORD)
        print("Connected successfully!")

        print("Starting deployment...")
        upload_directory(ftp, LOCAL_DIRECTORY, REMOTE_DIRECTORY)
        print("Deployment completed successfully!")

        ftp.quit()
    except Exception as e:
        print(f"Error during deployment: {e}")

if __name__ == "__main__":
    main()
```

### Notes:
- Replace placeholder values (`ftp.your-hostinger-domain.com`, `your-ftp-username`, etc.) with actual credentials.
- Ensure the required libraries (`ftplib` in Python or `lftp` in Bash) are installed.
- Store sensitive credentials securely (e.g., use environment variables or secret management tools in production).
