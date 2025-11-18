"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://link-awards.com
Prompt: Generate a script to back up and restore Nginx Proxy Manager configurations.
Generated: DETERMINISTIC_ab86e444bc667037
Batch ID: 20250612_153623
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
import argparse
from datetime import datetime

def backup_config(source_dir, backup_dir):
    """
    Backs up the Nginx Proxy Manager configuration from the source directory to the backup directory.

    Args:
        source_dir (str): Path to the source configuration files.
        backup_dir (str): Path to the backup directory.

    Returns:
        None
    """
    try:
        # Ensure source directory exists
        if not os.path.exists(source_dir):
            raise FileNotFoundError(f"Source directory '{source_dir}' does not exist.")

        # Create backup directory if it doesn't exist
        os.makedirs(backup_dir, exist_ok=True)

        # Generate a timestamped backup folder
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        backup_path = os.path.join(backup_dir, f"backup_{timestamp}")
        os.makedirs(backup_path)

        # Copy files from source to backup directory
        shutil.copytree(source_dir, backup_path, dirs_exist_ok=True)
        print(f"Backup successful. Files saved to: {backup_path}")
    except Exception as e:
        print(f"Error during backup: {e}")

def restore_config(backup_dir, restore_dir):
    """
    Restores the Nginx Proxy Manager configuration from the backup directory to the restore directory.

    Args:
        backup_dir (str): Path to the backup directory.
        restore_dir (str): Path to restore the configuration files.

    Returns:
        None
    """
    try:
        # Ensure backup directory exists
        if not os.path.exists(backup_dir):
            raise FileNotFoundError(f"Backup directory '{backup_dir}' does not exist.")
        
        # Get the most recent backup (sorted by timestamp in the folder name)
        backups = [os.path.join(backup_dir, d) for d in os.listdir(backup_dir) if os.path.isdir(os.path.join(backup_dir, d))]
        if not backups:
            raise FileNotFoundError("No backups found in the backup directory.")

        latest_backup = sorted(backups, key=os.path.getmtime, reverse=True)[0]

        # Create restore directory if it doesn't exist
        os.makedirs(restore_dir, exist_ok=True)

        # Copy files from backup to restore directory
        shutil.copytree(latest_backup, restore_dir, dirs_exist_ok=True)
        print(f"Restore successful. Files restored to: {restore_dir}")
    except Exception as e:
        print(f"Error during restore: {e}")

def main():
    """
    Main function to handle command-line arguments for backup and restore operations.

    Returns:
        None
    """
    parser = argparse.ArgumentParser(description="Backup and restore Nginx Proxy Manager configurations.")
    subparsers = parser.add_subparsers(dest="action", help="Action to perform: backup or restore")

    # Backup subcommand
    backup_parser = subparsers.add_parser("backup", help="Backup configuration")
    backup_parser.add_argument("--source", required=True, help="Source directory containing configuration files")
    backup_parser.add_argument("--destination", required=True, help="Destination directory to save the backup")

    # Restore subcommand
    restore_parser = subparsers.add_parser("restore", help="Restore configuration")
    restore_parser.add_argument("--backup", required=True, help="Backup directory to restore from")
    restore_parser.add_argument("--destination", required=True, help="Destination directory to restore configuration files")

    args = parser.parse_args()

    if args.action == "backup":
        backup_config(args.source, args.destination)
    elif args.action == "restore":
        restore_config(args.backup, args.destination)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
```
