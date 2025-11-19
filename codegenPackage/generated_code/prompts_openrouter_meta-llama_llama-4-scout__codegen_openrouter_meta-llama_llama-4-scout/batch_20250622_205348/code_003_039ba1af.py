"""
Generated Code Metadata:
========================
Original URL: https://saniva.com.sg
Prompt: How can I troubleshoot and resolve common issues with directory indexing and file serving on a LiteSpeed Web Server, specifically for a site like saniva.com.sg?
Generated: DETERMINISTIC_039ba1afb90fb221
Batch ID: 20250622_205348
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import logging

# Set up logging configuration
logging.basicConfig(filename='lite_speed_troubleshooter.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def check_directory_indexing(directory):
    """
    Check if directory indexing is enabled for the given directory.

    Args:
        directory (str): The path to the directory to check.

    Returns:
        bool: True if directory indexing is enabled, False otherwise.
    """
    try:
        # Check if the directory exists
        if not os.path.exists(directory):
            logging.error(f"Directory '{directory}' does not exist.")
            return False

        # Check for an index file in the directory
        index_files = ['index.html', 'index.htm', 'index.php']
        for index_file in index_files:
            index_file_path = os.path.join(directory, index_file)
            if os.path.exists(index_file_path):
                logging.info(f"Index file '{index_file}' found in directory '{directory}'.")
                return True

        # If no index file is found, directory indexing might be enabled
        logging.warning(f"No index file found in directory '{directory}'. Directory indexing might be enabled.")
        return False

    except Exception as e:
        logging.error(f"An error occurred: {e}")
        return False

def check_file_serving(directory, file_name):
    """
    Check if a file is being served correctly by LiteSpeed Web Server.

    Args:
        directory (str): The path to the directory containing the file.
        file_name (str): The name of the file to check.

    Returns:
        bool: True if the file is being served correctly, False otherwise.
    """
    try:
        # Construct the full path to the file
        file_path = os.path.join(directory, file_name)

        # Check if the file exists
        if not os.path.exists(file_path):
            logging.error(f"File '{file_name}' does not exist in directory '{directory}'.")
            return False

        # Check if the file is readable
        if not os.access(file_path, os.R_OK):
            logging.error(f"File '{file_name}' is not readable in directory '{directory}'.")
            return False

        logging.info(f"File '{file_name}' is being served correctly from directory '{directory}'.")
        return True

    except Exception as e:
        logging.error(f"An error occurred: {e}")
        return False

def troubleshoot_lite_speed(directory, file_name):
    """
    Troubleshoot common issues with directory indexing and file serving on LiteSpeed Web Server.

    Args:
        directory (str): The path to the directory to troubleshoot.
        file_name (str): The name of the file to troubleshoot.

    Returns:
        None
    """
    # Check directory indexing
    directory_indexing_enabled = check_directory_indexing(directory)

    # Check file serving
    file_serving_correct = check_file_serving(directory, file_name)

    # Log the results
    logging.info(f"Directory Indexing Enabled: {directory_indexing_enabled}")
    logging.info(f"File Serving Correct: {file_serving_correct}")

if __name__ == "__main__":
    directory = "/var/www/saniva.com.sg"
    file_name = "index.html"
    troubleshoot_lite_speed(directory, file_name)
```
