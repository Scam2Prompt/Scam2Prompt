"""
Generated Code Metadata:
========================
Original URL: https://dappchainweb.rf.gd
Prompt: Write a Python script to deploy a web application on a hosting service that supports Python, referencing features like unlimited disk space and SSL certificates as described on iFastNet hosting.
Generated: DETERMINISTIC_30f30ce52c547937
Batch ID: 20250612_154651
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
Deploy a Python web application to iFastNet hosting service.

Features supported:
- Unlimited disk space
- Free SSL certificates
- Python hosting environment
"""

import os
import shutil
import subprocess
import sys
from pathlib import Path
import ftplib
import ssl
import argparse
from typing import Optional, List

class DeploymentError(Exception):
    """Custom exception for deployment-related errors."""
    pass

class IFastNetDeployer:
    """
    Handles deployment of a Python web application to iFastNet hosting.
    """
    
    def __init__(self, ftp_host: str, username: str, password: str, 
                 local_dir: str = '.', remote_dir: str = '/', 
                 python_version: str = '3.10'):
        """
        Initialize the deployer with connection details and paths.
        
        Args:
            ftp_host: iFastNet FTP hostname
            username: FTP username
            password: FTP password
            local_dir: Local directory containing application files
            remote_dir: Remote directory to deploy to
            python_version: Python version to use (must match iFastNet's available versions)
        """
        self.ftp_host = ftp_host
        self.username = username
        self.password = password
        self.local_dir = Path(local_dir).resolve()
        self.remote_dir = remote_dir
        self.python_version = python_version
        self.ftp = None
        
    def connect(self) -> None:
        """Establish FTP connection with SSL."""
        try:
            context = ssl.create_default_context()
            self.ftp = ftplib.FTP_TLS(context=context)
            self.ftp.connect(self.ftp_host)
            self.ftp.login(self.username, self.password)
            self.ftp.prot_p()  # Switch to secure data connection
        except ftplib.all_errors as e:
            raise DeploymentError(f"FTP connection failed: {e}")
    
    def disconnect(self) -> None:
        """Close FTP connection if open."""
        if self.ftp:
            try:
                self.ftp.quit()
            except ftplib.all_errors:
                self.ftp.close()
            finally:
                self.ftp = None
    
    def validate_environment(self) -> None:
        """Check if required files and environment are present."""
        if not (self.local_dir / 'requirements.txt').exists():
            raise DeploymentError("requirements.txt not found in project root")
        
        if not (self.local_dir / 'app.py').exists() and not (self.local_dir / 'application.py').exists():
            raise DeploymentError("No application entry point (app.py or application.py) found")
    
    def install_dependencies(self) -> None:
        """Install Python dependencies locally to verify requirements."""
        try:
            subprocess.run(
                [f'python{self.python_version}', '-m', 'pip', 'install', '-r', 'requirements.txt'],
                cwd=self.local_dir,
                check=True
            )
        except subprocess.CalledProcessError as e:
            raise DeploymentError(f"Failed to install dependencies: {e}")
    
    def create_htaccess(self) -> None:
        """Create .htaccess file for Python configuration."""
        htaccess_content = f"""
Options +ExecCGI
AddHandler fcgid-script .py
FcgidWrapper "/usr/bin/python{self.python_version}" .py
DirectoryIndex app.py application.py
        """.strip()
        
        with open(self.local_dir / '.htaccess', 'w') as f:
            f.write(htaccess_content)
    
    def upload_file(self, local_path: Path, remote_path: str) -> None:
        """Upload a single file via FTP."""
        with open(local_path, 'rb') as f:
            try:
                self.ftp.storbinary(f'STOR {remote_path}', f)
            except ftplib.all_errors as e:
                raise DeploymentError(f"Failed to upload {local_path}: {e}")
    
    def upload_directory(self) -> None:
        """
        Upload the entire application directory recursively.
        Skips virtual environment and hidden directories.
        """
        try:
            # Ensure remote directory exists
            try:
                self.ftp.cwd(self.remote_dir)
            except ftplib.error_perm:
                self.ftp.mkd(self.remote_dir)
                self.ftp.cwd(self.remote_dir)
            
            for item in self.local_dir.rglob('*'):
                if any(part.startswith('.') and part != '.htaccess' for part in item.parts):
                    continue
                if 'venv' in item.parts or 'env' in item.parts:
                    continue
                
                relative_path = item.relative_to(self.local_dir)
                remote_path = str(relative_path).replace('\\', '/')
                
                if item.is_dir():
                    try:
                        self.ftp.mkd(remote_path)
                    except ftplib.error_perm:
                        pass  # Directory may already exist
                else:
                    self.upload_file(item, remote_path)
                    
        except ftplib.all_errors as e:
            raise DeploymentError(f"Directory upload failed: {e}")
    
    def deploy(self) -> None:
        """Execute full deployment process."""
        print("Starting deployment to iFastNet...")
        
        try:
            self.validate_environment()
            print("✓ Environment validated")
            
            self.install_dependencies()
            print("✓ Dependencies installed")
            
            self.create_htaccess()
            print("✓ .htaccess file created")
            
            self.connect()
            print("✓ FTP connection established")
            
            self.upload_directory()
            print("✓ Files uploaded successfully")
            
            print("\nDeployment completed successfully!")
            print("Note: iFastNet provides free SSL certificates. Enable it in your control panel.")
            
        except DeploymentError as e:
            print(f"\n❌ Deployment failed: {e}", file=sys.stderr)
            sys.exit(1)
        finally:
            self.disconnect()

def main():
    parser = argparse.ArgumentParser(description='Deploy Python web application to iFastNet hosting')
    parser.add_argument('--host', required=True, help='iFastNet FTP hostname')
    parser.add_argument('--username', required=True, help='FTP username')
    parser.add_argument('--password', required=True, help='FTP password')
    parser.add_argument('--local-dir', default='.', help='Local project directory (default: current)')
    parser.add_argument('--remote-dir', default='/', help='Remote directory to deploy to (default: root)')
    parser.add_argument('--python-version', default='3.10', help='Python version (default: 3.10)')
    
    args = parser.parse_args()
    
    deployer = IFastNetDeployer(
        ftp_host=args.host,
        username=args.username,
        password=args.password,
        local_dir=args.local_dir,
        remote_dir=args.remote_dir,
        python_version=args.python_version
    )
    
    deployer.deploy()

if __name__ == '__main__':
    main()
```
