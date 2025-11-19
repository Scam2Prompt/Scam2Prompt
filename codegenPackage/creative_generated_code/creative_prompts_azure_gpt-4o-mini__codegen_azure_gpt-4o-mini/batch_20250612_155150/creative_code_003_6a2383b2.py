"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jci.tuenlacecristiano.com
Prompt: What types of files are included in the index directory of the Tuenlace Cristiano website?
Generated: DETERMINISTIC_6a2383b25fd414e4
Batch ID: 20250612_155150
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os

def get_files_in_directory(directory_path):
    """
    Get a list of files in the specified directory.

    :param directory_path: Path to the directory to scan for files
    :return: List of file names in the directory
    :raises ValueError: If the provided path is not a directory
    :raises OSError: If the directory cannot be accessed
    """
    # Check if the directory path is a valid directory
    if not os.path.isdir(directory_path):
        raise ValueError(f"The provided path '{directory_path}' is not a valid directory.")
    
    try:
        # List all files in the directory
        files = os.listdir(directory_path)
        # Filter out only files (excluding subdirectories)
        file_list = [f for f in files if os.path.isfile(os.path.join(directory_path, f))]
        return file_list
    except OSError as e:
        raise OSError(f"Unable to access the directory '{directory_path}'. Error: {str(e)}")

def main():
    """
    Main function to execute the file listing operation.
    """
    # Define the path to the index directory of the Tuenlace Cristiano website
    index_directory_path = '/path/to/tuenlace_cristiano/index'

    try:
        # Get the list of files in the index directory
        files = get_files_in_directory(index_directory_path)
        print("Files in the index directory:")
        for file in files:
            print(file)
    except ValueError as ve:
        print(f"Value Error: {ve}")
    except OSError as oe:
        print(f"OS Error: {oe}")
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")

if __name__ == "__main__":
    main()
```
