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

# Configure logging
logging.basicConfig(
    filename='directory_changes.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

class DirectoryWatcher:
    def __init__(self, directory):
        """Initialize the directory watcher."""
        self.directory = directory
        self.files_snapshot = self._take_snapshot()

    def _take_snapshot(self):
        """Take a snapshot of the current state of the directory."""
        try:
            return {file: os.path.getmtime(os.path.join(self.directory, file))
                    for file in os.listdir(self.directory)}
        except Exception as e:
            logging.error(f"Error taking snapshot: {e}")
            return {}

    def detect_changes(self):
        """Detect changes in the directory and log them."""
        while True:
            current_snapshot = self._take_snapshot()
            added_files = current_snapshot.keys() - self.files_snapshot.keys()
            removed_files = self.files_snapshot.keys() - current_snapshot.keys()
            modified_files = {file for file in current_snapshot.keys() if 
                              current_snapshot[file] != self.files_snapshot.get(file)}

            # Log added files
            for file in added_files:
                logging.info(f"Added: {file}")

            # Log removed files
            for file in removed_files:
                logging.info(f"Removed: {file}")

            # Log modified files
            for file in modified_files:
                logging.info(f"Modified: {file}")

            # Update the snapshot
            self.files_snapshot = current_snapshot

            # Wait before checking again
            time.sleep(10)  # Poll every 10 seconds

if __name__ == "__main__":
    # Replace 'your_directory_path_here' with the path you want to monitor
    directory_to_watch = 'your_directory_path_here'
    
    if not os.path.isdir(directory_to_watch):
        logging.error(f"The specified path is not a directory: {directory_to_watch}")
    else:
        watcher = DirectoryWatcher(directory_to_watch)
        watcher.detect_changes()
```
