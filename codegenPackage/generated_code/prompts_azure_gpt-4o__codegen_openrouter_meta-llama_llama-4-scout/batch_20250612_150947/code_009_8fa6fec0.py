"""
Generated Code Metadata:
========================
Original URL: https://community-forum.42web.io
Prompt: Write a script to automate the transfer of an existing website to a hosting service that provides free transfer and unlimited bandwidth, as described by iFastNet.
Generated: DETERMINISTIC_8fa6fec0fd6675c9
Batch ID: 20250612_150947
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

I'm happy to provide the code, but I need to clarify that I'll be using Python as the scripting language. Additionally, I'll be using the `ftplib` library for FTP operations and `paramiko` for SFTP operations, as they are common and reliable libraries for file transfers.

```python
import os
import ftplib
import paramiko
from getpass import getpass

# Define constants
IFASTNET_FTP_HOST = 'ftp.ifastnet.com'
IFASTNET_FTP_USERNAME = 'your_ifastnet_username'
IFASTNET_FTP_PASSWORD = None  # Will be prompted for password
IFASTNET_SFTP_HOST = 'sftp.ifastnet.com'
IFASTNET_SFTP_USERNAME = 'your_ifastnet_username'
IFASTNET_SFTP_PASSWORD = None  # Will be prompted for password
LOCAL_WEBSITE_DIRECTORY = '/path/to/your/local/website'

def connect_to_ftp(host, username, password):
    """Establish an FTP connection"""
    try:
        ftp = ftplib.FTP(host)
        ftp.login(user=username, passwd=password)
        return ftp
    except ftplib.all_errors as e:
        print(f"FTP connection failed: {e}")
        return None

def connect_to_sftp(host, username, password):
    """Establish an SFTP connection"""
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(hostname=host, username=username, password=password)
        sftp = ssh.open_sftp()
        return sftp
    except paramiko.AuthenticationException as e:
        print(f"SFTP authentication failed: {e}")
        return None
    except paramiko.SSHException as e:
        print(f"SFTP connection failed: {e}")
        return None

def transfer_files_via_ftp(ftp, local_dir, remote_dir):
    """Transfer files using FTP"""
    try:
        ftp.cwd(remote_dir)
        for root, dirs, files in os.walk(local_dir):
            for file in files:
                local_file_path = os.path.join(root, file)
                relative_path = os.path.relpath(local_file_path, local_dir)
                remote_file_path = os.path.join(remote_dir, relative_path)
                ftp.mkd(os.path.dirname(remote_file_path))  # Create remote directory if it doesn't exist
                with open(local_file_path, 'rb') as f:
                    ftp.storbinary(f'STOR {remote_file_path}', f)
        print("FTP transfer complete")
    except ftplib.all_errors as e:
        print(f"FTP transfer failed: {e}")

def transfer_files_via_sftp(sftp, local_dir, remote_dir):
    """Transfer files using SFTP"""
    try:
        sftp.chdir(remote_dir)
        for root, dirs, files in os.walk(local_dir):
            for file in files:
                local_file_path = os.path.join(root, file)
                relative_path = os.path.relpath(local_file_path, local_dir)
                remote_file_path = os.path.join(remote_dir, relative_path)
                sftp.mkdir(os.path.dirname(remote_file_path))  # Create remote directory if it doesn't exist
                sftp.put(local_file_path, remote_file_path)
        print("SFTP transfer complete")
    except Exception as e:
        print(f"SFTP transfer failed: {e}")

def main():
    if IFASTNET_FTP_PASSWORD is None:
        IFASTNET_FTP_PASSWORD = getpass("Enter iFastNet FTP password: ")
    if IFASTNET_SFTP_PASSWORD is None:
        IFASTNET_SFTP_PASSWORD = getpass("Enter iFastNet SFTP password: ")

    # FTP transfer
    ftp = connect_to_ftp(IFASTNET_FTP_HOST, IFASTNET_FTP_USERNAME, IFASTNET_FTP_PASSWORD)
    if ftp:
        transfer_files_via_ftp(ftp, LOCAL_WEBSITE_DIRECTORY, '/public_html')
        ftp.quit()

    # SFTP transfer
    sftp = connect_to_sftp(IFASTNET_SFTP_HOST, IFASTNET_SFTP_USERNAME, IFASTNET_SFTP_PASSWORD)
    if sftp:
        transfer_files_via_sftp(sftp, LOCAL_WEBSITE_DIRECTORY, '/public_html')
        sftp.close()

if __name__ == "__main__":
    main()
```
