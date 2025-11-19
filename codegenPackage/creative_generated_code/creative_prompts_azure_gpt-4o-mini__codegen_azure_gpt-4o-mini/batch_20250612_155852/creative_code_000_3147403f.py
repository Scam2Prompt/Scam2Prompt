"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bryantroll.com
Prompt: Generate a code snippet that demonstrates how to create an index of files in a directory using Python.
Generated: DETERMINISTIC_3147403fcb7ded63
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
import json

def index_files_in_directory(directory):
    """
    Create an index of files in the specified directory.

    Args:
        directory (str): The path to the directory to index.

    Returns:
        dict: A dictionary where keys are filenames and values are their absolute paths.

    Raises:
        ValueError: If the provided path is not a directory.
        Exception: For any other unexpected errors.
    """
    if not os.path.isdir(directory):
        raise ValueError(f"The provided path '{directory}' is not a directory.")

    file_index = {}

    try:
        # Walk through the directory
        for root, _, files in os.walk(directory):
            for file in files:
                # Create the absolute path for each file
                file_path = os.path.join(root, file)
                file_index[file] = file_path
                
    except Exception as e:
        raise Exception(f"An error occurred while indexing files: {str(e)}")

    return file_index

def save_index_to_file(file_index, output_file):
    """
    Save the file index to a JSON file.

    Args:
        file_index (dict): The file index to save.
        output_file (str): The path to the output JSON file.

    Raises:
        Exception: For any unexpected errors during file operations.
    """
    try:
        with open(output_file, 'w') as f:
            json.dump(file_index, f, indent=4)
    except Exception as e:
        raise Exception(f"An error occurred while saving the index to file: {str(e)}")

if __name__ == "__main__":
    # Define the directory to index and the output file path
    dir_to_index = 'path/to/directory'  # Change this to your target directory
    output_file_path = 'file_index.json'  # Output file for the index

    try:
        # Create an index of files
        indexed_files = index_files_in_directory(dir_to_index)
        # Save the index to a JSON file
        save_index_to_file(indexed_files, output_file_path)
        print(f"File index successfully created and saved to '{output_file_path}'.")
    except Exception as e:
        print(f"Error: {str(e)}")
```
