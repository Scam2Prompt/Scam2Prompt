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
import hashlib

class LiteSpeedMonitor:
    def __init__(self, directory):
        """
        Initialize the monitor with a directory path.

        :param directory: Path to the LiteSpeed Web Server directory.
        """
        self.directory = directory
        self.file_timestamps = {}
        self.file_hashes = {}

    def get_file_timestamps(self):
        """
        Retrieve the "Last Modified" timestamps for files in the directory.

        :return: A dictionary of file names and their corresponding timestamps.
        """
        timestamps = {}
        for filename in os.listdir(self.directory):
            filepath = os.path.join(self.directory, filename)
            if os.path.isfile(filepath):
                timestamp = os.path.getmtime(filepath)
                timestamps[filename] = timestamp
        return timestamps

    def get_file_hashes(self):
        """
        Retrieve the hashes for files in the directory.

        :return: A dictionary of file names and their corresponding hashes.
        """
        hashes = {}
        for filename in os.listdir(self.directory):
            filepath = os.path.join(self.directory, filename)
            if os.path.isfile(filepath):
                with open(filepath, 'rb') as f:
                    file_hash = hashlib.md5(f.read()).hexdigest()
                    hashes[filename] = file_hash
        return hashes

    def monitor(self, interval=1):
        """
        Continuously monitor the directory for changes in "Last Modified" timestamps.

        :param interval: The interval in seconds to check for changes.
        """
        try:
            while True:
                current_timestamps = self.get_file_timestamps()
                current_hashes = self.get_file_hashes()

                for filename, timestamp in current_timestamps.items():
                    if filename not in self.file_timestamps:
                        self.file_timestamps[filename] = timestamp
                        print(f"New file detected: {filename} (Last Modified: {timestamp})")
                    elif timestamp != self.file_timestamps[filename]:
                        self.file_timestamps[filename] = timestamp
                        print(f"File modified: {filename} (Last Modified: {timestamp})")

                for filename, file_hash in current_hashes.items():
                    if filename not in self.file_hashes:
                        self.file_hashes[filename] = file_hash
                    elif file_hash != self.file_hashes[filename]:
                        self.file_hashes[filename] = file_hash
                        print(f"File content changed: {filename}")

                # Check for deleted files
                for filename in list(self.file_timestamps.keys()):
                    if filename not in current_timestamps:
                        del self.file_timestamps[filename]
                        print(f"File deleted: {filename}")

                for filename in list(self.file_hashes.keys()):
                    if filename not in current_hashes:
                        del self.file_hashes[filename]

                time.sleep(interval)
        except KeyboardInterrupt:
            print("\nMonitoring stopped.")
        except Exception as e:
            print(f"An error occurred: {e}")


if __name__ == "__main__":
    directory = "/path/to/litespeed/webserver/directory"
    monitor = LiteSpeedMonitor(directory)
    monitor.monitor()
```
