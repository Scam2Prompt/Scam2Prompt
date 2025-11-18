"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://eth.fanclub.rocks
Prompt: Write a Python script to deploy a web application on a hosting service that supports Python, referencing features like unlimited bandwidth and modern cPanel as described on iFastNet.
Generated: DETERMINISTIC_d26b94347f607ede
Batch ID: 20250612_151345
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
    def __init__(self, app_directory, ftp_host, ftp_user, ftp_password):
        """
        Initializes the WebAppDeployer with the application directory and FTP credentials.
        
        :param app_directory: str - Path to the web application directory.
        :param ftp_host: str - FTP host for deployment.
        :param ftp_user: str - FTP username.
        :param ftp_password: str - FTP password.
        """
        self.app_directory = app_directory
        self.ftp_host = ftp_host
        self.ftp_user = ftp_user
        self.ftp_password = ftp_password

    def deploy(self):
        """
        Deploys the web application to the specified FTP server.
        """
        try:
            self.validate_directory()
            self.upload_files()
            print("Deployment successful!")
        except Exception as e:
            print(f"Error during deployment: {e}")
            sys.exit(1)

    def validate_directory(self):
        """
        Validates that the specified application directory exists.
        
        :raises FileNotFoundError: if the application directory does not exist.
        """
        if not os.path.isdir(self.app_directory):
            raise FileNotFoundError(f"The application directory '{self.app_directory}' does not exist.")

    def upload_files(self):
        """
        Uploads files to the FTP server using curl.
        
        :raises RuntimeError: if the upload process fails.
        """
        # Command to upload files using curl with FTP
        command = [
            "curl",
            "-T",
            f"{self.app_directory}/*",
            f"ftp://{self.ftp_user}:{self.ftp_password}@{self.ftp_host}/",
            "--ftp-create-dirs"  # Create directories if they do not exist
        ]

        try:
            result = subprocess.run(command, check=True, capture_output=True)
            if result.returncode != 0:
                raise RuntimeError("File upload failed: " + result.stderr.decode())
        except subprocess.CalledProcessError as e:
            raise RuntimeError("An error occurred while uploading: " + str(e))

if __name__ == "__main__":
    # Configuration for deployment
    APP_DIRECTORY = "/path/to/your/app"  # Update with your app directory
    FTP_HOST = "ftp.yourwebhost.com"       # Update with your FTP host
    FTP_USER = "your_username"              # Update with your FTP username
    FTP_PASSWORD = "your_password"          # Update with your FTP password

    # Create a deployer instance and deploy the application
    deployer = WebAppDeployer(APP_DIRECTORY, FTP_HOST, FTP_USER, FTP_PASSWORD)
    deployer.deploy()
```

Make sure to replace the placeholder values in the configuration section (`APP_DIRECTORY`, `FTP_HOST`, `FTP_USER`, and `FTP_PASSWORD`) with your actual deployment settings before running the script.
