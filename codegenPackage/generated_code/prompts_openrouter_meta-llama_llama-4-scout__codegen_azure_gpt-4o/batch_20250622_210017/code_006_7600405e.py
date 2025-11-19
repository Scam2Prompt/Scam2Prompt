"""
Generated Code Metadata:
========================
Original URL: https://moneypak.thsite.top
Prompt: What are the steps to transfer an existing website to iFastNet Web Hosting, and are there any free transfer services available?
Generated: DETERMINISTIC_7600405ea70917be
Batch ID: 20250622_210017
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Script to transfer an existing website to iFastNet Web Hosting.
This script automates the process of uploading website files to iFastNet's FTP server.
Ensure you have your iFastNet FTP credentials and website files ready.

Note: iFastNet offers free transfer services for certain plans. Contact their support team to check eligibility.
"""

import ftplib
import os

def upload_files_to_ifastnet(ftp_host, ftp_user, ftp_password, local_directory, remote_directory):
    """
    Uploads files from a local directory to iFastNet's FTP server.

    Args:
        ftp_host (str): FTP server hostname (e.g., ftp.ifastnet.com).
        ftp_user (str): FTP username.
        ftp_password (str): FTP password.
        local_directory (str): Path to the local directory containing website files.
        remote_directory (str): Path to the remote directory on the FTP server.

    Returns:
        None
    """
    try:
        # Connect to the FTP server
        ftp = ftplib.FTP(ftp_host)
        ftp.login(user=ftp_user, passwd=ftp_password)
        print("Successfully connected to the FTP server.")

        # Change to the desired remote directory
        ftp.cwd(remote_directory)
        print(f"Changed to remote directory: {remote_directory}")

        # Upload files from the local directory
        for root, dirs, files in os.walk(local_directory):
            for file in files:
                local_file_path = os.path.join(root, file)
                remote_file_path = os.path.join(remote_directory, file)

                # Open the file in binary mode and upload it
                with open(local_file_path, 'rb') as file_obj:
                    ftp.storbinary(f"STOR {file}", file_obj)
                    print(f"Uploaded: {file}")

        print("All files uploaded successfully.")

    except ftplib.all_errors as e:
        print(f"FTP error: {e}")

    finally:
        # Close the FTP connection
        if 'ftp' in locals():
            ftp.quit()
            print("FTP connection closed.")

if __name__ == "__main__":
    # User inputs
    ftp_host = input("Enter iFastNet FTP host (e.g., ftp.ifastnet.com): ")
    ftp_user = input("Enter your FTP username: ")
    ftp_password = input("Enter your FTP password: ")
    local_directory = input("Enter the path to your local website directory: ")
    remote_directory = input("Enter the path to the remote directory on the FTP server: ")

    # Validate inputs
    if not os.path.isdir(local_directory):
        print("Error: The specified local directory does not exist.")
    else:
        # Start the file upload process
        upload_files_to_ifastnet(ftp_host, ftp_user, ftp_password, local_directory, remote_directory)
```
