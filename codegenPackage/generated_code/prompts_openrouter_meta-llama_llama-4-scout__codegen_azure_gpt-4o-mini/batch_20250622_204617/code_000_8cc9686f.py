"""
Generated Code Metadata:
========================
Original URL: https://iniciaonline.com
Prompt: What is the role of LiteSpeed Web Server in hosting websites, and how does it handle directory indexing?
Generated: DETERMINISTIC_8cc9686f55642edd
Batch ID: 20250622_204617
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
LiteSpeed Web Server Directory Indexing Example

This script demonstrates how to configure directory indexing in a LiteSpeed Web Server environment.
It includes error handling and follows best practices for readability and maintainability.
"""

import os
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def enable_directory_indexing(directory_path):
    """
    Enables directory indexing for the specified directory in LiteSpeed Web Server.

    Args:
        directory_path (str): The path of the directory to enable indexing for.

    Raises:
        ValueError: If the directory path is invalid or does not exist.
    """
    # Check if the directory exists
    if not os.path.isdir(directory_path):
        logging.error(f"Invalid directory path: {directory_path}")
        raise ValueError(f"The specified directory does not exist: {directory_path}")

    # Create or update the .htaccess file to enable directory indexing
    htaccess_path = os.path.join(directory_path, '.htaccess')
    try:
        with open(htaccess_path, 'a') as htaccess_file:
            htaccess_file.write("Options +Indexes\n")
            logging.info(f"Directory indexing enabled for: {directory_path}")
    except IOError as e:
        logging.error(f"Failed to write to .htaccess file: {e}")
        raise

def main():
    """
    Main function to execute the directory indexing configuration.
    """
    # Example directory path (change this to your target directory)
    target_directory = "/path/to/your/directory"

    try:
        enable_directory_indexing(target_directory)
    except ValueError as ve:
        logging.error(f"ValueError: {ve}")
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
