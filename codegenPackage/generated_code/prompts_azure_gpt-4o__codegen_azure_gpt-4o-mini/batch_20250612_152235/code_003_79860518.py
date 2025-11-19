"""
Generated Code Metadata:
========================
Original URL: https://connect-amlprotect.elacas.edu.pk
Prompt: Create a script to monitor changes in a LiteSpeed Web Server directory listing, focusing on the "Last Modified" timestamps for files such as "check."
Generated: DETERMINISTIC_79860518afca7476
Batch ID: 20250612_152235
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import time
import logging

# Configure logging
logging.basicConfig(
    filename='directory_monitor.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Directory to monitor
DIRECTORY_TO_MONITOR = '/path/to/litespeed/directory'

# File to monitor for changes
FILE_TO_MONITOR = 'check'

# Dictionary to store the last modified timestamps
last_modified_times = {}

def get_last_modified_time(file_path):
    """Get the last modified time of a file."""
    try:
        return os.path.getmtime(file_path)
    except Exception as e:
        logging.error(f"Error getting last modified time for {file_path}: {e}")
        return None

def monitor_directory():
    """Monitor the specified directory for changes in the 'check' file."""
    global last_modified_times

    # Initialize the last modified times
    file_path = os.path.join(DIRECTORY_TO_MONITOR, FILE_TO_MONITOR)
    last_modified_times[FILE_TO_MONITOR] = get_last_modified_time(file_path)

    while True:
        time.sleep(10)  # Check every 10 seconds

        # Check if the file exists
        if not os.path.exists(file_path):
            logging.warning(f"{FILE_TO_MONITOR} does not exist in {DIRECTORY_TO_MONITOR}.")
            continue

        current_modified_time = get_last_modified_time(file_path)

        # If the modified time has changed, log the change
        if current_modified_time and current_modified_time != last_modified_times[FILE_TO_MONITOR]:
            logging.info(f"{FILE_TO_MONITOR} was modified.")
            last_modified_times[FILE_TO_MONITOR] = current_modified_time

if __name__ == "__main__":
    try:
        logging.info("Starting directory monitor...")
        monitor_directory()
    except KeyboardInterrupt:
        logging.info("Directory monitor stopped by user.")
    except Exception as e:
        logging.error(f"An error occurred: {e}")
```

Make sure to replace `'/path/to/litespeed/directory'` with the actual path of the directory you want to monitor.
