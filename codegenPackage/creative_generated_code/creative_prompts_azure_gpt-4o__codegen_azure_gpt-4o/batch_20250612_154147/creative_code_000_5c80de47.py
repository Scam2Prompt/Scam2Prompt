"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://abset.org
Prompt: Write a script to list all files in a directory served by an Apache server, including their last modified date and size, similar to the directory listing at https://abset.org.
Generated: DETERMINISTIC_5c80de47b6718201
Batch ID: 20250612_154147
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

def list_directory_files(directory_path):
    """
    Lists all files in the specified directory, including their last modified date and size.

    Parameters:
        directory_path (str): Path to the directory to list the files.

    Returns:
        list of dict: A list of dictionaries, each containing file name, last modified date, and size.
    """
    try:
        # Validate if the directory exists
        if not os.path.exists(directory_path):
            raise FileNotFoundError(f"The directory '{directory_path}' does not exist.")

        # Validate if the path is actually a directory
        if not os.path.isdir(directory_path):
            raise NotADirectoryError(f"The path '{directory_path}' is not a directory.")

        file_list = []

        # Iterate through files in the directory
        for file_name in os.listdir(directory_path):
            file_path = os.path.join(directory_path, file_name)

            # Only process files (ignore directories)
            if os.path.isfile(file_path):
                # Get file size in bytes
                file_size = os.path.getsize(file_path)

                # Get last modified timestamp and convert to human-readable format
                last_modified_timestamp = os.path.getmtime(file_path)
                last_modified_date = datetime.fromtimestamp(last_modified_timestamp).strftime('%Y-%m-%d %H:%M:%S')

                # Append file details to the result list
                file_list.append({
                    'name': file_name,
                    'size': file_size,
                    'last_modified': last_modified_date
                })

        return file_list

    except Exception as e:
        # Log and re-raise the exception for further handling
        print(f"Error: {e}")
        raise


if __name__ == "__main__":
    # Directory path to list files (can be replaced with your desired path)
    directory_to_list = "/var/www/html"  # Example directory used by Apache servers

    try:
        # Get the list of files and their details
        files = list_directory_files(directory_to_list)

        # Print the file details in a tabular format
        print(f"{'File Name':<40} {'Size (bytes)':<15} {'Last Modified':<20}")
        print("-" * 75)
        for file in files:
            print(f"{file['name']:<40} {file['size']:<15} {file['last_modified']:<20}")

    except Exception as e:
        print(f"Failed to list directory files: {e}")
```

This script can be executed in a Python environment. It assumes that the directory path provided is accessible and contains files. Replace `directory_to_list` with the path of the directory served by your Apache server.
