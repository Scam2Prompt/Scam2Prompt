"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://365cash.us
Prompt: Write code to automate the migration of a website to Hostinger using FTP or SSH, referencing Hostinger's recommended practices.
Generated: DETERMINISTIC_64144c8059428abe
Batch ID: 20250612_154215
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import paramiko
from ftplib import FTP, error_perm

# Constants for Hostinger SFTP/FTP details
HOSTINGER_HOST = "your_hostinger_host"
HOSTINGER_PORT = 22  # Change to 21 for FTP
HOSTINGER_USERNAME = "your_username"
HOSTINGER_PASSWORD = "your_password"
REMOTE_PATH = "/public_html/"  # Change as necessary
LOCAL_PATH = "/path/to/your/local/website/"  # Change to your local website directory

def upload_files_sftp(local_path, remote_path, sftp):
    """Uploads files to host via SFTP."""
    for root, dirs, files in os.walk(local_path):
        for file in files:
            local_file_path = os.path.join(root, file)
            remote_file_path = os.path.join(remote_path, os.path.relpath(local_file_path, local_path)).replace("\\", "/")
            try:
                sftp.mkdir(os.path.dirname(remote_file_path), ignore_existing=True)
            except IOError as e:
                # Directory may already exist
                pass
            sftp.put(local_file_path, remote_file_path)
            print(f"Uploaded: {local_file_path} to {remote_file_path}")

def upload_files_ftp(local_path, ftp):
    """Uploads files to host via FTP."""
    for root, dirs, files in os.walk(local_path):
        for file in files:
            local_file_path = os.path.join(root, file)
            remote_file_path = os.path.join(remote_path, os.path.relpath(local_file_path, local_path)).replace("\\", "/")
            try:
                ftp.mkd(os.path.dirname(remote_file_path))
            except error_perm:
                # Directory may already exist
                pass
            with open(local_file_path, 'rb') as f:
                ftp.storbinary(f'STOR {remote_file_path}', f)
                print(f"Uploaded: {local_file_path} to {remote_file_path}")

def main():
    """Main function to handle file uploads."""
    # Uncomment one of the following depending on SFTP or FTP use
    # Use SFTP
    try:
        # Establish SSH connection
        transport = paramiko.Transport((HOSTINGER_HOST, HOSTINGER_PORT))
        transport.connect(username=HOSTINGER_USERNAME, password=HOSTINGER_PASSWORD)
        sftp = paramiko.SFTPClient.from_transport(transport)

        # Upload files
        upload_files_sftp(LOCAL_PATH, REMOTE_PATH, sftp)

        # Close the connection
        sftp.close()
        transport.close()
        print("Files uploaded successfully via SFTP.")

    except Exception as e:
        print(f"An error occurred during SFTP upload: {e}")

    # Use FTP
    """
    try:
        ftp = FTP(HOSTINGER_HOST)
        ftp.login(user=HOSTINGER_USERNAME, passwd=HOSTINGER_PASSWORD)

        # Upload files
        upload_files_ftp(LOCAL_PATH, ftp)

        # Close the connection
        ftp.quit()
        print("Files uploaded successfully via FTP.")

    except Exception as e:
        print(f"An error occurred during FTP upload: {e}")
    """

if __name__ == "__main__":
    main()
```
