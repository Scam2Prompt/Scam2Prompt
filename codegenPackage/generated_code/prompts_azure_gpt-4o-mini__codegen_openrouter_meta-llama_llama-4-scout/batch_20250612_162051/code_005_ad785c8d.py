"""
Generated Code Metadata:
========================
Original URL: https://jgendreau.fr
Prompt: What are the best practices for backing up a website hosted on LWS, and can you provide a code example for automated backups?
Generated: DETERMINISTIC_ad785c8dbbc2489b
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# website_backup.py

import os
import datetime
import paramiko
import tarfile
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def connect_to_ftp(host, username, password):
    """
    Establish a connection to the FTP server.

    Args:
        host (str): FTP host
        username (str): FTP username
        password (str): FTP password

    Returns:
        paramiko.SFTPClient: SFTP client object
    """
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(host, username=username, password=password)
        sftp = ssh.open_sftp()
        return sftp
    except paramiko.AuthenticationException:
        logging.error("Authentication failed. Check your credentials.")
        return None
    except Exception as e:
        logging.error(f"An error occurred: {e}")
        return None

def backup_website(sftp, website_dir, backup_dir):
    """
    Backup the website.

    Args:
        sftp (paramiko.SFTPClient): SFTP client object
        website_dir (str): Website directory on the server
        backup_dir (str): Local backup directory
    """
    try:
        # Create a timestamped backup file
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_file = f"backup_{timestamp}.tar.gz"

        # Create a local backup directory if it doesn't exist
        if not os.path.exists(backup_dir):
            os.makedirs(backup_dir)

        # Change to the website directory
        sftp.chdir(website_dir)

        # Get a list of files in the website directory
        files = sftp.listdir()

        # Create a tarball of the website directory
        with tarfile.open(os.path.join(backup_dir, backup_file), 'w:gz') as tar:
            for file in files:
                tar.addfile(tarfile.TarInfo(file), sftp.open(file))

        logging.info(f"Backup created: {backup_file}")
    except Exception as e:
        logging.error(f"An error occurred: {e}")

def main():
    # LWS FTP credentials
    host = 'your-lws-host'
    username = 'your-lws-username'
    password = 'your-lws-password'

    # Website directory on the server
    website_dir = '/path/to/your/website'

    # Local backup directory
    backup_dir = '/path/to/your/backup/dir'

    sftp = connect_to_ftp(host, username, password)
    if sftp:
        backup_website(sftp, website_dir, backup_dir)
        sftp.close()

if __name__ == "__main__":
    main()
```

```bash
# automated_backup.sh

#!/bin/bash

# Set up cron job to run the script daily
# 0 0 * * * python /path/to/website_backup.py

# Run the Python script
python /path/to/website_backup.py
```

To set up a cron job:

```bash
crontab -e
```

Add the following line:

```
0 0 * * * python /path/to/website_backup.py
```
