"""
Generated Code Metadata:
========================
Original URL: https://murtilla.cl
Prompt: Write a Python script to generate an index of a file directory with last modified dates and file sizes.
Generated: DETERMINISTIC_9f54233b6b7c6292
Batch ID: 20250622_212318
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

def generate_directory_index(directory_path):
    """
    Generates an index of files in the specified directory, including their last modified dates and sizes.

    Args:
        directory_path (str): Path to the directory to index.

    Returns:
        list[dict]: A list of dictionaries containing file information.
    """
    try:
        # Ensure the provided path is a valid directory
        if not os.path.isdir(directory_path):
            raise ValueError(f"The path '{directory_path}' is not a valid directory.")

        # List to store file information
        file_index = []

        # Walk through the directory and gather file details
        for root, _, files in os.walk(directory_path):
            for file in files:
                file_path = os.path.join(root, file)
                try:
                    # Get file stats
                    file_stats = os.stat(file_path)
                    file_info = {
                        "file_name": file,
                        "file_path": file_path,
                        "last_modified": datetime.datetime.fromtimestamp(file_stats.st_mtime).strftime('%Y-%m-%d %H:%M:%S'),
                        "file_size": file_stats.st_size  # File size in bytes
                    }
                    file_index.append(file_info)
                except FileNotFoundError:
                    # Handle cases where the file might have been removed during processing
                    print(f"Warning: File '{file_path}' not found. Skipping.")
                except PermissionError:
                    # Handle cases where the file is inaccessible
                    print(f"Warning: Permission denied for file '{file_path}'. Skipping.")

        return file_index

    except Exception as e:
        # Catch any unexpected errors and print a meaningful message
        print(f"Error: {e}")
        return []

def save_index_to_file(file_index, output_file):
    """
    Saves the directory index to a file in a readable format.

    Args:
        file_index (list[dict]): The directory index to save.
        output_file (str): Path to the output file.
    """
    try:
        with open(output_file, 'w') as f:
            for file_info in file_index:
                f.write(f"File Name: {file_info['file_name']}\n")
                f.write(f"File Path: {file_info['file_path']}\n")
                f.write(f"Last Modified: {file_info['last_modified']}\n")
                f.write(f"File Size: {file_info['file_size']} bytes\n")
                f.write("-" * 40 + "\n")
        print(f"Directory index successfully saved to '{output_file}'.")
    except Exception as e:
        print(f"Error: Unable to save index to file. {e}")

if __name__ == "__main__":
    # Example usage
    directory_path = input("Enter the directory path to index: ").strip()
    output_file = input("Enter the output file path: ").strip()

    # Generate the directory index
    file_index = generate_directory_index(directory_path)

    # Save the index to a file
    if file_index:
        save_index_to_file(file_index, output_file)
```
