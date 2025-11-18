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
import logging
from datetime import datetime, timedelta

# Configure logging for error handling and monitoring
logging.basicConfig(
    level=logging.INFO, 
    format='%(asctime)s - %(levelname)s - %(message)s',
)

def delete_transaction_logs(logs_directory: str, retention_period_days: int) -> None:
    """
    Deletes transaction logs from the specified directory that are older than the retention period.
    
    Args:
        logs_directory (str): Path to the directory containing transaction logs.
        retention_period_days (int): Number of days to retain logs. Older logs will be deleted.
    """
    try:
        # Ensure the directory exists
        if not os.path.exists(logs_directory):
            logging.error("Logs directory does not exist: %s", logs_directory)
            return
        
        logging.info("Starting log deletion process in directory: %s", logs_directory)
        
        # Calculate the cutoff time for deletion
        cutoff_time = datetime.now() - timedelta(days=retention_period_days)

        # List all files in the directory
        for log_file in os.listdir(logs_directory):
            file_path = os.path.join(logs_directory, log_file)
            
            # Ensure it's a file before proceeding
            if os.path.isfile(file_path):
                # Get the file's modification time
                file_mod_time = datetime.fromtimestamp(os.path.getmtime(file_path))
                
                # Check if the file is older than the retention period
                if file_mod_time < cutoff_time:
                    try:
                        # Delete the file
                        os.remove(file_path)
                        logging.info("Deleted file: %s", file_path)
                    except Exception as e:
                        logging.error("Failed to delete file: %s. Error: %s", file_path, e)
            else:
                logging.debug("Skipping non-file entry: %s", file_path)
        
        logging.info("Log deletion process completed.")

    except Exception as e:
        logging.error("An unexpected error occurred: %s", e)

# Example usage:
# delete_transaction_logs("/path/to/logs", 30)
```
