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
import logging

# Configure logging for better error tracking
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def list_files_and_directories(directory):
    """
    List all files and directories in the specified directory.

    Parameters:
    directory (str): The path of the directory to list contents from.

    Returns:
    list: A list of files and directories in the specified directory.
    """
    try:
        # Check if the provided path is a directory
        if not os.path.isdir(directory):
            raise ValueError(f"The provided path '{directory}' is not a valid directory.")
        
        # List all files and directories
        contents = os.listdir(directory)
        return contents
    
    except PermissionError:
        logging.error(f"Permission denied while accessing the directory: {directory}")
        return []
    except ValueError as ve:
        logging.error(ve)
        return []
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")
        return []

def main():
    # Define the directory to list
    directory_to_list = "/path/to/your/directory"  # Change this to your target directory

    # List files and directories
    contents = list_files_and_directories(directory_to_list)

    # Output the results
    if contents:
        logging.info("Contents of the directory:")
        for item in contents:
            logging.info(item)
    else:
        logging.info("No contents found or an error occurred.")

if __name__ == "__main__":
    main()
```

Make sure to replace `"/path/to/your/directory"` with the actual path you want to list.
