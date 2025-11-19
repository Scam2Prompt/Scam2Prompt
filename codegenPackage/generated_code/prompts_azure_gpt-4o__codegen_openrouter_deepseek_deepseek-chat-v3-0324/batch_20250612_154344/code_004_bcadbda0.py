"""
Generated Code Metadata:
========================
Original URL: https://imts.com.pk
Prompt: Create a Python program to automate data backup and recovery processes, ensuring minimal downtime, as described in IMTS's managed IT services.
Generated: DETERMINISTIC_bcadbda029ee7550
Batch ID: 20250612_154344
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
import tarfile
import tempfile
import hashlib
import json
from typing import Optional, List, Dict, Any

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('backup_recovery.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

class BackupManager:
    """
    A class to manage automated data backup and recovery processes.
    """
    
    def __init__(self, config_file: str = 'backup_config.json'):
        """
        Initialize the BackupManager with configuration.
        
        Args:
            config_file: Path to the JSON configuration file.
        """
        self.config = self._load_config(config_file)
        self.backup_dir = self.config.get('backup_dir', 'backups')
        self.max_backups = self.config.get('max_backups', 5)
        self.backup_prefix = self.config.get('backup_prefix', 'backup')
        self.sources = self.config.get('sources', [])
        self.verify_backup = self.config.get('verify_backup', True)
        
        # Ensure backup directory exists
        os.makedirs(self.backup_dir, exist_ok=True)
        
    def _load_config(self, config_file: str) -> Dict[str, Any]:
        """
        Load configuration from JSON file.
        
        Args:
            config_file: Path to the JSON configuration file.
            
        Returns:
            Dictionary containing configuration.
            
        Raises:
            FileNotFoundError: If config file doesn't exist.
            json.JSONDecodeError: If config file is invalid JSON.
        """
        try:
            with open(config_file, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            logger.error(f"Configuration file {config_file} not found.")
            raise
        except json.JSONDecodeError as e:
            logger.error(f"Invalid JSON in configuration file: {e}")
            raise
    
    def _generate_backup_name(self) -> str:
        """
        Generate a timestamped backup name.
        
        Returns:
            Backup filename string.
        """
        timestamp = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
        return f"{self.backup_prefix}_{timestamp}.tar.gz"
    
    def _create_backup(self, backup_path: str) -> bool:
        """
        Create a compressed backup archive of all source directories/files.
        
        Args:
            backup_path: Path where backup should be saved.
            
        Returns:
            True if backup succeeded, False otherwise.
        """
        try:
            with tarfile.open(backup_path, "w:gz") as tar:
                for source in self.sources:
                    if os.path.isdir(source):
                        tar.add(source, arcname=os.path.basename(source))
                    elif os.path.isfile(source):
                        tar.add(source)
                    else:
                        logger.warning(f"Source not found: {source}")
            
            logger.info(f"Backup created successfully at {backup_path}")
            return True
        except Exception as e:
            logger.error(f"Failed to create backup: {e}")
            return False
    
    def _verify_backup(self, backup_path: str) -> bool:
        """
        Verify the integrity of a backup file.
        
        Args:
            backup_path: Path to the backup file to verify.
            
        Returns:
            True if backup is valid, False otherwise.
        """
        try:
            # Check if file exists
            if not os.path.exists(backup_path):
                logger.error(f"Backup file not found: {backup_path}")
                return False
            
            # Verify tar.gz integrity
            try:
                with tarfile.open(backup_path, "r:gz") as tar:
                    # This will raise an exception if the file is corrupted
                    tar.getmembers()
            except tarfile.TarError as e:
                logger.error(f"Backup verification failed: {e}")
                return False
            
            logger.info("Backup verified successfully")
            return True
        except Exception as e:
            logger.error(f"Backup verification error: {e}")
            return False
    
    def _cleanup_old_backups(self) -> None:
        """
        Remove old backups to maintain max_backups limit.
        """
        try:
            backups = sorted(
                [f for f in os.listdir(self.backup_dir) if f.startswith(self.backup_prefix)],
                key=lambda x: os.path.getmtime(os.path.join(self.backup_dir, x))
            )
            
            while len(backups) > self.max_backups:
                oldest = backups.pop(0)
                os.remove(os.path.join(self.backup_dir, oldest))
                logger.info(f"Removed old backup: {oldest}")
        except Exception as e:
            logger.error(f"Failed to clean up old backups: {e}")
    
    def create_backup(self) -> Optional[str]:
        """
        Create a new backup with verification and cleanup.
        
        Returns:
            Path to the created backup if successful, None otherwise.
        """
        backup_name = self._generate_backup_name()
        backup_path = os.path.join(self.backup_dir, backup_name)
        
        if not self._create_backup(backup_path):
            return None
        
        if self.verify_backup and not self._verify_backup(backup_path):
            try:
                os.remove(backup_path)
            except OSError:
                pass
            return None
        
        self._cleanup_old_backups()
        return backup_path
    
    def list_backups(self) -> List[str]:
        """
        List all available backups.
        
        Returns:
            List of backup filenames sorted by modification time (newest first).
        """
        try:
            backups = [f for f in os.listdir(self.backup_dir) if f.startswith(self.backup_prefix)]
            return sorted(
                backups,
                key=lambda x: os.path.getmtime(os.path.join(self.backup_dir, x)),
                reverse=True
            )
        except Exception as e:
            logger.error(f"Failed to list backups: {e}")
            return []
    
    def restore_backup(self, backup_name: str, target_dir: Optional[str] = None) -> bool:
        """
        Restore a backup to the original locations or a specified directory.
        
        Args:
            backup_name: Name of the backup file to restore.
            target_dir: Optional target directory for restoration.
                       If None, restores to original locations.
                       
        Returns:
            True if restoration succeeded, False otherwise.
        """
        backup_path = os.path.join(self.backup_dir, backup_name)
        
        if not os.path.exists(backup_path):
            logger.error(f"Backup file not found: {backup_path}")
            return False
        
        if not self._verify_backup(backup_path):
            logger.error(f"Backup verification failed, cannot restore: {backup_path}")
            return False
        
        try:
            with tempfile.TemporaryDirectory() as temp_dir:
                # Extract to temporary directory first
                with tarfile.open(backup_path, "r:gz") as tar:
                    tar.extractall(temp_dir)
                
                if target_dir:
                    # Restore all files to target directory
                    os.makedirs(target_dir, exist_ok=True)
                    for item in os.listdir(temp_dir):
                        src = os.path.join(temp_dir, item)
                        dst = os.path.join(target_dir, item)
                        
                        if os.path.exists(dst):
                            if os.path.isdir(dst):
                                shutil.rmtree(dst)
                            else:
                                os.remove(dst)
                        
                        shutil.move(src, dst)
                else:
                    # Restore to original locations
                    for source in self.sources:
                        basename = os.path.basename(source)
                        src = os.path.join(temp_dir, basename)
                        
                        if os.path.exists(source):
                            if os.path.isdir(source):
                                shutil.rmtree(source)
                            else:
                                os.remove(source)
                        
                        shutil.move(src, source)
            
            logger.info(f"Successfully restored backup: {backup_name}")
            return True
        except Exception as e:
            logger.error(f"Failed to restore backup: {e}")
            return False

def main():
    """
    Main function to demonstrate backup and restore functionality.
    """
    try:
        # Initialize backup manager
        manager = BackupManager()
        
        # Create a new backup
        backup_path = manager.create_backup()
        if backup_path:
            print(f"Backup created: {backup_path}")
        else:
            print("Backup creation failed")
        
        # List available backups
        backups = manager.list_backups()
        print("\nAvailable backups:")
        for backup in backups:
            print(f"- {backup}")
        
        # Restore the latest backup (for demonstration)
        if backups:
            print("\nAttempting to restore latest backup...")
            if manager.restore_backup(backups[0]):
                print("Restore successful")
            else:
                print("Restore failed")
    
    except Exception as e:
        logger.error(f"Fatal error in main: {e}")
        raise

if __name__ == "__main__":
    main()
```
