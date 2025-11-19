"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-93--quirky-shannon-80b532.netlify.app
Prompt: Develop a script that automates system administration tasks, utilizing the knowledge shared by Susan Lunn in the FOSS@RIT community.
Generated: DETERMINISTIC_e5c8316f373108e8
Batch ID: 20250612_163408
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
Automated System Administration Script
Author: [Your Name]
Description:
This script automates common system administration tasks, inspired by the practices shared by Susan Lunn 
in the FOSS@RIT community. The script includes functionality for monitoring system health, managing user accounts, 
and automating backups.
"""

import os
import shutil
import subprocess
import logging
from datetime import datetime

# Configure logging
logging.basicConfig(
    filename="sys_admin.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def check_disk_usage(threshold=80):
    """
    Check disk usage and log an alert if usage exceeds the threshold.
    :param threshold: Percentage threshold to trigger an alert.
    """
    try:
        usage = shutil.disk_usage("/")
        used_percentage = (usage.used / usage.total) * 100
        if used_percentage > threshold:
            logging.warning(f"Disk usage at {used_percentage:.2f}% exceeds the threshold of {threshold}%!")
        else:
            logging.info(f"Disk usage is at {used_percentage:.2f}%.")
    except Exception as e:
        logging.error(f"Error checking disk usage: {e}")

def monitor_memory_usage(threshold=80):
    """
    Monitor memory usage and log an alert if usage exceeds the threshold.
    :param threshold: Percentage threshold to trigger an alert.
    """
    try:
        result = subprocess.run(["free", "-m"], capture_output=True, text=True)
        lines = result.stdout.splitlines()
        mem_info = lines[1].split()
        total_mem = int(mem_info[1])
        used_mem = int(mem_info[2])
        used_percentage = (used_mem / total_mem) * 100
        if used_percentage > threshold:
            logging.warning(f"Memory usage at {used_percentage:.2f}% exceeds the threshold of {threshold}%!")
        else:
            logging.info(f"Memory usage is at {used_percentage:.2f}%.")
    except Exception as e:
        logging.error(f"Error checking memory usage: {e}")

def backup_directory(source_dir, backup_dir):
    """
    Backup a directory to another location.
    :param source_dir: The directory to back up.
    :param backup_dir: The destination directory for the backup.
    """
    try:
        backup_path = os.path.join(backup_dir, f"{os.path.basename(source_dir)}_{datetime.now().strftime('%Y%m%d%H%M%S')}")
        shutil.copytree(source_dir, backup_path)
        logging.info(f"Successfully backed up '{source_dir}' to '{backup_path}'.")
    except Exception as e:
        logging.error(f"Error backing up directory '{source_dir}': {e}")

def manage_user_account(action, username):
    """
    Add or remove a user account.
    :param action: 'add' to create a user account or 'remove' to delete it.
    :param username: The username for the account.
    """
    try:
        if action == "add":
            subprocess.run(["sudo", "useradd", username], check=True)
            logging.info(f"User '{username}' added successfully.")
        elif action == "remove":
            subprocess.run(["sudo", "userdel", username], check=True)
            logging.info(f"User '{username}' removed successfully.")
        else:
            logging.error(f"Invalid action '{action}'. Use 'add' or 'remove'.")
    except Exception as e:
        logging.error(f"Error managing user account '{username}': {e}")

def main():
    """
    Main function to execute the system administration tasks.
    """
    logging.info("Starting system administration tasks...")

    # Check system health
    logging.info("Checking disk usage...")
    check_disk_usage()

    logging.info("Monitoring memory usage...")
    monitor_memory_usage()

    # Backup task
    logging.info("Backing up '/etc' directory...")
    backup_directory("/etc", "/var/backups")

    # User management task
    logging.info("Adding a new user 'example_user'...")
    manage_user_account("add", "example_user")

    logging.info("Removing user 'example_user'...")
    manage_user_account("remove", "example_user")

    logging.info("Completed all tasks.")

if __name__ == "__main__":
    main()
```
