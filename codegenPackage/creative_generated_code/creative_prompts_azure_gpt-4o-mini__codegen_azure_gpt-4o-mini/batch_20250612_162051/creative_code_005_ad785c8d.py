"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jgendreau.fr
Prompt: What are the best practices for backing up a website hosted on LWS, and can you provide a code example for automated backups?
Generated: DETERMINISTIC_ad785c8dbbc2489b
Batch ID: 20250612_162051
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
logging.basicConfig(filename='backup.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def backup_website(source_dir: str, backup_dir: str) -> None:
    """
    Backs up a website by copying its content from the source directory to the backup directory.

    :param source_dir: The directory where the website files are stored.
    :param backup_dir: The directory where the backup files will be saved.
    """
    try:
        # Ensure the source directory exists
        if not os.path.exists(source_dir):
            raise FileNotFoundError(f"Source directory '{source_dir}' does not exist.")

        # Create a timestamped backup directory
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_path = Path(backup_dir) / f"backup_{timestamp}"
        backup_path.mkdir(parents=True, exist_ok=True)

        # Copy the contents of the source directory to the backup directory
        shutil.copytree(source_dir, backup_path, dirs_exist_ok=True)
        
        logging.info(f"Backup completed successfully from '{source_dir}' to '{backup_path}'.")

    except Exception as e:
        logging.error(f"Error occurred during backup: {e}")

if __name__ == "__main__":
    # Define the source and backup directories
    source_directory = "/path/to/your/website"
    backup_directory = "/path/to/your/backup/location"

    # Perform the backup
    backup_website(source_directory, backup_directory)
```
