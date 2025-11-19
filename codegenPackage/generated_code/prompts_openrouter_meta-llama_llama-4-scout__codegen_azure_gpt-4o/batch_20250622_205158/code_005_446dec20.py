"""
Generated Code Metadata:
========================
Original URL: https://fuelgastech.co.ke
Prompt: How can I programmatically check the last modified dates of directories and files on a LiteSpeed server using a programming language of choice?
Generated: DETERMINISTIC_446dec2007feaf7d
Batch ID: 20250622_205158
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import sys
from datetime import datetime

def get_last_modified(path):
    """
    Get the last modified date of a file or directory.

    Args:
        path (str): The path to the file or directory.

    Returns:
        str: The last modified date in human-readable format.
    """
    try:
        # Get the last modified timestamp
        timestamp = os.path.getmtime(path)
        # Convert the timestamp to a human-readable format
        last_modified = datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')
        return last_modified
    except FileNotFoundError:
        return f"Error: Path '{path}' does not exist."
    except PermissionError:
        return f"Error: Permission denied for path '{path}'."
    except Exception as e:
        return f"Error: An unexpected error occurred - {str(e)}"

def check_last_modified_in_directory(directory_path):
    """
    Check the last modified dates of all files and subdirectories in a given directory.

    Args:
        directory_path (str): The path to the directory.

    Returns:
        None
    """
    try:
        # Check if the provided path is a valid directory
        if not os.path.isdir(directory_path):
            print(f"Error: '{directory_path}' is not a valid directory.")
            return

        print(f"Last modified dates for contents of directory: {directory_path}\n")
        
        # Iterate through all files and subdirectories in the directory
        for item in os.listdir(directory_path):
            item_path = os.path.join(directory_path, item)
            last_modified = get_last_modified(item_path)
            print(f"{item_path}: {last_modified}")
    except PermissionError:
        print(f"Error: Permission denied for directory '{directory_path}'.")
    except Exception as e:
        print(f"Error: An unexpected error occurred - {str(e)}")

if __name__ == "__main__":
    # Ensure the script is run with a directory path argument
    if len(sys.argv) != 2:
        print("Usage: python check_last_modified.py <directory_path>")
        sys.exit(1)

    directory_path = sys.argv[1]
    check_last_modified_in_directory(directory_path)
```

### Instructions:
1. Save the code to a file named `check_last_modified.py`.
2. Run the script from the command line, providing the directory path as an argument:
   ```
   python check_last_modified.py /path/to/directory
   ```
3. The script will output the last modified dates for all files and subdirectories in the specified directory.
