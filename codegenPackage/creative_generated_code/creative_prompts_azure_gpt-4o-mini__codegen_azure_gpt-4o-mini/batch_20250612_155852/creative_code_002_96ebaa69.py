"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bryantroll.com
Prompt: Write a script that lists all files in a specified directory and outputs their last modified date and size.
Generated: DETERMINISTIC_96ebaa6984330e73
Batch ID: 20250612_155852
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

def list_files_in_directory(directory):
    """
    Lists all files in the specified directory along with their last modified date and size.
    
    Args:
        directory (str): The path of the directory to list files from.
    
    Raises:
        ValueError: If the provided directory path is not valid.
        OSError: If there is an issue accessing the directory.
    """
    # Check if the provided directory path is valid
    if not os.path.isdir(directory):
        raise ValueError(f"The provided path '{directory}' is not a valid directory.")

    # Print the header for the output
    print(f"{'Filename':<50} {'Last Modified':<30} {'Size (bytes)':<15}")
    print("=" * 95)

    try:
        # Iterate through the files in the directory
        for filename in os.listdir(directory):
            file_path = os.path.join(directory, filename)

            # Check if the path is a file
            if os.path.isfile(file_path):
                # Get last modified time and file size
                last_modified_time = os.path.getmtime(file_path)
                file_size = os.path.getsize(file_path)

                # Convert last modified time to a readable format
                last_modified_date = datetime.datetime.fromtimestamp(last_modified_time).strftime('%Y-%m-%d %H:%M:%S')

                # Print the file details
                print(f"{filename:<50} {last_modified_date:<30} {file_size:<15}")

    except OSError as e:
        print(f"Error accessing the directory: {e}")

if __name__ == "__main__":
    # Example usage
    try:
        directory_path = input("Enter the directory path: ")
        list_files_in_directory(directory_path)
    except ValueError as ve:
        print(ve)
```
