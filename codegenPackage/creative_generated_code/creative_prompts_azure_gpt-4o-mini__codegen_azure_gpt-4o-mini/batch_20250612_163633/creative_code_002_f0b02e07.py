"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ecataloguegoodies-pepsico.com
Prompt: Create a code snippet that checks for the last modified date of files in a directory like the one found on the eCatalog Goodies PepsiCo website.
Generated: DETERMINISTIC_f0b02e07ae9d2e3e
Batch ID: 20250612_163633
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import datetime

def check_last_modified_dates(directory):
    """
    Check the last modified dates of files in a specified directory.

    Parameters:
    directory (str): The path to the directory to be scanned.

    Returns:
    dict: A dictionary mapping file names to their last modified dates.
    """
    # Dictionary to hold file names and their last modified dates
    last_modified_dates = {}

    try:
        # Iterate over all items in the specified directory
        for filename in os.listdir(directory):
            file_path = os.path.join(directory, filename)

            # Check if the item is a file
            if os.path.isfile(file_path):
                # Get the last modified time and convert to a readable format
                modified_time = os.path.getmtime(file_path)
                last_modified_dates[filename] = datetime.datetime.fromtimestamp(modified_time)

    except FileNotFoundError:
        print(f"Error: The directory '{directory}' does not exist.")
    except PermissionError:
        print(f"Error: Permission denied to access the directory '{directory}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

    return last_modified_dates

# Example usage:
if __name__ == "__main__":
    directory_path = '/path/to/your/directory'  # Replace with your directory path
    modified_files = check_last_modified_dates(directory_path)

    # Output the last modified dates
    for file, last_modified in modified_files.items():
        print(f"File: {file}, Last Modified: {last_modified}")
```
