"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://phantom-mining.com
Prompt: Write a script to list all files and directories in a web server directory structure, similar to the one displayed at phantom-mining.com.
Generated: DETERMINISTIC_4cfd35cc18393d8b
Batch ID: 20250612_152954
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os

def list_files_and_directories(base_directory):
    """
    List all files and directories in the given base directory.

    Args:
        base_directory (str): The path to the directory to be scanned.

    Returns:
        list: A list of files and directories in the specified path.
    """
    result = []

    # Check if the provided base_directory exists
    if not os.path.exists(base_directory):
        raise FileNotFoundError(f"The specified directory '{base_directory}' does not exist.")

    # Traverse the directory structure
    for root, dirs, files in os.walk(base_directory):
        # Append the root directory to the result
        result.append(f"Directory: {root}")

        # List all directories
        for dir_name in dirs:
            result.append(f"  Subdirectory: {os.path.join(root, dir_name)}")

        # List all files
        for file_name in files:
            result.append(f"  File: {os.path.join(root, file_name)}")

    return result

def main():
    """
    Main function to execute the script.
    """
    # Define the base directory to be scanned
    base_directory = '/path/to/web/server/directory'  # Update this path

    try:
        # List files and directories
        items = list_files_and_directories(base_directory)

        # Print the results
        for item in items:
            print(item)

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
