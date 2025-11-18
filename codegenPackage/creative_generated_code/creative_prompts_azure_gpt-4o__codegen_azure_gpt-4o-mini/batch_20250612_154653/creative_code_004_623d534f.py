"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://smartvalidation.net
Prompt: Develop a script to schedule automatic backups and implement disaster recovery solutions for websites hosted on Smart Validation. Ensure the script can restore data efficiently in case of an outage.
Generated: DETERMINISTIC_623d534f28387777
Batch ID: 20250612_154653
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
import time
import logging
from datetime import datetime
from pathlib import Path

# Configure logging for backup operations
logging.basicConfig(filename='backup.log', level=logging.INFO,
                    format='%(asctime)s:%(levelname)s:%(message)s')

# Constants
BACKUP_DIR = Path('/path/to/backup/directory')  # Change this to your backup directory
SOURCE_DIR = Path('/path/to/website/directory')  # Change this to your website directory
BACKUP_INTERVAL = 86400  # 24 hours in seconds
MAX_BACKUPS = 7  # Keep only the last 7 backups

def create_backup():
    """Creates a backup of the website directory."""
    try:
        # Create a timestamped backup folder
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        backup_path = BACKUP_DIR / f'backup_{timestamp}'
        backup_path.mkdir(parents=True, exist_ok=True)
        
        # Copy the source directory to the backup folder
        shutil.copytree(SOURCE_DIR, backup_path)
        logging.info(f'Backup created at {backup_path}')
        
        # Remove old backups if exceeding max backups
        cleanup_old_backups()
    except Exception as e:
        logging.error(f'Error creating backup: {e}')

def cleanup_old_backups():
    """Removes old backups exceeding the maximum limit."""
    try:
        backups = sorted(BACKUP_DIR.glob('backup_*'), key=os.path.getmtime)
        while len(backups) > MAX_BACKUPS:
            oldest_backup = backups.pop(0)  # Remove the oldest backup
            shutil.rmtree(oldest_backup)
            logging.info(f'Removed old backup: {oldest_backup}')
    except Exception as e:
        logging.error(f'Error cleaning up old backups: {e}')

def restore_backup(backup_folder):
    """Restores the website from a backup folder."""
    try:
        if not (BACKUP_DIR / backup_folder).exists():
            logging.error(f'Backup folder {backup_folder} does not exist.')
            return False
        
        # Remove the current website directory
        shutil.rmtree(SOURCE_DIR)
        
        # Copy the backup files back to the source directory
        shutil.copytree(BACKUP_DIR / backup_folder, SOURCE_DIR)
        logging.info(f'Restored backup from {backup_folder}')
        return True
    except Exception as e:
        logging.error(f'Error restoring backup from {backup_folder}: {e}')
        return False

def main():
    """Main function to schedule backups."""
    while True:
        create_backup()
        time.sleep(BACKUP_INTERVAL)  # Schedule the next backup

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        logging.info('Backup scheduling interrupted by user.')
    except Exception as e:
        logging.error(f'Unexpected error: {e}')
```

**Note:** Ensure to modify the `BACKUP_DIR` and `SOURCE_DIR` constants to point to the correct directories on your server.
