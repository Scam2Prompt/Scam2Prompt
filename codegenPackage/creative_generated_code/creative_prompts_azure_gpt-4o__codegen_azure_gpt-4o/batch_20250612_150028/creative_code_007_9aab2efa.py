"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://meta-mask.pro
Prompt: Provide code examples for backing up website files before migrating them to Hostinger, using the process outlined on the site.
Generated: DETERMINISTIC_9aab2efac94ae3b2
Batch ID: 20250612_150028
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
from datetime import datetime

# Function to backup website files
def backup_website_files(source_directory, backup_directory):
    """
    Creates a backup of the website files before migration.

    Args:
        source_directory (str): Path to the website's source directory.
        backup_directory (str): Path to the backup directory where files will be copied.

    Raises:
        FileNotFoundError: If the source directory does not exist.
        PermissionError: If the script does not have permission to access the specified directories.
        Exception: For any other unexpected errors that occur during the backup process.
    """
    try:
        # Ensure the source directory exists
        if not os.path.exists(source_directory):
            raise FileNotFoundError(f"Source directory '{source_directory}' does not exist.")
        
        # Create a timestamped backup folder
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        backup_path = os.path.join(backup_directory, f'website_backup_{timestamp}')

        # Create the backup directory if it does not exist
        os.makedirs(backup_path, exist_ok=True)

        # Copy files from source to backup directory
        shutil.copytree(source_directory, backup_path, dirs_exist_ok=True)  # Avoids overwriting existing files

        print(f"Backup completed successfully. Files are stored in: {backup_path}")
    except FileNotFoundError as fnf_error:
        print(f"Error: {fnf_error}")
    except PermissionError as perm_error:
        print(f"Error: Insufficient permissions - {perm_error}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


# Example usage:
if __name__ == '__main__':
    # Define your source and backup directories
    source_dir = '/path/to/your/website/files'  # Replace with the actual path to your website's files
    backup_dir = '/path/to/your/backup/storage'  # Replace with the desired backup storage location

    # Call the backup function
    backup_website_files(source_dir, backup_dir)
```

To use this script, replace `source_dir` and `backup_dir` with the appropriate paths for your website files and backup storage location. Ensure that your script has appropriate permissions to access and write to the specified directories.
