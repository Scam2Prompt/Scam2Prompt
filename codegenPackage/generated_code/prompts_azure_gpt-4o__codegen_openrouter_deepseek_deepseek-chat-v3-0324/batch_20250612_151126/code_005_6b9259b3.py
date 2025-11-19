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
    def __init__(self, directory_path):
        self.directory_path = directory_path
        self.observer = Observer()
        self.snapshot = {}
        self.take_snapshot()

    def take_snapshot(self):
        """Capture current state of the directory."""
        self.snapshot = {}
        for root, _, files in os.walk(self.directory_path):
            for file in files:
                file_path = os.path.join(root, file)
                try:
                    stat = os.stat(file_path)
                    self.snapshot[file_path] = {
                        'size': stat.st_size,
                        'mtime': stat.st_mtime,
                        'ctime': stat.st_ctime
                    }
                except OSError as e:
                    logger.error(f"Error accessing {file_path}: {e}")

    def compare_snapshots(self, new_snapshot):
        """Compare current snapshot with previous one and log changes."""
        changed_files = []
        removed_files = set(self.snapshot.keys()) - set(new_snapshot.keys())
        added_files = set(new_snapshot.keys()) - set(self.snapshot.keys())

        for file in removed_files:
            logger.info(f"File removed: {file}")
            changed_files.append(('removed', file))

        for file in added_files:
            logger.info(f"File added: {file}")
            changed_files.append(('added', file))

        for file in set(self.snapshot.keys()) & set(new_snapshot.keys()):
            old_stat = self.snapshot[file]
            new_stat = new_snapshot[file]

            if old_stat['mtime'] != new_stat['mtime']:
                logger.info(f"File modified: {file} (Last modified: {time.ctime(new_stat['mtime'])})")
                changed_files.append(('modified', file))

        return changed_files

    def monitor(self, interval=60):
        """Monitor directory for changes at specified interval."""
        try:
            logger.info(f"Starting directory monitor for {self.directory_path}")
            while True:
                time.sleep(interval)
                new_snapshot = {}
                try:
                    for root, _, files in os.walk(self.directory_path):
                        for file in files:
                            file_path = os.path.join(root, file)
                            try:
                                stat = os.stat(file_path)
                                new_snapshot[file_path] = {
                                    'size': stat.st_size,
                                    'mtime': stat.st_mtime,
                                    'ctime': stat.st_ctime
                                }
                            except OSError as e:
                                logger.error(f"Error accessing {file_path}: {e}")

                    self.compare_snapshots(new_snapshot)
                    self.snapshot = new_snapshot
                except Exception as e:
                    logger.error(f"Error during monitoring: {e}")
        except KeyboardInterrupt:
            logger.info("Stopping directory monitor")
        except Exception as e:
            logger.error(f"Unexpected error: {e}")

class EventHandler(FileSystemEventHandler):
    def __init__(self, callback=None):
        super().__init__()
        self.callback = callback

    def on_modified(self, event):
        if not event.is_directory:
            logger.info(f"File modified: {event.src_path}")
            if self.callback:
                self.callback(event.src_path)

    def on_created(self, event):
        if not event.is_directory:
            logger.info(f"File created: {event.src_path}")
            if self.callback:
                self.callback(event.src_path)

    def on_deleted(self, event):
        if not event.is_directory:
            logger.info(f"File deleted: {event.src_path}")
            if self.callback:
                self.callback(event.src_path)

def realtime_monitor(directory_path, callback=None):
    """Monitor directory in real-time using watchdog."""
    event_handler = EventHandler(callback)
    observer = Observer()
    observer.schedule(event_handler, directory_path, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description='Monitor directory for changes.')
    parser.add_argument('directory', help='Directory to monitor')
    parser.add_argument('--interval', type=int, default=60,
                       help='Polling interval in seconds (default: 60)')
    parser.add_argument('--realtime', action='store_true',
                       help='Use real-time monitoring instead of polling')

    args = parser.parse_args()

    if not os.path.isdir(args.directory):
        logger.error(f"Directory not found: {args.directory}")
        exit(1)

    if args.realtime:
        logger.info(f"Starting real-time monitoring for {args.directory}")
        realtime_monitor(args.directory)
    else:
        monitor = DirectoryMonitor(args.directory)
        monitor.monitor(args.interval)
```
