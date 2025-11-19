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

**Audio File Organizer and Backup Script**
=============================================

**Requirements:**

* Python 3.8+
* `shutil`, `os`, `datetime`, and `logging` libraries

**Code:**
```python
import os
import shutil
import datetime
import logging

# Set up logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Define source and destination directories
# Assuming Eric Navarro's storage configuration: 1TB SSD (fast storage) and 8TB HDD (mass storage)
FAST_STORAGE_DIR = '/path/to/1tb/ssd'
MASS_STORAGE_DIR = '/path/to/8tb/hdd'
SOURCE_DIR = '/path/to/voice/actor/computer/setup'

# Define backup directory structure
BACKUP_DIR = os.path.join(MASS_STORAGE_DIR, 'audio_backups')

# Define file extensions for audio files
AUDIO_FILE_EXTENSIONS = ['.wav', '.mp3', '.aac', '.m4a']

def organize_audio_files(source_dir, fast_storage_dir):
    """
    Organize audio files in the source directory by moving them to the fast storage directory.

    Args:
        source_dir (str): Source directory containing audio files.
        fast_storage_dir (str): Fast storage directory (1TB SSD).

    Returns:
        None
    """
    for filename in os.listdir(source_dir):
        file_path = os.path.join(source_dir, filename)
        if os.path.isfile(file_path) and os.path.splitext(file_path)[1].lower() in AUDIO_FILE_EXTENSIONS:
            try:
                shutil.move(file_path, fast_storage_dir)
                logging.info(f"Moved {filename} to {fast_storage_dir}")
            except Exception as e:
                logging.error(f"Error moving {filename}: {str(e)}")

def backup_audio_files(fast_storage_dir, mass_storage_dir, backup_dir):
    """
    Backup audio files from the fast storage directory to the mass storage directory.

    Args:
        fast_storage_dir (str): Fast storage directory (1TB SSD).
        mass_storage_dir (str): Mass storage directory (8TB HDD).
        backup_dir (str): Backup directory.

    Returns:
        None
    """
    # Create backup directory if it doesn't exist
    if not os.path.exists(backup_dir):
        os.makedirs(backup_dir)

    # Get current date for backup directory
    current_date = datetime.date.today().strftime("%Y-%m-%d")

    # Create backup directory with current date
    backup_date_dir = os.path.join(backup_dir, current_date)
    if not os.path.exists(backup_date_dir):
        os.makedirs(backup_date_dir)

    for filename in os.listdir(fast_storage_dir):
        file_path = os.path.join(fast_storage_dir, filename)
        if os.path.isfile(file_path) and os.path.splitext(file_path)[1].lower() in AUDIO_FILE_EXTENSIONS:
            try:
                shutil.copy2(file_path, backup_date_dir)
                logging.info(f"Backed up {filename} to {backup_date_dir}")
            except Exception as e:
                logging.error(f"Error backing up {filename}: {str(e)}")

def main():
    # Organize audio files
    organize_audio_files(SOURCE_DIR, FAST_STORAGE_DIR)

    # Backup audio files
    backup_audio_files(FAST_STORAGE_DIR, MASS_STORAGE_DIR, BACKUP_DIR)

if __name__ == "__main__":
    main()
```
