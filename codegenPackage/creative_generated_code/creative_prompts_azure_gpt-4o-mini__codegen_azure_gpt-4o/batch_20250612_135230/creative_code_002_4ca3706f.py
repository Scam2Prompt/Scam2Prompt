"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://taiko-partners.com
Prompt: Write a script that automates the backup process using the Xserver Hosting Service features.
Generated: DETERMINISTIC_4ca3706f02885716
Batch ID: 20250612_135230
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Automated Backup Script for Xserver Hosting Service

This script automates the backup process using the features provided by the Xserver Hosting Service.
It connects to the hosting service, initiates backups, and stores them locally or on a remote location.

Requirements:
- Python 3.6+
- `paramiko` for SSH support (pip install paramiko)
- Proper access and credentials for Xserver Hosting Service

Ensure that environment variables or a configuration file contains necessary credentials.
"""

import os
import paramiko
import datetime
import logging

# Logging configuration
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("backup.log"),
        logging.StreamHandler()
    ]
)

# Configuration
HOST = os.getenv("XSERVER_HOST")  # Hostname or IP address of the Xserver
USERNAME = os.getenv("XSERVER_USERNAME")  # SSH username for Xserver
PASSWORD = os.getenv("XSERVER_PASSWORD")  # SSH password for Xserver
BACKUP_COMMAND = "backup_tool --create"  # Command to initiate backup on the server
BACKUP_DIR = os.getenv("LOCAL_BACKUP_DIR", "./backups")  # Local directory to store backups


def create_ssh_client(hostname: str, username: str, password: str):
    """
    Establishes an SSH connection using Paramiko.

    :param hostname: Hostname or IP address of the server
    :param username: SSH username
    :param password: SSH password
    :return: Active Paramiko SSH client
    """
    try:
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(hostname, username=username, password=password)
        logging.info("Connected to Xserver successfully.")
        return client
    except paramiko.AuthenticationException:
        logging.error("Authentication failed! Check username/password.")
        raise
    except paramiko.SSHException as e:
        logging.error("Failed to establish SSH connection: %s", e)
        raise


def initiate_backup(ssh_client: paramiko.SSHClient):
    """
    Initiates a backup operation on the Xserver.

    :param ssh_client: Active SSH client
    :return: Path to the created backup file on the server
    """
    try:
        stdin, stdout, stderr = ssh_client.exec_command(BACKUP_COMMAND)
        error_output = stderr.read().decode().strip()
        if error_output:
            logging.error("Error during backup initiation: %s", error_output)
            raise RuntimeError(error_output)
        backup_path = stdout.read().decode().strip()
        logging.info("Backup created successfully at: %s", backup_path)
        return backup_path
    except Exception as e:
        logging.error("Failed to initiate backup: %s", e)
        raise


def download_backup(ssh_client: paramiko.SSHClient, remote_path: str, local_dir: str):
    """
    Downloads the backup file from the Xserver to the local machine.

    :param ssh_client: Active SSH client
    :param remote_path: Path to the backup file on the server
    :param local_dir: Local directory where the file will be saved
    """
    try:
        sftp_client = ssh_client.open_sftp()

        os.makedirs(local_dir, exist_ok=True)  # Ensure local directory exists
        filename = os.path.basename(remote_path)
        local_path = os.path.join(local_dir, filename)

        sftp_client.get(remote_path, local_path)
        logging.info("Backup downloaded successfully to: %s", local_path)

        sftp_client.close()
    except Exception as e:
        logging.error("Failed to download backup: %s", e)
        raise


def main():
    """
    Main function to execute the backup workflow.
    """
    try:
        # Establish SSH connection
        ssh_client = create_ssh_client(HOST, USERNAME, PASSWORD)

        # Initiate backup on the server
        remote_backup_path = initiate_backup(ssh_client)

        # Download the backup file to local machine
        download_backup(ssh_client, remote_backup_path, BACKUP_DIR)

        # Close SSH connection
        ssh_client.close()
        logging.info("Backup process completed successfully.")
    except Exception as e:
        logging.error("Backup process failed: %s", e)


if __name__ == "__main__":
    main()
```
