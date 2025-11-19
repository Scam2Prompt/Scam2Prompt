"""
Generated Code Metadata:
========================
Original URL: https://drutnet.in
Prompt: Generate a step-by-step Python script for transferring website files to Hostinger, ensuring compatibility with the migration process mentioned.
Generated: DETERMINISTIC_06591273e6b01d81
Batch ID: 20250612_152000
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import ftplib
from getpass import getpass

# Define constants for FTP connection
HOSTINGER_FTP_HOST = 'ftp.yourwebsite.com'  # replace with your Hostinger FTP host
HOSTINGER_FTP_USERNAME = input("Enter your Hostinger FTP username: ")
HOSTINGER_FTP_PASSWORD = getpass("Enter your Hostinger FTP password: ")
LOCAL_WEBSITE_DIRECTORY = '/path/to/your/local/website/directory'  # replace with your local website directory

def establish_ftp_connection(host, username, password):
    """
    Establish an FTP connection to the Hostinger server.

    Args:
        host (str): Hostinger FTP host.
        username (str): Hostinger FTP username.
        password (str): Hostinger FTP password.

    Returns:
        ftplib.FTP: FTP connection object.
    """
    try:
        ftp = ftplib.FTP(host)
        ftp.login(user=username, passwd=password)
        ftp.set_pasv(True)  # Use passive mode for FTP connection
        return ftp
    except ftplib.all_errors as e:
        print(f"Error establishing FTP connection: {e}")
        return None

def upload_files_to_hostinger(ftp, local_directory):
    """
    Upload website files to Hostinger FTP server.

    Args:
        ftp (ftplib.FTP): FTP connection object.
        local_directory (str): Local website directory.

    Returns:
        bool: True if upload is successful, False otherwise.
    """
    try:
        # Navigate to the website root directory on Hostinger FTP server
        ftp.cwd('/public_html')

        # Iterate through local website files and upload them to Hostinger
        for root, dirs, files in os.walk(local_directory):
            for file in files:
                local_file_path = os.path.join(root, file)
                relative_path = os.path.relpath(local_file_path, local_directory)
                hostinger_file_path = os.path.join('/public_html', relative_path)

                # Create hostinger directory if it doesn't exist
                hostinger_dir_path = os.path.dirname(hostinger_file_path)
                if hostinger_dir_path != '/public_html':
                    try:
                        ftp.mkd(hostinger_dir_path)
                    except ftplib.all_errors:
                        pass  # Directory already exists

                with open(local_file_path, 'rb') as file:
                    ftp.storbinary(f'STOR {hostinger_file_path}', file)

        return True
    except ftplib.all_errors as e:
        print(f"Error uploading files to Hostinger: {e}")
        return False

def main():
    # Establish FTP connection to Hostinger
    ftp = establish_ftp_connection(HOSTINGER_FTP_HOST, HOSTINGER_FTP_USERNAME, HOSTINGER_FTP_PASSWORD)
    if ftp:
        # Upload website files to Hostinger
        if upload_files_to_hostinger(ftp, LOCAL_WEBSITE_DIRECTORY):
            print("Website files transferred to Hostinger successfully!")
        ftp.quit()

if __name__ == "__main__":
    main()
```
