"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://web3-wave.com
Prompt: What are the best practices for backing up my website hosted on LWS?
Generated: DETERMINISTIC_e8f18de2cd75f8dd
Batch ID: 20250612_160600
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

# Configure logging
logging.basicConfig(filename='backup.log', level=logging.INFO,
                    format='%(asctime)s:%(levelname)s:%(message)s')

def backup_website(source_dir, backup_dir):
    """
    Backs up the website located at source_dir to the backup_dir.
    
    Args:
        source_dir (str): The directory of the website to back up.
        backup_dir (str): The directory where the backup will be stored.
        
    Raises:
        FileNotFoundError: If the source directory does not exist.
        PermissionError: If there are permission issues accessing the directories.
    """
    
    # Check if the source directory exists
    if not os.path.exists(source_dir):
        logging.error(f"Source directory '{source_dir}' does not exist.")
        raise FileNotFoundError(f"The source directory '{source_dir}' does not exist.")
    
    # Create a timestamped backup directory
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_path = os.path.join(backup_dir, f"backup_{timestamp}")
    
    try:
        # Create a backup copy of the website
        shutil.copytree(source_dir, backup_path)
        logging.info(f"Backup successful: {backup_path}")
    except PermissionError:
        logging.error(f"Permission denied when accessing '{source_dir}' or '{backup_dir}'.")
        raise
    except Exception as e:
        logging.error(f"An error occurred while backing up: {str(e)}")
        raise

if __name__ == "__main__":
    # Example usage of the backup_website function
    SOURCE_DIR = '/path/to/your/website'  # Change to your website directory
    BACKUP_DIR = '/path/to/backup/location'  # Change to your backup directory

    try:
        backup_website(SOURCE_DIR, BACKUP_DIR)
    except Exception as e:
        print(f"Backup failed: {str(e)}")
```

### Note:
Remember to replace `'/path/to/your/website'` and `'/path/to/backup/location'` with actual paths. This script uses Python's built-in libraries to copy the website directory and logs the backup process.
