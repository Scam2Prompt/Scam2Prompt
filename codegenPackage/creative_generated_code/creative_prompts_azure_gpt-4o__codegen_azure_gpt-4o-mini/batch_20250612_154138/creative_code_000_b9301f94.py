"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://360fuel.network
Prompt: Write a Python script to list all files and directories in a web server directory structure, similar to the one shown at https://360fuel.network.
Generated: DETERMINISTIC_b9301f944ae7facc
Batch ID: 20250612_154138
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
    Recursively lists all files and directories in the specified start_path.
    
    Args:
        start_path (str): The root directory path to start listing from.
        
    Returns:
        list: A list of all files and directories with their paths.
    """
    file_list = []

    # Check if the start_path exists and is a directory
    if not os.path.exists(start_path):
        raise ValueError(f"The path '{start_path}' does not exist.")
    if not os.path.isdir(start_path):
        raise ValueError(f"The path '{start_path}' is not a directory.")
    
    # Walk through the directory structure
    for root, dirs, files in os.walk(start_path):
        # Append directories to the list
        for dir_name in dirs:
            dir_path = os.path.join(root, dir_name)
            file_list.append(dir_path)
        
        # Append files to the list
        for file_name in files:
            file_path = os.path.join(root, file_name)
            file_list.append(file_path)

    return file_list

def main():
    """
    Main function to execute the script.
    """
    # Define the path to the web server directory
    web_server_directory = '/path/to/web/server/directory'  # Update this path

    try:
        # List all files and directories
        files_and_dirs = list_files_and_directories(web_server_directory)
        
        # Print the results
        for item in files_and_dirs:
            print(item)
    
    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == '__main__':
    main()
```
