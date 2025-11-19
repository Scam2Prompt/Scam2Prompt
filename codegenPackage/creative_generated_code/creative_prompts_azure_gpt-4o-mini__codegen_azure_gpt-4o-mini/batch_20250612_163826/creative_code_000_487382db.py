"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://groupists.com
Prompt: Generate a script that lists all files in a directory similar to the index of / on groupists.com.
Generated: DETERMINISTIC_487382dbf74d9947
Batch ID: 20250612_163826
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os

def list_files_in_directory(directory_path):
    """
    Lists all files and directories in the specified directory.

    Args:
        directory_path (str): The path to the directory to list files from.

    Returns:
        list: A list of file and directory names in the specified directory.
    """
    try:
        # Get the list of all files and directories
        entries = os.listdir(directory_path)
        
        # Filter and sort the entries
        files_and_dirs = sorted(entries, key=lambda x: x.lower())
        
        return files_and_dirs
    except FileNotFoundError:
        print(f"Error: The directory '{directory_path}' does not exist.")
        return []
    except PermissionError:
        print(f"Error: Permission denied to access '{directory_path}'.")
        return []
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return []

def main():
    # Specify the directory path
    directory_path = input("Enter the directory path: ")
    
    # List files and directories
    files_list = list_files_in_directory(directory_path)
    
    # Print the results
    if files_list:
        print(f"\nContents of '{directory_path}':")
        for entry in files_list:
            print(entry)
    else:
        print("No files or directories found.")

if __name__ == "__main__":
    main()
```
