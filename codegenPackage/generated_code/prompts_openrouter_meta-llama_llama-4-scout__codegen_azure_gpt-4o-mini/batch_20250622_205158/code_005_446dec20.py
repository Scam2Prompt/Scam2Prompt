"""
Generated Code Metadata:
========================
Original URL: https://fuelgastech.co.ke
Prompt: How can I programmatically check the last modified dates of directories and files on a LiteSpeed server using a programming language of choice?
Generated: DETERMINISTIC_446dec2007feaf7d
Batch ID: 20250622_205158
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
from datetime import datetime

def get_last_modified_dates(path):
    """
    Recursively retrieves the last modified dates of all files and directories
    in the specified path.

    Args:
        path (str): The directory path to check.

    Returns:
        dict: A dictionary with file/directory names as keys and their last modified
              timestamps as values.
    """
    last_modified_dates = {}

    # Check if the provided path is a valid directory
    if not os.path.isdir(path):
        raise ValueError(f"The provided path '{path}' is not a valid directory.")

    # Walk through the directory
    for root, dirs, files in os.walk(path):
        # Get last modified date for directories
        for dir_name in dirs:
            dir_path = os.path.join(root, dir_name)
            last_modified_dates[dir_path] = os.path.getmtime(dir_path)

        # Get last modified date for files
        for file_name in files:
            file_path = os.path.join(root, file_name)
            last_modified_dates[file_path] = os.path.getmtime(file_path)

    return last_modified_dates

def format_timestamps(last_modified_dates):
    """
    Formats the last modified timestamps into a human-readable format.

    Args:
        last_modified_dates (dict): A dictionary with file/directory names as keys
                                     and their last modified timestamps as values.

    Returns:
        dict: A dictionary with file/directory names as keys and their last modified
              dates as formatted strings.
    """
    formatted_dates = {}
    for path, timestamp in last_modified_dates.items():
        formatted_dates[path] = datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')
    return formatted_dates

def main():
    # Specify the path to check
    path_to_check = '/path/to/your/directory'  # Change this to your target directory

    try:
        # Get last modified dates
        last_modified_dates = get_last_modified_dates(path_to_check)
        
        # Format the timestamps for better readability
        formatted_dates = format_timestamps(last_modified_dates)

        # Print the results
        for path, date in formatted_dates.items():
            print(f"{path}: {date}")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
