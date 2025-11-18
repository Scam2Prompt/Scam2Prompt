"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://optimismai.live
Prompt: Create a script to back up LiteSpeed Web Server configuration files and restore them when needed.
Generated: DETERMINISTIC_a86d1f3f15ad23fd
Batch ID: 20250612_153849
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

# Define constants for the backup and restore process
CONFIG_DIR = "/usr/local/lsws/conf"  # Path to LiteSpeed Web Server configuration directory
BACKUP_DIR = "/usr/local/lsws/conf_backups"  # Path to store backups
TIMESTAMP_FORMAT = "%Y%m%d_%H%M%S"  # Timestamp format for backup naming


def create_backup():
    """
    Creates a backup of the LiteSpeed Web Server configuration files.
    The backup is stored in a timestamped directory inside BACKUP_DIR.
    """
    try:
        # Ensure BACKUP_DIR exists, create it if necessary
        if not os.path.exists(BACKUP_DIR):
            os.makedirs(BACKUP_DIR)
        
        # Generate a timestamped backup folder name
        timestamp = datetime.datetime.now().strftime(TIMESTAMP_FORMAT)
        backup_path = os.path.join(BACKUP_DIR, f"conf_backup_{timestamp}")
        
        # Copy the configuration directory to the backup location
        shutil.copytree(CONFIG_DIR, backup_path)
        
        print(f"Backup created successfully at: {backup_path}")
    except shutil.Error as e:
        print(f"Error during backup: {e}")
    except FileNotFoundError as e:
        print(f"Configuration directory not found: {e}")


def restore_backup(backup_name):
    """
    Restores a backup of the LiteSpeed Web Server configuration files.
    
    :param backup_name: Name of the backup directory to restore from (e.g., 'conf_backup_YYYYMMDD_HHMMSS')
    """
    try:
        backup_path = os.path.join(BACKUP_DIR, backup_name)
        
        # Check if the specified backup exists
        if not os.path.exists(backup_path):
            raise FileNotFoundError(f"Backup '{backup_name}' does not exist.")
        
        # Restore the backup by copying its contents to the original configuration directory
        if os.path.exists(CONFIG_DIR):
            # Backup the current configuration before restoring
            current_backup_path = os.path.join(BACKUP_DIR, "conf_current_backup")
            shutil.copytree(CONFIG_DIR, current_backup_path)
            print(f"Existing configuration backed up at: {current_backup_path}")
            
            # Remove the current configuration directory
            shutil.rmtree(CONFIG_DIR)
        
        shutil.copytree(backup_path, CONFIG_DIR)
        print(f"Backup '{backup_name}' restored successfully.")
    except shutil.Error as e:
        print(f"Error during restoration: {e}")
    except FileNotFoundError as e:
        print(f"Error: {e}")


def list_backups():
    """
    Lists all available backups stored in the BACKUP_DIR.
    """
    try:
        # Ensure the backup directory exists
        if not os.path.exists(BACKUP_DIR):
            print("No backups found.")
            return
        
        backups = os.listdir(BACKUP_DIR)
        if backups:
            print("Available backups:")
            for backup in backups:
                print(f" - {backup}")
        else:
            print("No backups found.")
    except OSError as e:
        print(f"Error listing backups: {e}")


if __name__ == "__main__":
    # Main menu for the backup and restore script
    print("LiteSpeed Web Server Backup Script")
    print("1. Create Backup")
    print("2. Restore Backup")
    print("3. List Backups")
    print("4. Exit")
    
    try:
        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            create_backup()
        elif choice == 2:
            backup_name = input("Enter the name of the backup to restore: ")
            restore_backup(backup_name)
        elif choice == 3:
            list_backups()
        elif choice == 4:
            print("Exiting...")
        else:
            print("Invalid choice.")
    except ValueError:
        print("Invalid input. Please enter a number.")
```
