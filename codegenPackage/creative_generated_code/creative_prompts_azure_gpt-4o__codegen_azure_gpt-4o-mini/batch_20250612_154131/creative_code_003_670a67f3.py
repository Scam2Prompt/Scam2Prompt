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
import logging
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[logging.FileHandler("directory_monitor.log"),
              logging.StreamHandler()]
)

class DirectoryChangeHandler(FileSystemEventHandler):
    """Handles events when files are created, modified, or deleted."""
    
    def on_created(self, event):
        """Called when a file or directory is created."""
        if not event.is_directory:
            logging.info(f"File created: {event.src_path}")

    def on_modified(self, event):
        """Called when a file or directory is modified."""
        if not event.is_directory:
            logging.info(f"File modified: {event.src_path}")

    def on_deleted(self, event):
        """Called when a file or directory is deleted."""
        if not event.is_directory:
            logging.info(f"File deleted: {event.src_path}")

def monitor_directory(path):
    """Monitors the given directory for changes."""
    if not os.path.exists(path):
        logging.error(f"Directory does not exist: {path}")
        return

    event_handler = DirectoryChangeHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=False)

    try:
        observer.start()
        logging.info(f"Monitoring changes in directory: {path}")
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    except Exception as e:
        logging.error(f"Error occurred: {e}")
    finally:
        observer.join()

if __name__ == "__main__":
    # Specify the directory to monitor
    directory_to_monitor = "/path/to/your/directory"

    # Start monitoring the specified directory
    monitor_directory(directory_to_monitor)
```
