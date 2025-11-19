"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://elmensajero.e-kraken.net
Prompt: Write a script that retrieves the last modified date of files in the e-Kraken directory structure.
Generated: DETERMINISTIC_9b49838c53e855eb
Batch ID: 20250612_140024
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
from datetime import datetime

def get_last_modified_dates(dir_path):
    """
    Retrieve the last modified dates of all files in the given directory structure.

    Args:
        dir_path (str): The path to the e-Kraken directory.

    Returns:
        dict: A dictionary with file paths as keys and last modified dates as values.
    """
    last_modified_dates = {}

    # Check if the provided path is a directory
    if not os.path.isdir(dir_path):
        raise ValueError(f"The provided path '{dir_path}' is not a valid directory.")

    # Walk through the directory structure
    for root, dirs, files in os.walk(dir_path):
        for file in files:
            file_path = os.path.join(root, file)
            try:
                # Get the last modified time and format it
                modified_time = os.path.getmtime(file_path)
                last_modified_dates[file_path] = datetime.fromtimestamp(modified_time).strftime('%Y-%m-%d %H:%M:%S')
            except Exception as e:
                print(f"Error retrieving last modified date for file {file_path}: {e}")

    return last_modified_dates

if __name__ == "__main__":
    # Define the path to the e-Kraken directory
    e_kraken_directory = "/path/to/e-Kraken"  # Update this path accordingly

    try:
        # Retrieve and print the last modified dates
        modified_dates = get_last_modified_dates(e_kraken_directory)
        for file_path, modified_date in modified_dates.items():
            print(f"{file_path}: Last Modified Date - {modified_date}")
    except ValueError as ve:
        print(ve)
    except Exception as e:
        print(f"An error occurred: {e}")
```
