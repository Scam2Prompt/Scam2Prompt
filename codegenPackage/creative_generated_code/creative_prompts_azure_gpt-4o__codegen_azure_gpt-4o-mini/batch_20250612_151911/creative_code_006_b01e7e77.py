"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://teslatrust.net
Prompt: Provide a code snippet to list all files in the `/home/USERNAME/public_html` directory and identify if `index.html` exists on a CentOS-WebPanel server.
Generated: DETERMINISTIC_b01e7e7702a4fb64
Batch ID: 20250612_151911
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os

def list_files_in_directory(directory):
    """
    List all files in the specified directory and check for the presence of 'index.html'.

    Args:
        directory (str): The path to the directory to be scanned.

    Returns:
        list: A list of file names in the directory.
        bool: True if 'index.html' exists, False otherwise.
    """
    try:
        # List all files in the given directory
        files = os.listdir(directory)
        
        # Check if 'index.html' exists
        index_exists = 'index.html' in files

        return files, index_exists

    except FileNotFoundError:
        print(f"Error: The directory '{directory}' does not exist.")
        return [], False
    except PermissionError:
        print(f"Error: Permission denied when trying to access '{directory}'.")
        return [], False
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return [], False

if __name__ == "__main__":
    # Define the target directory
    user_home_directory = "/home/USERNAME/public_html"
    
    # Execute the function to list files and check for index.html
    files, index_exists = list_files_in_directory(user_home_directory)
    
    # Print the results
    print("Files in directory:", files)
    print("Does 'index.html' exist?", index_exists)
```
