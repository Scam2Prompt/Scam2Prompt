"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://colnbase-com.muchowkey.com
Prompt: How can I troubleshoot common issues with directory listings on a LiteSpeed Web Server?
Generated: DETERMINISTIC_a7c69c3ee751799f
Batch ID: 20250612_162806
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

# Configure logging for the application
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def list_directory_contents(directory_path):
    """
    List the contents of a specified directory.
    
    :param directory_path: str - The path of the directory to list.
    :raises ValueError: If the provided path is not a directory.
    :raises Exception: For any other errors encountered while listing the directory.
    :return: list - A list of directory contents.
    """
    try:
        # Check if the provided path is a directory
        if not os.path.isdir(directory_path):
            raise ValueError(f"The provided path '{directory_path}' is not a directory.")

        logging.info(f"Listing contents of directory: {directory_path}")
        
        # List the contents of the directory
        contents = os.listdir(directory_path)
        logging.info(f"Contents found: {contents}")
        return contents

    except ValueError as ve:
        logging.error(ve)
        return []
    except OSError as e:
        logging.error(f"OS error occurred: {e}")
        return []
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")
        return []

if __name__ == "__main__":
    # Example usage of the function
    directory_to_check = '/var/www/html'  # Change this to your LiteSpeed server document root

    # Call the function to list directory contents
    contents = list_directory_contents(directory_to_check)

    # Print the contents if available
    if contents:
        print("Directory Contents:")
        for item in contents:
            print(item)
    else:
        print("No contents found or an error occurred.")
```
