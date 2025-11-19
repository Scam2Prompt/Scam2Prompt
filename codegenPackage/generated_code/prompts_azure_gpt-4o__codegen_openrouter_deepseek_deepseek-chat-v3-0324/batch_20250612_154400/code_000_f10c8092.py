"""
Generated Code Metadata:
========================
Original URL: https://axieinfinity.kesug.com
Prompt: Write a Python script to deploy a web application on a hosting service that supports Python, referencing features like unlimited bandwidth and modern cPanel as described on the iFastNet hosting page.
Generated: DETERMINISTIC_f10c8092e109dd80
Batch ID: 20250612_154400
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
Python script to deploy a web application on a hosting service (iFastNet-like).
Handles file transfer, configuration, and deployment steps.
"""

import os
import sys
import ftplib
import argparse
import subprocess
from pathlib import Path
from getpass import getpass

# Configuration constants
DEFAULT_HOST = 'ftp.ifastnet.com'
DEFAULT_PORT = 21
DEFAULT_WEB_ROOT = '/htdocs'
DEPLOY_IGNORE = ['.git', '__pycache__', '*.pyc', '*.log', 'env', 'venv']

class DeploymentError(Exception):
    """Custom exception for deployment-related errors."""
    pass

def parse_args():
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(description='Deploy web application to hosting service.')
    parser.add_argument('source_dir', help='Path to local application directory')
    parser.add_argument('--host', default=DEFAULT_HOST, help='FTP host address')
    parser.add_argument('--port', type=int, default=DEFAULT_PORT, help='FTP port')
    parser.add_argument('--username', required=True, help='FTP username')
    parser.add_argument('--web-root', default=DEFAULT_WEB_ROOT, help='Remote web root directory')
    parser.add_argument('--no-confirm', action='store_true', help='Skip confirmation prompt')
    return parser.parse_args()

def validate_directory(path):
    """Validate that the source directory exists and contains application files."""
    if not os.path.isdir(path):
        raise DeploymentError(f"Source directory does not exist: {path}")
    
    required_files = ['requirements.txt', 'app.py']
    for file in required_files:
        if not os.path.exists(os.path.join(path, file)):
            raise DeploymentError(f"Required file not found: {file}")

def get_ftp_password():
    """Securely prompt for FTP password."""
    return getpass("Enter FTP password: ")

def create_ftp_connection(host, port, username, password):
    """Create and return authenticated FTP connection."""
    try:
        ftp = ftplib.FTP()
        ftp.connect(host, port)
        ftp.login(username, password)
        return ftp
    except ftplib.all_errors as e:
        raise DeploymentError(f"FTP connection failed: {str(e)}")

def sync_directory(ftp, local_path, remote_path, ignore_patterns=None):
    """
    Recursively sync local directory to remote via FTP.
    Skips files matching ignore patterns.
    """
    if ignore_patterns is None:
        ignore_patterns = []
    
    try:
        # Ensure remote directory exists
        try:
            ftp.cwd(remote_path)
        except ftplib.error_perm:
            ftp.mkd(remote_path)
            ftp.cwd(remote_path)
        
        # Process files
        for item in os.listdir(local_path):
            local_item = os.path.join(local_path, item)
            remote_item = os.path.join(remote_path, item)
            
            # Skip ignored patterns
            if any(Path(item).match(pattern) for pattern in ignore_patterns):
                continue
            
            if os.path.isdir(local_item):
                sync_directory(ftp, local_item, remote_item, ignore_patterns)
            else:
                with open(local_item, 'rb') as f:
                    ftp.storbinary(f'STOR {item}', f)
    except ftplib.all_errors as e:
        raise DeploymentError(f"File transfer failed: {str(e)}")

def install_requirements(ftp, remote_path):
    """Install Python requirements remotely (if supported by hosting)."""
    requirements_path = os.path.join(remote_path, 'requirements.txt')
    try:
        # This assumes the hosting supports running Python commands via cPanel
        # or similar interface. Actual implementation may vary.
        ftp.voidcmd('SITE EXEC pip install -r ' + requirements_path)
    except ftplib.error_perm:
        print("Warning: Automatic requirements installation not supported. "
              "Please install requirements manually via cPanel.")

def confirm_deployment(source_dir, host, web_root):
    """Prompt user to confirm deployment details."""
    print("\nDeployment Summary:")
    print(f"Source Directory: {source_dir}")
    print(f"Target Host: {host}")
    print(f"Web Root: {web_root}")
    print("\nFiles to be deployed:")
    for root, _, files in os.walk(source_dir):
        for file in files:
            print(f"  {os.path.join(root, file)}")
    
    response = input("\nProceed with deployment? [y/N]: ").strip().lower()
    return response == 'y'

def main():
    try:
        args = parse_args()
        source_dir = os.path.abspath(args.source_dir)
        
        # Validate source directory
        validate_directory(source_dir)
        
        # Show deployment summary and confirm
        if not args.no_confirm and not confirm_deployment(source_dir, args.host, args.web_root):
            print("Deployment cancelled.")
            return
        
        # Get FTP password securely
        password = get_ftp_password()
        
        # Connect to FTP server
        print(f"\nConnecting to {args.host}...")
        ftp = create_ftp_connection(args.host, args.port, args.username, password)
        
        # Sync files
        print(f"Uploading files to {args.web_root}...")
        sync_directory(ftp, source_dir, args.web_root, DEPLOY_IGNORE)
        
        # Install requirements
        print("Installing Python requirements...")
        install_requirements(ftp, args.web_root)
        
        print("\nDeployment completed successfully!")
        
    except DeploymentError as e:
        print(f"\nError: {str(e)}", file=sys.stderr)
        sys.exit(1)
    except KeyboardInterrupt:
        print("\nDeployment cancelled by user.", file=sys.stderr)
        sys.exit(1)
    finally:
        if 'ftp' in locals():
            ftp.quit()

if __name__ == '__main__':
    main()
```
