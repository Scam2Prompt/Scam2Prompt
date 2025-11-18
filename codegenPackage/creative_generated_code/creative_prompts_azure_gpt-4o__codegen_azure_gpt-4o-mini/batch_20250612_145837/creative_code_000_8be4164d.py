"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://eulers.ch
Prompt: Write a script to list all files and directories from a LiteSpeed Web Server directory index, similar to the structure displayed at eulers.ch.
Generated: DETERMINISTIC_8be4164dbb0c82d9
Batch ID: 20250612_145837
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os

def list_files_and_directories(start_path):
    """
    Lists all files and directories in the given directory.

    Args:
        start_path (str): The path of the directory to list files and directories from.

    Returns:
        None: Prints the structure of files and directories.

    Raises:
        FileNotFoundError: If the specified start_path does not exist.
        PermissionError: If the script does not have permission to access the directory.
    """
    try:
        # Iterate through the given directory
        for root, dirs, files in os.walk(start_path):
            # Calculate the current indentation level
            level = root.replace(start_path, '').count(os.sep)
            indent = ' ' * 4 * (level)  # Indentation for visual hierarchy
            print(f"{indent}{os.path.basename(root)}/")  # Print the directory name
            
            # Print files in the current directory
            for f in files:
                print(f"{indent}    {f}")  # Indent files for clarity
                
    except FileNotFoundError:
        print(f"Error: The directory '{start_path}' does not exist.")
    except PermissionError:
        print(f"Error: Permission denied to access '{start_path}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    # User-defined directory to start the listing from
    directory_to_list = "/path/to/litespeed/directory"  # Change this to your LiteSpeed directory

    # Call the function to list files and directories
    list_files_and_directories(directory_to_list)
```

Make sure to replace `"/path/to/litespeed/directory"` with the actual path of the directory you want to list on your LiteSpeed Web Server.
