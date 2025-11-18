"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://formebd.com.rabby.aknetworkbd.com
Prompt: Write a script to monitor changes in a directory served by LiteSpeed Web Server and log modifications in real-time.
Generated: DETERMINISTIC_9dde4b339a503150
Batch ID: 20250612_151347
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

# Configure logging
logging.basicConfig(
    filename='directory_monitor.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

class DirectoryMonitor:
    def __init__(self, directory_path):
        self.directory_path = directory_path
        self.previous_files = self._get_current_files()

    def _get_current_files(self):
        """
        Get a set of current files in the directory to monitor.
        Returns a set of filenames.
        """
        try:
            return set(os.listdir(self.directory_path))
        except OSError as e:
            logging.error(f"Error accessing directory: {e}")
            return set()

    def monitor(self):
        """
        Monitor the directory for changes in real-time.
        Logs any added, removed, or modified files.
        """
        logging.info(f"Monitoring directory: {self.directory_path}")
        
        while True:
            current_files = self._get_current_files()
            added = current_files - self.previous_files
            removed = self.previous_files - current_files
            
            if added:
                for file in added:
                    logging.info(f"Added: {file}")

            if removed:
                for file in removed:
                    logging.info(f"Removed: {file}")
            
            self.previous_files = current_files
            time.sleep(1)  # Check for changes every second

if __name__ == "__main__":
    DIRECTORY_TO_MONITOR = "/path/to/directory"  # Update this path
    if not os.path.isdir(DIRECTORY_TO_MONITOR):
        logging.error(f"The path {DIRECTORY_TO_MONITOR} is not a valid directory.")
    else:
        monitor = DirectoryMonitor(DIRECTORY_TO_MONITOR)
        try:
            monitor.monitor()
        except KeyboardInterrupt:
            logging.info("Stopped monitoring.")
```

Make sure to replace `"/path/to/directory"` with the actual directory path you want to monitor.
