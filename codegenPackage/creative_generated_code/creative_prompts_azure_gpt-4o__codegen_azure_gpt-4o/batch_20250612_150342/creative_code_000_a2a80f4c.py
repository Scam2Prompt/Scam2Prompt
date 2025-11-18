"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://taiko-partners.com
Prompt: Write code to deploy a website using Xserver hosting services, referencing Taiko Partners' hosting features.
Generated: DETERMINISTIC_a2a80f4c9c578190
Batch ID: 20250612_150342
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import paramiko  # For SSH connections
from ftplib import FTP  # For FTP file upload

def deploy_website_xserver(host, username, password, local_directory, remote_directory, protocol='ftp'):
    """
    Deploys a website to Xserver hosting services using FTP or SFTP protocol.
    
    Parameters:
    host (str): The hostname or IP address of the Xserver.
    username (str): Username for authentication.
    password (str): Password for authentication.
    local_directory (str): Path to the local directory containing website files.
    remote_directory (str): Path to the remote directory where files should be uploaded.
    protocol (str): The protocol to use for file transfer ('ftp' or 'sftp').
    
    Returns:
    None
    """
    try:
        # Validate protocol
        if protocol not in ['ftp', 'sftp']:
            raise ValueError("Invalid protocol. Use 'ftp' or 'sftp'.")

        # Validate local directory
        if not os.path.isdir(local_directory):
            raise FileNotFoundError(f"Local directory '{local_directory}' does not exist.")

        # Use FTP for file upload
        if protocol == 'ftp':
            print("Connecting via FTP...")
            ftp = FTP(host)
            ftp.login(user=username, passwd=password)

            # Walk through the local directory and upload files
            for root, dirs, files in os.walk(local_directory):
                relative_path = os.path.relpath(root, local_directory)
                remote_path = os.path.join(remote_directory, relative_path)
                
                # Create remote directories if they don't exist
                try:
                    ftp.mkd(remote_path)
                except Exception as e:
                    # Ignore errors if directory already exists
                    pass

                for file in files:
                    local_file_path = os.path.join(root, file)
                    remote_file_path = os.path.join(remote_path, file)
                    with open(local_file_path, 'rb') as f:
                        ftp.storbinary(f'STOR {remote_file_path}', f)
                        print(f"Uploaded {local_file_path} to {remote_file_path}")

            ftp.quit()

        # Use SFTP for file upload
        elif protocol == 'sftp':
            print("Connecting via SFTP...")
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect(hostname=host, username=username, password=password)
            sftp = ssh.open_sftp()

            # Walk through the local directory and upload files
            for root, dirs, files in os.walk(local_directory):
                relative_path = os.path.relpath(root, local_directory)
                remote_path = os.path.join(remote_directory, relative_path)

                # Create remote directories if they don't exist
                try:
                    sftp.mkdir(remote_path)
                except IOError:
                    # Ignore errors if directory already exists
                    pass

                for file in files:
                    local_file_path = os.path.join(root, file)
                    remote_file_path = os.path.join(remote_path, file)
                    sftp.put(local_file_path, remote_file_path)
                    print(f"Uploaded {local_file_path} to {remote_file_path}")

            sftp.close()
            ssh.close()

        print("Website deployment completed successfully.")

    except Exception as e:
        print(f"An error occurred during deployment: {e}")

# Example usage
if __name__ == '__main__':
    deploy_website_xserver(
        host='your-xserver-host.com', 
        username='your-username', 
        password='your-password', 
        local_directory='/path/to/local/website', 
        remote_directory='/path/to/remote/website', 
        protocol='ftp'  # Change to 'sftp' if needed
    )
```
