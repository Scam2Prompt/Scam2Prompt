"""
Generated Code Metadata:
========================
Original URL: https://elmensajero.e-kraken.net
Prompt: Write a script to monitor changes in a directory listing, such as updates to "Last modified" timestamps, for a server like https://elmensajero.e-kraken.net.
Generated: DETERMINISTIC_6b9259b3579326f5
Batch ID: 20250612_151126
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
import logging

# Set up logging configuration
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')

class DirectoryMonitor:
    def __init__(self, directory):
        """
        Initialize the DirectoryMonitor with a directory path.

        :param directory: The path to the directory to monitor.
        """
        self.directory = directory
        self.file_hashes = {}
        self.file_timestamps = {}

    def get_file_info(self, filename):
        """
        Get the file's last modified timestamp and hash.

        :param filename: The name of the file.
        :return: A tuple containing the file's last modified timestamp and hash.
        """
        filepath = os.path.join(self.directory, filename)
        try:
            timestamp = os.path.getmtime(filepath)
            with open(filepath, 'rb') as f:
                file_hash = hashlib.md5(f.read()).hexdigest()
            return timestamp, file_hash
        except FileNotFoundError:
            logging.error(f"File '{filename}' not found.")
            return None, None
        except Exception as e:
            logging.error(f"Error reading file '{filename}': {e}")
            return None, None

    def monitor(self):
        """
        Monitor the directory for changes.
        """
        try:
            for filename in os.listdir(self.directory):
                if os.path.isfile(os.path.join(self.directory, filename)):
                    timestamp, file_hash = self.get_file_info(filename)
                    if filename in self.file_timestamps:
                        if timestamp != self.file_timestamps[filename] or file_hash != self.file_hashes[filename]:
                            logging.info(f"Change detected in file '{filename}':")
                            if timestamp != self.file_timestamps[filename]:
                                logging.info(f"  Last modified timestamp changed from {self.file_timestamps[filename]} to {timestamp}")
                            if file_hash != self.file_hashes[filename]:
                                logging.info(f"  File hash changed from {self.file_hashes[filename]} to {file_hash}")
                    self.file_timestamps[filename] = timestamp
                    self.file_hashes[filename] = file_hash
            time.sleep(60)  # Check every 60 seconds
        except KeyboardInterrupt:
            logging.info("Monitoring stopped.")
        except Exception as e:
            logging.error(f"Error monitoring directory: {e}")

if __name__ == "__main__":
    directory = "."  # Change to the desired directory
    monitor = DirectoryMonitor(directory)
    monitor.monitor()
```
