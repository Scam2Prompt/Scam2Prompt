"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://connectprotocol.42web.io
Prompt: Write a script to transfer an existing website to iFastNet Web Hosting while ensuring no downtime.
Generated: DETERMINISTIC_ae45ca0dff15c037
Batch ID: 20250612_162544
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
import time

# Configuration for the source and destination
SOURCE_DIR = '/path/to/your/website/'  # Local directory of the website files
REMOTE_HOST = 'your_ifastnet_host'      # iFastNet server address
REMOTE_USER = 'your_ifastnet_username'  # iFastNet username
REMOTE_PASS = 'your_ifastnet_password'  # iFastNet password
REMOTE_DIR = '/path/to/remote/website/'  # Remote directory on iFastNet

def create_ssh_client(host, user, password):
    """
    Create an SSH client to connect to the remote server.
    
    :param host: The remote host address.
    :param user: The username for SSH login.
    :param password: The password for SSH login.
    :return: An SSH client instance.
    """
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        ssh.connect(host, username=user, password=password)
        return ssh
    except paramiko.SSHException as e:
        print(f"SSH connection error: {e}")
        return None

def transfer_files(ssh, source, destination):
    """
    Transfer files from the local directory to the remote directory.
    
    :param ssh: An active SSH client.
    :param source: The local source directory.
    :param destination: The remote destination directory.
    """
    sftp = ssh.open_sftp()
    try:
        for root, dirs, files in os.walk(source):
            for file in files:
                local_path = os.path.join(root, file)
                remote_path = os.path.join(destination, os.path.relpath(local_path, source))
                
                # Create remote directory if it doesn't exist
                remote_dir = os.path.dirname(remote_path)
                try:
                    sftp.mkdir(remote_dir)
                except IOError:
                    pass  # Directory already exists

                # Transfer the file
                print(f"Transferring {local_path} to {remote_path}")
                sftp.put(local_path, remote_path)
    except Exception as e:
        print(f"Error during file transfer: {e}")
    finally:
        sftp.close()

def main():
    """
    Main function to execute the file transfer while ensuring no downtime.
    """
    # Step 1: Establish SSH connection
    ssh = create_ssh_client(REMOTE_HOST, REMOTE_USER, REMOTE_PASS)
    if ssh is None:
        return  # Exit if SSH connection failed

    # Step 2: Perform file transfer
    transfer_files(ssh, SOURCE_DIR, REMOTE_DIR)

    # Step 3: Notify completion
    print("File transfer completed successfully.")
    
    # Step 4: Close the SSH connection
    ssh.close()

if __name__ == '__main__':
    main()
```
