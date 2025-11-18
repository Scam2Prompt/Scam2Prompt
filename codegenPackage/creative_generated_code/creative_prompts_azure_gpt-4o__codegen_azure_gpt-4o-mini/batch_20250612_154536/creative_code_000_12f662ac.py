"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://infrastructure.bincom.net
Prompt: Write code to programmatically list and parse the contents of a directory from a server, similar to the structure shown at https://infrastructure.bincom.net.
Generated: DETERMINISTIC_12f662ac002a668d
Batch ID: 20250612_154536
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os

def list_directory_contents(directory_path):
    """
    List and parse the contents of the specified directory.

    Args:
        directory_path (str): The path to the directory to be listed.

    Returns:
        dict: A dictionary containing the names of the files and directories within the specified directory,
              categorized as 'files' and 'directories'.
    """
    # Initialize a structure to hold the contents
    contents = {
        'directories': [],
        'files': []
    }

    try:
        # Check if the provided path is indeed a directory
        if not os.path.isdir(directory_path):
            raise ValueError(f"The path '{directory_path}' is not a valid directory.")

        # List all items in the directory
        for entry in os.listdir(directory_path):
            full_path = os.path.join(directory_path, entry)

            # Check if entry is a directory or a file and append to the respective list
            if os.path.isdir(full_path):
                contents['directories'].append(entry)
            else:
                contents['files'].append(entry)

    except PermissionError:
        print(f"Permission denied: Unable to access the directory '{directory_path}'")
    except Exception as e:
        print(f"An error occurred: {e}")

    return contents

if __name__ == "__main__":
    # Example usage of the function
    directory_to_list = '/path/to/your/directory'  # Update this path as needed
    directory_contents = list_directory_contents(directory_to_list)

    # Print the results
    print("Directories:", directory_contents['directories'])
    print("Files:", directory_contents['files'])
```
