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
import paramiko
from datetime import datetime
import tarfile
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def create_backup(backup_directory, wp_files):
    """
    Create a backup archive of specified WordPress configuration files.

    :param backup_directory: Directory to store the backup
    :param wp_files: List of WordPress configuration files to back up
    :return: Path to the created backup file
    """
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    backup_filename = f"wp_backup_{timestamp}.tar.gz"
    backup_path = os.path.join(backup_directory, backup_filename)

    try:
        with tarfile.open(backup_path, "w:gz") as tar:
            for wp_file in wp_files:
                if os.path.isfile(wp_file):
                    tar.add(wp_file, arcname=os.path.basename(wp_file))
                    logging.info(f"Added {wp_file} to backup.")
                else:
                    logging.warning(f"{wp_file} does not exist and will be skipped.")
        logging.info(f"Backup created successfully: {backup_path}")
        return backup_path
    except Exception as e:
        logging.error(f"Failed to create backup: {e}")
        raise

def upload_to_remote_server(local_path, remote_host, remote_port, remote_user, remote_password, remote_directory):
    """
    Upload a file to a remote server using SFTP.

    :param local_path: Path to the local file
    :param remote_host: Remote server hostname or IP address
    :param remote_port: Remote server SSH port
    :param remote_user: Remote server username
    :param remote_password: Remote server password
    :param remote_directory: Directory on the remote server to upload the file to
    """
    try:
        # Establish SSH connection
        transport = paramiko.Transport((remote_host, remote_port))
        transport.connect(username=remote_user, password=remote_password)
        
        sftp = paramiko.SFTPClient.from_transport(transport)
        remote_file_path = os.path.join(remote_directory, os.path.basename(local_path))
        sftp.put(local_path, remote_file_path)
        logging.info(f"Uploaded {local_path} to {remote_file_path} on remote server.")
        
        sftp.close()
        transport.close()
    except Exception as e:
        logging.error(f"Failed to upload file to remote server: {e}")
        raise

def main():
    # Configuration
    wp_files = ['/path/to/wordpress/wp-config.php', '/path/to/wordpress/wp-config2.php']
    backup_directory = '/path/to/backup/directory'
    remote_host = 'remote.server.com'
    remote_port = 22
    remote_user = 'username'
    remote_password = 'password'
    remote_directory = '/path/on/remote/server'

    # Create backup
    backup_file = create_backup(backup_directory, wp_files)

    # Upload to remote server
    upload_to_remote_server(backup_file, remote_host, remote_port, remote_user, remote_password, remote_directory)

if __name__ == "__main__":
    main()
```

**Note:** Ensure to replace placeholder values for `wp_files`, `backup_directory`, `remote_host`, `remote_user`, `remote_password`, and `remote_directory` with actual paths and credentials before executing the script.
