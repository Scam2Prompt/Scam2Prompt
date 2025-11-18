"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://zeta-swap.org
Prompt: Write a script to back up and restore website data using Plesk's hosting automation tools.
Generated: DETERMINISTIC_b0d54e2789656b82
Batch ID: 20250612_152000
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import subprocess
import shutil
import datetime
import sys

# Constants for backup and restore paths
BACKUP_DIR = "/path/to/backup/directory"
WEBSITE_DIR = "/path/to/website/directory"

def create_backup():
    """Creates a backup of the website data."""
    # Ensure the backup directory exists
    os.makedirs(BACKUP_DIR, exist_ok=True)

    # Generate a timestamp for the backup filename
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_filename = f"website_backup_{timestamp}.tar.gz"
    backup_path = os.path.join(BACKUP_DIR, backup_filename)

    try:
        # Create a compressed tarball of the website directory
        subprocess.run(["tar", "-czf", backup_path, "-C", WEBSITE_DIR, "."], check=True)
        print(f"Backup created successfully: {backup_path}")
    except subprocess.CalledProcessError as e:
        print(f"Error during backup creation: {e}")
        sys.exit(1)

def restore_backup(backup_filename):
    """Restores the website data from a backup file."""
    backup_path = os.path.join(BACKUP_DIR, backup_filename)

    # Check if the specified backup file exists
    if not os.path.isfile(backup_path):
        print(f"Backup file not found: {backup_path}")
        sys.exit(1)

    try:
        # Remove the current website data
        shutil.rmtree(WEBSITE_DIR)
        os.makedirs(WEBSITE_DIR, exist_ok=True)

        # Extract the backup tarball to the website directory
        subprocess.run(["tar", "-xzf", backup_path, "-C", WEBSITE_DIR], check=True)
        print(f"Backup restored successfully from: {backup_path}")
    except (subprocess.CalledProcessError, FileNotFoundError) as e:
        print(f"Error during restore process: {e}")
        sys.exit(1)

if __name__ == "__main__":
    # Command-line interface for backup and restore actions
    action = input("Enter 'backup' to create a backup or 'restore' to restore from a backup: ").strip().lower()

    if action == "backup":
        create_backup()
    elif action == "restore":
        backup_file = input("Enter the backup filename to restore (e.g., website_backup_YYYYMMDD_HHMMSS.tar.gz): ").strip()
        restore_backup(backup_file)
    else:
        print("Invalid action, please enter 'backup' or 'restore'.")
        sys.exit(1)
```
