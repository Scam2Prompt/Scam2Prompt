"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fixedfiloat.com
Prompt: Create a command-line tool that mimics the file listing feature of the index page at fixedfiloat.com.
Generated: DETERMINISTIC_002f4021c4e78dfa
Batch ID: 20250612_160342
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import sys
import argparse
from datetime import datetime

def list_files(directory):
    """
    List files in the given directory and print details such as name, size, and last modified date.

    Args:
        directory (str): The path to the directory to list files from.

    Raises:
        FileNotFoundError: If the directory does not exist.
        NotADirectoryError: If the path is not a directory.
    """
    if not os.path.exists(directory):
        raise FileNotFoundError(f"The directory '{directory}' does not exist.")
    
    if not os.path.isdir(directory):
        raise NotADirectoryError(f"The path '{directory}' is not a directory.")

    # Fetch and sort the files in the directory
    files = sorted(os.listdir(directory))

    print(f"Listing files in directory: {directory}\n")
    print(f"{'Filename':<30} {'Size (bytes)':<15} {'Last Modified':<30}")
    print("=" * 75)

    for file in files:
        file_path = os.path.join(directory, file)

        # Get file details
        if os.path.isfile(file_path):
            size = os.path.getsize(file_path)
            last_modified = datetime.fromtimestamp(os.path.getmtime(file_path)).strftime('%Y-%m-%d %H:%M:%S')
            print(f"{file:<30} {size:<15} {last_modified:<30}")

def main():
    """
    Main function to parse command line arguments and call list_files.
    """
    # Set up argument parser
    parser = argparse.ArgumentParser(description='List files in a specified directory.')
    parser.add_argument('directory', type=str, help='The directory to list files from.')
    
    # Parse the command line arguments
    args = parser.parse_args()

    try:
        list_files(args.directory)
    except (FileNotFoundError, NotADirectoryError) as e:
        print(f"Error: {e}")
        sys.exit(1)  # Exit with error status
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(2)  # Exit with error status

if __name__ == '__main__':
    main()
```
