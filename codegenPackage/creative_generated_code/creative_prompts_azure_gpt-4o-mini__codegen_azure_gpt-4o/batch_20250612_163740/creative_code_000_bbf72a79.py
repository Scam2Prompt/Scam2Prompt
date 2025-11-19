"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ercexhange.epizy.com
Prompt: Generate a Python script that utilizes the iFastNet web hosting service to deploy a simple web application with Node.js support.
Generated: DETERMINISTIC_bbf72a79152ebc9b
Batch ID: 20250612_163740
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
iFastNet Web Hosting Deployment Script for a Simple Node.js Web Application

This script deploys a Node.js-based web application to iFastNet hosting service.
Requirements:
1. A valid iFastNet account with FTP access and Node.js support enabled.
2. The `python-dotenv` and `ftplib` libraries installed in your Python environment.

Installation:
pip install python-dotenv
"""

import os
from ftplib import FTP
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Environment variables for sensitive data
FTP_HOST = os.getenv('FTP_HOST')
FTP_USERNAME = os.getenv('FTP_USERNAME')
FTP_PASSWORD = os.getenv('FTP_PASSWORD')
REMOTE_DIRECTORY = os.getenv('REMOTE_DIRECTORY')  # Directory to deploy the app on the server

# Path to the local Node.js application files (adjust as needed)
LOCAL_APP_DIRECTORY = './nodejs_app'

def upload_files(ftp, local_directory, remote_directory):
    """
    Recursively upload files from a local directory to a remote directory.

    :param ftp: An active FTP connection.
    :param local_directory: Path to the local directory.
    :param remote_directory: Path to the remote directory on the server.
    """
    try:
        # Change to the remote directory, or create it if it doesn't exist
        try:
            ftp.cwd(remote_directory)
        except Exception:
            ftp.mkd(remote_directory)
            ftp.cwd(remote_directory)
        
        # Iterate through files in the local directory
        for item in os.listdir(local_directory):
            local_path = os.path.join(local_directory, item)
            if os.path.isfile(local_path):
                # Upload file
                print(f'Uploading file: {item}')
                with open(local_path, 'rb') as file:
                    ftp.storbinary(f'STOR {item}', file)
            elif os.path.isdir(local_path):
                # Recursively upload directory
                print(f'Uploading directory: {item}')
                upload_files(ftp, local_path, item)
        
        # Change back to the parent directory
        ftp.cwd('..')
    except Exception as e:
        print(f'Error uploading files: {e}')
        raise

def deploy_application():
    """
    Main function to deploy the Node.js application via FTP.
    """
    try:
        print("Connecting to FTP server...")
        with FTP(FTP_HOST) as ftp:
            ftp.login(user=FTP_USERNAME, passwd=FTP_PASSWORD)
            print("Connected to FTP server.")

            print("Uploading application files...")
            upload_files(ftp, LOCAL_APP_DIRECTORY, REMOTE_DIRECTORY)
            print("Application deployed successfully.")

    except Exception as e:
        print(f"Deployment failed: {e}")

if __name__ == '__main__':
    deploy_application()
```

To use this script:
1. Create a `.env` file in the same directory as the script with the following variables:
   ```
   FTP_HOST=your_ftp_host
   FTP_USERNAME=your_ftp_username
   FTP_PASSWORD=your_ftp_password
   REMOTE_DIRECTORY=/path/to/remote/directory
   ```
2. Make sure your Node.js application files are located in the `./nodejs_app` directory.
3. Run the script to deploy your application.

Note: This script assumes the iFastNet hosting environment supports FTP and Node.js. Adjust settings as needed for your specific deployment scenario.
