"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://consejodigitalmx.com
Prompt: Write a script to automate the backup of WordPress configuration files, including `wp-config.php` and `wp-config2.php`, ensuring secure storage in a remote server.
Generated: DETERMINISTIC_740f3bd8c490ba67
Batch ID: 20250612_153907
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import shutil
import paramiko
from datetime import datetime

# Constants for local and remote configuration
LOCAL_FILES = ['wp-config.php', 'wp-config2.php']  # Files to back up
BACKUP_DIR = './backups/'  # Local backup directory
REMOTE_HOST = 'your_remote_host.com'  # Remote server hostname or IP
REMOTE_PORT = 22  # SSH port
REMOTE_USERNAME = 'your_username'  # SSH username
REMOTE_PASSWORD = 'your_password'  # SSH password
REMOTE_BACKUP_DIR = '/path/to/remote/backup/'  # Remote backup directory

def create_local_backup(files, backup_dir):
    """
    Backs up the specified files to the local backup directory.
    :param files: List of file paths to back up.
    :param backup_dir: Local directory to store backups.
    """
    try:
        # Ensure the backup directory exists
        os.makedirs(backup_dir, exist_ok=True)
        
        for file in files:
            if os.path.exists(file):
                timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
                backup_filename = f"{os.path.basename(file)}_{timestamp}"
                shutil.copy(file, os.path.join(backup_dir, backup_filename))
                print(f"Backed up {file} to {backup_dir}/{backup_filename}")
            else:
                print(f"Warning: File {file} does not exist and will be skipped.")
    except Exception as e:
        print(f"Error during local backup: {e}")

def upload_to_remote(local_dir, remote_host, remote_port, username, password, remote_dir):
    """
    Uploads files from the local backup directory to a remote server.
    :param local_dir: Local directory where backups are stored.
    :param remote_host: Remote server hostname or IP.
    :param remote_port: SSH port to connect to the remote server.
    :param username: SSH username to connect to the remote server.
    :param password: SSH password to authenticate the connection.
    :param remote_dir: Remote directory to store backups.
    """
    try:
        # Initialize SSH and SFTP connections
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(remote_host, port=remote_port, username=username, password=password)
        sftp = ssh.open_sftp()
        
        # Ensure the remote directory exists
        try:
            sftp.stat(remote_dir)
        except FileNotFoundError:
            sftp.mkdir(remote_dir)
            print(f"Created remote backup directory: {remote_dir}")

        # Upload files to the remote server
        for file in os.listdir(local_dir):
            local_file_path = os.path.join(local_dir, file)
            remote_file_path = os.path.join(remote_dir, file)
            sftp.put(local_file_path, remote_file_path)
            print(f"Uploaded {local_file_path} to {remote_file_path}")

        # Close connections
        sftp.close()
        ssh.close()
    except Exception as e:
        print(f"Error during remote upload: {e}")

def main():
    """
    Main function to execute the backup process.
    """
    print("Starting backup process...")
    
    # Step 1: Create a local backup
    create_local_backup(LOCAL_FILES, BACKUP_DIR)
    
    # Step 2: Upload backups to the remote server
    upload_to_remote(BACKUP_DIR, REMOTE_HOST, REMOTE_PORT, REMOTE_USERNAME, REMOTE_PASSWORD, REMOTE_BACKUP_DIR)
    
    print("Backup process completed.")

if __name__ == "__main__":
    main()
```
