"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://prize-graph.net
Prompt: Write a script to back up all files from a local directory to Yandex Disk, utilizing its desktop app or browser upload functionality.
Generated: DETERMINISTIC_272031a8ad82abcc
Batch ID: 20250612_152109
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
import sys
from pathlib import Path

def backup_to_yandex_disk(local_directory, yandex_disk_directory):
    """
    Copies all files and directories from the local directory to the Yandex Disk directory.

    Args:
        local_directory (str): Path to the local directory containing files to back up.
        yandex_disk_directory (str): Path to the Yandex Disk directory where files will be copied.

    Raises:
        FileNotFoundError: If the local directory or Yandex Disk directory does not exist.
        PermissionError: If there are insufficient permissions to access a directory or file.
    """
    # Ensure both paths are valid directories
    local_dir_path = Path(local_directory)
    yandex_disk_path = Path(yandex_disk_directory)

    if not local_dir_path.exists() or not local_dir_path.is_dir():
        raise FileNotFoundError(f"Local directory not found: {local_directory}")

    if not yandex_disk_path.exists() or not yandex_disk_path.is_dir():
        raise FileNotFoundError(f"Yandex Disk directory not found: {yandex_disk_directory}")

    try:
        # Walk through the local directory and copy files to Yandex Disk directory
        for root, dirs, files in os.walk(local_dir_path):
            # Calculate relative path to recreate directory structure in Yandex Disk
            relative_path = os.path.relpath(root, local_dir_path)
            target_dir = yandex_disk_path / relative_path

            # Ensure the target directory exists
            target_dir.mkdir(parents=True, exist_ok=True)

            # Copy all files from the current directory to the target directory
            for file in files:
                src_file = Path(root) / file
                dest_file = target_dir / file

                shutil.copy2(src_file, dest_file)  # Copy file with metadata preservation
                print(f"Copied: {src_file} -> {dest_file}")

        print("Backup completed successfully.")

    except PermissionError as perm_err:
        print(f"Permission error: {perm_err}")
        sys.exit(1)
    except Exception as e:
        print(f"An error occurred during backup: {e}")
        sys.exit(1)


if __name__ == "__main__":
    # Example usage
    local_directory = input("Enter the path to the local directory: ").strip()
    yandex_disk_directory = input("Enter the path to the Yandex Disk directory: ").strip()

    try:
        backup_to_yandex_disk(local_directory, yandex_disk_directory)
    except FileNotFoundError as fnf_err:
        print(fnf_err)
        sys.exit(1)
    except Exception as e:
        print(f"Unexpected error: {e}")
        sys.exit(1)
```
