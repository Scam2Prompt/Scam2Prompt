"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://elmensajero.e-kraken.net
Prompt: Generate code to extract and log directory metadata (e.g., file names, sizes, timestamps) from a server environment similar to https://elmensajero.e-kraken.net.
Generated: DETERMINISTIC_57aeee9c1a6ed363
Batch ID: 20250612_151126
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
from datetime import datetime

# Configure logging
logging.basicConfig(
    filename='directory_metadata.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def log_directory_metadata(directory_path):
    """
    Extract and log metadata of files in the specified directory.

    Args:
        directory_path (str): The path of the directory to scan.

    Raises:
        FileNotFoundError: If the specified directory does not exist.
        PermissionError: If the directory cannot be accessed due to permission issues.
    """
    # Validate the directory path
    if not os.path.exists(directory_path):
        logging.error(f"Directory not found: {directory_path}")
        raise FileNotFoundError(f"The directory {directory_path} does not exist.")

    if not os.path.isdir(directory_path):
        logging.error(f"Path is not a directory: {directory_path}")
        raise NotADirectoryError(f"The path {directory_path} is not a directory.")

    # Iterate over the files in the directory
    try:
        for entry in os.scandir(directory_path):
            if entry.is_file():
                # Get file metadata
                file_info = {
                    'name': entry.name,
                    'size': entry.stat().st_size,  # Size in bytes
                    'created': datetime.fromtimestamp(entry.stat().st_ctime),
                    'modified': datetime.fromtimestamp(entry.stat().st_mtime),
                    'accessed': datetime.fromtimestamp(entry.stat().st_atime),
                }
                
                # Log the file metadata
                logging.info(f"File: {file_info['name']}, Size: {file_info['size']} bytes, "
                             f"Created: {file_info['created']}, Modified: {file_info['modified']}, "
                             f"Accessed: {file_info['accessed']}")
    
    except PermissionError:
        logging.error(f"Permission denied: Unable to access {directory_path}")
        raise

# Example usage
if __name__ == "__main__":
    try:
        log_directory_metadata('/path/to/directory')  # Replace with the target directory path
    except Exception as e:
        logging.exception("An error occurred while logging directory metadata.")
```
