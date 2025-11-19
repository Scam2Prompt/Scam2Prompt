"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://symbioticfi.cloud
Prompt: Write a script to list files in the cgi-bin directory on SymbioticFI.cloud.
Generated: DETERMINISTIC_44662314762c9673
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
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def list_cgi_bin_files(directory):
    """
    Lists all files in the specified CGI-BIN directory.

    :param directory: The path to the CGI-BIN directory.
    :return: A list of filenames in the directory.
    :raises FileNotFoundError: If the specified directory does not exist.
    :raises OSError: If an error occurs while accessing the directory.
    """
    try:
        # Check if the directory exists
        if not os.path.exists(directory):
            logging.error(f"Directory not found: {directory}")
            raise FileNotFoundError(f"The directory '{directory}' does not exist.")

        # List files in the directory
        files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
        
        logging.info(f"Files in '{directory}': {files}")
        return files

    except OSError as e:
        logging.error(f"Error accessing the directory: {e}")
        raise

if __name__ == "__main__":
    # Define the path to the cgi-bin directory
    cgi_bin_directory = '/path/to/cgi-bin'  # Update this path accordingly

    try:
        # Call the function to list files
        cgi_bin_files = list_cgi_bin_files(cgi_bin_directory)
        print("CGI-BIN Files:")
        for file in cgi_bin_files:
            print(file)
    except Exception as e:
        logging.critical(f"An error occurred: {e}")
```
