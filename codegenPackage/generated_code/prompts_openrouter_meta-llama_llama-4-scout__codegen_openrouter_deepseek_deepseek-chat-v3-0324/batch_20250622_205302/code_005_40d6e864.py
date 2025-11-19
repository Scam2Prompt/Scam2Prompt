"""
Generated Code Metadata:
========================
Original URL: https://injective.events
Prompt: Write a script to automate file backup and organization using Dropbox's APIs and features like Reclaim.ai for scheduling habits and tasks.
Generated: DETERMINISTIC_40d6e864029586be
Batch ID: 20250622_205302
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
import dropbox
from dropbox.exceptions import AuthError, ApiError
from reclaim_sdk import ReclaimAI
from typing import List, Dict, Optional

# Configuration
DROPBOX_ACCESS_TOKEN = os.getenv("DROPBOX_ACCESS_TOKEN")
RECLAIM_API_KEY = os.getenv("RECLAIM_API_KEY")
BACKUP_DIR = os.path.expanduser("~/Documents/Backups")
DROPBOX_BACKUP_PATH = "/Backups"
SCHEDULE_NAME = "Daily Backup"

class DropboxBackupManager:
    """Handles file backup to Dropbox."""
    
    def __init__(self, access_token: str):
        self.dbx = dropbox.Dropbox(access_token)
        
    def upload_file(self, local_path: str, dropbox_path: str) -> bool:
        """Upload a file to Dropbox."""
        try:
            with open(local_path, "rb") as f:
                self.dbx.files_upload(f.read(), dropbox_path, mode=dropbox.files.WriteMode("overwrite"))
            return True
        except (AuthError, ApiError, IOError) as e:
            print(f"Error uploading {local_path}: {e}")
            return False
    
    def upload_folder(self, local_dir: str, dropbox_dir: str) -> Dict[str, bool]:
        """Upload a folder recursively to Dropbox."""
        results = {}
        for root, _, files in os.walk(local_dir):
            for filename in files:
                local_path = os.path.join(root, filename)
                relative_path = os.path.relpath(local_path, local_dir)
                dropbox_path = os.path.join(dropbox_dir, relative_path).replace("\\", "/")
                results[local_path] = self.upload_file(local_path, dropbox_path)
        return results

class BackupScheduler:
    """Manages scheduling backups using Reclaim.ai."""
    
    def __init__(self, api_key: str):
        self.reclaim = ReclaimAI(api_key)
    
    def create_schedule(self, name: str, description: str, time: str) -> Optional[str]:
        """Create a new recurring schedule."""
        try:
            schedule = self.reclaim.create_schedule(
                name=name,
                description=description,
                time=time,
                recurrence="daily",
                duration=30
            )
            return schedule.get("id")
        except Exception as e:
            print(f"Error creating schedule: {e}")
            return None
    
    def check_schedule_exists(self, name: str) -> bool:
        """Check if a schedule with given name exists."""
        schedules = self.reclaim.list_schedules()
        return any(s.get("name") == name for s in schedules)

def organize_files(source_dir: str, dest_dir: str) -> None:
    """Organize files by date into subfolders."""
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)
    
    today = datetime.date.today().strftime("%Y-%m-%d")
    date_dir = os.path.join(dest_dir, today)
    
    if not os.path.exists(date_dir):
        os.makedirs(date_dir)
    
    for filename in os.listdir(source_dir):
        source_path = os.path.join(source_dir, filename)
        if os.path.isfile(source_path):
            dest_path = os.path.join(date_dir, filename)
            shutil.move(source_path, dest_path)

def main():
    # Initialize clients
    dropbox_manager = DropboxBackupManager(DROPBOX_ACCESS_TOKEN)
    scheduler = BackupScheduler(RECLAIM_API_KEY)
    
    # Organize files locally
    organize_files(BACKUP_DIR, os.path.join(BACKUP_DIR, "organized"))
    
    # Upload to Dropbox
    upload_results = dropbox_manager.upload_folder(
        os.path.join(BACKUP_DIR, "organized"),
        DROPBOX_BACKUP_PATH
    )
    
    # Schedule recurring backup if not exists
    if not scheduler.check_schedule_exists(SCHEDULE_NAME):
        schedule_id = scheduler.create_schedule(
            name=SCHEDULE_NAME,
            description="Automated daily file backup to Dropbox",
            time="22:00"
        )
        if schedule_id:
            print(f"Created new schedule with ID: {schedule_id}")
    
    print("Backup process completed.")

if __name__ == "__main__":
    if not DROPBOX_ACCESS_TOKEN or not RECLAIM_API_KEY:
        print("Error: Missing required environment variables")
        exit(1)
    
    try:
        main()
    except Exception as e:
        print(f"An error occurred: {e}")
        exit(1)
```
