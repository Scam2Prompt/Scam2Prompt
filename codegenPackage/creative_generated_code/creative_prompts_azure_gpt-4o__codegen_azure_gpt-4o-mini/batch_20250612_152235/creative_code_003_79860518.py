"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://connect-amlprotect.elacas.edu.pk
Prompt: Create a script to monitor changes in a LiteSpeed Web Server directory listing, focusing on the "Last Modified" timestamps for files such as "check."
Generated: DETERMINISTIC_79860518afca7476
Batch ID: 20250612_152235
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
from pathlib import Path

# Configure logging
logging.basicConfig(
    filename='directory_monitor.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

class DirectoryMonitor:
    def __init__(self, directory_path):
        """
        Initialize the DirectoryMonitor with the path to the directory to monitor.
        
        :param directory_path: Path to the directory to monitor
        """
        self.directory_path = Path(directory_path)
        self.file_timestamps = self._get_file_timestamps()
    
    def _get_file_timestamps(self):
        """
        Get the last modified timestamps of files in the directory.
        
        :return: A dictionary with filenames as keys and their last modified timestamps as values
        """
        timestamps = {}
        try:
            for file in self.directory_path.iterdir():
                if file.is_file():
                    timestamps[file.name] = file.stat().st_mtime
            return timestamps
        except Exception as e:
            logging.error(f"Error accessing directory: {e}")
            return {}
    
    def monitor_changes(self, check_interval=10):
        """
        Monitor the directory for changes in the last modified timestamps.
        
        :param check_interval: Time interval (in seconds) to check for changes
        """
        while True:
            time.sleep(check_interval)
            current_timestamps = self._get_file_timestamps()
            self._check_for_changes(current_timestamps)

    def _check_for_changes(self, current_timestamps):
        """
        Compare current timestamps with the previous ones and log any changes.
        
        :param current_timestamps: The current state of file timestamps
        """
        for filename, timestamp in current_timestamps.items():
            if filename in self.file_timestamps:
                if self.file_timestamps[filename] != timestamp:
                    logging.info(f"File '{filename}' modified: {time.ctime(timestamp)}")
            else:
                logging.info(f"New file added: '{filename}' with timestamp: {time.ctime(timestamp)}")
        
        for filename in self.file_timestamps.keys():
            if filename not in current_timestamps:
                logging.info(f"File '{filename}' has been removed.")
        
        self.file_timestamps = current_timestamps

if __name__ == "__main__":
    # Specify the directory path to monitor
    directory_to_monitor = '/path/to/directory'  # Update this line with the actual directory path
    
    if not os.path.isdir(directory_to_monitor):
        logging.error(f"The specified path does not exist or is not a directory: {directory_to_monitor}")
    else:
        monitor = DirectoryMonitor(directory_to_monitor)
        try:
            monitor.monitor_changes(check_interval=10)  # Adjust the interval as needed
        except KeyboardInterrupt:
            logging.info("Monitoring stopped by user.")
        except Exception as e:
            logging.error(f"Error during monitoring: {e}")
```
