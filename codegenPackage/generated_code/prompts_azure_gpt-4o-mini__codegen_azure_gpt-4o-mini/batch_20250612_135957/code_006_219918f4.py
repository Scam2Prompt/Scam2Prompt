"""
Generated Code Metadata:
========================
Original URL: https://luke.jecool.net
Prompt: Explain how to perform regular data backups for a website hosted on Endora.cz.
Generated: DETERMINISTIC_219918f4947a615b
Batch ID: 20250612_135957
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import shutil
import datetime
import logging

# Configure logging
logging.basicConfig(filename='backup.log', level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

def create_backup(source_dir, backup_dir):
    """
    Create a backup of the specified directory.

    :param source_dir: The directory to back up.
    :param backup_dir: The directory where the backup will be stored.
    :raises FileNotFoundError: If the source directory does not exist.
    :raises Exception: For any other errors that occur during backup.
    """
    try:
        # Check if the source directory exists
        if not os.path.exists(source_dir):
            raise FileNotFoundError(f"Source directory '{source_dir}' does not exist.")

        # Create a timestamped backup directory
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_path = os.path.join(backup_dir, f"backup_{timestamp}")

        # Copy the source directory to the backup path
        shutil.copytree(source_dir, backup_path)
        logging.info(f"Backup created successfully at '{backup_path}'.")

    except FileNotFoundError as fnf_error:
        logging.error(fnf_error)
        print(fnf_error)
    except Exception as e:
        logging.error(f"An error occurred during backup: {e}")
        print(f"An error occurred during backup: {e}")

if __name__ == "__main__":
    # Define the source and backup directories
    source_directory = "/path/to/your/website"  # Change this to your website's directory
    backup_directory = "/path/to/backup/location"  # Change this to your desired backup location

    # Perform the backup
    create_backup(source_directory, backup_directory)
```

Make sure to replace `"/path/to/your/website"` and `"/path/to/backup/location"` with the actual paths relevant to your setup before running the code.
