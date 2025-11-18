"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sunnyhurghada.com
Prompt: Write a Python script to detect and log errors like "Illegal string offset 'enabled'" from sunnyhurghada.com’s WordPress theme files.
Generated: DETERMINISTIC_7f7b7251b3c421ed
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import re
import logging

# Configure logging
logging.basicConfig(
    filename='wordpress_error_log.txt',
    level=logging.ERROR,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def scan_files_for_errors(directory, error_pattern):
    """
    Scans all PHP files in the given directory and subdirectories for specific error patterns.

    Args:
        directory (str): Path to the directory containing WordPress theme files.
        error_pattern (str): Regex pattern to search for specific errors in files.

    Returns:
        None
    """
    try:
        # Walk through the directory and its subdirectories
        for root, _, files in os.walk(directory):
            for file in files:
                # Check only PHP files
                if file.endswith('.php'):
                    file_path = os.path.join(root, file)
                    try:
                        # Read the file content
                        with open(file_path, 'r', encoding='utf-8') as f:
                            content = f.read()
                        # Search for the error pattern
                        matches = re.findall(error_pattern, content)
                        if matches:
                            for match in matches:
                                logging.error(f"Error found in file {file_path}: {match}")
                    except Exception as e:
                        # Log file reading errors
                        logging.error(f"Failed to read file {file_path}: {e}")
    except Exception as e:
        # Log directory traversal errors
        logging.error(f"Failed to scan directory {directory}: {e}")

if __name__ == '__main__':
    # Define the path to the WordPress theme files directory
    theme_directory = '/path/to/wordpress/theme/files'

    # Define the error pattern to search for
    error_regex = r"Illegal string offset 'enabled'"

    # Scan the theme files for errors
    scan_files_for_errors(theme_directory, error_regex)
```
