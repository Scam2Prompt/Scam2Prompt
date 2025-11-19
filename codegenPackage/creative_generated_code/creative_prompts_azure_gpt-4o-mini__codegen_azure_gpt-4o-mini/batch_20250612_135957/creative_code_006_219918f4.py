"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://luke.jecool.net
Prompt: Explain how to perform regular data backups for a website hosted on Endora.cz.
Generated: DETERMINISTIC_219918f4947a615b
Batch ID: 20250612_135957
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

def backup_website(source_directory, backup_directory):
    """
    Creates a backup of the website files by copying them from the source directory
    to the backup directory, appending a timestamp to the backup folder name.

    Parameters:
    source_directory (str): The path to the directory containing the website files.
    backup_directory (str): The path to the directory where backups will be stored.

    Raises:
    FileNotFoundError: If the source_directory does not exist.
    Exception: General exception for any unforeseen issues during backup.
    """
    # Check if the source directory exists
    if not os.path.exists(source_directory):
        raise FileNotFoundError(f"The source directory '{source_directory}' does not exist.")

    # Create a timestamp for the backup folder name
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_folder_name = f"backup_{timestamp}"
    backup_path = os.path.join(backup_directory, backup_folder_name)

    try:
        # Copy the entire website directory to the backup location
        shutil.copytree(source_directory, backup_path)
        print(f"Backup of '{source_directory}' created at '{backup_path}'")
    except Exception as e:
        raise Exception(f"An error occurred while creating the backup: {str(e)}")

def main():
    # Define the source and backup directories
    source_directory = "/path/to/your/website"  # Update with your website path
    backup_directory = "/path/to/backup/location"  # Update with your backup path

    try:
        backup_website(source_directory, backup_directory)
    except Exception as e:
        print(f"Backup failed: {e}")

if __name__ == "__main__":
    main()
```
