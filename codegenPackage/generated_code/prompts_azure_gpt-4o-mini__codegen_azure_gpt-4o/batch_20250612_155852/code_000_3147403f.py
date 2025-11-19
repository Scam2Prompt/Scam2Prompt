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

def create_file_index(directory_path):
    """
    Creates an index of files in the specified directory.

    Args:
        directory_path (str): The path to the directory to index.

    Returns:
        dict: A dictionary where keys are filenames and values are their absolute paths.
    """
    # Validate the input directory path
    if not os.path.isdir(directory_path):
        raise ValueError(f"The provided path '{directory_path}' is not a valid directory.")

    file_index = {}

    try:
        # Iterate through the directory contents
        for root, _, files in os.walk(directory_path):
            for file in files:
                # Get the absolute path of the file
                absolute_path = os.path.join(root, file)
                # Add the file to the index
                file_index[file] = absolute_path
    except Exception as e:
        # Handle unexpected errors
        raise RuntimeError(f"An error occurred while indexing files: {e}")

    return file_index


if __name__ == "__main__":
    # Example usage
    try:
        directory = input("Enter the directory path to index: ").strip()
        index = create_file_index(directory)
        print("File Index:")
        for filename, path in index.items():
            print(f"{filename}: {path}")
    except ValueError as ve:
        print(f"Input Error: {ve}")
    except RuntimeError as re:
        print(f"Runtime Error: {re}")
    except Exception as e:
        print(f"Unexpected Error: {e}")
```
