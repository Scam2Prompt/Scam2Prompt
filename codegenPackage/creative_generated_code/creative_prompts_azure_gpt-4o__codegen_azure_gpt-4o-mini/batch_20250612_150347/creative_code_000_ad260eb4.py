"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://abelltodoit.com.au
Prompt: Write a script to list all files and directories in a web server directory, similar to the structure shown at https://abelltodoit.com.au, using Python and the `os` module.
Generated: DETERMINISTIC_ad260eb441c33f31
Batch ID: 20250612_150347
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
        base_directory (str): The path of the directory to list.
        
    Returns:
        list: A list of tuples containing directory and file names.
    """
    if not os.path.exists(base_directory):
        raise FileNotFoundError(f"The directory '{base_directory}' does not exist.")
    
    if not os.path.isdir(base_directory):
        raise NotADirectoryError(f"The path '{base_directory}' is not a directory.")

    results = []

    # Walk through the directory structure
    for root, dirs, files in os.walk(base_directory):
        # Save the directory name
        results.append(('Directory', root))
        
        # Save the files in the current directory
        for file in files:
            results.append(('File', os.path.join(root, file)))

    return results

def display_results(results):
    """
    Display the results in a readable format.
    
    Args:
        results (list): A list of tuples containing directory and file names.
    """
    for item_type, name in results:
        print(f"{item_type}: {name}")

if __name__ == "__main__":
    # Specify the base directory for the web server or any directory
    base_directory = '/path/to/web_server_directory'
    
    try:
        # List files and directories
        results = list_files_and_directories(base_directory)
        # Display the results
        display_results(results)
    except (FileNotFoundError, NotADirectoryError) as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
