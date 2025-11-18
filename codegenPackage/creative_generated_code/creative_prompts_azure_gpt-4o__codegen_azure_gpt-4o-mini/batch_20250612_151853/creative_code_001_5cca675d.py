"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://smartd.org.ls
Prompt: Provide a Python script to identify and back up WordPress directories like `wp-admin` and `wp-includes` from a server directory listing.
Generated: DETERMINISTIC_5cca675dd32c717d
Batch ID: 20250612_151853
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
import logging
from datetime import datetime

# Set up logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def backup_wordpress_directories(source_directory, backup_directory):
    """
    Backs up specific WordPress directories from a source directory to a backup directory.

    Parameters:
    - source_directory (str): The path to the WordPress installation on the server.
    - backup_directory (str): The path where the backups will be stored.

    Returns:
    - None
    """

    # List of WordPress directories to back up
    directories_to_backup = ['wp-admin', 'wp-includes']

    # Ensure the backup directory exists
    os.makedirs(backup_directory, exist_ok=True)

    for directory in directories_to_backup:
        source_path = os.path.join(source_directory, directory)
        backup_path = os.path.join(backup_directory, f"{directory}-{datetime.now().strftime('%Y%m%d%H%M%S')}")

        try:
            # Check if the source directory exists
            if os.path.exists(source_path):
                # Copy the directory to the backup location
                shutil.copytree(source_path, backup_path)
                logging.info(f"Successfully backed up: {source_path} to {backup_path}")
            else:
                logging.warning(f"Directory not found, skipping backup: {source_path}")

        except Exception as e:
            logging.error(f"Error occurred while backing up {directory}: {e}")

if __name__ == '__main__':
    # Define the source WordPress directory and backup location
    source_wp_directory = '/path/to/wordpress'  # Replace with your actual WordPress path
    backup_wp_directory = '/path/to/backup'      # Replace with your backup path

    # Run the backup function
    backup_wordpress_directories(source_wp_directory, backup_wp_directory)
```
