"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://eric-navarro.com
Prompt: Write a Python script to automate audio file management for a voice actor's portfolio, considering the storage specifications of 1TB SSD and 8TB HDD.
Generated: DETERMINISTIC_35932047314190a7
Batch ID: 20250612_162051
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
from pathlib import Path

# Define storage paths and specifications
SSD_STORAGE_PATH = Path("C:/VoiceActorPortfolio/SSD")  # Path for SSD storage
HDD_STORAGE_PATH = Path("D:/VoiceActorPortfolio/HDD")  # Path for HDD storage
SSD_MAX_CAPACITY = 1 * 1024 ** 3  # SSD max capacity in bytes (1TB)
HDD_MAX_CAPACITY = 8 * 1024 ** 3  # HDD max capacity in bytes (8TB)

# Define file size thresholds
SSD_PRIORITY_SIZE = 50 * 1024 ** 2  # Files <= 50MB go to SSD, else HDD

def ensure_directories_exist():
    """Ensure the storage directories exist."""
    SSD_STORAGE_PATH.mkdir(parents=True, exist_ok=True)
    HDD_STORAGE_PATH.mkdir(parents=True, exist_ok=True)

def get_directory_size(path):
    """Calculate the total size of files in a directory."""
    total_size = 0
    for dirpath, _, filenames in os.walk(path):
        for filename in filenames:
            filepath = Path(dirpath) / filename
            total_size += filepath.stat().st_size
    return total_size

def move_file_to_storage(file_path):
    """
    Move an audio file to the appropriate storage based on size and availability.
    :param file_path: Path to the audio file to be moved.
    """
    try:
        # Ensure the file exists
        file = Path(file_path)
        if not file.is_file():
            print(f"Skipping non-existent file: {file}")
            return

        # Determine file size
        file_size = file.stat().st_size

        # Check SSD storage conditions
        ssd_used = get_directory_size(SSD_STORAGE_PATH)
        if file_size <= SSD_PRIORITY_SIZE and ssd_used + file_size <= SSD_MAX_CAPACITY:
            destination = SSD_STORAGE_PATH / file.name
        else:
            # Check HDD storage conditions
            hdd_used = get_directory_size(HDD_STORAGE_PATH)
            if hdd_used + file_size <= HDD_MAX_CAPACITY:
                destination = HDD_STORAGE_PATH / file.name
            else:
                print(f"Insufficient storage for file: {file}")
                return
        
        # Move file to the selected destination
        shutil.move(str(file), str(destination))
        print(f"Moved file '{file.name}' to '{destination}'")
    except Exception as e:
        print(f"Error processing file '{file_path}': {e}")

def organize_audio_files(source_directory):
    """
    Organize audio files from a source directory into SSD and HDD storage.
    :param source_directory: Path to the source directory containing audio files.
    """
    try:
        source_path = Path(source_directory)
        if not source_path.is_dir():
            print("Invalid source directory.")
            return

        # Process each file in the source directory
        for audio_file in source_path.iterdir():
            if audio_file.is_file() and audio_file.suffix in {".mp3", ".wav", ".flac"}:
                move_file_to_storage(audio_file)
    except Exception as e:
        print(f"Error organizing files: {e}")

if __name__ == "__main__":
    # Define source directory for audio files
    SOURCE_DIRECTORY = "C:/VoiceActorPortfolio/AudioFiles"

    # Ensure storage directories exist
    ensure_directories_exist()

    # Organize audio files into SSD and HDD storage
    organize_audio_files(SOURCE_DIRECTORY)
```
