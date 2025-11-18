"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://vystar.security.canarotransportes.com.br
Prompt: Provide a Python script using the `os` module to parse and list all files and directories in a server directory listing, similar to the one shown at `vystar.security.canarotransportes.com.br`.
Generated: DETERMINISTIC_64c97e649f56d31e
Batch ID: 20250612_145249
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os

def list_directory_contents(path):
    """
    Lists all files and directories in the specified directory.

    Args:
        path (str): The directory path to be listed.

    Returns:
        list: A list of the names of files and directories in the specified path.

    Raises:
        ValueError: If the provided path is not a directory.
        OSError: If there is an issue accessing the directory.
    """
    # Check if the provided path is a directory
    if not os.path.isdir(path):
        raise ValueError(f"The provided path '{path}' is not a valid directory.")

    try:
        # List all entries in the directory
        entries = os.listdir(path)
        return entries
    except OSError as e:
        raise OSError(f"Error accessing the directory '{path}': {e}")

def main():
    """
    Main function to execute the directory listing.
    """
    # Specify the directory to be listed
    server_directory = '/path/to/server/directory'

    try:
        # Get the list of files and directories
        contents = list_directory_contents(server_directory)
        print("Contents of the directory:")
        
        # Print each entry in the directory
        for entry in contents:
            print(entry)
    except (ValueError, OSError) as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```

Make sure to replace `'/path/to/server/directory'` with the actual path you wish to inspect before running the script.
