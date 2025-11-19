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
# Script to list all files in a specified directory along with their last modified date and size

import os
import sys
from datetime import datetime

def list_files_in_directory(directory):
    """
    Lists all files in the specified directory and outputs their last modified date and size.

    Args:
        directory (str): The path to the directory to list files from.

    Raises:
        ValueError: If the provided directory path does not exist or is not a directory.
    """
    try:
        # Check if the path exists and is a directory
        if not os.path.exists(directory):
            raise ValueError(f"The directory '{directory}' does not exist.")
        if not os.path.isdir(directory):
            raise ValueError(f"The path '{directory}' is not a directory.")

        # Iterate through all files in the directory
        print(f"Listing files in directory: {directory}")
        print(f"{'File Name':<30}{'Last Modified':<25}{'Size (bytes)':<15}")
        print("=" * 70)
        for entry in os.scandir(directory):
            if entry.is_file():  # Process only files
                file_name = entry.name
                last_modified = datetime.fromtimestamp(entry.stat().st_mtime).strftime('%Y-%m-%d %H:%M:%S')
                file_size = entry.stat().st_size
                print(f"{file_name:<30}{last_modified:<25}{file_size:<15}")
    except ValueError as ve:
        # Handle invalid directory paths
        print(f"Error: {ve}")
    except Exception as e:
        # Catch any unforeseen errors
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    # Check if the directory argument was provided
    if len(sys.argv) < 2:
        print("Usage: python list_files.py <directory_path>")
        sys.exit(1)

    # Get the directory path from the command-line arguments
    directory_path = sys.argv[1]
    list_files_in_directory(directory_path)
```
