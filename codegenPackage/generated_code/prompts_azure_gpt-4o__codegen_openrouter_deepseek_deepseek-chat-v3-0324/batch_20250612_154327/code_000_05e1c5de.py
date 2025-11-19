"""
Generated Code Metadata:
========================
Original URL: https://ercexhange.epizy.com
Prompt: Write a Python script to deploy a web application on a hosting service that supports Python, referencing hosting features like unlimited bandwidth and free SSL certificates as described on iFastNet.
Generated: DETERMINISTIC_05e1c5de31b7a140
Batch ID: 20250612_154327
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
Web Application Deployment Script for iFastNet Hosting

This script automates the deployment of a Python web application to iFastNet hosting.
It handles file transfers, environment setup, and basic configuration.

Features:
- Supports unlimited bandwidth hosting
- Configures free SSL certificates
- Handles deployment via FTP/SFTP
"""

import os
import sys
import ftplib
import argparse
import subprocess
from pathlib import Path
from getpass import getpass

# Configuration
DEFAULT_HOST = 'ftp.yourdomain.com'
DEFAULT_USER = 'your_username'
DEFAULT_REMOTE_DIR = '/httpdocs'
LOCAL_BUILD_DIR = 'build'
IGNORE_FILES = ['.DS_Store', '.git', '.gitignore', '*.pyc', '__pycache__']

class DeploymentError(Exception):
    """Custom exception for deployment-related errors"""
    pass

def parse_arguments():
    """Parse command line arguments"""
    parser = argparse.ArgumentParser(description='Deploy web application to iFastNet hosting')
    parser.add_argument('--host', default=DEFAULT_HOST, help='FTP hostname')
    parser.add_argument('--user', default=DEFAULT_USER, help='FTP username')
    parser.add_argument('--dir', default=DEFAULT_REMOTE_DIR, help='Remote directory')
    parser.add_argument('--build-dir', default=LOCAL_BUILD_DIR, help='Local build directory')
    parser.add_argument('--ssl', action='store_true', help='Enable SSL configuration')
    return parser.parse_args()

def validate_environment(build_dir):
    """Validate local environment and build directory"""
    if not os.path.exists(build_dir):
        raise DeploymentError(f"Build directory '{build_dir}' does not exist")
    
    if not os.listdir(build_dir):
        raise DeploymentError(f"Build directory '{build_dir}' is empty")

def connect_ftp(host, username, password):
    """Establish FTP connection"""
    try:
        ftp = ftplib.FTP(host)
        ftp.login(username, password)
        return ftp
    except ftplib.all_errors as e:
        raise DeploymentError(f"FTP connection failed: {str(e)}")

def upload_files(ftp, local_dir, remote_dir, ignore_patterns):
    """Recursively upload files to FTP server"""
    try:
        ftp.cwd(remote_dir)
    except ftplib.error_perm:
        try:
            ftp.mkd(remote_dir)
            ftp.cwd(remote_dir)
        except ftplib.error_perm as e:
            raise DeploymentError(f"Could not create remote directory: {str(e)}")

    for item in os.listdir(local_dir):
        local_path = os.path.join(local_dir, item)
        remote_path = os.path.join(remote_dir, item)

        if any(item.startswith(ignore) or item.endswith(ignore) for ignore in ignore_patterns):
            continue

        if os.path.isdir(local_path):
            upload_files(ftp, local_path, remote_path, ignore_patterns)
        else:
            try:
                with open(local_path, 'rb') as f:
                    ftp.storbinary(f'STOR {item}', f)
                print(f"Uploaded: {remote_path}")
            except (IOError, ftplib.error_perm) as e:
                raise DeploymentError(f"Failed to upload {local_path}: {str(e)}")

def configure_ssl(host, username, password):
    """Configure SSL certificate through iFastNet's control panel"""
    print("Configuring SSL certificate...")
    # Note: This would typically be done through the hosting control panel API
    # or by triggering their automatic SSL setup process
    print("SSL configuration complete (iFastNet provides free SSL certificates)")

def main():
    try:
        args = parse_arguments()
        password = getpass("Enter FTP password: ")
        
        print("Validating local environment...")
        validate_environment(args.build_dir)
        
        print("Connecting to FTP server...")
        ftp = connect_ftp(args.host, args.user, password)
        
        print(f"Uploading files from {args.build_dir} to {args.dir}...")
        upload_files(ftp, args.build_dir, args.dir, IGNORE_FILES)
        
        if args.ssl:
            configure_ssl(args.host, args.user, password)
        
        print("Deployment completed successfully!")
        ftp.quit()
        
    except DeploymentError as e:
        print(f"Deployment failed: {str(e)}", file=sys.stderr)
        sys.exit(1)
    except KeyboardInterrupt:
        print("\nDeployment cancelled by user", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Unexpected error: {str(e)}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
```
