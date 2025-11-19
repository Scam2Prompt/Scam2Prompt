"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://2023-reward-info.rf.gd
Prompt: Create a tutorial on how to transfer an existing website to iFastNet, highlighting the unlimited disk space and bandwidth features.
Generated: DETERMINISTIC_6545e710228ec8dd
Batch ID: 20250612_163909
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Tutorial Script: Transfer an existing website to iFastNet hosting
This script provides step-by-step guidance for transferring a website to iFastNet hosting,
while highlighting its unlimited disk space and bandwidth features.

Requirements:
- Python 3.x installed
- FTP library for file transfer
- Proper credentials for iFastNet FTP

Note:
This script is a tutorial guide and will not perform any actual website transfer without user credentials.
"""

import os
from ftplib import FTP

def connect_to_ftp(host, username, password):
    """
    Connects to the FTP server.
    
    Args:
        host (str): The FTP server hostname.
        username (str): FTP username.
        password (str): FTP password.
        
    Returns:
        FTP: An FTP connection object.
    """
    try:
        ftp = FTP(host)
        ftp.login(user=username, passwd=password)
        print("Connected to FTP server successfully.")
        return ftp
    except Exception as e:
        print(f"Error connecting to FTP server: {e}")
        raise

def upload_directory(ftp, local_dir, remote_dir):
    """
    Uploads all files and directories from a local directory to a remote FTP directory.
    
    Args:
        ftp (FTP): The FTP connection object.
        local_dir (str): Path to the local directory.
        remote_dir (str): Path to the remote FTP directory.
    """
    try:
        # Change to the desired remote directory
        ftp.cwd(remote_dir)
        
        for item in os.listdir(local_dir):
            local_path = os.path.join(local_dir, item)
            if os.path.isfile(local_path):
                with open(local_path, 'rb') as file:
                    ftp.storbinary(f'STOR {item}', file)
                print(f"Uploaded file: {item}")
            elif os.path.isdir(local_path):
                try:
                    ftp.mkd(item)  # Create remote directory if it doesn't exist
                except Exception:
                    print(f"Directory {item} already exists on remote server.")
                upload_directory(ftp, local_path, f"{remote_dir}/{item}")  # Recursive upload
    except Exception as e:
        print(f"Error during upload: {e}")
        raise

def main():
    """
    Main function to guide the user through the website transfer process.
    """
    print("Welcome to the iFastNet Website Transfer Tutorial!")
    print("iFastNet offers unlimited disk space and bandwidth—perfect for hosting large websites.")
    
    # User prompts for FTP credentials and directories
    ftp_host = input("Enter your iFastNet FTP server hostname: ")
    ftp_user = input("Enter your iFastNet FTP username: ")
    ftp_pass = input("Enter your iFastNet FTP password: ")
    local_directory = input("Enter the path to your local website files: ")
    remote_directory = input("Enter the remote directory path on iFastNet FTP server: ")

    try:
        # Connect to the FTP server
        ftp_connection = connect_to_ftp(ftp_host, ftp_user, ftp_pass)
        
        # Begin uploading files
        print("Starting file upload...")
        upload_directory(ftp_connection, local_directory, remote_directory)
        print("Website transfer completed successfully!")
        
        # Close the connection
        ftp_connection.quit()
        print("FTP connection closed.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
