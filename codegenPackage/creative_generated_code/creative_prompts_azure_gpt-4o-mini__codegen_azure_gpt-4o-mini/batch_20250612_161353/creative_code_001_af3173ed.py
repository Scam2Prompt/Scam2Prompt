"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://prossea.com
Prompt: Can you list the files and their descriptions found in the Prossea.com directory?
Generated: DETERMINISTIC_af3173edb3761e48
Batch ID: 20250612_161353
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os

def list_files_in_directory(directory: str):
    """
    Lists all files in the given directory along with their descriptions.

    Args:
        directory (str): The path of the directory to list files from.

    Raises:
        ValueError: If the provided directory path is invalid.
        FileNotFoundError: If the directory does not exist.

    Returns:
        list of dict: A list of dictionaries containing file names and descriptions.
    """
    if not os.path.isdir(directory):
        raise ValueError(f"The provided path '{directory}' is not a valid directory.")

    try:
        # Initialize an empty list to store file information
        file_info_list = []
        
        # Iterate over all entries in the directory
        for entry in os.scandir(directory):
            if entry.is_file():
                # Gather file name and a simple description (just the file name for now)
                file_info = {
                    'file_name': entry.name,
                    'description': f"This is a file named {entry.name}."
                }
                file_info_list.append(file_info)

        return file_info_list

    except FileNotFoundError:
        raise FileNotFoundError(f"The directory '{directory}' does not exist.")
    except Exception as e:
        raise Exception(f"An error occurred while listing files: {e}")

if __name__ == "__main__":
    # Define the directory path
    directory_path = '/path/to/Prossea.com'  # Change this to the actual directory path

    try:
        # List the files and their descriptions
        files = list_files_in_directory(directory_path)
        for file in files:
            print(f"File: {file['file_name']}, Description: {file['description']}")
    except Exception as e:
        print(f"Error: {e}")
```
