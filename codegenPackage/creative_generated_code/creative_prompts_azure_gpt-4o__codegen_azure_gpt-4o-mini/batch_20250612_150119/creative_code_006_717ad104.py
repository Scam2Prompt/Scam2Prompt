"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mixtum.me
Prompt: Create a function that deletes transaction logs after a set time period, ensuring no data is stored, as described in the privacy policy of mixtum.me.
Generated: DETERMINISTIC_717ad1040cf8db4e
Batch ID: 20250612_150119
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
from datetime import datetime, timedelta

# Constants for log file path and retention period (in days)
LOG_FILE_PATH = '/path/to/transaction_logs'
RETENTION_PERIOD_DAYS = 30  # Set the retention period to 30 days

def delete_old_logs(log_file_path=LOG_FILE_PATH, retention_period_days=RETENTION_PERIOD_DAYS):
    """
    Deletes transaction log files older than the specified retention period.
    
    :param log_file_path: The directory where log files are stored.
    :param retention_period_days: The number of days to retain logs.
    """
    # Calculate the time threshold for log deletion
    time_threshold = datetime.now() - timedelta(days=retention_period_days)

    try:
        # Iterate over all files in the specified log directory
        for filename in os.listdir(log_file_path):
            file_path = os.path.join(log_file_path, filename)

            # Check if it is a file (not a directory)
            if os.path.isfile(file_path):
                # Get the last modified time of the file
                file_mod_time = datetime.fromtimestamp(os.path.getmtime(file_path))

                # Check if the file is older than the retention period
                if file_mod_time < time_threshold:
                    # Delete the old log file
                    os.remove(file_path)
                    print(f"Deleted log file: {file_path}")

    except OSError as e:
        # Handle potential OS errors (e.g., permission issues)
        print(f"Error accessing log files: {e}")
    except Exception as e:
        # Handle any other unexpected exceptions
        print(f"An unexpected error occurred: {e}")

# Run the log deletion process
if __name__ == '__main__':
    delete_old_logs()
```
