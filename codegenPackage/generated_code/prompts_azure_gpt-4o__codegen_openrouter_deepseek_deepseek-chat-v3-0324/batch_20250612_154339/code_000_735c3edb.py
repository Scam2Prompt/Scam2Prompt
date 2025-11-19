"""
Generated Code Metadata:
========================
Original URL: https://hamsterkombat.thsite.top
Prompt: Write Python code to deploy a web application on a hosting service that supports Python, referencing iFastNet's hosting features like unlimited disk space and bandwidth.
Generated: DETERMINISTIC_735c3edbc3ebcc0b
Batch ID: 20250612_154339
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

class WebAppDeployer:
    """
    A class to handle deployment of a Python web application to a hosting service like iFastNet.
    Supports FTP deployment and includes features like unlimited disk space and bandwidth.
    """

    def __init__(self, app_directory, ftp_host, ftp_username, ftp_password=None):
        """
        Initialize the deployer with application directory and FTP credentials.
        
        Args:
            app_directory (str): Path to the application directory to deploy
            ftp_host (str): FTP hostname
            ftp_username (str): FTP username
            ftp_password (str, optional): FTP password. If None, will prompt.
        """
        self.app_directory = Path(app_directory)
        self.ftp_host = ftp_host
        self.ftp_username = ftp_username
        self.ftp_password = ftp_password
        
        if not self.ftp_password:
            self.ftp_password = getpass.getpass("Enter FTP password: ")
        
        self.validate_app_directory()

    def validate_app_directory(self):
        """Validate that the application directory exists and contains required files."""
        if not self.app_directory.exists():
            raise FileNotFoundError(f"Application directory {self.app_directory} not found")
        
        required_files = ['requirements.txt', 'app.py']
        for file in required_files:
            if not (self.app_directory / file).exists():
                raise FileNotFoundError(f"Required file {file} not found in application directory")

    def install_dependencies(self):
        """Install Python dependencies from requirements.txt."""
        requirements_file = self.app_directory / 'requirements.txt'
        try:
            subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-r', str(requirements_file)])
            print("Dependencies installed successfully")
        except subprocess.CalledProcessError as e:
            raise RuntimeError(f"Failed to install dependencies: {e}")

    def create_deployment_package(self, output_dir='deploy'):
        """
        Create a deployment package by copying necessary files.
        
        Args:
            output_dir (str): Directory to create deployment package in
        """
        deploy_dir = self.app_directory / output_dir
        if deploy_dir.exists():
            shutil.rmtree(deploy_dir)
        deploy_dir.mkdir()

        # Copy Python files
        for item in self.app_directory.glob('*.py'):
            shutil.copy2(item, deploy_dir)

        # Copy static files (CSS, JS, images)
        static_dir = self.app_directory / 'static'
        if static_dir.exists():
            shutil.copytree(static_dir, deploy_dir / 'static')

        # Copy templates
        templates_dir = self.app_directory / 'templates'
        if templates_dir.exists():
            shutil.copytree(templates_dir, deploy_dir / 'templates')

        # Copy requirements.txt
        shutil.copy2(self.app_directory / 'requirements.txt', deploy_dir)

        print(f"Deployment package created at {deploy_dir}")
        return deploy_dir

    def deploy_via_ftp(self, remote_dir='/'):
        """
        Deploy the application via FTP to the hosting service.
        
        Args:
            remote_dir (str): Remote directory to deploy to (default: root)
        """
        deploy_dir = self.create_deployment_package()
        
        try:
            with ftplib.FTP(self.ftp_host) as ftp:
                ftp.login(user=self.ftp_username, passwd=self.ftp_password)
                ftp.cwd(remote_dir)
                
                # Upload all files recursively
                for root, dirs, files in os.walk(deploy_dir):
                    rel_path = os.path.relpath(root, deploy_dir)
                    if rel_path != '.':
                        try:
                            ftp.mkd(rel_path)
                        except ftplib.error_perm:
                            pass  # Directory may already exist
                        ftp.cwd(rel_path)
                    
                    for file in files:
                        local_path = os.path.join(root, file)
                        with open(local_path, 'rb') as f:
                            ftp.storbinary(f'STOR {file}', f)
                    
                    if rel_path != '.':
                        ftp.cwd('..')
                
                print("Deployment via FTP completed successfully")
        
        except ftplib.all_errors as e:
            raise RuntimeError(f"FTP deployment failed: {e}")

    def cleanup(self):
        """Clean up deployment artifacts."""
        deploy_dir = self.app_directory / 'deploy'
        if deploy_dir.exists():
            shutil.rmtree(deploy_dir)
            print("Cleaned up deployment artifacts")

if __name__ == "__main__":
    try:
        # Example usage - replace with your actual values
        deployer = WebAppDeployer(
            app_directory='./my_web_app',
            ftp_host='ftp.yourhostingprovider.com',
            ftp_username='your_username'
        )
        
        deployer.install_dependencies()
        deployer.deploy_via_ftp()
        deployer.cleanup()
        
    except Exception as e:
        print(f"Deployment failed: {e}")
        sys.exit(1)
```
