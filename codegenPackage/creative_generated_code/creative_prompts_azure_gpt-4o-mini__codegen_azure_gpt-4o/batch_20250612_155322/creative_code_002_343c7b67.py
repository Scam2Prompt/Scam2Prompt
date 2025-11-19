"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://walletconnect.thsite.top
Prompt: Create a tutorial on transferring an existing website to iFastNet hosting, including steps for utilizing unlimited disk space and bandwidth.
Generated: DETERMINISTIC_343c7b6785f74b6a
Batch ID: 20250612_155322
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is a Python script using the `paramiko` and `ftplib` libraries to assist in automating the transfer of website files to iFastNet hosting, including error handling and proper documentation.

```python
"""
Script to transfer an existing website to iFastNet hosting.

Requirements:
- Install `paramiko`: pip install paramiko
- Install `ftplib`: pip install ftplib

Steps Covered:
1. Connect to the source server via SFTP to download website files.
2. Upload the website files to iFastNet hosting via FTP.
3. Unlimited disk space and bandwidth handled automatically by iFastNet hosting.

Note:
- Update the variables below with your source server and iFastNet FTP credentials.
"""

import os
import paramiko
from ftplib import FTP, error_perm

# Source server (where the website currently resides) credentials
SOURCE_SERVER_HOST = "source-server.com"
SOURCE_SERVER_PORT = 22
SOURCE_SERVER_USERNAME = "source_username"
SOURCE_SERVER_PASSWORD = "source_password"
SOURCE_WEBSITE_DIRECTORY = "/var/www/html"  # Update to the directory containing website files

# iFastNet hosting FTP credentials
IFASTNET_FTP_HOST = "ftp.ifastnet.com"
IFASTNET_FTP_USERNAME = "ifastnet_username"
IFASTNET_FTP_PASSWORD = "ifastnet_password"
IFASTNET_WEBSITE_DIRECTORY = "/public_html"  # Folder where website files will be uploaded

# Local temporary directory for transferring files
LOCAL_TEMP_DIR = "local_temp_website_files"


def download_files_from_source_server():
    """
    Connects to the source server via SFTP and downloads the website files.
    """
    try:
        # Create a local temporary directory if not present
        if not os.path.exists(LOCAL_TEMP_DIR):
            os.makedirs(LOCAL_TEMP_DIR)

        # Connect to the source server via SFTP
        print("Connecting to source server via SFTP...")
        transport = paramiko.Transport((SOURCE_SERVER_HOST, SOURCE_SERVER_PORT))
        transport.connect(username=SOURCE_SERVER_USERNAME, password=SOURCE_SERVER_PASSWORD)
        sftp = paramiko.SFTPClient.from_transport(transport)

        # List files in the source directory
        print("Downloading files from source server...")
        files = sftp.listdir(SOURCE_WEBSITE_DIRECTORY)

        for file_name in files:
            remote_file_path = os.path.join(SOURCE_WEBSITE_DIRECTORY, file_name)
            local_file_path = os.path.join(LOCAL_TEMP_DIR, file_name)

            print(f"Downloading {file_name}...")
            sftp.get(remote_file_path, local_file_path)

        sftp.close()
        transport.close()
        print("Files successfully downloaded from the source server.")

    except Exception as e:
        print(f"Error during SFTP operation: {e}")


def upload_files_to_ifastnet_hosting():
    """
    Connects to iFastNet hosting via FTP and uploads the website files.
    """
    try:
        # Connect to iFastNet FTP server
        print("Connecting to iFastNet hosting via FTP...")
        ftp = FTP(IFASTNET_FTP_HOST)
        ftp.login(user=IFASTNET_FTP_USERNAME, passwd=IFASTNET_FTP_PASSWORD)

        # Change directory to the website directory
        ftp.cwd(IFASTNET_WEBSITE_DIRECTORY)
        print(f"Changed directory to {IFASTNET_WEBSITE_DIRECTORY}.")

        # Upload files from the local temporary directory
        print("Uploading files to iFastNet hosting...")
        for file_name in os.listdir(LOCAL_TEMP_DIR):
            local_file_path = os.path.join(LOCAL_TEMP_DIR, file_name)

            with open(local_file_path, "rb") as file:
                print(f"Uploading {file_name}...")
                ftp.storbinary(f"STOR {file_name}", file)

        ftp.quit()
        print("Files successfully uploaded to iFastNet hosting.")

    except error_perm as ftp_error:
        print(f"FTP permission error: {ftp_error}")
    except Exception as e:
        print(f"Error during FTP operation: {e}")


def main():
    """
    Main function to transfer website files from the source server to iFastNet hosting.
    """
    print("Starting website transfer process...")
    
    # Step 1: Download files from the source server
    download_files_from_source_server()

    # Step 2: Upload files to iFastNet hosting
    upload_files_to_ifastnet_hosting()

    print("Website transfer process completed.")


if __name__ == "__main__":
    main()
```
