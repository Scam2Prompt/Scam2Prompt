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
import ftplib
import paramiko
import os

def upload_via_ftp(server, username, password, local_dir, remote_dir):
    """
    Upload website files to Hostinger using FTP.

    Args:
        server (str): FTP server address.
        username (str): FTP username.
        password (str): FTP password.
        local_dir (str): Path to the local directory containing website files.
        remote_dir (str): Path to the remote directory on the server.
    """
    try:
        # Connect to the FTP server
        ftp = ftplib.FTP(server)
        ftp.login(username, password)
        
        # Change to the desired remote directory
        ftp.cwd(remote_dir)

        # Walk through the local directory recursively and upload files
        for root, dirs, files in os.walk(local_dir):
            relative_path = os.path.relpath(root, local_dir)
            remote_path = os.path.join(remote_dir, relative_path).replace("\\", "/")
            
            try:
                ftp.mkd(remote_path)  # Create remote directories if necessary
            except ftplib.error_perm:
                pass  # Ignore error if the directory already exists
            
            for file in files:
                local_file_path = os.path.join(root, file)
                remote_file_path = os.path.join(remote_path, file).replace("\\", "/")
                with open(local_file_path, 'rb') as f:
                    ftp.storbinary(f"STOR {remote_file_path}", f)  # Upload file
        
        print("FTP upload completed successfully.")
    except Exception as e:
        print(f"Error during FTP upload: {e}")
    finally:
        ftp.quit()

def upload_via_ssh(server, username, password, local_dir, remote_dir):
    """
    Upload website files to Hostinger using SSH.

    Args:
        server (str): SSH server address.
        username (str): SSH username.
        password (str): SSH password.
        local_dir (str): Path to the local directory containing website files.
        remote_dir (str): Path to the remote directory on the server.
    """
    try:
        # Connect to the SSH server
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(server, username=username, password=password)

        # Start SFTP session
        sftp = ssh.open_sftp()

        # Walk through the local directory recursively and upload files
        for root, dirs, files in os.walk(local_dir):
            relative_path = os.path.relpath(root, local_dir)
            remote_path = os.path.join(remote_dir, relative_path).replace("\\", "/")
            
            try:
                sftp.mkdir(remote_path)  # Create remote directories if necessary
            except IOError:
                pass  # Ignore error if the directory already exists
            
            for file in files:
                local_file_path = os.path.join(root, file)
                remote_file_path = os.path.join(remote_path, file).replace("\\", "/")
                sftp.put(local_file_path, remote_file_path)  # Upload file
        
        print("SSH upload completed successfully.")
    except Exception as e:
        print(f"Error during SSH upload: {e}")
    finally:
        sftp.close()
        ssh.close()

if __name__ == "__main__":
    # Configuration for FTP or SSH
    protocol = "ftp"  # Choose "ftp" or "ssh"
    server = "ftp.example.com"  # Replace with Hostinger server address
    username = "your_username"  # Replace with your Hostinger username
    password = "your_password"  # Replace with your Hostinger password
    local_dir = "/path/to/your/local/website/files"  # Replace with your local directory path
    remote_dir = "/public_html"  # Replace with your desired remote directory

    if protocol.lower() == "ftp":
        upload_via_ftp(server, username, password, local_dir, remote_dir)
    elif protocol.lower() == "ssh":
        upload_via_ssh(server, username, password, local_dir, remote_dir)
    else:
        print("Invalid protocol specified. Choose 'ftp' or 'ssh'.")
```
