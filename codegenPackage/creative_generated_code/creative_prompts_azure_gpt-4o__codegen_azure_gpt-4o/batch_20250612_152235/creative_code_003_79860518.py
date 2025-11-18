"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://connect-amlprotect.elacas.edu.pk
Prompt: Create a script to monitor changes in a LiteSpeed Web Server directory listing, focusing on the "Last Modified" timestamps for files such as "check."
Generated: DETERMINISTIC_79860518afca7476
Batch ID: 20250612_152235
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here is the clean, production-ready Python script for monitoring changes in a LiteSpeed Web Server directory listing focusing on the "Last Modified" timestamps for files:

```python
import os
import time
from datetime import datetime

def monitor_directory(directory_path, target_file, interval=5):
    """
    Monitors a directory for changes in the 'Last Modified' timestamp of a specific file.

    Args:
        directory_path (str): The path of the directory to monitor.
        target_file (str): The name of the file to monitor (e.g., 'check').
        interval (int): The interval in seconds to check for changes (default is 5 seconds).

    Raises:
        FileNotFoundError: Raised if the directory or file does not exist.
    """
    # Ensure the directory exists
    if not os.path.isdir(directory_path):
        raise FileNotFoundError(f"Directory '{directory_path}' does not exist.")
    
    # Full path to the target file
    file_path = os.path.join(directory_path, target_file)
    
    # Ensure the target file exists
    if not os.path.isfile(file_path):
        raise FileNotFoundError(f"File '{target_file}' does not exist in the directory '{directory_path}'.")
    
    # Get the initial 'Last Modified' timestamp
    last_modified = os.path.getmtime(file_path)
    
    print(f"Monitoring '{target_file}' in directory '{directory_path}' for changes...")
    print(f"Initial Last Modified timestamp: {datetime.fromtimestamp(last_modified)}\n")
    
    try:
        while True:
            # Get the current 'Last Modified' timestamp
            current_modified = os.path.getmtime(file_path)
            
            # Compare timestamps
            if current_modified != last_modified:
                print(f"[{datetime.now()}] File '{target_file}' has been modified!")
                print(f"New Last Modified timestamp: {datetime.fromtimestamp(current_modified)}\n")
                
                # Update the last modified timestamp
                last_modified = current_modified
            
            # Sleep for the specified interval before checking again
            time.sleep(interval)
    except KeyboardInterrupt:
        print("\nMonitoring stopped by user.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example Usage
if __name__ == "__main__":
    # Replace '/path/to/directory' with the actual directory to monitor
    # Replace 'check' with the file name to monitor
    monitor_directory('/path/to/directory', 'check', interval=5)
```

This script follows best practices, including error handling for missing directories or files, and allows graceful termination via `KeyboardInterrupt`. Replace `/path/to/directory` and `check` with actual values before executing the script.
