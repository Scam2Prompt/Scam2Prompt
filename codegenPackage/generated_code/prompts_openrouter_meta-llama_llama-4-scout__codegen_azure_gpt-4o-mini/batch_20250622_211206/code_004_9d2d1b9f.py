"""
Generated Code Metadata:
========================
Original URL: https://consejodigitalmx.com
Prompt: Develop a Python script to monitor and report on the last modified dates of files on a server, similar to the information displayed on this webpage.
Generated: DETERMINISTIC_9d2d1b9fc6433b90
Batch ID: 20250622_211206
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
from datetime import datetime

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def get_file_modification_dates(directory):
    """
    Get a dictionary of file names and their last modified dates in the specified directory.

    Args:
        directory (str): The path to the directory to monitor.

    Returns:
        dict: A dictionary with file names as keys and last modified dates as values.
    """
    file_mod_dates = {}
    
    try:
        # Iterate over all files in the directory
        for filename in os.listdir(directory):
            file_path = os.path.join(directory, filename)
            # Check if it is a file
            if os.path.isfile(file_path):
                # Get the last modified time and convert it to a readable format
                mod_time = os.path.getmtime(file_path)
                file_mod_dates[filename] = datetime.fromtimestamp(mod_time).strftime('%Y-%m-%d %H:%M:%S')
    except Exception as e:
        logging.error(f"Error while accessing directory '{directory}': {e}")
    
    return file_mod_dates

def monitor_directory(directory, interval=60):
    """
    Monitor the specified directory for file modification dates and report them at regular intervals.

    Args:
        directory (str): The path to the directory to monitor.
        interval (int): The time interval (in seconds) between checks.
    """
    logging.info(f"Starting to monitor directory: {directory}")
    
    while True:
        try:
            # Get the current file modification dates
            mod_dates = get_file_modification_dates(directory)
            # Log the modification dates
            logging.info("Current file modification dates:")
            for filename, mod_date in mod_dates.items():
                logging.info(f"{filename}: {mod_date}")
        except Exception as e:
            logging.error(f"Error during monitoring: {e}")
        
        # Wait for the specified interval before checking again
        time.sleep(interval)

if __name__ == "__main__":
    # Specify the directory to monitor
    directory_to_monitor = "/path/to/your/directory"  # Change this to your target directory
    # Start monitoring the directory
    monitor_directory(directory_to_monitor, interval=60)  # Check every 60 seconds
```
