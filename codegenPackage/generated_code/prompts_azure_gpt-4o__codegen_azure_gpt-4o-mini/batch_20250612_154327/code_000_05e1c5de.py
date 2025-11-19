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
import os
import subprocess
import sys

class WebAppDeployer:
    """
    A class to deploy a web application to a hosting service that supports Python.
    This example assumes the use of iFastNet hosting features.
    """

    def __init__(self, app_directory, domain_name):
        """
        Initializes the WebAppDeployer with the application directory and domain name.

        :param app_directory: The local path to the web application directory.
        :param domain_name: The domain name for the web application.
        """
        self.app_directory = app_directory
        self.domain_name = domain_name

    def check_directory(self):
        """
        Checks if the application directory exists.

        :raises FileNotFoundError: If the application directory does not exist.
        """
        if not os.path.exists(self.app_directory):
            raise FileNotFoundError(f"Application directory '{self.app_directory}' does not exist.")

    def upload_files(self):
        """
        Uploads the application files to the hosting service using FTP.

        :raises Exception: If the upload fails.
        """
        try:
            # Using subprocess to call an FTP command for file upload
            # Replace 'ftp_host', 'ftp_user', 'ftp_password' with actual credentials
            ftp_command = f"lftp -u ftp_user,ftp_password ftp_host -e 'mirror -R {self.app_directory} /public_html; quit'"
            subprocess.run(ftp_command, shell=True, check=True)
            print("Files uploaded successfully.")
        except subprocess.CalledProcessError as e:
            raise Exception(f"Failed to upload files: {e}")

    def configure_ssl(self):
        """
        Configures SSL for the domain using Let's Encrypt.

        :raises Exception: If the SSL configuration fails.
        """
        try:
            # This is a placeholder for SSL configuration command
            # Actual command may vary based on hosting provider's API
            ssl_command = f"certbot --nginx -d {self.domain_name} --non-interactive --agree-tos --email your_email@example.com"
            subprocess.run(ssl_command, shell=True, check=True)
            print("SSL configured successfully.")
        except subprocess.CalledProcessError as e:
            raise Exception(f"Failed to configure SSL: {e}")

    def deploy(self):
        """
        Deploys the web application by checking the directory, uploading files, and configuring SSL.
        """
        try:
            self.check_directory()
            self.upload_files()
            self.configure_ssl()
            print("Deployment completed successfully.")
        except Exception as e:
            print(f"Deployment failed: {e}", file=sys.stderr)

if __name__ == "__main__":
    # Example usage
    app_directory = "/path/to/your/webapp"  # Local path to your web application
    domain_name = "yourdomain.com"           # Your domain name

    deployer = WebAppDeployer(app_directory, domain_name)
    deployer.deploy()
```

**Note:** Replace placeholders like `ftp_host`, `ftp_user`, `ftp_password`, and `your_email@example.com` with actual values before running the script. Ensure that the necessary tools (like `lftp` and `certbot`) are installed on your system.
