"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fixedfiloat.com
Prompt: Generate a script to list all files in a directory similar to the index page at fixedfiloat.com.
Generated: DETERMINISTIC_493165b6ef6211c6
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

def list_files_in_directory(directory_path):
    """
    List all files in the specified directory.

    Args:
        directory_path (str): The path of the directory to list files from.

    Returns:
        list: A list of file names in the directory.
    
    Raises:
        ValueError: If the directory_path is not a valid directory.
        Exception: For any other unexpected errors.
    """
    try:
        # Validate the provided directory path
        if not os.path.isdir(directory_path):
            raise ValueError(f"The provided path '{directory_path}' is not a valid directory.")
        
        # List all files in the directory
        files = os.listdir(directory_path)
        
        # Filter out directories, only keep files
        files = [f for f in files if os.path.isfile(os.path.join(directory_path, f))]
        
        return files
    except ValueError as ve:
        print(f"Error: {ve}")
        return []
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return []

def main():
    # Set the directory path (change this to your target directory)
    directory_path = 'path/to/your/directory'
    
    # Get the list of files
    files = list_files_in_directory(directory_path)
    
    # Display the files
    if files:
        print("Files in the directory:")
        for file in files:
            print(f"- {file}")
    else:
        print("No files found or an error occurred.")

if __name__ == "__main__":
    main()
```

Make sure to replace `'path/to/your/directory'` with the actual path you want to scan for files.
