"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://syneoshealthls.com
Prompt: Generate code to create a backup of data on a server using the guidelines provided in Media Temple's KnowledgeBase articles.
Generated: DETERMINISTIC_8e47416104e506ac
Batch ID: 20250612_151639
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

def create_backup(source_directory, backup_directory):
    """
    Creates a backup of files from the source_directory to the backup_directory.
    
    Args:
        source_directory (str): Path to the directory to be backed up.
        backup_directory (str): Path to the directory where the backup will be stored.

    Raises:
        FileNotFoundError: If the source directory doesn't exist.
        Exception: If an error occurs during the backup process.
    """
    # Ensure the source directory exists
    if not os.path.exists(source_directory):
        raise FileNotFoundError(f"Source directory '{source_directory}' does not exist.")
    
    # Create the backup directory if it doesn't exist
    if not os.path.exists(backup_directory):
        os.makedirs(backup_directory)

    # Generate a timestamp for the backup
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_path = os.path.join(backup_directory, f"backup_{timestamp}")

    try:
        # Copy the entire source_directory to the new backup directory
        shutil.copytree(source_directory, backup_path)
        print(f"Backup successful! Files copied to '{backup_path}'")
    except shutil.Error as e:
        raise Exception(f"Error during backup: {e}")
    except Exception as e:
        raise Exception(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    # Define source and backup directories
    source_dir = "/path/to/source_directory"  # Replace with the actual source directory path
    backup_dir = "/path/to/backup_directory"  # Replace with the actual backup directory path

    try:
        create_backup(source_dir, backup_dir)
    except FileNotFoundError as fnfe:
        print(fnfe)
    except Exception as e:
        print(e)
```
