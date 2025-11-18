"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://formebd.com.rabby.aknetworkbd.com
Prompt: Write a script to list all files and directories in a server directory using Python, ensuring compatibility with LiteSpeed Web Server.
Generated: DETERMINISTIC_76cd861cf9262733
Batch ID: 20250612_151347
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os

def list_server_directory(path):
    """
    Lists all files and directories in a given server directory.

    Args:
        path (str): The absolute or relative path to the directory.

    Returns:
        dict: A dictionary containing 'files' and 'directories' as keys 
              and lists of respective items as values.
    """
    try:
        # Validate the provided path
        if not os.path.exists(path):
            raise FileNotFoundError(f"The path '{path}' does not exist.")

        if not os.path.isdir(path):
            raise NotADirectoryError(f"The path '{path}' is not a directory.")

        # Initialize data structures for files and directories
        result = {
            'files': [],
            'directories': []
        }

        # Iterate through the directory contents
        for item in os.listdir(path):
            full_path = os.path.join(path, item)
            if os.path.isfile(full_path):
                result['files'].append(item)
            elif os.path.isdir(full_path):
                result['directories'].append(item)

        # Return the collected data
        return result

    except Exception as e:
        # Handle unexpected errors gracefully
        print(f"Error: {e}")
        return {"files": [], "directories": []}


if __name__ == "__main__":
    # Define the directory path (modify as needed for your server)
    server_directory = "/path/to/server/directory"

    # List files and directories in the specified path
    directory_contents = list_server_directory(server_directory)

    # Display the output
    print("Files:")
    for file in directory_contents['files']:
        print(f"  - {file}")

    print("\nDirectories:")
    for directory in directory_contents['directories']:
        print(f"  - {directory}")
```
