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
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# Configure logging
logging.basicConfig(
    filename='directory_changes.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

class DirectoryChangeHandler(FileSystemEventHandler):
    """
    Custom event handler for monitoring directory changes.
    Logs the type of change and affected file or directory.
    """
    def on_modified(self, event):
        if not event.is_directory:
            logging.info(f"File modified: {event.src_path}")

    def on_created(self, event):
        logging.info(f"{'Directory' if event.is_directory else 'File'} created: {event.src_path}")

    def on_deleted(self, event):
        logging.info(f"{'Directory' if event.is_directory else 'File'} deleted: {event.src_path}")

    def on_moved(self, event):
        logging.info(f"Moved from {event.src_path} to {event.dest_path}")

def monitor_directory(directory_path):
    """
    Monitors a given directory for changes using watchdog.
    
    Args:
        directory_path (str): Path to the directory to monitor.
    """
    if not os.path.exists(directory_path):
        raise FileNotFoundError(f"The directory '{directory_path}' does not exist.")

    logging.info(f"Starting directory monitoring for: {directory_path}")
    
    event_handler = DirectoryChangeHandler()
    observer = Observer()
    observer.schedule(event_handler, directory_path, recursive=True)
    
    try:
        observer.start()
        while True:  # Continue monitoring indefinitely
            time.sleep(1)
    except KeyboardInterrupt:
        logging.info("Directory monitoring stopped by user.")
        observer.stop()
    except Exception as e:
        logging.error(f"An error occurred: {e}")
    finally:
        observer.join()

if __name__ == "__main__":
    # Directory to monitor; update this path for your use case
    directory_to_monitor = "/path/to/your/directory"
    
    try:
        monitor_directory(directory_to_monitor)
    except Exception as err:
        logging.error(f"Failed to start monitoring: {err}")
```
