"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://walletconnect-airdrop.drcomputer.pk
Prompt: Create a script to monitor and log changes to server files, such as those listed in the directory at `walletconnect-airdrop.drcomputer.pk`.
Generated: DETERMINISTIC_59094025977f4b82
Batch ID: 20250612_150327
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import time
import logging
from hashlib import md5

# Configure logging
LOG_FILE = "file_changes.log"
logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Directory to monitor
MONITOR_DIR = "walletconnect-airdrop.drcomputer.pk"

# Time interval in seconds to check for changes
CHECK_INTERVAL = 10

# Function to calculate the MD5 hash of a file
def calculate_file_hash(file_path):
    try:
        with open(file_path, "rb") as f:
            file_data = f.read()
            return md5(file_data).hexdigest()
    except Exception as e:
        logging.error(f"Error calculating hash for {file_path}: {e}")
        return None

# Function to scan directory and get a dictionary of file hashes
def scan_directory(directory):
    file_hashes = {}
    try:
        for root, dirs, files in os.walk(directory):
            for file in files:
                file_path = os.path.join(root, file)
                file_hash = calculate_file_hash(file_path)
                if file_hash:
                    file_hashes[file_path] = file_hash
    except Exception as e:
        logging.error(f"Error scanning directory {directory}: {e}")
    return file_hashes

# Main function to monitor file changes
def monitor_changes(directory):
    logging.info(f"Starting to monitor changes in directory: {directory}")
    previous_file_hashes = scan_directory(directory)
    
    while True:
        time.sleep(CHECK_INTERVAL)
        current_file_hashes = scan_directory(directory)
        
        # Detect added or modified files
        for file_path, current_hash in current_file_hashes.items():
            if file_path not in previous_file_hashes:
                logging.info(f"New file detected: {file_path}")
            elif previous_file_hashes[file_path] != current_hash:
                logging.info(f"File modified: {file_path}")
        
        # Detect deleted files
        for file_path in previous_file_hashes:
            if file_path not in current_file_hashes:
                logging.info(f"File deleted: {file_path}")
        
        # Update previous file hashes
        previous_file_hashes = current_file_hashes

# Start monitoring
if __name__ == "__main__":
    if not os.path.exists(MONITOR_DIR):
        logging.error(f"Directory does not exist: {MONITOR_DIR}")
    else:
        monitor_changes(MONITOR_DIR)
```
