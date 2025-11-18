"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://giacotex.cl
Prompt: Write a script to automate backups for a website hosted on a Windows ASP hosting service, ensuring compatibility with Chilean hosting providers.
Generated: DETERMINISTIC_9cecf77c7353898d
Batch ID: 20250612_154331
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
import sys

# Configure logging
logging.basicConfig(level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    handlers=[logging.FileHandler("backup.log"),
                              logging.StreamHandler(sys.stdout)])

def create_backup(source_dir, backup_dir):
    """Create a backup of the specified source directory.

    Args:
        source_dir (str): The directory to back up.
        backup_dir (str): The directory where the backup will be stored.

    Raises:
        FileNotFoundError: If the source directory does not exist.
        Exception: For any other errors during the backup process.
    """
    if not os.path.exists(source_dir):
        logging.error(f"Source directory does not exist: {source_dir}")
        raise FileNotFoundError(f"Source directory does not exist: {source_dir}")

    # Create a timestamped backup folder
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_folder = os.path.join(backup_dir, f"backup_{timestamp}")
    
    try:
        logging.info(f"Creating backup from {source_dir} to {backup_folder}")
        shutil.copytree(source_dir, backup_folder)
        logging.info(f"Backup completed successfully: {backup_folder}")
    except Exception as e:
        logging.error(f"Error during backup: {e}")
        raise

def main():
    # Define source and backup directories
    # Modify these paths as necessary for your environment
    source_directory = r"C:\inetpub\wwwroot\mywebsite"  # Path to the website root
    backup_directory = r"D:\Backups\MyWebsite"           # Path where backups will be stored

    # Ensure backup directory exists
    os.makedirs(backup_directory, exist_ok=True)

    try:
        create_backup(source_directory, backup_directory)
    except FileNotFoundError as e:
        logging.error(e)
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
