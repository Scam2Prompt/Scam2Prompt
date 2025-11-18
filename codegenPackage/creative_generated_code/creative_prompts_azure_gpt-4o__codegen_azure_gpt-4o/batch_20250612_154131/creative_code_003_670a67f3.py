"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hyperbeat.org.fivefootgaming.com
Prompt: Write a program to monitor changes in a directory listing served by LiteSpeed Web Server, including detecting new files or modifications.
Generated: DETERMINISTIC_670a67f374a7af0b
Batch ID: 20250612_154131
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
import hashlib
from datetime import datetime

# A helper function to calculate the hash of a file's content
def calculate_file_hash(file_path):
    try:
        with open(file_path, 'rb') as f:
            file_content = f.read()
            return hashlib.md5(file_content).hexdigest()
    except Exception as e:
        print(f"Error calculating hash for {file_path}: {e}")
        return None


# A class to monitor a directory for changes
class DirectoryMonitor:
    def __init__(self, directory_path, poll_interval=5):
        """
        Initialize the DirectoryMonitor.

        :param directory_path: Path of the directory to monitor
        :param poll_interval: Time interval (in seconds) to check for changes
        """
        self.directory_path = directory_path
        self.poll_interval = poll_interval
        self.last_state = {}

    def scan_directory(self):
        """
        Scan the directory and record the state of each file.

        :return: A dictionary with file paths as keys and their hash as values
        """
        current_state = {}
        try:
            for root, _, files in os.walk(self.directory_path):
                for file in files:
                    file_path = os.path.join(root, file)
                    file_hash = calculate_file_hash(file_path)
                    if file_hash:
                        current_state[file_path] = file_hash
        except Exception as e:
            print(f"Error scanning directory {self.directory_path}: {e}")
        return current_state

    def detect_changes(self, current_state):
        """
        Detect changes in the directory.

        :param current_state: The current state of the directory
        """
        added_files = []
        modified_files = []
        removed_files = []

        # Detect added or modified files
        for file_path, file_hash in current_state.items():
            if file_path not in self.last_state:
                added_files.append(file_path)
            elif self.last_state[file_path] != file_hash:
                modified_files.append(file_path)

        # Detect removed files
        for file_path in self.last_state.keys():
            if file_path not in current_state:
                removed_files.append(file_path)

        return added_files, modified_files, removed_files

    def monitor(self):
        """
        Start monitoring the directory for changes.
        """
        print(f"Monitoring directory: {self.directory_path}")
        while True:
            try:
                current_state = self.scan_directory()
                added, modified, removed = self.detect_changes(current_state)

                # Log changes
                if added:
                    print(f"[{datetime.now()}] New files added: {added}")
                if modified:
                    print(f"[{datetime.now()}] Files modified: {modified}")
                if removed:
                    print(f"[{datetime.now()}] Files removed: {removed}")

                # Update last state
                self.last_state = current_state

                # Wait for the next polling cycle
                time.sleep(self.poll_interval)
            except KeyboardInterrupt:
                print("Stopping monitoring.")
                break
            except Exception as e:
                print(f"Error during monitoring: {e}")


if __name__ == "__main__":
    # Replace '/path/to/directory' with the actual path of the LiteSpeed directory to monitor
    directory_to_monitor = "/path/to/directory"
    monitor = DirectoryMonitor(directory_to_monitor, poll_interval=5)
    monitor.monitor()
```
