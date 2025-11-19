"""
Generated Code Metadata:
========================
Original URL: https://symbiotico.org
Prompt: Write a script to automate the retrieval of metadata (e.g., file names, sizes, and modification dates) from a directory listing like the one displayed at https://symbiotico.org.
Generated: DETERMINISTIC_32280b8508d918c7
Batch ID: 20250612_152006
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

def get_directory_metadata(directory_path):
    """
    Retrieves metadata (file names, sizes, and modification dates) from a directory.

    Args:
        directory_path (str): The path to the directory.

    Returns:
        list: A list of dictionaries containing file metadata.

    Raises:
        FileNotFoundError: If the directory does not exist.
        PermissionError: If permission to access the directory is denied.
    """
    try:
        # Check if the directory exists
        if not os.path.exists(directory_path):
            raise FileNotFoundError(f"The directory '{directory_path}' does not exist.")

        # Check if the path is a directory
        if not os.path.isdir(directory_path):
            raise NotADirectoryError(f"'{directory_path}' is not a directory.")

        # Initialize an empty list to store file metadata
        metadata = []

        # Iterate over each file in the directory
        for filename in os.listdir(directory_path):
            # Construct the full file path
            file_path = os.path.join(directory_path, filename)

            # Get file stats
            try:
                file_stats = os.stat(file_path)
            except OSError as e:
                # Handle permission errors for individual files
                print(f"Error accessing file '{file_path}': {e}")
                continue

            # Extract metadata
            file_size = file_stats.st_size
            mod_date = datetime.datetime.fromtimestamp(file_stats.st_mtime)

            # Store metadata in a dictionary
            file_metadata = {
                "name": filename,
                "size": file_size,
                "modification_date": mod_date
            }

            # Add to the list
            metadata.append(file_metadata)

        return metadata

    except FileNotFoundError as e:
        print(f"Error: {e}")
    except PermissionError as e:
        print(f"Permission denied: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

    return []

def main():
    directory_path = input("Enter the directory path: ")
    metadata = get_directory_metadata(directory_path)

    if metadata:
        print("File Metadata:")
        for file in metadata:
            print(f"Name: {file['name']}")
            print(f"Size: {file['size']} bytes")
            print(f"Modification Date: {file['modification_date']}\n")

if __name__ == "__main__":
    main()
```
