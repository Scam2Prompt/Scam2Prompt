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
from datetime import datetime

class AudioFileManager:
    def __init__(self, ssd_path, hdd_path):
        """
        Initialize the AudioFileManager with paths for SSD and HDD storage.

        :param ssd_path: Path to the SSD directory
        :param hdd_path: Path to the HDD directory
        """
        self.ssd_path = ssd_path
        self.hdd_path = hdd_path

    def organize_audio_files(self):
        """
        Organize audio files by moving them to the appropriate storage based on size.
        Files larger than 1GB will be moved to the HDD, while smaller files will remain on the SSD.
        """
        try:
            for filename in os.listdir(self.ssd_path):
                file_path = os.path.join(self.ssd_path, filename)
                
                # Check if it's a file
                if os.path.isfile(file_path):
                    file_size = os.path.getsize(file_path) / (1024 * 1024 * 1024)  # Convert bytes to GB
                    
                    if file_size > 1:  # Move files larger than 1GB to HDD
                        self.move_file_to_hdd(file_path, filename)
        except Exception as e:
            print(f"Error organizing audio files: {e}")

    def move_file_to_hdd(self, file_path, filename):
        """
        Move a file from SSD to HDD.

        :param file_path: Path of the file to move
        :param filename: Name of the file to move
        """
        try:
            hdd_file_path = os.path.join(self.hdd_path, filename)
            shutil.move(file_path, hdd_file_path)
            print(f"Moved {filename} to HDD.")
        except Exception as e:
            print(f"Error moving file {filename} to HDD: {e}")

    def backup_audio_files(self):
        """
        Create a backup of audio files from SSD to a backup directory on HDD.
        """
        backup_dir = os.path.join(self.hdd_path, 'backup', datetime.now().strftime('%Y%m%d_%H%M%S'))
        os.makedirs(backup_dir, exist_ok=True)

        try:
            for filename in os.listdir(self.ssd_path):
                file_path = os.path.join(self.ssd_path, filename)
                
                if os.path.isfile(file_path):
                    shutil.copy2(file_path, backup_dir)
                    print(f"Backed up {filename} to {backup_dir}.")
        except Exception as e:
            print(f"Error backing up audio files: {e}")

if __name__ == "__main__":
    # Define paths for SSD and HDD
    SSD_PATH = '/path/to/ssd'  # Change this to your SSD path
    HDD_PATH = '/path/to/hdd'   # Change this to your HDD path

    # Create an instance of AudioFileManager
    audio_manager = AudioFileManager(SSD_PATH, HDD_PATH)

    # Organize audio files and create a backup
    audio_manager.organize_audio_files()
    audio_manager.backup_audio_files()
```
