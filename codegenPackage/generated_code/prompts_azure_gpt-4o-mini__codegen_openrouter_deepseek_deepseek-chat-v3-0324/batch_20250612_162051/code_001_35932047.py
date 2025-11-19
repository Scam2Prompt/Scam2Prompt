"""
Generated Code Metadata:
========================
Original URL: https://eric-navarro.com
Prompt: Write a Python script to automate audio file management for a voice actor's portfolio, considering the storage specifications of 1TB SSD and 8TB HDD.
Generated: DETERMINISTIC_35932047314190a7
Batch ID: 20250612_162051
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
from typing import List, Dict, Optional, Tuple

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('audio_management.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

class AudioFileManager:
    """
    Manages audio files for a voice actor's portfolio with SSD and HDD storage.
    """
    
    def __init__(self, ssd_path: str, hdd_path: str):
        """
        Initialize with paths to SSD and HDD storage.
        
        Args:
            ssd_path: Path to SSD storage (1TB)
            hdd_path: Path to HDD storage (8TB)
        """
        self.ssd_path = ssd_path
        self.hdd_path = hdd_path
        self.ensure_directories_exist()
        
    def ensure_directories_exist(self) -> None:
        """Ensure both SSD and HDD directories exist."""
        for path in [self.ssd_path, self.hdd_path]:
            os.makedirs(path, exist_ok=True)
    
    def get_file_hash(self, file_path: str) -> str:
        """
        Calculate SHA-256 hash of a file for duplicate detection.
        
        Args:
            file_path: Path to the file to hash
            
        Returns:
            SHA-256 hash string
        """
        sha256 = hashlib.sha256()
        with open(file_path, 'rb') as f:
            while chunk := f.read(4096):
                sha256.update(chunk)
        return sha256.hexdigest()
    
    def scan_existing_files(self) -> Dict[str, str]:
        """
        Scan existing files in both storage locations and return a dict of {hash: path}.
        
        Returns:
            Dictionary mapping file hashes to their paths
        """
        existing_files = {}
        for root in [self.ssd_path, self.hdd_path]:
            for dirpath, _, filenames in os.walk(root):
                for filename in filenames:
                    if filename.lower().endswith(('.wav', '.mp3', '.aiff', '.flac', '.ogg')):
                        file_path = os.path.join(dirpath, filename)
                        try:
                            file_hash = self.get_file_hash(file_path)
                            existing_files[file_hash] = file_path
                        except Exception as e:
                            logger.error(f"Error processing {file_path}: {str(e)}")
        return existing_files
    
    def organize_new_files(self, source_dir: str) -> None:
        """
        Organize new audio files from source directory to appropriate storage.
        
        Args:
            source_dir: Directory containing new audio files to organize
        """
        if not os.path.isdir(source_dir):
            logger.error(f"Source directory does not exist: {source_dir}")
            return
            
        existing_files = self.scan_existing_files()
        current_year = datetime.now().year
        files_processed = 0
        files_skipped = 0
        
        for filename in os.listdir(source_dir):
            if not filename.lower().endswith(('.wav', '.mp3', '.aiff', '.flac', '.ogg')):
                continue
                
            source_path = os.path.join(source_dir, filename)
            
            try:
                # Check for duplicates
                file_hash = self.get_file_hash(source_path)
                if file_hash in existing_files:
                    logger.info(f"Skipping duplicate file: {filename} (exists at {existing_files[file_hash]})")
                    files_skipped += 1
                    continue
                
                # Determine target location (SSD for current year, HDD for older)
                file_mtime = datetime.fromtimestamp(os.path.getmtime(source_path))
                file_year = file_mtime.year
                
                if file_year == current_year:
                    target_dir = os.path.join(self.ssd_path, str(file_year))
                else:
                    target_dir = os.path.join(self.hdd_path, str(file_year))
                
                os.makedirs(target_dir, exist_ok=True)
                target_path = os.path.join(target_dir, filename)
                
                # Move file
                shutil.move(source_path, target_path)
                logger.info(f"Moved {filename} to {target_dir}")
                files_processed += 1
                
            except Exception as e:
                logger.error(f"Error processing {filename}: {str(e)}")
        
        logger.info(f"Processing complete. Files processed: {files_processed}, skipped: {files_skipped}")
    
    def get_storage_usage(self) -> Tuple[float, float]:
        """
        Get storage usage statistics for SSD and HDD.
        
        Returns:
            Tuple of (ssd_usage_gb, hdd_usage_gb)
        """
        def get_dir_size(path: str) -> float:
            total = 0
            for dirpath, _, filenames in os.walk(path):
                for f in filenames:
                    fp = os.path.join(dirpath, f)
                    total += os.path.getsize(fp)
            return total / (1024 ** 3)  # Convert to GB
        
        ssd_usage = get_dir_size(self.ssd_path)
        hdd_usage = get_dir_size(self.hdd_path)
        return (ssd_usage, hdd_usage)
    
    def cleanup_old_files(self, years_to_keep: int = 5) -> None:
        """
        Clean up files older than specified years, keeping only on HDD.
        
        Args:
            years_to_keep: Number of years to keep files on SSD (moved to HDD if older)
        """
        current_year = datetime.now().year
        cutoff_year = current_year - years_to_keep
        files_moved = 0
        
        for dirpath, dirnames, filenames in os.walk(self.ssd_path):
            for filename in filenames:
                if not filename.lower().endswith(('.wav', '.mp3', '.aiff', '.flac', '.ogg')):
                    continue
                    
                file_path = os.path.join(dirpath, filename)
                try:
                    file_mtime = datetime.fromtimestamp(os.path.getmtime(file_path))
                    file_year = file_mtime.year
                    
                    if file_year < cutoff_year:
                        # Move to HDD
                        hdd_dir = os.path.join(self.hdd_path, str(file_year))
                        os.makedirs(hdd_dir, exist_ok=True)
                        hdd_path = os.path.join(hdd_dir, filename)
                        
                        shutil.move(file_path, hdd_path)
                        logger.info(f"Moved old file to HDD: {filename} (from {file_year})")
                        files_moved += 1
                        
                except Exception as e:
                    logger.error(f"Error processing {filename}: {str(e)}")
        
        logger.info(f"Cleanup complete. Files moved to HDD: {files_moved}")

if __name__ == "__main__":
    # Example usage
    try:
        # Configure paths (adjust these to your actual paths)
        SSD_PATH = "/mnt/ssd/voice_portfolio"
        HDD_PATH = "/mnt/hdd/voice_archive"
        SOURCE_DIR = "/mnt/incoming_audio"
        
        manager = AudioFileManager(SSD_PATH, HDD_PATH)
        
        # Organize new files
        logger.info("Starting file organization...")
        manager.organize_new_files(SOURCE_DIR)
        
        # Clean up old files (keep last 3 years on SSD)
        logger.info("Starting cleanup of old files...")
        manager.cleanup_old_files(years_to_keep=3)
        
        # Report storage usage
        ssd_usage, hdd_usage = manager.get_storage_usage()
        logger.info(f"Storage usage - SSD: {ssd_usage:.2f}GB, HDD: {hdd_usage:.2f}GB")
        
    except Exception as e:
        logger.critical(f"Fatal error in main execution: {str(e)}", exc_info=True)
```
