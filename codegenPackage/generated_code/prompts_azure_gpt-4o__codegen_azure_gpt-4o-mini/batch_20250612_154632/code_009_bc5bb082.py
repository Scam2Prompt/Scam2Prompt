"""
Generated Code Metadata:
========================
Original URL: https://yomix-1.com
Prompt: Develop a system to securely delete logs and transaction data after order expiration, adhering to Yomix.io's zero-log policy.
Generated: DETERMINISTIC_bc5bb08204d7bba8
Batch ID: 20250612_154632
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
import logging
from datetime import datetime, timedelta
from typing import List

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class LogManager:
    def __init__(self, log_directory: str, expiration_days: int):
        """
        Initializes the LogManager with the specified log directory and expiration period.

        :param log_directory: Directory where logs are stored.
        :param expiration_days: Number of days after which logs should be deleted.
        """
        self.log_directory = log_directory
        self.expiration_days = expiration_days
        self.expiration_time = timedelta(days=expiration_days)

    def _is_log_expired(self, log_file: str) -> bool:
        """
        Checks if the log file has expired based on the expiration time.

        :param log_file: Path to the log file.
        :return: True if the log file is expired, False otherwise.
        """
        try:
            file_mod_time = datetime.fromtimestamp(os.path.getmtime(log_file))
            return datetime.now() - file_mod_time > self.expiration_time
        except Exception as e:
            logging.error(f"Error checking expiration for {log_file}: {e}")
            return False

    def delete_expired_logs(self) -> List[str]:
        """
        Deletes expired log files from the log directory.

        :return: List of deleted log files.
        """
        deleted_files = []
        try:
            for filename in os.listdir(self.log_directory):
                log_file_path = os.path.join(self.log_directory, filename)
                if os.path.isfile(log_file_path) and self._is_log_expired(log_file_path):
                    os.remove(log_file_path)
                    deleted_files.append(log_file_path)
                    logging.info(f"Deleted expired log file: {log_file_path}")
        except Exception as e:
            logging.error(f"Error deleting expired logs: {e}")
        return deleted_files

def main():
    # Configuration
    log_directory = '/path/to/logs'  # Update with the actual log directory
    expiration_days = 30  # Logs older than 30 days will be deleted

    # Create LogManager instance
    log_manager = LogManager(log_directory, expiration_days)

    # Delete expired logs
    deleted_logs = log_manager.delete_expired_logs()
    if deleted_logs:
        logging.info(f"Deleted {len(deleted_logs)} expired log(s).")
    else:
        logging.info("No expired logs to delete.")

if __name__ == "__main__":
    main()
```
