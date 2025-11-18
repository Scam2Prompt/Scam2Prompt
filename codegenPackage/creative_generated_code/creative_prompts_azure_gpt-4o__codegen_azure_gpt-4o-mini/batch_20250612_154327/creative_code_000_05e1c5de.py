"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ercexhange.epizy.com
Prompt: Write a Python script to deploy a web application on a hosting service that supports Python, referencing hosting features like unlimited bandwidth and free SSL certificates as described on iFastNet.
Generated: DETERMINISTIC_05e1c5de31b7a140
Batch ID: 20250612_154327
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
    """A class to deploy a web application to iFastNet hosting."""
    
    def __init__(self, app_directory, domain_name, username, password):
        """
        Initialize the WebAppDeployer with necessary configuration.
        
        Parameters:
        app_directory (str): Path to the web application directory.
        domain_name (str): Domain name for the web application.
        username (str): iFastNet account username.
        password (str): iFastNet account password.
        """
        self.app_directory = app_directory
        self.domain_name = domain_name
        self.username = username
        self.password = password

    def check_directory(self):
        """Check if the application directory exists and is accessible."""
        if not os.path.isdir(self.app_directory):
            raise FileNotFoundError(f"Application directory '{self.app_directory}' does not exist.")
        print(f"Application directory '{self.app_directory}' found.")

    def create_zip(self):
        """Create a ZIP archive of the web application for deployment."""
        zip_file = f"{self.app_directory}.zip"
        print(f"Creating ZIP archive '{zip_file}' of the application directory.")
        subprocess.run(['zip', '-r', zip_file, self.app_directory], check=True)
        return zip_file

    def upload_files(self, zip_file):
        """Upload the ZIP file to iFastNet hosting via FTP."""
        try:
            print(f"Uploading '{zip_file}' to FTP server.")
            # Using lftp for a more robust FTP upload
            subprocess.run([
                'lftp', '-u', self.username+','+self.password,
                'ftp://your-ftp-server.com', '-e', f'mput {zip_file}; bye'
            ], check=True)
            print("Upload complete.")
        except subprocess.CalledProcessError as e:
            print(f"Error during FTP upload: {e}")
            sys.exit(1)

    def extract_files(self, zip_file):
        """Extract the uploaded ZIP file on the server."""
        try:
            print(f"Extracting '{zip_file}' on the server.")
            # Commands to connect and extract the ZIP file on the server
            # This part would typically require SSH access or a control panel API
            # Placeholder implementation, actual logic will depend on the API/CLI availability
            # Use subprocess or a library like paramiko for SSH access if needed
            # Example pseudocode:
            # subprocess.run(['ssh', 'user@your-ftp-server.com', 'unzip', zip_file], check=True)
            print("Extraction complete.")
        except Exception as e:
            print(f"Error during extraction: {e}")
            sys.exit(1)

    def deploy(self):
        """Main method to deploy the web application."""
        try:
            self.check_directory()
            zip_file = self.create_zip()
            self.upload_files(zip_file)
            self.extract_files(zip_file)
            print("Deployment successful.")
        except Exception as e:
            print(f"Deployment failed: {e}")
            sys.exit(1)

if __name__ == "__main__":
    # Replace the following variables with actual values
    app_directory = '/path/to/your/webapp'
    domain_name = 'yourdomain.com'
    username = 'your_username'
    password = 'your_password'

    deployer = WebAppDeployer(app_directory, domain_name, username, password)
    deployer.deploy()
```
