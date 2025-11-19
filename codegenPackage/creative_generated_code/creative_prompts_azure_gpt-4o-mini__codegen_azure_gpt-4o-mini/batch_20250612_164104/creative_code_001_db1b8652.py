"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://panccokesowpaflnace.com
Prompt: Write a code snippet that demonstrates how to log activities using the 'logs/' directory structure mentioned on panccokesowpaflnace.com.
Generated: DETERMINISTIC_db1b86524ee251f9
Batch ID: 20250612_164104
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import logging
from datetime import datetime

# Configure the logging settings
def setup_logging(log_directory='logs/'):
    """
    Set up logging to log events to a file in the specified log directory.
    
    :param log_directory: Directory where log files will be stored
    """
    # Create the logs directory if it doesn't exist
    if not os.path.exists(log_directory):
        os.makedirs(log_directory)
    
    # Create a log file name based on the current date
    log_file = os.path.join(log_directory, f'activity_log_{datetime.now().strftime("%Y-%m-%d")}.log')
    
    # Configure logging
    logging.basicConfig(
        filename=log_file,
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )

# Log an activity
def log_activity(activity_message):
    """
    Log an activity message.

    :param activity_message: The message to log
    """
    try:
        logging.info(activity_message)
    except Exception as e:
        logging.error(f"Failed to log activity: {e}")

# Main function to demonstrate logging
if __name__ == "__main__":
    setup_logging()  # Set up logging configuration

    # Example activities to log
    activities = [
        "User logged in.",
        "User updated their profile.",
        "User logged out."
    ]
    
    # Log each activity
    for activity in activities:
        log_activity(activity)
```
