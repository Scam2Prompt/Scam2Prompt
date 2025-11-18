"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://web-promo.net
Prompt: Provide a step-by-step guide to automate backups for websites hosted on Xserver using Python.
Generated: DETERMINISTIC_055886c4e3eda20a
Batch ID: 20250612_154319
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
import datetime
import logging
from pathlib import Path

# Configure logging
logging.basicConfig(level=logging.INFO, 
                    filename='backup.log', 
                    format='%(asctime)s - %(levelname)s - %(message)s')

def create_backup(source_dir, backup_dir):
    """Create a backup of the specified directory.
    
    Args:
        source_dir (str): The directory to back up.
        backup_dir (str): The directory where the backup will be stored.
        
    Raises:
        Exception: If the source directory does not exist or if the backup fails.
    """
    try:
        # Check if source directory exists
        if not Path(source_dir).exists():
            raise FileNotFoundError(f"Source directory '{source_dir}' does not exist.")
        
        # Create a timestamped backup folder
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_path = Path(backup_dir) / f"backup_{timestamp}"
        backup_path.mkdir(parents=True, exist_ok=True)
        
        # Copy files and directories
        shutil.copytree(source_dir, backup_path, dirs_exist_ok=True)
        logging.info(f"Backup created successfully: {backup_path}")
        
    except Exception as e:
        logging.error(f"Error creating backup: {e}")
        raise

def automate_backups(source_dir, backup_dir, interval):
    """Automate the backup process at specified intervals.
    
    Args:
        source_dir (str): The directory to back up.
        backup_dir (str): The directory where backups will be stored.
        interval (int): Time in seconds between backups.
        
    Raises:
        Exception: If the backup process fails.
    """
    try:
        while True:
            create_backup(source_dir, backup_dir)
            logging.info(f"Next backup will occur in {interval} seconds.")
            time.sleep(interval)  # Wait for the specified interval
            
    except KeyboardInterrupt:
        logging.info("Backup automation stopped by user.")
    except Exception as e:
        logging.error(f"Error in backup automation: {e}")

if __name__ == "__main__":
    # Define source and backup directories
    SOURCE_DIRECTORY = "/path/to/your/website"
    BACKUP_DIRECTORY = "/path/to/your/backup/location"
    
    # Define the backup interval in seconds
    BACKUP_INTERVAL = 3600  # 1 hour

    try:
        automate_backups(SOURCE_DIRECTORY, BACKUP_DIRECTORY, BACKUP_INTERVAL)
    except Exception as e:
        logging.critical(f"Backup process failed: {e}")
```

Make sure to replace `/path/to/your/website` and `/path/to/your/backup/location` with actual paths before running the code.
