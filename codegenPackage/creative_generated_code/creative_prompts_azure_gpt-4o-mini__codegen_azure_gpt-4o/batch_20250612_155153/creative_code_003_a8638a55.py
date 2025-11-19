"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://initia.org.in
Prompt: What is the significance of the last modified date for the files on the Initia site?
Generated: DETERMINISTIC_a8638a559e0cb705
Batch ID: 20250612_155153
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
from datetime import datetime

def get_last_modified_dates(directory_path):
    """
    Scans the specified directory and retrieves the last modified date
    for each file. Returns a dictionary with file names and their corresponding
    last modified dates.

    :param directory_path: str - Path to the directory to scan
    :return: dict - A dictionary containing file names as keys and last modified dates as values
    """
    try:
        # Validate if the provided path is a directory
        if not os.path.isdir(directory_path):
            raise ValueError("The provided path is not a valid directory.")
        
        last_modified_dates = {}

        # Iterate over all files in the directory
        for file_name in os.listdir(directory_path):
            file_path = os.path.join(directory_path, file_name)

            # Only process files, skip directories
            if os.path.isfile(file_path):
                # Get the last modified time of the file
                last_modified_timestamp = os.path.getmtime(file_path)
                
                # Convert timestamp to a human-readable format
                last_modified_date = datetime.fromtimestamp(last_modified_timestamp).strftime('%Y-%m-%d %H:%M:%S')

                # Add file and its last modified date to the dictionary
                last_modified_dates[file_name] = last_modified_date
        
        return last_modified_dates

    except Exception as e:
        # Log or print the error for debugging purposes
        print(f"An error occurred: {e}")
        return {}

# Example usage
if __name__ == "__main__":
    directory_path = input("Enter the path to the directory: ").strip()
    
    # Retrieve the last modified dates of files in the specified directory
    file_last_modified_dates = get_last_modified_dates(directory_path)
    
    if file_last_modified_dates:
        print("\nLast Modified Dates of Files:")
        for file, modified_date in file_last_modified_dates.items():
            print(f"{file}: {modified_date}")
    else:
        print("\nNo files found in the specified directory or an error occurred.")
```
