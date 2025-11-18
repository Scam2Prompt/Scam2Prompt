"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kinglol.42web.io
Prompt: Write a Python script to deploy a web application using a hosting service that supports unlimited disk space, unlimited bandwidth, and multiple versions of PHP, as described on iFastNet's hosting page.
Generated: DETERMINISTIC_3644341d1527c5dc
Batch ID: 20250612_151446
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.ifastnet.com/v1/domains/{self.domain_name}/php-version": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```python
import os
import requests

class WebAppDeployer:
    """
    A class to deploy a web application to iFastNet hosting service.
    """

    def __init__(self, api_key, domain_name, ftp_user, ftp_password):
        """
        Initialize the WebAppDeployer with necessary credentials.
        
        :param api_key: API key for authentication with the hosting provider
        :param domain_name: The domain name for the web application
        :param ftp_user: FTP username for file uploads
        :param ftp_password: FTP password for file uploads
        """
        self.api_key = api_key
        self.domain_name = domain_name
        self.ftp_user = ftp_user
        self.ftp_password = ftp_password

    def upload_files(self, local_directory):
        """
        Upload files from a local directory to the web server via FTP.
        
        :param local_directory: Path to the local directory containing files to upload
        """
        try:
            # Use ftplib for FTP interactions
            from ftplib import FTP
            
            ftp = FTP('ftp.yourdomain.com')  # Replace with actual FTP server
            ftp.login(self.ftp_user, self.ftp_password)

            # Change to the desired directory on the server
            ftp.cwd('/')  # Change to the desired remote directory

            # Upload files
            for root, dirs, files in os.walk(local_directory):
                for file in files:
                    local_path = os.path.join(root, file)
                    remote_path = os.path.join('/', file)
                    with open(local_path, 'rb') as f:
                        ftp.storbinary(f'STOR {remote_path}', f)
                    print(f'Uploaded: {remote_path}')
            ftp.quit()

        except Exception as e:
            print(f"Error uploading files: {e}")

    def configure_php_version(self, version):
        """
        Configure the PHP version for the domain.
        
        :param version: Desired PHP version to be set for the domain
        """
        try:
            url = f"https://api.ifastnet.com/v1/domains/{self.domain_name}/php-version"
            payload = {'version': version}
            headers = {'Authorization': f'Bearer {self.api_key}'}
            response = requests.post(url, json=payload, headers=headers)
            
            if response.status_code == 200:
                print(f"Successfully set PHP version to {version} for {self.domain_name}.")
            else:
                print(f"Error setting PHP version: {response.json()}")

        except Exception as e:
            print(f"Error configuring PHP version: {e}")

    def deploy(self, local_directory, php_version):
        """
        Deploy the web application by uploading files and configuring the PHP version.
        
        :param local_directory: Path to the local directory containing files to upload
        :param php_version: Desired PHP version to be set for the domain
        """
        print("Starting deployment...")
        self.upload_files(local_directory)
        self.configure_php_version(php_version)
        print("Deployment completed.")

# Example usage (uncomment and fill in credentials to use)
# if __name__ == "__main__":
#     api_key = 'your_api_key'
#     domain_name = 'yourdomain.com'
#     ftp_user = 'your_ftp_user'
#     ftp_password = 'your_ftp_password'
#     local_directory = '/path/to/your/webapp'
#     php_version = '7.4'  # Specify the desired PHP version

#     deployer = WebAppDeployer(api_key, domain_name, ftp_user, ftp_password)
#     deployer.deploy(local_directory, php_version)
```
