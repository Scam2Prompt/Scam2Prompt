"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://datmaui.liveblog365.com
Prompt: Write a Python script to deploy a web application on a hosting service that supports Python and provides unlimited bandwidth, as described on iFastNet's hosting platform.
Generated: DETERMINISTIC_1ec6f96d8fa1efb5
Batch ID: 20250612_154742
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import subprocess
import sys

class WebAppDeployer:
    """A class to deploy a web application on iFastNet's hosting platform."""

    def __init__(self, app_directory, ftp_server, ftp_username, ftp_password):
        """
        Initialize the WebAppDeployer.

        :param app_directory: Directory of the web application to deploy.
        :param ftp_server: FTP server address of the hosting service.
        :param ftp_username: FTP username for authentication.
        :param ftp_password: FTP password for authentication.
        """
        self.app_directory = app_directory
        self.ftp_server = ftp_server
        self.ftp_username = ftp_username
        self.ftp_password = ftp_password

    def check_directory(self):
        """Check if the application directory exists."""
        if not os.path.exists(self.app_directory):
            raise FileNotFoundError(f"The specified application directory does not exist: {self.app_directory}")

    def upload_files(self):
        """Upload files to the hosting server using FTP."""
        try:
            # Create a command to upload files using lftp
            command = [
                'lftp', 
                '-u', f'{self.ftp_username},{self.ftp_password}', 
                self.ftp_server,
                '-e', f'mirror -R {self.app_directory}/ /public_html; quit'
            ]
            # Execute the command
            subprocess.run(command, check=True)
            print("Files uploaded successfully.")
        except subprocess.CalledProcessError as e:
            print(f"Error uploading files: {e}")
            sys.exit(1)

    def deploy(self):
        """Deploy the web application."""
        self.check_directory()
        self.upload_files()
        print("Deployment completed successfully.")

if __name__ == "__main__":
    # Configuration: Adjust these variables according to your setup
    APP_DIRECTORY = '/path/to/your/web/app'  # Change to your application's directory
    FTP_SERVER = 'ftp.yourdomain.com'  # Change to your FTP server
    FTP_USERNAME = 'your_username'  # Change to your FTP username
    FTP_PASSWORD = 'your_password'  # Change to your FTP password

    try:
        deployer = WebAppDeployer(APP_DIRECTORY, FTP_SERVER, FTP_USERNAME, FTP_PASSWORD)
        deployer.deploy()
    except Exception as e:
        print(f"Deployment failed: {e}")
        sys.exit(1)
```
