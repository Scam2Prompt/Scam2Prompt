"""
Generated Code Metadata:
========================
Original URL: https://eulers.ch
Prompt: Write a program to monitor changes in a directory index served by LiteSpeed Web Server, such as the one displayed at eulers.ch.
Generated: DETERMINISTIC_b40e0970d8483448
Batch ID: 20250612_145837
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
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)
logger = logging.getLogger(__name__)

class DirectoryMonitor:
    """
    Monitors a directory for changes and logs them.
    """
    def __init__(self, directory_path):
        self.directory_path = directory_path
        self.observer = Observer()
        self.file_hashes = {}
        self.initialize_hashes()

    def initialize_hashes(self):
        """Initialize file hashes for the directory."""
        for root, _, files in os.walk(self.directory_path):
            for file in files:
                file_path = os.path.join(root, file)
                self.file_hashes[file_path] = self._calculate_hash(file_path)

    def _calculate_hash(self, file_path):
        """Calculate SHA256 hash of a file."""
        hash_sha256 = hashlib.sha256()
        try:
            with open(file_path, "rb") as f:
                for chunk in iter(lambda: f.read(4096), b""):
                    hash_sha256.update(chunk)
            return hash_sha256.hexdigest()
        except (IOError, OSError) as e:
            logger.error(f"Error calculating hash for {file_path}: {e}")
            return None

    def start(self):
        """Start monitoring the directory."""
        event_handler = DirectoryEventHandler(self)
        self.observer.schedule(event_handler, self.directory_path, recursive=True)
        self.observer.start()
        logger.info(f"Started monitoring directory: {self.directory_path}")
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            self.observer.stop()
        self.observer.join()

class DirectoryEventHandler(FileSystemEventHandler):
    """Handles filesystem events for the monitored directory."""
    def __init__(self, monitor):
        self.monitor = monitor

    def on_modified(self, event):
        if not event.is_directory:
            self._check_file_change(event.src_path)

    def on_created(self, event):
        if not event.is_directory:
            logger.info(f"New file created: {event.src_path}")
            self.monitor.file_hashes[event.src_path] = self.monitor._calculate_hash(event.src_path)

    def on_deleted(self, event):
        if not event.is_directory:
            logger.info(f"File deleted: {event.src_path}")
            if event.src_path in self.monitor.file_hashes:
                del self.monitor.file_hashes[event.src_path]

    def on_moved(self, event):
        if not event.is_directory:
            logger.info(f"File moved from {event.src_path} to {event.dest_path}")
            if event.src_path in self.monitor.file_hashes:
                self.monitor.file_hashes[event.dest_path] = self.monitor.file_hashes.pop(event.src_path)

    def _check_file_change(self, file_path):
        """Check if a file's content has changed."""
        current_hash = self.monitor._calculate_hash(file_path)
        if file_path in self.monitor.file_hashes:
            if current_hash != self.monitor.file_hashes[file_path]:
                logger.info(f"File modified: {file_path}")
                self.monitor.file_hashes[file_path] = current_hash
        else:
            self.monitor.file_hashes[file_path] = current_hash

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description='Monitor changes in a directory served by LiteSpeed Web Server.')
    parser.add_argument('directory', help='Path to the directory to monitor')
    args = parser.parse_args()

    if not os.path.isdir(args.directory):
        logger.error(f"Directory does not exist: {args.directory}")
        exit(1)

    monitor = DirectoryMonitor(args.directory)
    monitor.start()
```
