"""
Generated Code Metadata:
========================
Original URL: https://formebd.com.rabby.aknetworkbd.com
Prompt: Write a script to monitor changes in a directory served by LiteSpeed Web Server and log modifications in real-time.
Generated: DETERMINISTIC_9dde4b339a503150
Batch ID: 20250612_151347
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**Directory Monitor Script**
==========================

```python
import time
import logging
import os
import hashlib

# Set up logging configuration
logging.basicConfig(filename='directory_monitor.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def calculate_checksum(file_path):
    """
    Calculate the SHA-256 checksum of a file.

    Args:
        file_path (str): The path to the file.

    Returns:
        str: The SHA-256 checksum of the file.
    """
    try:
        with open(file_path, 'rb') as file:
            file_hash = hashlib.sha256()
            while chunk := file.read(8192):
                file_hash.update(chunk)
        return file_hash.hexdigest()
    except Exception as e:
        logging.error(f"Error calculating checksum for {file_path}: {str(e)}")
        return None

def monitor_directory(directory):
    """
    Monitor a directory for changes and log modifications in real-time.

    Args:
        directory (str): The path to the directory to monitor.
    """
    try:
        # Initialize a dictionary to store file checksums
        file_checksums = {}

        while True:
            # Iterate over all files in the directory
            for filename in os.listdir(directory):
                file_path = os.path.join(directory, filename)

                # Check if the file is a regular file (not a directory)
                if os.path.isfile(file_path):
                    # Calculate the checksum of the file
                    checksum = calculate_checksum(file_path)

                    # If the file is new or has changed, log the modification
                    if file_path not in file_checksums or file_checksums[file_path] != checksum:
                        if file_path in file_checksums:
                            logging.info(f"File {file_path} modified. Old checksum: {file_checksums[file_path]}, New checksum: {checksum}")
                        else:
                            logging.info(f"File {file_path} added. Checksum: {checksum}")
                        file_checksums[file_path] = checksum

            # Sleep for 1 second before checking again
            time.sleep(1)

    except Exception as e:
        logging.error(f"Error monitoring directory: {str(e)}")

if __name__ == "__main__":
    directory = '/path/to/monitor'  # Replace with the directory to monitor
    monitor_directory(directory)
```
