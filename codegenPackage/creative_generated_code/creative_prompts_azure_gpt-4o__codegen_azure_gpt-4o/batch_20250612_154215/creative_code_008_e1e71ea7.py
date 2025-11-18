"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://agromec.cl
Prompt: Write a script to automate backups for websites hosted on a Linux-based hosting service in Chile.
Generated: DETERMINISTIC_e1e71ea70c66d12e
Batch ID: 20250612_154215
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
#!/usr/bin/env python3

"""
Website Backup Automation Script

This script automates the backup process for websites hosted on a Linux-based hosting service.
It compresses website files and databases, saves the backups locally, and optionally uploads them to a remote server.

Author: Your Name
Date: YYYY-MM-DD
"""

import os
import subprocess
import datetime
import logging
import shutil
import tarfile

# Configuration
BACKUP_DIR = "/path/to/backup/directory"  # Local directory to store backups
WEBSITES = [
    {
        "name": "example_site",
        "path": "/var/www/example_site",  # Path to website files
        "db": {
            "name": "example_db",         # Database name
            "user": "db_user",            # Database user
            "password": "db_password",    # Database password
            "host": "localhost",          # Database host
        },
    },
    # Add more websites here as needed
]
REMOTE_BACKUP_ENABLED = True  # Set to False to disable remote backups
REMOTE_SERVER = {
    "host": "192.168.1.100",  # Remote server IP or hostname
    "user": "remote_user",    # Remote server user
    "port": 22,               # SSH port (default: 22)
    "remote_dir": "/path/to/remote/backup/directory",
}

# Logging configuration
LOG_FILE = "/var/log/website_backup.log"
logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

def create_backup_dir():
    """Create the backup directory if it doesn't exist."""
    if not os.path.exists(BACKUP_DIR):
        os.makedirs(BACKUP_DIR)
        logging.info(f"Created backup directory: {BACKUP_DIR}")

def backup_website_files(website_name, website_path):
    """Compress website files into a tar.gz archive."""
    logging.info(f"Starting backup of website files for {website_name}")
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    archive_name = f"{website_name}_files_{timestamp}.tar.gz"
    archive_path = os.path.join(BACKUP_DIR, archive_name)

    try:
        with tarfile.open(archive_path, "w:gz") as tar:
            tar.add(website_path, arcname=os.path.basename(website_path))
        logging.info(f"Website files backup completed: {archive_path}")
    except Exception as e:
        logging.error(f"Error during website files backup for {website_name}: {e}")
        raise

    return archive_path

def backup_database(db_config, website_name):
    """Dump the database to a SQL file."""
    logging.info(f"Starting database backup for {website_name}")
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    dump_name = f"{website_name}_db_{timestamp}.sql"
    dump_path = os.path.join(BACKUP_DIR, dump_name)

    try:
        command = [
            "mysqldump",
            f"--user={db_config['user']}",
            f"--password={db_config['password']}",
            f"--host={db_config['host']}",
            db_config["name"],
        ]
        with open(dump_path, "w") as dump_file:
            subprocess.run(command, check=True, stdout=dump_file)
        logging.info(f"Database backup completed: {dump_path}")
    except subprocess.CalledProcessError as e:
        logging.error(f"Error during database backup for {website_name}: {e}")
        raise

    return dump_path

def upload_backup_to_remote_server(local_path, remote_config):
    """Upload backup file to a remote server using SCP."""
    logging.info(f"Uploading {local_path} to remote server {remote_config['host']}")
    try:
        command = [
            "scp",
            "-P", str(remote_config["port"]),
            local_path,
            f"{remote_config['user']}@{remote_config['host']}:{remote_config['remote_dir']}",
        ]
        subprocess.run(command, check=True)
        logging.info(f"Successfully uploaded {local_path} to remote server")
    except subprocess.CalledProcessError as e:
        logging.error(f"Error during upload to remote server: {e}")
        raise

def main():
    """Main function to orchestrate the backup process."""
    logging.info("Website backup script started")
    create_backup_dir()

    for website in WEBSITES:
        try:
            # Backup website files
            files_archive = backup_website_files(website["name"], website["path"])

            # Backup database
            db_dump = backup_database(website["db"], website["name"])

            # Upload backups to remote server if enabled
            if REMOTE_BACKUP_ENABLED:
                upload_backup_to_remote_server(files_archive, REMOTE_SERVER)
                upload_backup_to_remote_server(db_dump, REMOTE_SERVER)
        except Exception as e:
            logging.error(f"Backup process failed for {website['name']}: {e}")

    logging.info("Website backup script completed")

if __name__ == "__main__":
    main()
```
