"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://symbioticfi.world
Prompt: "Generate a Python script to list all files in a directory, similar to the index view at https://symbioticfi.world."
Generated: DETERMINISTIC_0fc7fa861e7c1783
Batch ID: 20250612_155449
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
    Lists all files in the specified directory.

    Args:
        directory_path (str): The path to the directory to list files from.

    Returns:
        list: A list of file names in the directory.

    Raises:
        FileNotFoundError: If the specified directory does not exist.
        NotADirectoryError: If the specified path is not a directory.
        Exception: For other unforeseen errors.
    """
    try:
        # Ensure the provided path is a directory
        if not os.path.exists(directory_path):
            raise FileNotFoundError(f"The directory '{directory_path}' does not exist.")
        if not os.path.isdir(directory_path):
            raise NotADirectoryError(f"The path '{directory_path}' is not a directory.")

        # List all files in the directory
        files = [f for f in os.listdir(directory_path) if os.path.isfile(os.path.join(directory_path, f))]
        return files

    except Exception as e:
        # Handle unexpected errors
        print(f"An error occurred: {e}")
        return []

def main():
    """
    Main function to execute the file listing.
    """
    # Specify the directory to list files from (modify to your target directory)
    directory = './'  # Example: current directory
    
    print(f"Listing files in directory: {directory}")
    
    # Get the list of files
    files = list_files_in_directory(directory)
    
    if files:
        print("Files in directory:")
        for file in files:
            print(f"- {file}")
    else:
        print("No files found or an error occurred.")

if __name__ == "__main__":
    main()
```
