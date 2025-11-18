"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://linkbonus.net
Prompt: Generate code to back up and restore Nginx Proxy Manager configurations programmatically.
Generated: DETERMINISTIC_ecaebb8b67b88411
Batch ID: 20250612_154420
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
import json
from datetime import datetime

# Configuration paths
CONFIG_DIR = "/etc/nginx-proxy-manager"
BACKUP_DIR = "/path/to/backup"

def create_backup():
    """Creates a backup of Nginx Proxy Manager configurations."""
    try:
        # Ensure backup directory exists
        os.makedirs(BACKUP_DIR, exist_ok=True)

        # Generate a timestamped backup folder
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_path = os.path.join(BACKUP_DIR, f"npm_backup_{timestamp}")
        os.makedirs(backup_path)

        # Copy configuration files to the backup folder
        shutil.copytree(CONFIG_DIR, backup_path)
        print(f"Backup created successfully at: {backup_path}")
    except Exception as e:
        print(f"Error creating backup: {e}")

def restore_backup(backup_folder):
    """
    Restores Nginx Proxy Manager configurations from a backup folder.
    Args:
        backup_folder (str): Path to the backup folder to restore.
    """
    try:
        # Validate the backup folder
        if not os.path.exists(backup_folder):
            raise FileNotFoundError(f"Backup folder {backup_folder} does not exist.")

        # Restore configuration by copying files back to the NPM directory
        shutil.copytree(backup_folder, CONFIG_DIR, dirs_exist_ok=True)
        print(f"Backup restored successfully from: {backup_folder}")
    except Exception as e:
        print(f"Error restoring backup: {e}")

def list_backups():
    """Lists all available backups."""
    try:
        if not os.path.exists(BACKUP_DIR):
            print("No backups found.")
            return

        backups = [f for f in os.listdir(BACKUP_DIR) if os.path.isdir(os.path.join(BACKUP_DIR, f))]
        if backups:
            print("Available backups:")
            for backup in backups:
                print(f"- {backup}")
        else:
            print("No backups found.")
    except Exception as e:
        print(f"Error listing backups: {e}")

def main():
    """Main function to interact with the backup and restore system."""
    print("Nginx Proxy Manager Backup and Restore Tool")
    print("1. Create Backup")
    print("2. Restore Backup")
    print("3. List Backups")
    print("4. Exit")

    try:
        choice = int(input("Enter your choice (1-4): "))
        if choice == 1:
            create_backup()
        elif choice == 2:
            backup_folder = input("Enter path to backup folder to restore: ")
            restore_backup(backup_folder)
        elif choice == 3:
            list_backups()
        elif choice == 4:
            print("Exiting...")
        else:
            print("Invalid choice. Please select between 1-4.")
    except ValueError:
        print("Invalid input. Please enter a number between 1-4.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
