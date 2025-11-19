"""
Generated Code Metadata:
========================
Original URL: https://allinonesync.com
Prompt: Generate code to integrate All In One Sync with an existing file management system.
Generated: DETERMINISTIC_756a5f78823b96b2
Batch ID: 20250612_161119
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
import logging
from typing import List, Dict, Optional
from pathlib import Path
from datetime import datetime

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger('AllInOneSync')

class FileManager:
    """Core file management operations."""
    
    def __init__(self, root_path: str):
        self.root_path = Path(root_path)
        if not self.root_path.exists():
            raise FileNotFoundError(f"Root path {root_path} does not exist")
    
    def list_files(self, recursive: bool = False) -> List[Path]:
        """List files in directory."""
        if recursive:
            return list(self.root_path.rglob('*'))
        return list(self.root_path.glob('*'))
    
    def copy_file(self, src: Path, dest: Path) -> bool:
        """Copy file from src to dest."""
        try:
            shutil.copy2(src, dest)
            logger.info(f"Copied {src} to {dest}")
            return True
        except Exception as e:
            logger.error(f"Failed to copy {src} to {dest}: {str(e)}")
            return False
    
    def delete_file(self, file_path: Path) -> bool:
        """Delete a file."""
        try:
            if file_path.is_file():
                file_path.unlink()
                logger.info(f"Deleted {file_path}")
                return True
            return False
        except Exception as e:
            logger.error(f"Failed to delete {file_path}: {str(e)}")
            return False
    
    def get_file_metadata(self, file_path: Path) -> Dict:
        """Get file metadata."""
        if not file_path.exists():
            raise FileNotFoundError(f"File {file_path} does not exist")
        
        stat = file_path.stat()
        return {
            'path': str(file_path),
            'size': stat.st_size,
            'modified': datetime.fromtimestamp(stat.st_mtime),
            'created': datetime.fromtimestamp(stat.st_ctime)
        }

class AllInOneSync:
    """Integration with All In One Sync service."""
    
    def __init__(self, file_manager: FileManager, sync_dir: str):
        self.file_manager = file_manager
        self.sync_dir = Path(sync_dir)
        self._ensure_sync_dir()
    
    def _ensure_sync_dir(self) -> None:
        """Ensure sync directory exists."""
        if not self.sync_dir.exists():
            self.sync_dir.mkdir(parents=True, exist_ok=True)
            logger.info(f"Created sync directory at {self.sync_dir}")
    
    def sync_files(self, files: List[Path]) -> Dict[str, bool]:
        """Sync files to All In One Sync directory."""
        results = {}
        for file in files:
            if not file.exists():
                logger.warning(f"File {file} does not exist, skipping")
                results[str(file)] = False
                continue
            
            dest = self.sync_dir / file.name
            if dest.exists():
                logger.warning(f"File {dest} already exists, skipping")
                results[str(file)] = False
                continue
                
            success = self.file_manager.copy_file(file, dest)
            results[str(file)] = success
        
        return results
    
    def cleanup_sync_dir(self, older_than_days: int = 30) -> int:
        """Clean up files in sync directory older than specified days."""
        cutoff = datetime.now().timestamp() - (older_than_days * 86400)
        deleted_count = 0
        
        for file in self.sync_dir.glob('*'):
            if file.is_file() and file.stat().st_mtime < cutoff:
                if self.file_manager.delete_file(file):
                    deleted_count += 1
        
        logger.info(f"Deleted {deleted_count} old files from sync directory")
        return deleted_count

def main():
    try:
        # Initialize file manager with your existing system's root path
        file_manager = FileManager('/path/to/your/files')
        
        # Initialize sync service
        sync_service = AllInOneSync(file_manager, '/path/to/sync/directory')
        
        # Example usage
        files_to_sync = file_manager.list_files(recursive=True)
        sync_results = sync_service.sync_files(files_to_sync[:5])  # Sync first 5 files
        
        # Clean up old files
        sync_service.cleanup_sync_dir(older_than_days=30)
        
    except Exception as e:
        logger.error(f"Error in main execution: {str(e)}", exc_info=True)

if __name__ == '__main__':
    main()
```
