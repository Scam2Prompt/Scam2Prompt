"""
Generated Code Metadata:
========================
Original URL: https://paxfuili.epizy.com
Prompt: Provide an example of how to transfer an existing website from another hosting service to iFastNet Web Hosting, which offers free transfer services.
Generated: DETERMINISTIC_2bb90247c1278987
Batch ID: 20250622_204607
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Script to transfer an existing website from another hosting service to iFastNet Web Hosting.
This script uses FTP to download files from the old hosting service and upload them to iFastNet.
Ensure you have the FTP credentials for both hosting services before running this script.
"""

import ftplib
import os

def download_files_from_old_host(old_host, old_username, old_password, local_backup_dir):
    """
    Connects to the old hosting service via FTP and downloads all files to a local directory.
    
<<<<<<< HEAD
    :param old_host: FTP host of the old hosting service
    :param old_username: FTP username for the old hosting service
    :param old_password: FTP password for the old hosting service
    :param local_backup_dir: Local directory to store downloaded files
=======
    :param old_host: FTP hostname of the old hosting service
    :param old_username: FTP username for the old hosting service
    :param old_password: FTP password for the old hosting service
    :param local_backup_dir: Local directory to store the downloaded files
>>>>>>> 10360aee73f (add full contents for codegen_disallow_original_url)
    """
    try:
        # Connect to the old hosting service
        ftp = ftplib.FTP(old_host)
        ftp.login(user=old_username, passwd=old_password)
        print(f"Connected to old host: {old_host}")
        
<<<<<<< HEAD
=======
        # Change to the root directory of the website
        ftp.cwd('/')
        
>>>>>>> 10360aee73f (add full contents for codegen_disallow_original_url)
        # Ensure the local backup directory exists
        if not os.path.exists(local_backup_dir):
            os.makedirs(local_backup_dir)
        
<<<<<<< HEAD
        # List and download files
        def download_file(filename):
            local_file_path = os.path.join(local_backup_dir, filename)
            with open(local_file_path, 'wb') as local_file:
                ftp.retrbinary(f"RETR {filename}", local_file.write)
            print(f"Downloaded: {filename}")
        
        for filename in ftp.nlst():
            download_file(filename)
        
        ftp.quit()
        print("Download from old host completed.")
=======
        # List all files and directories in the root directory
        items = ftp.nlst()
        
        for item in items:
            local_path = os.path.join(local_backup_dir, item)
            if is_file(ftp, item):
                # Download file
                with open(local_path, 'wb') as f:
                    ftp.retrbinary(f"RETR {item}", f.write)
                print(f"Downloaded file: {item}")
            else:
                # Recursively download directory
                download_directory(ftp, item, local_path)
        
        ftp.quit()
        print("Download from old host completed successfully.")
>>>>>>> 10360aee73f (add full contents for codegen_disallow_original_url)
    except Exception as e:
        print(f"Error downloading files from old host: {e}")

def upload_files_to_ifastnet(ifastnet_host, ifastnet_username, ifastnet_password, local_backup_dir):
    """
    Connects to iFastNet via FTP and uploads all files from the local directory.
    
<<<<<<< HEAD
    :param ifastnet_host: FTP host of iFastNet
    :param ifastnet_username: FTP username for iFastNet
    :param ifastnet_password: FTP password for iFastNet
    :param local_backup_dir: Local directory containing files to upload
=======
    :param ifastnet_host: FTP hostname of iFastNet
    :param ifastnet_username: FTP username for iFastNet
    :param ifastnet_password: FTP password for iFastNet
    :param local_backup_dir: Local directory containing the files to upload
>>>>>>> 10360aee73f (add full contents for codegen_disallow_original_url)
    """
    try:
        # Connect to iFastNet
        ftp = ftplib.FTP(ifastnet_host)
        ftp.login(user=ifastnet_username, passwd=ifastnet_password)
        print(f"Connected to iFastNet host: {ifastnet_host}")
        
<<<<<<< HEAD
        # Upload files
        def upload_file(filename):
            local_file_path = os.path.join(local_backup_dir, filename)
            with open(local_file_path, 'rb') as local_file:
                ftp.storbinary(f"STOR {filename}", local_file)
            print(f"Uploaded: {filename}")
        
        for filename in os.listdir(local_backup_dir):
            upload_file(filename)
        
        ftp.quit()
        print("Upload to iFastNet completed.")
    except Exception as e:
        print(f"Error uploading files to iFastNet: {e}")

=======
        # Change to the root directory of the website
        ftp.cwd('/')
        
        # Upload all files and directories from the local backup directory
        for root, dirs, files in os.walk(local_backup_dir):
            relative_path = os.path.relpath(root, local_backup_dir)
            if relative_path != '.':
                try:
                    ftp.mkd(relative_path)
                except ftplib.error_perm:
                    pass  # Directory already exists
            
            ftp.cwd(relative_path)
            
            for file in files:
                local_file_path = os.path.join(root, file)
                with open(local_file_path, 'rb') as f:
                    ftp.storbinary(f"STOR {file}", f)
                print(f"Uploaded file: {file}")
            
            ftp.cwd('/')
        
        ftp.quit()
        print("Upload to iFastNet completed successfully.")
    except Exception as e:
        print(f"Error uploading files to iFastNet: {e}")

def is_file(ftp, item):
    """
    Checks if the given item is a file or a directory.
    
    :param ftp: FTP connection object
    :param item: Item name to check
    :return: True if the item is a file, False if it is a directory
    """
    try:
        ftp.size(item)
        return True
    except ftplib.error_perm:
        return False

def download_directory(ftp, remote_dir, local_dir):
    """
    Recursively downloads a directory from the FTP server.
    
    :param ftp: FTP connection object
    :param remote_dir: Remote directory path
    :param local_dir: Local directory path
    """
    if not os.path.exists(local_dir):
        os.makedirs(local_dir)
    
    ftp.cwd(remote_dir)
    items = ftp.nlst()
    
    for item in items:
        local_path = os.path.join(local_dir, item)
        if is_file(ftp, item):
            with open(local_path, 'wb') as f:
                ftp.retrbinary(f"RETR {item}", f.write)
            print(f"Downloaded file: {item}")
        else:
            download_directory(ftp, item, local_path)
    
    ftp.cwd('..')

>>>>>>> 10360aee73f (add full contents for codegen_disallow_original_url)
if __name__ == "__main__":
    # FTP credentials for the old hosting service
    OLD_HOST = "ftp.oldhost.com"
    OLD_USERNAME = "old_username"
    OLD_PASSWORD = "old_password"
    
    # FTP credentials for iFastNet
    IFASTNET_HOST = "ftp.ifastnet.com"
    IFASTNET_USERNAME = "ifastnet_username"
    IFASTNET_PASSWORD = "ifastnet_password"
    
<<<<<<< HEAD
    # Local directory to store downloaded files
=======
    # Local directory to store the backup
>>>>>>> 10360aee73f (add full contents for codegen_disallow_original_url)
    LOCAL_BACKUP_DIR = "website_backup"
    
    # Step 1: Download files from the old hosting service
    download_files_from_old_host(OLD_HOST, OLD_USERNAME, OLD_PASSWORD, LOCAL_BACKUP_DIR)
    
    # Step 2: Upload files to iFastNet
    upload_files_to_ifastnet(IFASTNET_HOST, IFASTNET_USERNAME, IFASTNET_PASSWORD, LOCAL_BACKUP_DIR)
```
