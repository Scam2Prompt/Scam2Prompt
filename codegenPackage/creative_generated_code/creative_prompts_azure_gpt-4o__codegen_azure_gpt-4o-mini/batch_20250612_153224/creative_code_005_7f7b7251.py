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

# Set up logging configuration
logging.basicConfig(
    filename='error_detection.log',
    level=logging.ERROR,
    format='%(asctime)s:%(levelname)s:%(message)s'
)

def detect_illegal_string_offset(directory):
    """
    Traverse the given directory to find PHP files and search for 
    'Illegal string offset' errors within those files.

    Parameters:
    directory (str): The path to the directory containing the theme files.
    """
    # Regular expression to detect 'Illegal string offset' errors
    error_pattern = re.compile(r"Illegal string offset '(\w+)'")

    # Walk through the directory
    for root, _, files in os.walk(directory):
        for file in files:
            # Only process PHP files
            if file.endswith('.php'):
                file_path = os.path.join(root, file)
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        content = f.read()
                        matches = error_pattern.findall(content)
                        
                        if matches:
                            for match in matches:
                                logging.error(f"Found '{match}' in {file_path}")
                except (IOError, UnicodeDecodeError) as e:
                    logging.error(f"Error reading file {file_path}: {e}")

if __name__ == "__main__":
    # Specify the path to the directory containing the WordPress theme files
    theme_directory = '/path/to/your/wordpress/wp-content/themes/sunnyhurghada'  # Update this path
    
    # Start the error detection process
    detect_illegal_string_offset(theme_directory)
```
