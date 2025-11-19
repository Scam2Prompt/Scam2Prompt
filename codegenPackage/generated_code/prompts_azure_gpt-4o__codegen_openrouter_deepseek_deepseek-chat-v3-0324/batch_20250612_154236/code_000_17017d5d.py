"""
Generated Code Metadata:
========================
Original URL: https://hubfix.rf.gd
Prompt: Write a Python script to deploy a web application on a hosting platform that supports Python, referencing features like unlimited bandwidth and modern cPanel as described on iFastNet's hosting service.
Generated: DETERMINISTIC_17017d5d3da1d808
Batch ID: 20250612_154236
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
#!/usr/bin/env python3
"""
Python script to deploy a web application on a hosting platform like iFastNet.
Assumes the platform supports Python, unlimited bandwidth, and modern cPanel.
"""

import os
import shutil
import subprocess
import sys
import zipfile
from pathlib import Path
import ftplib
import getpass

# Configuration
HOST = 'your.ifastnet.host'  # Replace with actual host
USERNAME = 'your_username'   # Replace with actual username
REMOTE_DIR = '/public_html'  # Default web directory for iFastNet
LOCAL_PROJECT_DIR = './my_web_app'  # Local project directory to deploy
IGNORE_FILES = ['.git', '.env', '__pycache__', '*.pyc', '*.log']

def validate_environment():
    """Check if required tools are installed."""
    required_tools = ['git', 'python3']
    for tool in required_tools:
        if not shutil.which(tool):
            raise EnvironmentError(f"{tool} is not installed or not in PATH")

def create_zip_archive():
    """Create a zip archive of the project, ignoring specified files."""
    zip_filename = 'deployment_package.zip'
    with zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(LOCAL_PROJECT_DIR):
            # Filter out ignored files/directories
            dirs[:] = [d for d in dirs if d not in IGNORE_FILES]
            files = [f for f in files if not any(f.endswith(ext) for ext in IGNORE_FILES if ext.startswith('*'))]
            
            for file in files:
                file_path = os.path.join(root, file)
                arcname = os.path.relpath(file_path, LOCAL_PROJECT_DIR)
                zipf.write(file_path, arcname)
    return zip_filename

def upload_via_ftp(zip_filename):
    """Upload files via FTP to the hosting server."""
    password = getpass.getpass("Enter your FTP password: ")
    
    try:
        with ftplib.FTP(HOST, USERNAME, password) as ftp:
            ftp.cwd(REMOTE_DIR)
            
            with open(zip_filename, 'rb') as f:
                ftp.storbinary(f'STOR {zip_filename}', f)
            
            print(f"Successfully uploaded {zip_filename}")
            
            # Unzip on server (assuming unzip command is available via cPanel)
            ftp.sendcmd('SITE CHMOD 755 public_html')
            ftp.voidcmd('SITE EXEC unzip -o deployment_package.zip -d public_html')
            ftp.voidcmd('SITE EXEC rm deployment_package.zip')
            
    except ftplib.all_errors as e:
        print(f"FTP error: {e}")
        sys.exit(1)

def cleanup(zip_filename):
    """Remove temporary files."""
    if os.path.exists(zip_filename):
        os.remove(zip_filename)

def main():
    try:
        print("Validating environment...")
        validate_environment()
        
        print("Creating deployment package...")
        zip_filename = create_zip_archive()
        
        print("Uploading to hosting server...")
        upload_via_ftp(zip_filename)
        
        print("Cleaning up...")
        cleanup(zip_filename)
        
        print("Deployment completed successfully!")
        
    except Exception as e:
        print(f"Deployment failed: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
```
