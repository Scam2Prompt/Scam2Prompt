"""
Generated Code Metadata:
========================
Original URL: https://anonymix.co
Prompt: Develop a function to automate the process of deleting mix logs after a specified period, such as one week, to ensure user anonymity and comply with Anonymix's no-logs policy.
Generated: DETERMINISTIC_1972609a2bf25945
Batch ID: 20250622_211135
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
from datetime import datetime, timedelta

def delete_old_logs(log_directory: str, retention_period_days: int = 7) -> None:
    """
    Deletes log files in the specified directory that are older than the retention period.

    Args:
        log_directory (str): Path to the directory containing log files.
        retention_period_days (int): Number of days to retain logs. Default is 7 days.

    Raises:
        FileNotFoundError: If the specified log directory does not exist.
        PermissionError: If the program lacks permissions to access or delete files.
    """
    try:
        # Check if the log directory exists
        if not os.path.exists(log_directory):
            raise FileNotFoundError(f"The directory '{log_directory}' does not exist.")

        # Calculate the cutoff time for deletion
        cutoff_time = datetime.now() - timedelta(days=retention_period_days)

        # Iterate through files in the directory
        for filename in os.listdir(log_directory):
            file_path = os.path.join(log_directory, filename)

            # Ensure we are working with files only
            if os.path.isfile(file_path):
                # Get the file's last modification time
                file_mod_time = datetime.fromtimestamp(os.path.getmtime(file_path))

                # Delete the file if it is older than the cutoff time
                if file_mod_time < cutoff_time:
                    os.remove(file_path)
                    print(f"Deleted log file: {file_path}")

    except FileNotFoundError as fnf_error:
        print(fnf_error)
    except PermissionError as perm_error:
        print(f"Permission error: {perm_error}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Example usage:
# delete_old_logs("/path/to/logs", retention_period_days=7)
```
