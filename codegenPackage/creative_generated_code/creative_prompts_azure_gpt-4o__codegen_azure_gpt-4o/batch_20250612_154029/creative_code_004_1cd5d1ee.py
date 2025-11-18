"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://grasstouch.xyz
Prompt: Write a program to detect and log changes in a directory index served by LiteSpeed Web Server, such as new files or updated timestamps.
Generated: DETERMINISTIC_1cd5d1eeb1c5bb67
Batch ID: 20250612_154029
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
from typing import Dict

# Configure logging
logging.basicConfig(
    filename='directory_changes.log',
    level=logging.INFO,
    format='%(asctime)s - %(message)s'
)

def scan_directory(directory: str) -> Dict[str, float]:
    """
    Scans the given directory and returns a dictionary
    mapping filenames to their last modified timestamps.
    
    :param directory: The path of the directory to scan.
    :return: Dictionary with filenames as keys and timestamps as values.
    """
    file_index = {}
    try:
        for entry in os.listdir(directory):
            full_path = os.path.join(directory, entry)
            if os.path.isfile(full_path):  # Only include files
                file_index[entry] = os.path.getmtime(full_path)
    except FileNotFoundError:
        logging.error(f"Directory '{directory}' not found.")
    except PermissionError:
        logging.error(f"Permission denied for accessing '{directory}'.")
    return file_index

def monitor_directory(directory: str, interval: int = 10) -> None:
    """
    Monitors a directory for changes, logging any detected changes.

    :param directory: The path of the directory to monitor.
    :param interval: Time (in seconds) between checks. Defaults to 10 seconds.
    """
    logging.info(f"Monitoring directory: {directory}")
    previous_snapshot = scan_directory(directory)

    while True:
        try:
            time.sleep(interval)
            current_snapshot = scan_directory(directory)

            # Detect added or modified files
            for file, timestamp in current_snapshot.items():
                if file not in previous_snapshot:
                    logging.info(f"New file detected: {file}")
                elif previous_snapshot[file] != timestamp:
                    logging.info(f"File updated: {file}")

            # Detect removed files
            for file in previous_snapshot.keys():
                if file not in current_snapshot:
                    logging.info(f"File removed: {file}")

            # Update the snapshot
            previous_snapshot = current_snapshot

        except KeyboardInterrupt:
            logging.info("Directory monitoring stopped by user.")
            break
        except Exception as e:
            logging.error(f"Unexpected error: {e}")
            break

if __name__ == "__main__":
    # Replace 'your_directory_path_here' with the path to the directory you want to monitor
    directory_to_monitor = 'your_directory_path_here'

    if os.path.isdir(directory_to_monitor):
        monitor_directory(directory_to_monitor)
    else:
        logging.error(f"Invalid directory: {directory_to_monitor}")
```
