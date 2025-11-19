"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nvavid.com
Prompt: Write a script to automate the management of server logs on a LiteSpeed web server.
Generated: DETERMINISTIC_4959c8d2b4c29f47
Batch ID: 20250612_155200
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import shutil
import logging
from datetime import datetime, timedelta

# Configure logging
logging.basicConfig(
    filename='server_log_management.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

class LogManager:
    def __init__(self, log_directory, archive_directory, retention_days=30):
        """
        Initialize the LogManager with the specified directories and retention policy.

        :param log_directory: Directory where current log files are stored.
        :param archive_directory: Directory where old log files will be archived.
        :param retention_days: Number of days to retain archived logs.
        """
        self.log_directory = log_directory
        self.archive_directory = archive_directory
        self.retention_days = retention_days

    def archive_old_logs(self):
        """
        Archive logs older than the specified retention days.
        """
        try:
            # Ensure the archive directory exists
            os.makedirs(self.archive_directory, exist_ok=True)
            logging.info("Ensured archive directory exists.")

            # Get the current time and calculate the cutoff time
            cutoff_time = datetime.now() - timedelta(days=self.retention_days)

            # Iterate through log files in the log directory
            for log_file in os.listdir(self.log_directory):
                log_file_path = os.path.join(self.log_directory, log_file)
                
                # Check if the file is older than the cutoff time
                if os.path.isfile(log_file_path):
                    file_modified_time = datetime.fromtimestamp(os.path.getmtime(log_file_path))
                    if file_modified_time < cutoff_time:
                        self._archive_log(log_file_path)

        except Exception as e:
            logging.error(f"Error archiving old logs: {e}")

    def _archive_log(self, log_file_path):
        """
        Move a log file to the archive directory.

        :param log_file_path: The path to the log file to archive.
        """
        try:
            # Construct the destination file path
            log_file_name = os.path.basename(log_file_path)
            archived_file_path = os.path.join(self.archive_directory, log_file_name)

            # Move the log file
            shutil.move(log_file_path, archived_file_path)
            logging.info(f"Archived log file: {log_file_name}")

        except Exception as e:
            logging.error(f"Failed to archive log file {log_file_path}: {e}")

    def clean_old_archived_logs(self):
        """
        Remove archived logs older than the retention policy.
        """
        try:
            # Get the current time and calculate the cutoff time for archived logs
            cutoff_time = datetime.now() - timedelta(days=self.retention_days)

            # Iterate through archived log files in the archive directory
            for archived_file in os.listdir(self.archive_directory):
                archived_file_path = os.path.join(self.archive_directory, archived_file)

                # Check if the file is older than the cutoff time
                if os.path.isfile(archived_file_path):
                    file_modified_time = datetime.fromtimestamp(os.path.getmtime(archived_file_path))
                    if file_modified_time < cutoff_time:
                        self._remove_old_archived_log(archived_file_path)

        except Exception as e:
            logging.error(f"Error cleaning old archived logs: {e}")

    def _remove_old_archived_log(self, archived_file_path):
        """
        Remove an old archived log file.

        :param archived_file_path: The path to the archived log file to remove.
        """
        try:
            os.remove(archived_file_path)
            logging.info(f"Removed old archived log file: {archived_file_path}")

        except Exception as e:
            logging.error(f"Failed to remove old archived log file {archived_file_path}: {e}")

if __name__ == "__main__":
    # Define log directory and archive directory
    LOG_DIRECTORY = '/path/to/litespeed/logs'
    ARCHIVE_DIRECTORY = '/path/to/litespeed/archive'

    # Initialize LogManager
    log_manager = LogManager(LOG_DIRECTORY, ARCHIVE_DIRECTORY)

    # Run the log management tasks
    log_manager.archive_old_logs()
    log_manager.clean_old_archived_logs()
```
