"""
Generated Code Metadata:
========================
Original URL: https://allinonesync.com
Prompt: "Write a Python script that demonstrates how to synchronize data across different platforms, akin to the functionality of All In One Sync."
Generated: DETERMINISTIC_81914be416b3617f
Batch ID: 20250622_212204
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
import hashlib
import json
from datetime import datetime
import logging
from logging.handlers import RotatingFileHandler
from typing import Dict, List, Optional, Tuple

# Configuration constants
CONFIG_FILE = "sync_config.json"
LOG_FILE = "sync_log.log"
MAX_LOG_SIZE = 5 * 1024 * 1024  # 5MB
BACKUP_COUNT = 3

# Setup logging
def setup_logging() -> None:
    """Configure logging with rotation."""
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=[
            RotatingFileHandler(
                LOG_FILE,
                maxBytes=MAX_LOG_SIZE,
                backupCount=BACKUP_COUNT
            ),
            logging.StreamHandler()
        ]
    )

class SyncManager:
    """Manages synchronization between different platforms."""
    
    def __init__(self) -> None:
        """Initialize SyncManager with configuration."""
        self.config: Dict = self._load_config()
        self.last_sync: Optional[datetime] = None
        self.file_hashes: Dict[str, str] = {}
        
    def _load_config(self) -> Dict:
        """Load synchronization configuration from file."""
        try:
            with open(CONFIG_FILE, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            logging.error("Configuration file not found. Creating default.")
            default_config = {
                "source_dirs": [],
                "target_dirs": [],
                "exclude_extensions": [".tmp", ".bak"],
                "sync_interval": 3600  # 1 hour
            }
            self._save_config(default_config)
            return default_config
        except json.JSONDecodeError:
            logging.error("Invalid configuration file. Using defaults.")
            return {
                "source_dirs": [],
                "target_dirs": [],
                "exclude_extensions": [".tmp", ".bak"],
                "sync_interval": 3600
            }
    
    def _save_config(self, config: Dict) -> None:
        """Save configuration to file."""
        try:
            with open(CONFIG_FILE, 'w') as f:
                json.dump(config, f, indent=4)
        except IOError as e:
            logging.error(f"Failed to save configuration: {e}")
    
    def _calculate_file_hash(self, file_path: str) -> str:
        """Calculate SHA-256 hash of a file."""
        sha256 = hashlib.sha256()
        try:
            with open(file_path, 'rb') as f:
                while chunk := f.read(4096):
                    sha256.update(chunk)
            return sha256.hexdigest()
        except IOError as e:
            logging.error(f"Error calculating hash for {file_path}: {e}")
            return ""
    
    def _should_sync_file(self, file_path: str) -> bool:
        """Determine if a file should be synchronized."""
        if not os.path.isfile(file_path):
            return False
        
        _, ext = os.path.splitext(file_path)
        if ext.lower() in self.config["exclude_extensions"]:
            return False
            
        current_hash = self._calculate_file_hash(file_path)
        if not current_hash:
            return False
            
        last_hash = self.file_hashes.get(file_path, "")
        return current_hash != last_hash
    
    def _sync_file(self, source_path: str, target_path: str) -> bool:
        """Synchronize a single file from source to target."""
        try:
            os.makedirs(os.path.dirname(target_path), exist_ok=True)
            shutil.copy2(source_path, target_path)
            logging.info(f"Synced {source_path} to {target_path}")
            return True
        except (IOError, OSError) as e:
            logging.error(f"Failed to sync {source_path} to {target_path}: {e}")
            return False
    
    def _scan_directory(self, dir_path: str) -> List[Tuple[str, str]]:
        """Scan directory for files that need synchronization."""
        files_to_sync = []
        for root, _, files in os.walk(dir_path):
            for file in files:
                full_path = os.path.join(root, file)
                if self._should_sync_file(full_path):
                    files_to_sync.append((full_path, self._calculate_file_hash(full_path)))
        return files_to_sync
    
    def sync_all(self) -> None:
        """Perform synchronization across all configured directories."""
        logging.info("Starting synchronization process")
        
        # Update file hashes from last sync
        for source_dir in self.config["source_dirs"]:
            for file_path, file_hash in self._scan_directory(source_dir):
                self.file_hashes[file_path] = file_hash
        
        # Perform sync operations
        for source_dir in self.config["source_dirs"]:
            for target_dir in self.config["target_dirs"]:
                for root, _, files in os.walk(source_dir):
                    for file in files:
                        source_path = os.path.join(root, file)
                        if not self._should_sync_file(source_path):
                            continue
                            
                        rel_path = os.path.relpath(source_path, source_dir)
                        target_path = os.path.join(target_dir, rel_path)
                        
                        if self._sync_file(source_path, target_path):
                            self.file_hashes[source_path] = self._calculate_file_hash(source_path)
        
        self.last_sync = datetime.now()
        logging.info("Synchronization completed")

def main() -> None:
    """Main function to run the synchronization."""
    setup_logging()
    try:
        sync_manager = SyncManager()
        sync_manager.sync_all()
    except Exception as e:
        logging.error(f"Fatal error during synchronization: {e}", exc_info=True)

if __name__ == "__main__":
    main()
```
