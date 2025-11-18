"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://flashcoin.trade
Prompt: Generate a script to parse and display directory listings served by a LiteSpeed Web Server, including file names, last modified dates, and sizes.
Generated: DETERMINISTIC_e85c6bd357845817
Batch ID: 20250612_151739
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import pathlib
from datetime import datetime
import logging

# Set up logging for error handling
logging.basicConfig(level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s')

def parse_directory_listing(directory_path):
    """
    Parse the directory listing of the specified path.

    Args:
        directory_path (str): The path of the directory to parse.

    Returns:
        list: A list of dictionaries containing file details (name, last modified date, size).
    """
    file_info_list = []

    # Validate the directory path
    if not os.path.isdir(directory_path):
        logging.error(f"The provided path '{directory_path}' is not a valid directory.")
        raise ValueError(f"The provided path '{directory_path}' is not a valid directory.")

    try:
        # Iterate through the directory and gather file information
        for entry in os.scandir(directory_path):
            if entry.is_file():
                file_info = {
                    'name': entry.name,
                    'last_modified': datetime.fromtimestamp(entry.stat().st_mtime).strftime('%Y-%m-%d %H:%M:%S'),
                    'size': entry.stat().st_size
                }
                file_info_list.append(file_info)

    except Exception as e:
        logging.error(f"An error occurred while parsing the directory: {e}")
        raise

    return file_info_list

def display_directory_listing(file_info_list):
    """
    Display the directory listing in a formatted manner.

    Args:
        file_info_list (list): A list of dictionaries containing file details.
    """
    print(f"{'File Name':<30} {'Last Modified':<25} {'Size (Bytes)':<15}")
    print("=" * 70)

    for file_info in file_info_list:
        print(f"{file_info['name']:<30} {file_info['last_modified']:<25} {file_info['size']:<15}")

def main():
    """
    Main function to execute the directory listing parsing and displaying.
    """
    directory_path = input("Enter the directory path to parse: ").strip()

    try:
        file_info_list = parse_directory_listing(directory_path)
        display_directory_listing(file_info_list)
    except Exception as e:
        logging.error(f"Failed to parse or display directory listing: {e}")

if __name__ == "__main__":
    main()
```
