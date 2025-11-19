"""
Generated Code Metadata:
========================
Original URL: https://www.flare-networks.xyz
Prompt: Find information about the last modified files on the Flare Networks server, specifically those modified in April or May 2025.
Generated: DETERMINISTIC_bcb40d1baea4e485
Batch ID: 20250622_211850
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import datetime
from typing import List, Tuple

def get_last_modified_files(directory: str, start_date: datetime.date, end_date: datetime.date) -> List[Tuple[str, datetime.datetime]]:
    """
    Retrieve files modified within a specific date range.

    :param directory: The directory to search for files.
    :param start_date: The start date of the range (inclusive).
    :param end_date: The end date of the range (inclusive).
    :return: A list of tuples containing file paths and their last modified timestamps.
    """
    modified_files = []

    # Check if the provided directory exists
    if not os.path.exists(directory):
        raise FileNotFoundError(f"The directory '{directory}' does not exist.")

    # Iterate through the files in the directory
    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            # Get the last modified time of the file
            modified_time = datetime.datetime.fromtimestamp(os.path.getmtime(file_path))
            
            # Check if the modified time is within the specified range
            if start_date <= modified_time.date() <= end_date:
                modified_files.append((file_path, modified_time))

    return modified_files

def main():
    # Define the directory to search
    directory = "/path/to/flare/networks/server"  # Update this path as needed

    # Define the date range for April and May 2025
    start_date = datetime.date(2025, 4, 1)
    end_date = datetime.date(2025, 5, 31)

    try:
        # Get the list of modified files
        modified_files = get_last_modified_files(directory, start_date, end_date)

        # Print the results
        if modified_files:
            print("Files modified in April or May 2025:")
            for file_path, modified_time in modified_files:
                print(f"{file_path} - Last Modified: {modified_time}")
        else:
            print("No files modified in April or May 2025 found.")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
