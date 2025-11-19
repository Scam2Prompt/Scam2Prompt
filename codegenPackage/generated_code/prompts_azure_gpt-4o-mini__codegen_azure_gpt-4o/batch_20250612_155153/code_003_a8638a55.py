"""
Generated Code Metadata:
========================
Original URL: https://initia.org.in
Prompt: What is the significance of the last modified date for the files on the Initia site?
Generated: DETERMINISTIC_a8638a559e0cb705
Batch ID: 20250612_155153
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
from datetime import datetime

def get_last_modified_dates(directory_path):
    """
    Retrieves the last modified dates for all files in the specified directory.

    Args:
        directory_path (str): The path to the directory containing the files.

    Returns:
        dict: A dictionary where keys are file names and values are their last modified dates.
    """
    try:
        # Validate if the provided path is a directory
        if not os.path.isdir(directory_path):
            raise ValueError(f"The path '{directory_path}' is not a valid directory.")

        last_modified_dates = {}

        # Iterate through all files in the directory
        for file_name in os.listdir(directory_path):
            file_path = os.path.join(directory_path, file_name)

            # Check if the current item is a file
            if os.path.isfile(file_path):
                # Get the last modified timestamp and convert it to a readable format
                timestamp = os.path.getmtime(file_path)
                readable_date = datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')
                last_modified_dates[file_name] = readable_date

        return last_modified_dates

    except Exception as e:
        # Handle unexpected errors gracefully
        print(f"An error occurred: {e}")
        return {}

def main():
    """
    Main function to demonstrate the retrieval of last modified dates for files.
    """
    # Example directory path (replace with the actual path to the Initia site files)
    directory_path = "/path/to/initia/site/files"

    # Get last modified dates for files in the directory
    last_modified_dates = get_last_modified_dates(directory_path)

    # Display the results
    if last_modified_dates:
        print("Last Modified Dates for Files:")
        for file_name, modified_date in last_modified_dates.items():
            print(f"{file_name}: {modified_date}")
    else:
        print("No files found or an error occurred.")

if __name__ == "__main__":
    main()
```
