"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://syneoshealthls.com
Prompt: Write a script to automate the process of creating data backups in Plesk for Media Temple hosting.
Generated: DETERMINISTIC_9ceb2b05d1a9403b
Batch ID: 20250612_155200
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import subprocess
import sys
import datetime
from pathlib import Path

# Define constants
BACKUP_STORAGE_PATH = "/path/to/backup/storage"  # Replace with actual path
PLESK_BIN_PATH = "/usr/local/psa/bin"  # Default path to Plesk binaries; check and update if necessary
DOMAIN_NAME = "example.com"  # Replace with your domain name
BACKUP_PASSWORD = "your-secure-password"  # Replace with your secure backup password
RETENTION_DAYS = 7  # Number of days to retain backups

def validate_paths():
    """Validates the Plesk binary path and backup storage path."""
    if not Path(PLESK_BIN_PATH).exists():
        raise FileNotFoundError(f"Plesk binary path does not exist: {PLESK_BIN_PATH}")
    if not Path(BACKUP_STORAGE_PATH).exists():
        raise FileNotFoundError(f"Backup storage path does not exist: {BACKUP_STORAGE_PATH}")

def create_backup():
    """
    Generates a backup for a specified domain in Plesk.
    Uses the 'plesk bin' command to create backups.
    """
    try:
        # Define the backup file name based on the current timestamp
        timestamp = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
        backup_file = f"{BACKUP_STORAGE_PATH}/{DOMAIN_NAME}_{timestamp}.tar"

        # Command to create the backup using Plesk CLI
        command = [
            f"{PLESK_BIN_PATH}/pleskbackup",
            "--domains", DOMAIN_NAME,
            "--output", backup_file,
            "--password", BACKUP_PASSWORD
        ]

        # Execute the backup command
        print("Starting backup...")
        subprocess.run(command, check=True)
        print(f"Backup created successfully: {backup_file}")
    except subprocess.CalledProcessError as e:
        print(f"Failed to create backup: {e}")
        sys.exit(1)

def clean_old_backups():
    """
    Removes backups older than the specified retention period.
    """
    try:
        cutoff_time = datetime.datetime.now() - datetime.timedelta(days=RETENTION_DAYS)

        # Iterate through files in the backup storage path
        for backup_file in Path(BACKUP_STORAGE_PATH).glob(f"{DOMAIN_NAME}_*.tar"):
            # Get the last modified time of the file
            modified_time = datetime.datetime.fromtimestamp(backup_file.stat().st_mtime)

            # Delete files older than the retention period
            if modified_time < cutoff_time:
                print(f"Deleting old backup: {backup_file}")
                backup_file.unlink()
    except Exception as e:
        print(f"Failed to clean old backups: {e}")
        sys.exit(1)

def main():
    """
    Main entry point for the script.
    Validates paths, creates backups, and cleans up old backups.
    """
    try:
        # Validate paths
        validate_paths()

        # Create a new backup
        create_backup()

        # Clean old backups
        clean_old_backups()

        print("Backup process completed successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
```
