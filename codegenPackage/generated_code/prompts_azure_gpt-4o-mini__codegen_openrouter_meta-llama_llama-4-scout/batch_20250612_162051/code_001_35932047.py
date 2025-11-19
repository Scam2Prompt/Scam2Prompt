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

# Define storage devices and their capacities
STORAGE_DEVICES = {
    "SSD": {"path": "/mnt/ssd", "capacity": 1e12},  # 1TB SSD
    "HDD": {"path": "/mnt/hdd", "capacity": 8e12}  # 8TB HDD
}

# Define audio file extensions
AUDIO_FILE_EXTENSIONS = [".mp3", ".wav", ".aac", ".m4a"]

def get_audio_files(directory):
    """
    Retrieves a list of audio files in the specified directory.

    Args:
        directory (str): The directory to search for audio files.

    Returns:
        list: A list of audio file paths.
    """
    audio_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if os.path.splitext(file)[1].lower() in AUDIO_FILE_EXTENSIONS:
                audio_files.append(os.path.join(root, file))
    return audio_files

def calculate_storage_usage(audio_files):
    """
    Calculates the total storage usage of the specified audio files.

    Args:
        audio_files (list): A list of audio file paths.

    Returns:
        int: The total storage usage in bytes.
    """
    total_size = 0
    for file in audio_files:
        total_size += os.path.getsize(file)
    return total_size

def manage_audio_files():
    """
    Manages audio files by moving them to the optimal storage device.

    Returns:
        None
    """
    # Get audio files from the current working directory
    audio_files = get_audio_files(os.getcwd())

    # Calculate total storage usage
    total_size = calculate_storage_usage(audio_files)

    # Sort storage devices by available capacity
    available_devices = sorted(
        [(device, STORAGE_DEVICES[device]["capacity"] - calculate_storage_usage(get_audio_files(STORAGE_DEVICES[device]["path"]))) 
         for device in STORAGE_DEVICES],
        key=lambda x: x[1],
        reverse=True
    )

    # Move audio files to the device with the most available capacity
    for file in audio_files:
        for device, available_capacity in available_devices:
            if available_capacity >= os.path.getsize(file):
                try:
                    shutil.move(file, STORAGE_DEVICES[device]["path"])
                    print(f"Moved {file} to {device} ({STORAGE_DEVICES[device]['path']})")
                except Exception as e:
                    print(f"Error moving {file}: {str(e)}")
                break

def main():
    try:
        manage_audio_files()
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()
```
