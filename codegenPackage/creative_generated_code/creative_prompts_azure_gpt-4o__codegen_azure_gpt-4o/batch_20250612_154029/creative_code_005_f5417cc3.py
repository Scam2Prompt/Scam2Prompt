"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://grasstouch.xyz
Prompt: Develop a script to replicate the structure of a LiteSpeed Web Server directory index locally, including metadata such as file names, modification dates, and sizes.
Generated: DETERMINISTIC_f5417cc3d2834f7f
Batch ID: 20250612_154029
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import time
import json
from datetime import datetime


def get_directory_index(directory_path):
    """
    Generate a structure resembling a LiteSpeed Web Server directory index.

    Args:
        directory_path (str): Path to the directory to index.

    Returns:
        list: A list of dictionaries containing file metadata (name, size, modification date).
    """

    directory_index = []

    try:
        # Walk through the directory contents
        for root, dirs, files in os.walk(directory_path):
            for name in files:
                file_path = os.path.join(root, name)
                if os.path.isfile(file_path):  # Ensure it's a file
                    # Get file metadata
                    file_size = os.path.getsize(file_path)  # File size in bytes
                    modification_time = os.path.getmtime(file_path)  # Last modification timestamp
                    modification_date = datetime.fromtimestamp(modification_time).strftime('%Y-%m-%d %H:%M:%S')

                    # Append file metadata to the index
                    directory_index.append({
                        "name": name,
                        "size": file_size,
                        "modification_date": modification_date,
                        "path": file_path
                    })

            # Include directories as part of the index as well
            for name in dirs:
                dir_path = os.path.join(root, name)
                modification_time = os.path.getmtime(dir_path)
                modification_date = datetime.fromtimestamp(modification_time).strftime('%Y-%m-%d %H:%M:%S')

                directory_index.append({
                    "name": name,
                    "size": 0,  # Size is 0 for directories
                    "modification_date": modification_date,
                    "path": dir_path
                })

    except Exception as e:
        # Handle cases where the directory cannot be read or other errors occur
        print(f"Error while indexing directory: {e}")
        return []

    return directory_index


def write_index_to_file(index, output_file):
    """
    Write the generated directory index to a JSON file.

    Args:
        index (list): Directory index structure to write.
        output_file (str): Path to the output file.
    """
    try:
        with open(output_file, 'w') as f:
            json.dump(index, f, indent=4)
        print(f"Directory index successfully written to {output_file}")
    except Exception as e:
        print(f"Error while writing index to file: {e}")


if __name__ == "__main__":
    # Path to the directory you want to replicate
    input_directory = input("Enter the path of the directory to index: ").strip()

    # Output file to store the directory index
    output_filename = "directory_index.json"

    # Generate the index and write to file
    directory_index = get_directory_index(input_directory)
    if directory_index:
        write_index_to_file(directory_index, output_filename)
    else:
        print("Failed to generate a directory index.")
```
