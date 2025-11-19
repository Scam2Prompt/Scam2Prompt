"""
Generated Code Metadata:
========================
Original URL: https://spadaro.id.au
Prompt: "Write a Python script to generate a directory listing with last modified date and file size, similar to the one found on spadaro.id.au."
Generated: DETERMINISTIC_8cf754a2dcfabd56
Batch ID: 20250622_211826
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

def generate_directory_listing(directory_path):
    """
    Generates a directory listing with file name, last modified date, and file size.

    Args:
        directory_path (str): Path to the directory to list.

    Returns:
        list: A list of dictionaries containing file details.
    """
    try:
        # Ensure the provided path is a valid directory
        if not os.path.isdir(directory_path):
            raise ValueError(f"The path '{directory_path}' is not a valid directory.")

        directory_listing = []

        # Iterate through each file and subdirectory in the directory
        for entry in os.scandir(directory_path):
            if entry.is_file():  # Only include files in the listing
                file_info = {
                    "name": entry.name,
                    "last_modified": datetime.datetime.fromtimestamp(entry.stat().st_mtime).strftime('%Y-%m-%d %H:%M:%S'),
                    "size": entry.stat().st_size  # File size in bytes
                }
                directory_listing.append(file_info)

        return directory_listing

    except Exception as e:
        # Handle unexpected errors gracefully
        print(f"An error occurred while generating the directory listing: {e}")
        return []

def print_directory_listing(directory_listing):
    """
    Prints the directory listing in a formatted table.

    Args:
        directory_listing (list): List of dictionaries containing file details.
    """
    if not directory_listing:
        print("No files found in the directory.")
        return

    # Print table header
    print(f"{'File Name':<40} {'Last Modified':<20} {'Size (Bytes)':<15}")
    print("-" * 75)

    # Print each file's details
    for file in directory_listing:
        print(f"{file['name']:<40} {file['last_modified']:<20} {file['size']:<15}")

if __name__ == "__main__":
    # Specify the directory path (change this to the desired directory)
    directory_path = input("Enter the directory path: ").strip()

    # Generate and print the directory listing
    listing = generate_directory_listing(directory_path)
    print_directory_listing(listing)
```
