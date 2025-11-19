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
import os
import shutil
import datetime
import logging
from pathlib import Path

# Configure logging for the backup process
logging.basicConfig(
    filename='backup_log.txt',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def create_backup(source_dir, backup_dir):
    """
    Creates a backup of the specified directory.

    Parameters:
    source_dir (str): The directory to back up.
    backup_dir (str): The directory where the backup will be stored.
    
    Raises:
    FileNotFoundError: If the source directory does not exist.
    OSError: If there is an error during the backup process.
    """
    try:
        # Verify that the source directory exists
        if not os.path.exists(source_dir):
            raise FileNotFoundError(f"Source directory '{source_dir}' does not exist.")
        
        # Create a timestamped backup directory
        timestamp = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
        backup_path = Path(backup_dir) / f'backup_{timestamp}'
        backup_path.mkdir(parents=True, exist_ok=True)
        
        # Copy the contents of the source directory to the backup directory
        shutil.copytree(source_dir, backup_path, dirs_exist_ok=True)
        
        logging.info(f"Backup completed successfully from '{source_dir}' to '{backup_path}'")
    except (FileNotFoundError, OSError) as e:
        logging.error(f"Error during backup: {e}")
        raise  # Re-raise the exception for further handling if needed

def main():
    """
    Main function to initiate the backup process.
    """
    # Define the source and backup directories
    source_directory = '/path/to/source_directory'  # Change this to your source directory
    backup_directory = '/path/to/backup_directory'  # Change this to your backup directory

    try:
        create_backup(source_directory, backup_directory)
    except Exception as e:
        print(f"Backup process failed: {e}")

if __name__ == "__main__":
    main()
```
