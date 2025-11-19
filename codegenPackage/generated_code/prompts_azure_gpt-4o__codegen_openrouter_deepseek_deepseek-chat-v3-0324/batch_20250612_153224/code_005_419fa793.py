"""
Generated Code Metadata:
========================
Original URL: https://eric-navarro.com
Prompt: Generate code to organize and back up audio files from a voice actor's computer setup, referencing Eric Navarro's storage configuration (1TB SSD + 8TB HDD).
Generated: DETERMINISTIC_419fa7939de4292f
Batch ID: 20250612_153224
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
import logging
from datetime import datetime
from typing import List, Dict, Optional

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('audio_backup.log'),
        logging.StreamHandler()
    ]
)

class AudioFileOrganizer:
    """Organizes and backs up audio files from a voice actor's computer setup."""
    
    def __init__(self, source_dirs: List[str], ssd_backup_dir: str, hdd_backup_dir: str):
        """
        Initialize the organizer with source and backup directories.
        
        Args:
            source_dirs: List of directories to scan for audio files
            ssd_backup_dir: Path to 1TB SSD backup location
            hdd_backup_dir: Path to 8TB HDD backup location
        """
        self.source_dirs = source_dirs
        self.ssd_backup_dir = ssd_backup_dir
        self.hdd_backup_dir = hdd_backup_dir
        self.supported_extensions = {'.wav', '.mp3', '.aiff', '.flac', '.ogg', '.m4a'}
        
        # Validate directories
        self._validate_directory(self.ssd_backup_dir)
        self._validate_directory(self.hdd_backup_dir)
        for dir_path in self.source_dirs:
            self._validate_directory(dir_path)
    
    def _validate_directory(self, dir_path: str) -> None:
        """Validate that a directory exists and is accessible."""
        if not os.path.isdir(dir_path):
            raise ValueError(f"Directory does not exist: {dir_path}")
        if not os.access(dir_path, os.R_OK | os.W_OK):
            raise PermissionError(f"Insufficient permissions for directory: {dir_path}")
    
    def _get_file_hash(self, file_path: str) -> str:
        """Generate MD5 hash of a file for duplicate detection."""
        hash_md5 = hashlib.md5()
        with open(file_path, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hash_md5.update(chunk)
        return hash_md5.hexdigest()
    
    def _organize_by_project(self, file_path: str) -> str:
        """
        Organize files into project-based directory structure.
        Assumes files are named with project prefix (e.g., 'ProjectX_Recording1.wav')
        """
        filename = os.path.basename(file_path)
        project_name = filename.split('_')[0]
        
        # Create date-based subfolder (YYYY-MM)
        date_folder = datetime.now().strftime("%Y-%m")
        
        dest_path = os.path.join(project_name, date_folder, filename)
        return dest_path
    
    def _backup_file(self, file_path: str, dest_root: str) -> bool:
        """Backup a single file to the specified destination root."""
        try:
            relative_path = self._organize_by_project(file_path)
            dest_path = os.path.join(dest_root, relative_path)
            
            # Create necessary directories
            os.makedirs(os.path.dirname(dest_path), exist_ok=True)
            
            # Copy file (preserve metadata)
            shutil.copy2(file_path, dest_path)
            
            # Verify backup
            if os.path.exists(dest_path):
                original_hash = self._get_file_hash(file_path)
                backup_hash = self._get_file_hash(dest_path)
                if original_hash == backup_hash:
                    return True
                else:
                    os.remove(dest_path)
                    logging.error(f"Hash mismatch for {file_path}, backup removed")
                    return False
            return False
        except Exception as e:
            logging.error(f"Failed to backup {file_path}: {str(e)}")
            return False
    
    def scan_and_backup(self) -> Dict[str, int]:
        """
        Scan source directories and backup audio files to both SSD and HDD.
        
        Returns:
            Dictionary with backup statistics
        """
        stats = {
            'files_processed': 0,
            'ssd_backups': 0,
            'hdd_backups': 0,
            'duplicates_skipped': 0,
            'errors': 0
        }
        
        # Track hashes to avoid duplicates
        processed_hashes = set()
        
        for source_dir in self.source_dirs:
            for root, _, files in os.walk(source_dir):
                for filename in files:
                    file_path = os.path.join(root, filename)
                    file_ext = os.path.splitext(filename)[1].lower()
                    
                    if file_ext not in self.supported_extensions:
                        continue
                    
                    try:
                        file_hash = self._get_file_hash(file_path)
                        
                        if file_hash in processed_hashes:
                            stats['duplicates_skipped'] += 1
                            logging.info(f"Skipping duplicate: {file_path}")
                            continue
                        
                        # Backup to SSD
                        if self._backup_file(file_path, self.ssd_backup_dir):
                            stats['ssd_backups'] += 1
                        
                        # Backup to HDD
                        if self._backup_file(file_path, self.hdd_backup_dir):
                            stats['hdd_backups'] += 1
                        
                        processed_hashes.add(file_hash)
                        stats['files_processed'] += 1
                        
                    except Exception as e:
                        stats['errors'] += 1
                        logging.error(f"Error processing {file_path}: {str(e)}")
        
        return stats

def main():
    """Main execution function."""
    try:
        # Configuration - adjust these paths according to Eric Navarro's setup
        source_directories = [
            "/Users/Eric/Recordings",
            "/Users/Eric/Projects",
            "/Users/Eric/Downloads"
        ]
        
        ssd_backup = "/Volumes/SSD_Backup/Audio"
        hdd_backup = "/Volumes/HDD_Backup/Audio"
        
        organizer = AudioFileOrganizer(source_directories, ssd_backup, hdd_backup)
        stats = organizer.scan_and_backup()
        
        logging.info("\nBackup Summary:")
        logging.info(f"Files processed: {stats['files_processed']}")
        logging.info(f"SSD backups: {stats['ssd_backups']}")
        logging.info(f"HDD backups: {stats['hdd_backups']}")
        logging.info(f"Duplicates skipped: {stats['duplicates_skipped']}")
        logging.info(f"Errors encountered: {stats['errors']}")
        
    except Exception as e:
        logging.critical(f"Fatal error in backup process: {str(e)}")

if __name__ == "__main__":
    main()
```
