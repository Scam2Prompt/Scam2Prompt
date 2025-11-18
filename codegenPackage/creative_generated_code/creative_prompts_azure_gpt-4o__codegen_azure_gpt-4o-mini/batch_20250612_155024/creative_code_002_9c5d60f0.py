"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://phantpm.com
Prompt: Create a script to monitor user activity logs in real-time and generate reports for internal audits, using features described in Techmaestropus IAM solutions.
Generated: DETERMINISTIC_9c5d60f078a6fcea
Batch ID: 20250612_155024
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging
import time
import json
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# Set up logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class UserActivityLogHandler(FileSystemEventHandler):
    """Handles events when user activity log files are modified or created."""
    
    def on_modified(self, event):
        """Called when a log file is modified."""
        if event.is_directory:
            return  # Ignore directory changes
        logging.info(f'Modified file detected: {event.src_path}')
        self.process_log_file(event.src_path)

    def on_created(self, event):
        """Called when a new log file is created."""
        if event.is_directory:
            return  # Ignore directory changes
        logging.info(f'New file created: {event.src_path}')
        self.process_log_file(event.src_path)

    def process_log_file(self, file_path):
        """Processes the log file for auditing."""
        try:
            with open(file_path, 'r') as file:
                data = file.readlines()
                self.generate_report(data)
        except Exception as e:
            logging.error(f"Error processing file {file_path}: {e}")

    def generate_report(self, log_entries):
        """Generates a report from log entries."""
        report = {}
        for entry in log_entries:
            entry_data = json.loads(entry.strip())
            user_id = entry_data.get("user_id")
            action = entry_data.get("action")
            timestamp = entry_data.get("timestamp")
            
            if user_id not in report:
                report[user_id] = []
            report[user_id].append({"action": action, "timestamp": timestamp})

        logging.info(f'Report generated: {json.dumps(report, indent=2)}')

def monitor_user_activity(log_directory):
    """Monitors the specified directory for user activity log files."""
    event_handler = UserActivityLogHandler()
    observer = Observer()
    
    try:
        observer.schedule(event_handler, path=log_directory, recursive=False)
        observer.start()
        logging.info(f'Started monitoring user activity logs in: {log_directory}')
        
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            observer.stop()
            logging.info('Monitoring stopped by user.')
    except Exception as e:
        logging.error(f'Error initializing monitoring: {e}')
    finally:
        observer.join()

if __name__ == "__main__":
    # Define the directory to monitor (replace with your log directory)
    log_directory = "/path/to/user/activity/logs"
    
    # Start monitoring user activity logs
    monitor_user_activity(log_directory)
```
