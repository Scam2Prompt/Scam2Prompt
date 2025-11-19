"""
Generated Code Metadata:
========================
Original URL: https://panemicav2.rf.gd
Prompt: Write a Python script to automate the deployment of a web application on iFastNet Web Hosting using their Node.js and Python app support.
Generated: DETERMINISTIC_30bdb920eb5a3f6b
Batch ID: 20250622_212148
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
Automated deployment script for iFastNet Web Hosting with Node.js/Python support.
"""

import os
import sys
import ftplib
import time
import subprocess
import argparse
from pathlib import Path
from typing import List, Optional

# Configuration - Update these values according to your iFastNet account
CONFIG = {
    'ftp_host': 'your-ftp-host.ifastnet.com',
    'ftp_username': 'your_ftp_username',
    'ftp_password': 'your_ftp_password',
    'remote_root': '/httpdocs',  # Default web root for iFastNet
    'local_project_dir': './project_files',
    'backup_dir': './backups',
    'nodejs_version': '16',  # Supported versions: 10, 12, 14, 16
    'python_version': '3.9',  # Supported versions: 3.7, 3.8, 3.9
    'app_type': 'nodejs',  # 'nodejs' or 'python'
    'app_start_file': 'app.js' if 'nodejs' else 'app.py',
    'exclude_files': ['.env', 'node_modules', '.git', '__pycache__']
}

class DeploymentError(Exception):
    """Custom exception for deployment-related errors."""
    pass

class IFastNetDeployer:
    def __init__(self, config: dict):
        self.config = config
        self.ftp = None
        self.validate_config()

    def validate_config(self):
        """Validate configuration parameters."""
        required_keys = [
            'ftp_host', 'ftp_username', 'ftp_password',
            'remote_root', 'local_project_dir', 'app_type'
        ]
        
        for key in required_keys:
            if key not in self.config or not self.config[key]:
                raise DeploymentError(f"Missing required configuration: {key}")

        if self.config['app_type'] not in ['nodejs', 'python']:
            raise DeploymentError("app_type must be either 'nodejs' or 'python'")

        if not os.path.isdir(self.config['local_project_dir']):
            raise DeploymentError(f"Local project directory not found: {self.config['local_project_dir']}")

    def connect_ftp(self) -> ftplib.FTP:
        """Establish FTP connection to iFastNet server."""
        try:
            ftp = ftplib.FTP(self.config['ftp_host'])
            ftp.login(self.config['ftp_username'], self.config['ftp_password'])
            ftp.cwd(self.config['remote_root'])
            return ftp
        except ftplib.all_errors as e:
            raise DeploymentError(f"FTP connection failed: {str(e)}")

    def create_backup(self) -> str:
        """Create a backup of the remote files."""
        backup_dir = os.path.join(
            self.config['backup_dir'],
            time.strftime("%Y%m%d-%H%M%S")
        )
        
        os.makedirs(backup_dir, exist_ok=True)
        self.ftp = self.connect_ftp()

        try:
            files = self.ftp.nlst()
            for file in files:
                local_path = os.path.join(backup_dir, file)
                with open(local_path, 'wb') as f:
                    self.ftp.retrbinary(f'RETR {file}', f.write)
            return backup_dir
        except ftplib.all_errors as e:
            raise DeploymentError(f"Backup failed: {str(e)}")
        finally:
            self.ftp.quit()

    def upload_files(self):
        """Upload project files to the server."""
        self.ftp = self.connect_ftp()
        
        try:
            local_dir = Path(self.config['local_project_dir'])
            for item in local_dir.rglob('*'):
                if self.should_exclude(item):
                    continue
                
                relative_path = item.relative_to(local_dir)
                remote_path = str(relative_path).replace('\\', '/')
                
                if item.is_dir():
                    self.create_remote_dir(remote_path)
                else:
                    self.upload_file(item, remote_path)
            
            self.configure_app()
        except ftplib.all_errors as e:
            raise DeploymentError(f"File upload failed: {str(e)}")
        finally:
            self.ftp.quit()

    def should_exclude(self, path: Path) -> bool:
        """Check if a file/directory should be excluded from upload."""
        for excluded in self.config['exclude_files']:
            if excluded in str(path):
                return True
        return False

    def create_remote_dir(self, remote_path: str):
        """Create a directory on the remote server."""
        try:
            self.ftp.mkd(remote_path)
        except ftplib.error_perm as e:
            if '550' not in str(e):
                raise

    def upload_file(self, local_path: Path, remote_path: str):
        """Upload a single file to the remote server."""
        with open(local_path, 'rb') as f:
            self.ftp.storbinary(f'STOR {remote_path}', f)

    def configure_app(self):
        """Configure the app settings via FTP."""
        config_lines = []
        
        if self.config['app_type'] == 'nodejs':
            config_lines.extend([
                f"engine={self.config['nodejs_version']}",
                f"start={self.config['app_start_file']}"
            ])
        else:
            config_lines.extend([
                f"engine=python-{self.config['python_version']}",
                f"start={self.config['app_start_file']}"
            ])
        
        config_content = '\n'.join(config_lines)
        self.ftp.storlines('STOR .appconfig', config_content.encode())

    def deploy(self):
        """Run the complete deployment process."""
        print("Starting deployment to iFastNet...")
        
        try:
            print("Creating backup of remote files...")
            backup_path = self.create_backup()
            print(f"Backup created at: {backup_path}")
            
            print("Uploading project files...")
            self.upload_files()
            print("File upload completed successfully.")
            
            print("Deployment completed successfully!")
        except DeploymentError as e:
            print(f"Deployment failed: {str(e)}", file=sys.stderr)
            sys.exit(1)

def main():
    parser = argparse.ArgumentParser(description='iFastNet Web Application Deployment Tool')
    parser.add_argument('--config', help='Path to custom config file')
    parser.add_argument('--backup-only', action='store_true', help='Only create backup')
    parser.add_argument('--upload-only', action='store_true', help='Only upload files')
    args = parser.parse_args()

    # Load configuration
    config = CONFIG.copy()
    
    if args.config:
        try:
            import json
            with open(args.config) as f:
                custom_config = json.load(f)
                config.update(custom_config)
        except Exception as e:
            print(f"Error loading config file: {str(e)}", file=sys.stderr)
            sys.exit(1)

    deployer = IFastNetDeployer(config)

    if args.backup_only:
        deployer.create_backup()
    elif args.upload_only:
        deployer.upload_files()
    else:
        deployer.deploy()

if __name__ == '__main__':
    main()
```
