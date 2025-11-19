"""
Generated Code Metadata:
========================
Original URL: https://a2ip.ru
Prompt: Write a Python script to automate a simple task, such as data backup or file management, using popular libraries and frameworks.
Generated: DETERMINISTIC_55b01a34190074a2
Batch ID: 20250622_212010
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
import logging
from typing import List, Optional

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('backup_manager.log'),
        logging.StreamHandler()
    ]
)

class BackupManager:
    """
    A class to manage file backups with rotation and logging capabilities.
    """
    
    def __init__(self, source_dir: str, backup_dir: str, max_backups: int = 5):
        """
        Initialize the BackupManager.
        
        Args:
            source_dir: Directory to backup
            backup_dir: Directory where backups will be stored
            max_backups: Maximum number of backups to keep (default: 5)
        """
        self.source_dir = source_dir
        self.backup_dir = backup_dir
        self.max_backups = max_backups
        
        # Validate directories
        if not os.path.isdir(source_dir):
            raise ValueError(f"Source directory does not exist: {source_dir}")
        if not os.path.isdir(backup_dir):
            os.makedirs(backup_dir, exist_ok=True)
            logging.info(f"Created backup directory: {backup_dir}")

    def _get_backup_name(self) -> str:
        """
        Generate a timestamped backup folder name.
        
        Returns:
            str: Backup folder name with timestamp
        """
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        return f"backup_{timestamp}"

    def _get_existing_backups(self) -> List[str]:
        """
        Get a list of existing backups sorted by creation time (oldest first).
        
        Returns:
            List[str]: List of backup folder paths
        """
        backups = []
        for item in os.listdir(self.backup_dir):
            item_path = os.path.join(self.backup_dir, item)
            if os.path.isdir(item_path) and item.startswith("backup_"):
                backups.append((os.path.getctime(item_path), item_path))
        
        # Sort by creation time (oldest first)
        backups.sort()
        return [path for (_, path) in backups]

    def _rotate_backups(self) -> None:
        """
        Rotate backups to maintain only the most recent max_backups.
        """
        existing_backups = self._get_existing_backups()
        if len(existing_backups) <= self.max_backups:
            return
            
        # Remove oldest backups
        backups_to_remove = existing_backups[:len(existing_backups) - self.max_backups]
        for backup in backups_to_remove:
            try:
                shutil.rmtree(backup)
                logging.info(f"Removed old backup: {backup}")
            except Exception as e:
                logging.error(f"Failed to remove backup {backup}: {str(e)}")

    def create_backup(self) -> Optional[str]:
        """
        Create a new backup of the source directory.
        
        Returns:
            Optional[str]: Path to the created backup, or None if failed
        """
        backup_name = self._get_backup_name()
        backup_path = os.path.join(self.backup_dir, backup_name)
        
        try:
            # Copy the directory tree
            shutil.copytree(self.source_dir, backup_path)
            logging.info(f"Created backup: {backup_path}")
            
            # Rotate old backups
            self._rotate_backups()
            
            return backup_path
        except Exception as e:
            logging.error(f"Backup failed: {str(e)}")
            return None

def main():
    """
    Example usage of the BackupManager.
    """
    try:
        # Example configuration - replace with your actual paths
        source_directory = "/path/to/source"
        backup_directory = "/path/to/backups"
        
        backup_manager = BackupManager(
            source_dir=source_directory,
            backup_dir=backup_directory,
            max_backups=3
        )
        
        result = backup_manager.create_backup()
        if result:
            print(f"Backup created successfully at: {result}")
        else:
            print("Backup failed. Check logs for details.")
            
    except Exception as e:
        logging.error(f"Application error: {str(e)}")
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()
```
