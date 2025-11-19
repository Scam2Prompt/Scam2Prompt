"""
Generated Code Metadata:
========================
Original URL: https://openspa.info
Prompt: Write a guide on backing up OpenSPA settings for a Zgemma receiver.
Generated: DETERMINISTIC_f3904d464921ddd1
Batch ID: 20250612_135046
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
#!/usr/bin/env python3
"""
OpenSPA Backup Script for Zgemma Receivers

This script automates the backup of OpenSPA settings on a Zgemma receiver.
It creates a compressed archive of the settings directory and saves it to a specified location.
"""

import os
import tarfile
import datetime
import shutil
import logging
from pathlib import Path

# Configuration
SETTINGS_DIR = "/etc/enigma2"
BACKUP_DIR = "/media/hdd/backups"
LOG_FILE = "/var/log/openspa_backup.log"

def setup_logging():
    """Configure logging for the backup script."""
    logging.basicConfig(
        filename=LOG_FILE,
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )
    logging.info("OpenSPA Backup Script Started")

def create_backup_directory():
    """Create backup directory if it doesn't exist."""
    try:
        Path(BACKUP_DIR).mkdir(parents=True, exist_ok=True)
        logging.info(f"Backup directory ready: {BACKUP_DIR}")
    except Exception as e:
        logging.error(f"Failed to create backup directory: {e}")
        raise

def validate_settings_directory():
    """Verify that settings directory exists and is accessible."""
    if not os.path.isdir(SETTINGS_DIR):
        logging.error(f"Settings directory not found: {SETTINGS_DIR}")
        raise FileNotFoundError(f"Settings directory not found: {SETTINGS_DIR}")
    if not os.access(SETTINGS_DIR, os.R_OK):
        logging.error(f"No read permissions for: {SETTINGS_DIR}")
        raise PermissionError(f"No read permissions for: {SETTINGS_DIR}")

def create_backup():
    """Create a compressed backup of the settings directory."""
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_filename = f"openspa_settings_{timestamp}.tar.gz"
    backup_path = os.path.join(BACKUP_DIR, backup_filename)

    try:
        with tarfile.open(backup_path, "w:gz") as tar:
            tar.add(SETTINGS_DIR, arcname=os.path.basename(SETTINGS_DIR))
        logging.info(f"Backup created successfully: {backup_path}")
        return backup_path
    except Exception as e:
        logging.error(f"Failed to create backup: {e}")
        raise

def cleanup_old_backups(max_backups=5):
    """Remove old backups, keeping only the specified number of most recent ones."""
    try:
        backups = sorted(Path(BACKUP_DIR).glob("openspa_settings_*.tar.gz"), key=os.path.getmtime)
        if len(backups) > max_backups:
            for old_backup in backups[:-max_backups]:
                os.remove(old_backup)
                logging.info(f"Removed old backup: {old_backup}")
    except Exception as e:
        logging.error(f"Error during backup cleanup: {e}")

def main():
    """Main function to execute the backup process."""
    try:
        setup_logging()
        create_backup_directory()
        validate_settings_directory()
        backup_path = create_backup()
        cleanup_old_backups()
        logging.info("Backup process completed successfully")
        print(f"Backup created: {backup_path}")
    except Exception as e:
        logging.error(f"Backup failed: {e}")
        print(f"Error: {e}")
        return 1
    return 0

if __name__ == "__main__":
    exit(main())
```
