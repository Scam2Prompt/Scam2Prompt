"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://openspa.info
Prompt: Write a guide on backing up OpenSPA settings for a Zgemma receiver.
Generated: DETERMINISTIC_f3904d464921ddd1
Batch ID: 20250612_135046
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
logging.basicConfig(
    filename='openSPA_backup.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def backup_openspa_settings(source_directory: str, backup_directory: str) -> None:
    """
    Back up OpenSPA settings from the source directory to the specified backup directory.
    
    Args:
        source_directory (str): The path to the OpenSPA settings directory.
        backup_directory (str): The path to the directory where backups will be stored.
        
    Raises:
        FileNotFoundError: If the source directory does not exist.
        Exception: For other unexpected errors.
    """
    try:
        # Check if source directory exists
        if not os.path.exists(source_directory):
            logging.error(f"Source directory does not exist: {source_directory}")
            raise FileNotFoundError(f"Source directory does not exist: {source_directory}")

        # Create backup directory if it does not exist
        os.makedirs(backup_directory, exist_ok=True)

        # Create a timestamped backup folder
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_folder = os.path.join(backup_directory, f"openspa_backup_{timestamp}")
        os.makedirs(backup_folder)

        # Copy the contents of the source directory to the backup folder
        shutil.copytree(source_directory, backup_folder)
        logging.info(f"Backup successful: {backup_folder}")

    except FileNotFoundError as e:
        logging.error(f"Error during backup: {e}")
    except Exception as e:
        logging.error(f"Unexpected error: {e}")

# Example usage
if __name__ == "__main__":
    # Define the source and backup directories
    source_dir = "/path/to/openspa/settings"  # Replace with your OpenSPA settings directory
    backup_dir = "/path/to/backup/directory"  # Replace with your desired backup directory
    
    # Perform the backup
    backup_openspa_settings(source_dir, backup_dir)
```
