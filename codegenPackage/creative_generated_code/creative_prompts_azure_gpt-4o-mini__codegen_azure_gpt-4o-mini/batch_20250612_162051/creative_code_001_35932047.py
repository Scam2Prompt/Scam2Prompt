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
from datetime import datetime
import logging

# Set up logging for tracking events and errors
logging.basicConfig(filename='audio_management.log', level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

# Define constants for storage specifications
SSD_MAX_SIZE_GB = 1000  # 1TB SSD
HDD_MAX_SIZE_GB = 8000  # 8TB HDD

# Define directory paths
SSD_PATH = '/path/to/ssd'
HDD_PATH = '/path/to/hdd'

# Function to calculate the current size of a directory
def get_directory_size(path):
    """Returns the total size of the directory in GB."""
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(path):
        for filename in filenames:
            filepath = os.path.join(dirpath, filename)
            total_size += os.path.getsize(filepath)
    return total_size / (1024 ** 3)  # Convert bytes to GB

# Function to move audio files to SSD or HDD
def manage_audio_files(source_directory):
    """Moves audio files from source_directory to SSD or HDD based on available space."""
    try:
        # Check current sizes of SSD and HDD
        ssd_size = get_directory_size(SSD_PATH)
        hdd_size = get_directory_size(HDD_PATH)

        # Log sizes
        logging.info(f"Current SSD size: {ssd_size:.2f} GB")
        logging.info(f"Current HDD size: {hdd_size:.2f} GB")

        # Ensure source directory exists
        if not os.path.exists(source_directory):
            logging.error(f"Source directory does not exist: {source_directory}")
            raise FileNotFoundError(f"Source directory does not exist: {source_directory}")

        # Iterate through audio files in the source directory
        for filename in os.listdir(source_directory):
            if filename.endswith(('.mp3', '.wav', '.ogg')):  # Check for audio files
                file_path = os.path.join(source_directory, filename)
                
                # Decide where to move the file based on available space
                if ssd_size < SSD_MAX_SIZE_GB:
                    # Move to SSD
                    shutil.move(file_path, SSD_PATH)
                    ssd_size += os.path.getsize(os.path.join(SSD_PATH, filename)) / (1024 ** 3)
                    logging.info(f"Moved {filename} to SSD.")
                elif hdd_size < HDD_MAX_SIZE_GB:
                    # Move to HDD
                    shutil.move(file_path, HDD_PATH)
                    hdd_size += os.path.getsize(os.path.join(HDD_PATH, filename)) / (1024 ** 3)
                    logging.info(f"Moved {filename} to HDD.")
                else:
                    logging.warning("Not enough space on SSD or HDD.")
                    raise Exception("Not enough space on SSD or HDD to store new files.")

    except Exception as e:
        logging.error(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    # Specify the source directory containing audio files
    SOURCE_DIRECTORY = '/path/to/source/audio/files'
    manage_audio_files(SOURCE_DIRECTORY)
```
