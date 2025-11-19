"""
Generated Code Metadata:
========================
Original URL: https://consejodigitalmx.com
Prompt: Develop a Python script to monitor and report on the last modified dates of files on a server, similar to the information displayed on this webpage.
Generated: DETERMINISTIC_9d2d1b9fc6433b90
Batch ID: 20250622_211206
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

def get_file_modification_dates(directory):
    """
    Scans the specified directory and retrieves the last modified dates of all files.

    Args:
        directory (str): The path to the directory to scan.

    Returns:
        dict: A dictionary where keys are file paths and values are last modified timestamps.
    """
    file_mod_dates = {}
    try:
        # Walk through the directory and its subdirectories
        for root, _, files in os.walk(directory):
            for file in files:
                file_path = os.path.join(root, file)
                try:
                    # Get the last modified time of the file
                    mod_time = os.path.getmtime(file_path)
                    file_mod_dates[file_path] = mod_time
                except OSError as e:
                    # Handle errors related to file access
                    print(f"Error accessing file {file_path}: {e}")
    except Exception as e:
        # Handle errors related to directory traversal
        print(f"Error scanning directory {directory}: {e}")
    return file_mod_dates

def format_modification_dates(file_mod_dates):
    """
    Formats the file modification dates into a human-readable format.

    Args:
        file_mod_dates (dict): A dictionary of file paths and their last modified timestamps.

    Returns:
        dict: A dictionary where keys are file paths and values are formatted timestamps.
    """
    formatted_dates = {}
    for file_path, mod_time in file_mod_dates.items():
        # Convert the timestamp to a human-readable format
        formatted_dates[file_path] = datetime.fromtimestamp(mod_time).strftime('%Y-%m-%d %H:%M:%S')
    return formatted_dates

def main():
    """
    Main function to monitor and report on the last modified dates of files in a directory.
    """
    # Specify the directory to monitor
    directory_to_monitor = input("Enter the directory path to monitor: ").strip()

    if not os.path.isdir(directory_to_monitor):
        print("Invalid directory path. Please provide a valid directory.")
        return

    print(f"Scanning directory: {directory_to_monitor}")
    
    # Get the file modification dates
    file_mod_dates = get_file_modification_dates(directory_to_monitor)
    
    # Format the modification dates for reporting
    formatted_dates = format_modification_dates(file_mod_dates)
    
    # Display the results
    print("\nLast Modified Dates of Files:")
    for file_path, mod_date in formatted_dates.items():
        print(f"{file_path}: {mod_date}")

if __name__ == "__main__":
    main()
```
