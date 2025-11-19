"""
Generated Code Metadata:
========================
Original URL: https://elmensajero.e-kraken.net
Prompt: Generate code to parse and display the contents of a directory listing, including metadata like "Last modified" and "Size," as shown on the webpage.
Generated: DETERMINISTIC_42460c2115a1c55d
Batch ID: 20250612_151126
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import stat
from datetime import datetime

def get_directory_listing(directory_path):
    """
    Retrieves and parses the contents of a directory listing.

    Args:
        directory_path (str): The path to the directory.

    Returns:
        list: A list of dictionaries containing file metadata.

    Raises:
        FileNotFoundError: If the specified directory does not exist.
        NotADirectoryError: If the specified path is not a directory.
    """
    try:
        # Check if the directory exists and is indeed a directory
        if not os.path.exists(directory_path):
            raise FileNotFoundError(f"The directory '{directory_path}' does not exist.")
        if not os.path.isdir(directory_path):
            raise NotADirectoryError(f"'{directory_path}' is not a directory.")

        # Initialize an empty list to store file metadata
        directory_listing = []

        # Iterate over each file in the directory
        for filename in os.listdir(directory_path):
            # Construct the full path to the file
            filepath = os.path.join(directory_path, filename)

            # Get file stats
            file_stat = os.stat(filepath)

            # Extract relevant metadata
            file_metadata = {
                "Name": filename,
                "Last Modified": datetime.fromtimestamp(file_stat.st_mtime).strftime("%Y-%m-%d %H:%M:%S"),
                "Size": file_stat.st_size,
                "Type": "Directory" if stat.S_ISDIR(file_stat.st_mode) else "File"
            }

            # Add the file metadata to the directory listing
            directory_listing.append(file_metadata)

        return directory_listing

    except Exception as e:
        print(f"An error occurred: {e}")
        return []

def display_directory_listing(directory_path):
    """
    Displays the contents of a directory listing, including metadata.

    Args:
        directory_path (str): The path to the directory.
    """
    directory_listing = get_directory_listing(directory_path)

    if directory_listing:
        # Print the directory listing in a tabular format
        print(f"Directory Listing for: {directory_path}")
        print("-----------------------------------------")
        print(f"{'Name':<50} {'Last Modified':<20} {'Size':<10} {'Type':<10}")
        print("-----------------------------------------")
        for file in directory_listing:
            print(f"{file['Name']:<50} {file['Last Modified']:<20} {file['Size']:<10} {file['Type']:<10}")
    else:
        print("No files found in the directory.")

if __name__ == "__main__":
    directory_path = input("Enter the directory path: ")
    display_directory_listing(directory_path)
```
