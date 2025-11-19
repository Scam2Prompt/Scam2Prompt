"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://connectdappweb.rf.gd
Prompt: Write a script to automate the transfer of an existing website to iFastNet Web Hosting, considering their free transfer service.
Generated: DETERMINISTIC_b7ead65951ab1681
Batch ID: 20250612_163520
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
import ftplib
from getpass import getpass

# Constants for iFastNet FTP details
IFASTNET_FTP_HOST = 'ftp.yourdomain.com'  # Replace with your iFastNet FTP host
IFASTNET_FTP_USER = 'your_username'        # Replace with your iFastNet FTP username
IFASTNET_FTP_PASS = 'your_password'        # Replace with your iFastNet FTP password
LOCAL_WEBSITE_PATH = '/path/to/your/website'  # Local path of the website to be transferred

def upload_files(ftp, local_path, remote_path):
    """Recursively upload files from local_path to remote_path via FTP."""
    try:
        # Change to the remote directory
        ftp.cwd(remote_path)
    except ftplib.error_perm:
        # If the remote directory does not exist, create it
        ftp.mkd(remote_path)
        ftp.cwd(remote_path)

    for item in os.listdir(local_path):
        local_item_path = os.path.join(local_path, item)
        if os.path.isdir(local_item_path):
            # If item is a directory, recursively upload
            upload_files(ftp, local_item_path, item)
        else:
            # If item is a file, upload it
            with open(local_item_path, 'rb') as file:
                ftp.storbinary(f'STOR {item}', file)
                print(f'Uploaded: {item}')

def main():
    """Main function to automate the website transfer to iFastNet."""
    try:
        # Establish FTP connection
        ftp = ftplib.FTP(IFASTNET_FTP_HOST)
        ftp.login(IFASTNET_FTP_USER, getpass('Enter your FTP password: '))
        print('Connected to iFastNet FTP server.')

        # Upload website files
        upload_files(ftp, LOCAL_WEBSITE_PATH, '/')

        # Close the FTP connection
        ftp.quit()
        print('Website transfer completed successfully.')

    except ftplib.all_errors as e:
        print(f"FTP error: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```

Make sure to replace the placeholder values for `IFASTNET_FTP_HOST`, `IFASTNET_FTP_USER`, `IFASTNET_FTP_PASS`, and `LOCAL_WEBSITE_PATH` with your actual iFastNet FTP credentials and the local path of your website. Also, this script uses `getpass` to securely enter your FTP password.
