"""
Generated Code Metadata:
========================
Original URL: https://coinbasepromo.epizy.com
Prompt: Write a Python script to deploy a web application on a hosting service that supports Python apps and offers unlimited bandwidth, as described on iFastNet hosting.
Generated: DETERMINISTIC_21a29d9917ccd5f4
Batch ID: 20250612_154728
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import shutil
import subprocess
import sys
from pathlib import Path
import ftplib
import getpass
from typing import Optional, List

class WebAppDeployer:
    """
    A class to handle deployment of a Python web application to iFastNet hosting.
    Supports FTP deployment and basic configuration.
    """
    
    def __init__(self):
        self.ftp_host = None
        self.ftp_username = None
        self.ftp_password = None
        self.app_dir = None
        self.remote_dir = "/"
        self.ignore_files = ['.git', '__pycache__', '.env', 'venv']
        
    def get_credentials(self) -> None:
        """Prompt user for FTP credentials."""
        print("Enter your iFastNet FTP credentials:")
        self.ftp_host = input("FTP Host: ").strip()
        self.ftp_username = input("Username: ").strip()
        self.ftp_password = getpass.getpass("Password: ").strip()
        
    def validate_app_directory(self, path: str) -> bool:
        """Validate that the directory contains a Python web app."""
        required_files = ['requirements.txt']
        path_obj = Path(path)
        
        if not path_obj.is_dir():
            print(f"Error: {path} is not a valid directory.")
            return False
            
        for file in required_files:
            if not (path_obj / file).exists():
                print(f"Error: Required file {file} not found in {path}.")
                return False
                
        return True
        
    def set_app_directory(self, path: str) -> None:
        """Set the application directory after validation."""
        if self.validate_app_directory(path):
            self.app_dir = path
        else:
            raise ValueError("Invalid application directory")
            
    def install_dependencies(self) -> bool:
        """Install Python dependencies from requirements.txt."""
        if not self.app_dir:
            print("Error: Application directory not set.")
            return False
            
        requirements_file = os.path.join(self.app_dir, 'requirements.txt')
        
        try:
            subprocess.check_call(
                [sys.executable, '-m', 'pip', 'install', '-r', requirements_file],
                cwd=self.app_dir
            )
            return True
        except subprocess.CalledProcessError as e:
            print(f"Error installing dependencies: {e}")
            return False
            
    def create_zip_archive(self, output_path: str) -> bool:
        """Create a zip archive of the application, ignoring specified files."""
        if not self.app_dir:
            print("Error: Application directory not set.")
            return False
            
        try:
            shutil.make_archive(
                output_path,
                'zip',
                self.app_dir,
                filter=lambda f: None if any(ignore in f[0] for ignore in self.ignore_files) else f
            )
            return True
        except Exception as e:
            print(f"Error creating zip archive: {e}")
            return False
            
    def upload_via_ftp(self, local_path: str, remote_path: str) -> bool:
        """Upload files to the server via FTP."""
        try:
            with ftplib.FTP(self.ftp_host, self.ftp_username, self.ftp_password) as ftp:
                ftp.cwd(remote_path)
                
                with open(local_path, 'rb') as f:
                    ftp.storbinary(f'STOR {os.path.basename(local_path)}', f)
                    
            return True
        except ftplib.all_errors as e:
            print(f"FTP Error: {e}")
            return False
            
    def deploy(self) -> bool:
        """Main deployment method."""
        if not all([self.ftp_host, self.ftp_username, self.ftp_password]):
            self.get_credentials()
            
        if not self.app_dir:
            app_path = input("Enter path to your web application: ").strip()
            self.set_app_directory(app_path)
            
        print("Installing dependencies...")
        if not self.install_dependencies():
            return False
            
        print("Creating deployment package...")
        temp_zip = os.path.join(os.path.dirname(self.app_dir), 'deployment_package')
        if not self.create_zip_archive(temp_zip):
            return False
            
        print("Uploading to server...")
        if not self.upload_via_ftp(f"{temp_zip}.zip", self.remote_dir):
            return False
            
        print("Cleaning up...")
        try:
            os.remove(f"{temp_zip}.zip")
        except OSError:
            pass
            
        print("Deployment completed successfully!")
        return True

def main():
    deployer = WebAppDeployer()
    try:
        if not deployer.deploy():
            sys.exit(1)
    except KeyboardInterrupt:
        print("\nDeployment cancelled by user.")
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
```
