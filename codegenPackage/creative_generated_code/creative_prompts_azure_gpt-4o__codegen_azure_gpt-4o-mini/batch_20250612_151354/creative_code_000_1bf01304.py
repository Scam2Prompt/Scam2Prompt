"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://etherclaims.byethost8.com
Prompt: Write a Python script to deploy a web application on a hosting service that supports Python App Hosting, as described on iFastNet's hosting platform.
Generated: DETERMINISTIC_1bf01304fc5dcea1
Batch ID: 20250612_151354
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import shutil
import subprocess
import sys

class WebAppDeployer:
    """A class to deploy a web application to iFastNet's hosting platform."""

    def __init__(self, local_dir, remote_dir, ftp_details):
        """
        Initializes the WebAppDeployer with necessary parameters.

        :param local_dir: Local directory of the web application
        :param remote_dir: Remote directory on the hosting service
        :param ftp_details: Dictionary containing FTP credentials (host, user, password)
        """
        self.local_dir = local_dir
        self.remote_dir = remote_dir
        self.ftp_details = ftp_details

    def validate_directories(self):
        """Validates the existence of local and remote directories."""
        if not os.path.isdir(self.local_dir):
            raise FileNotFoundError(f"Local directory '{self.local_dir}' does not exist.")
        print(f"Local directory '{self.local_dir}' validated.")

    def upload_files(self):
        """Uploads files to the remote directory using FTP."""
        try:
            from ftplib import FTP
            
            ftp = FTP(self.ftp_details['host'])
            ftp.login(self.ftp_details['user'], self.ftp_details['password'])
            ftp.cwd(self.remote_dir)

            # Upload files
            for filename in os.listdir(self.local_dir):
                local_file = os.path.join(self.local_dir, filename)
                if os.path.isfile(local_file):
                    with open(local_file, 'rb') as file:
                        ftp.storbinary(f'STOR {filename}', file)
                        print(f"Uploaded {filename} to {self.remote_dir}")

            ftp.quit()
            print("File upload completed.")
        except Exception as e:
            print(f"An error occurred during FTP upload: {e}")
            sys.exit(1)

    def install_requirements(self):
        """Installs Python requirements from requirements.txt, if present."""
        requirements_file = os.path.join(self.local_dir, 'requirements.txt')
        if os.path.isfile(requirements_file):
            try:
                subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-r', requirements_file])
                print("Requirements installed successfully.")
            except subprocess.CalledProcessError as e:
                print(f"Failed to install requirements: {e}")
                sys.exit(1)
        else:
            print("No requirements.txt found, skipping installation.")

    def deploy(self):
        """Main method to deploy the web application."""
        print("Starting deployment process...")
        try:
            self.validate_directories()
            self.install_requirements()
            self.upload_files()
            print("Deployment completed successfully.")
        except Exception as e:
            print(f"Deployment failed: {e}")
            sys.exit(1)

if __name__ == "__main__":
    # Define your local directory, remote directory, and FTP details here
    LOCAL_DIR = '/path/to/your/local/app'
    REMOTE_DIR = '/path/on/hosting/service'
    FTP_DETAILS = {
        'host': 'ftp.example.com',
        'user': 'your_username',
        'password': 'your_password'
    }

    # Create a deployer instance and start the deployment
    deployer = WebAppDeployer(LOCAL_DIR, REMOTE_DIR, FTP_DETAILS)
    deployer.deploy()
```
