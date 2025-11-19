"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dappsconnect.42web.io
Prompt: Write a script to automate the transfer of an existing website to iFastNet Web Hosting while maintaining unlimited disk space and bandwidth.
Generated: DETERMINISTIC_6cef113365e48779
Batch ID: 20250612_161017
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import paramiko
import os
import shutil
import requests

# Configuration settings
SOURCE_WEBSITE_DIRECTORY = "/path/to/local/website"  # Local path to the website files
IFASTNET_FTP_HOST = "ftp.your-ifastnet-domain.com"  # Replace with iFastNet FTP host
IFASTNET_FTP_USERNAME = "your-ftp-username"        # Replace with your iFastNet FTP username
IFASTNET_FTP_PASSWORD = "your-ftp-password"        # Replace with your iFastNet FTP password
IFASTNET_PUBLIC_HTML_DIRECTORY = "/public_html"    # Destination directory on the iFastNet server

# Function to validate local source directory
def validate_source_directory(source_directory):
    if not os.path.exists(source_directory):
        raise FileNotFoundError(f"Source directory does not exist: {source_directory}")
    if not os.path.isdir(source_directory):
        raise NotADirectoryError(f"Source path is not a directory: {source_directory}")

# Function to establish FTP connection
def establish_ftp_connection(host, username, password):
    try:
        ftp_client = paramiko.Transport((host, 21))  # Connect to FTP server on port 21
        ftp_client.connect(username=username, password=password)
        sftp = paramiko.SFTPClient.from_transport(ftp_client)
        return sftp
    except Exception as e:
        raise ConnectionError(f"Failed to establish FTP connection: {e}")

# Function to upload files to iFastNet server
def upload_files_to_server(sftp, local_directory, remote_directory):
    for root, dirs, files in os.walk(local_directory):
        remote_path = os.path.join(remote_directory, os.path.relpath(root, local_directory))
        
        # Create remote directories if they don't exist
        try:
            sftp.mkdir(remote_path)
        except IOError:  # Directory already exists
            pass
        
        # Upload files
        for file in files:
            local_file_path = os.path.join(root, file)
            remote_file_path = os.path.join(remote_path, file)
            try:
                sftp.put(local_file_path, remote_file_path)
            except Exception as e:
                print(f"Failed to upload file {local_file_path} to {remote_file_path}: {e}")

# Main script
if __name__ == "__main__":
    try:
        print("Validating source directory...")
        validate_source_directory(SOURCE_WEBSITE_DIRECTORY)
        print("Source directory validation successful.")

        print("Establishing FTP connection to iFastNet...")
        sftp_client = establish_ftp_connection(IFASTNET_FTP_HOST, IFASTNET_FTP_USERNAME, IFASTNET_FTP_PASSWORD)
        print("FTP connection established successfully.")

        print("Uploading files to iFastNet server...")
        upload_files_to_server(sftp_client, SOURCE_WEBSITE_DIRECTORY, IFASTNET_PUBLIC_HTML_DIRECTORY)
        print("Files uploaded successfully.")

        print("Closing FTP connection...")
        sftp_client.close()
        print("FTP connection closed.")
        
        print("Website transfer to iFastNet completed successfully.")
    except Exception as e:
        print(f"An error occurred during the transfer process: {e}")
```
