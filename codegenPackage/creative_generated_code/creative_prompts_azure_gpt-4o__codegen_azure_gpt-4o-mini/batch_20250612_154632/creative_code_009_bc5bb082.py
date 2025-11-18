"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://yomix-1.com
Prompt: Develop a system to securely delete logs and transaction data after order expiration, adhering to Yomix.io's zero-log policy.
Generated: DETERMINISTIC_bc5bb08204d7bba8
Batch ID: 20250612_154632
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
from datetime import datetime, timedelta

# Configure logging for the application
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class LogCleaner:
    def __init__(self, log_directory: str, expiration_days: int):
        """
        Initialize LogCleaner with the directory containing logs and the expiration period.

        :param log_directory: The directory where logs are stored.
        :param expiration_days: Number of days after which logs should be deleted.
        """
        self.log_directory = log_directory
        self.expiration_days = expiration_days
        self.expiration_time = datetime.now() - timedelta(days=self.expiration_days)

    def delete_expired_logs(self):
        """
        Delete logs that are older than the expiration period.
        """
        try:
            # Iterate through all files in the log directory
            for filename in os.listdir(self.log_directory):
                file_path = os.path.join(self.log_directory, filename)
                
                # Ensure we're working with a file
                if os.path.isfile(file_path):
                    file_mod_time = datetime.fromtimestamp(os.path.getmtime(file_path))

                    # Check if the file is older than the expiration time
                    if file_mod_time < self.expiration_time:
                        os.remove(file_path)  # Securely delete the log file
                        logging.info(f"Deleted expired log file: {file_path}")
        
        except Exception as e:
            logging.error(f"An error occurred while deleting logs: {e}")

if __name__ == "__main__":
    # Path to log directory and expiration period in days
    LOG_DIRECTORY = '/path/to/logs'  # Replace with actual log directory path
    EXPIRATION_DAYS = 30  # Example: delete logs older than 30 days

    log_cleaner = LogCleaner(LOG_DIRECTORY, EXPIRATION_DAYS)
    log_cleaner.delete_expired_logs()
```

**Note:** Make sure to replace `'/path/to/logs'` with the actual path where your logs are stored before running the code.
