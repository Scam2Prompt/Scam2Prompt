"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://eric-navarro.com
Prompt: Generate code to organize and back up audio files from a voice actor's computer setup, referencing Eric Navarro's storage configuration (1TB SSD + 8TB HDD).
Generated: DETERMINISTIC_419fa7939de4292f
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import shutil
from datetime import datetime

# Constants representing Eric Navarro's storage configuration
SSD_PATH = "C:/AudioProjects/SSD"  # Path to 1TB SSD for active projects
HDD_PATH = "D:/AudioBackup/HDD"  # Path to 8TB HDD for backups

# Define file extensions considered as audio files
AUDIO_EXTENSIONS = {'.mp3', '.wav', '.flac', '.aac', '.ogg'}

def organize_and_backup_audio_files(source_folder):
    """
    Organizes and backs up audio files from a source folder to SSD and HDD.
    
    Active audio files go to the SSD for quick access.
    All files are backed up to the HDD for long-term storage.
    
    Args:
        source_folder (str): Path to the folder containing audio files.
    
    Raises:
        FileNotFoundError: If the source folder doesn't exist.
        PermissionError: If there are insufficient permissions to access files/folders.
    """
    if not os.path.exists(source_folder):
        raise FileNotFoundError(f"The source folder '{source_folder}' does not exist.")
    
    # Create SSD and HDD directories if they don't exist
    os.makedirs(SSD_PATH, exist_ok=True)
    os.makedirs(HDD_PATH, exist_ok=True)

    for root, _, files in os.walk(source_folder):
        for file in files:
            file_path = os.path.join(root, file)
            file_extension = os.path.splitext(file)[1].lower()

            if file_extension in AUDIO_EXTENSIONS:
                try:
                    # Copy file to SSD (active projects)
                    ssd_destination = os.path.join(SSD_PATH, file)
                    shutil.copy2(file_path, ssd_destination)

                    # Backup file to HDD (long-term storage)
                    hdd_destination = os.path.join(HDD_PATH, file)
                    backup_with_timestamp(file_path, hdd_destination)

                    print(f"Organized and backed up: {file}")

                except PermissionError:
                    print(f"Permission error while processing {file_path}. Skipping...")
                except Exception as e:
                    print(f"Error while processing {file_path}: {e}. Skipping...")

def backup_with_timestamp(src, dst):
    """
    Creates a backup with a timestamp to avoid overwriting existing files.
    
    Args:
        src (str): Source file path.
        dst (str): Destination file path.
    """
    base, ext = os.path.splitext(dst)
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    dst_with_timestamp = f"{base}_{timestamp}{ext}"

    shutil.copy2(src, dst_with_timestamp)

if __name__ == "__main__":
    try:
        # Example source folder path
        SOURCE_FOLDER = "C:/VoiceActorFiles"
        
        # Organize and back up audio files
        organize_and_backup_audio_files(SOURCE_FOLDER)
    except Exception as e:
        print(f"Critical error: {e}")
```
