"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metamark.lt
Prompt: Develop a script to automate backups for a WordPress website, incorporating features similar to those mentioned by Metamark for website protection.
Generated: DETERMINISTIC_7a9b4070f77faefd
Batch ID: 20250612_150323
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
import argparse

def create_backup(source_dir, backup_dir):
    """
    Creates a backup of the WordPress website by copying files from the source directory to the backup directory.
    
    Args:
        source_dir (str): Path to the WordPress installation directory.
        backup_dir (str): Path to the directory where backups should be stored.

    Returns:
        str: Path to the newly created backup directory.
    """
    try:
        # Ensure source directory exists
        if not os.path.exists(source_dir):
            raise FileNotFoundError(f"Source directory '{source_dir}' does not exist.")

        # Create a timestamped backup directory
        timestamp = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
        new_backup_dir = os.path.join(backup_dir, f"wp_backup_{timestamp}")
        os.makedirs(new_backup_dir)

        # Copy all files and subdirectories from source to the backup directory
        shutil.copytree(source_dir, new_backup_dir, dirs_exist_ok=True)

        print(f"Backup successfully created at: {new_backup_dir}")
        return new_backup_dir

    except Exception as e:
        print(f"Error while creating backup: {e}")
        raise

def main():
    """
    Main function for automating WordPress backups.
    """
    # Argument parser for user input
    parser = argparse.ArgumentParser(description="Automate backups for a WordPress website.")
    parser.add_argument("--source_dir", required=True, help="Path to the WordPress installation directory.")
    parser.add_argument("--backup_dir", required=True, help="Path to the directory where backups should be stored.")
    args = parser.parse_args()

    # Perform the backup
    try:
        print("Starting WordPress backup process...")
        create_backup(args.source_dir, args.backup_dir)
        print("Backup process completed successfully.")
    except Exception as e:
        print(f"Backup process failed: {e}")

if __name__ == "__main__":
    main()
```
