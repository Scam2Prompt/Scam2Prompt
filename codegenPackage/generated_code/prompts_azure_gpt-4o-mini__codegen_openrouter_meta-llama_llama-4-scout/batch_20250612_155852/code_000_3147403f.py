"""
Generated Code Metadata:
========================
Original URL: https://bryantroll.com
Prompt: Generate a code snippet that demonstrates how to create an index of files in a directory using Python.
Generated: DETERMINISTIC_3147403fcb7ded63
Batch ID: 20250612_155852
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import logging

# Set up logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def create_file_index(directory_path):
    """
    Creates an index of files in a specified directory.

    Args:
        directory_path (str): The path to the directory to be indexed.

    Returns:
        dict: A dictionary containing file names as keys and their corresponding paths as values.

    Raises:
        FileNotFoundError: If the specified directory does not exist.
        NotADirectoryError: If the specified path is not a directory.
        PermissionError: If there is no permission to access the directory.
    """
    try:
        # Check if the directory exists
        if not os.path.exists(directory_path):
            raise FileNotFoundError(f"The directory '{directory_path}' does not exist.")

        # Check if the path is a directory
        if not os.path.isdir(directory_path):
            raise NotADirectoryError(f"The path '{directory_path}' is not a directory.")

        # Initialize an empty dictionary to store the file index
        file_index = {}

        # Iterate over each file in the directory
        for filename in os.listdir(directory_path):
            # Construct the full path to the file
            filepath = os.path.join(directory_path, filename)

            # Check if the path is a file (not a subdirectory)
            if os.path.isfile(filepath):
                # Add the file to the index
                file_index[filename] = filepath

        return file_index

    except FileNotFoundError as e:
        logging.error(e)
        raise
    except NotADirectoryError as e:
        logging.error(e)
        raise
    except PermissionError as e:
        logging.error(e)
        raise
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")
        raise

def main():
    directory_path = input("Enter the directory path: ")
    try:
        file_index = create_file_index(directory_path)
        print("File Index:")
        for filename, filepath in file_index.items():
            print(f"{filename}: {filepath}")
    except Exception as e:
        logging.error(f"Failed to create file index: {e}")

if __name__ == "__main__":
    main()
```
