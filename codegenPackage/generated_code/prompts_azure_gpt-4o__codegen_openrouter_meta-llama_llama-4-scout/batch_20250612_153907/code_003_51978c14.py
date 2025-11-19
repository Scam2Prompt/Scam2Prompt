"""
Generated Code Metadata:
========================
Original URL: https://consejodigitalmx.com
Prompt: Create a Python script to scan a directory for files like `license.txt` and `wp-config.php`, log their metadata (e.g., size, last modified date), and store the results in a JSON file.
Generated: DETERMINISTIC_51978c14ad19612a
Batch ID: 20250612_153907
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
import json
from datetime import datetime

# Set up logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def scan_directory(directory):
    """
    Scan a directory for files like `license.txt` and `wp-config.php`, 
    log their metadata and store the results in a JSON file.

    Args:
        directory (str): The path to the directory to scan.

    Returns:
        dict: A dictionary containing the metadata of the found files.
    """
    file_metadata = {}

    try:
        # Iterate over all files in the directory
        for filename in os.listdir(directory):
            filepath = os.path.join(directory, filename)

            # Check if the path is a file
            if os.path.isfile(filepath):
                # Check if the file matches the target filenames
                if filename in ['license.txt', 'wp-config.php']:
                    # Get file metadata
                    file_size = os.path.getsize(filepath)
                    modified_date = datetime.fromtimestamp(os.path.getmtime(filepath))

                    # Log file metadata
                    logging.info(f"Found file: {filename}")
                    logging.info(f"  Size: {file_size} bytes")
                    logging.info(f"  Last modified: {modified_date}")

                    # Store file metadata in a dictionary
                    file_metadata[filename] = {
                        'size': file_size,
                        'last_modified': modified_date.isoformat()
                    }

    except FileNotFoundError:
        logging.error(f"Directory not found: {directory}")
    except PermissionError:
        logging.error(f"Permission denied for directory: {directory}")
    except Exception as e:
        logging.error(f"An error occurred: {e}")

    return file_metadata

def save_to_json(file_metadata, output_file):
    """
    Save the file metadata to a JSON file.

    Args:
        file_metadata (dict): A dictionary containing the metadata of the found files.
        output_file (str): The path to the output JSON file.
    """
    try:
        with open(output_file, 'w') as f:
            json.dump(file_metadata, f, indent=4)
        logging.info(f"Metadata saved to: {output_file}")
    except Exception as e:
        logging.error(f"Failed to save metadata to JSON file: {e}")

def main():
    directory = '.'  # Current working directory
    output_file = 'file_metadata.json'

    file_metadata = scan_directory(directory)
    save_to_json(file_metadata, output_file)

if __name__ == "__main__":
    main()
```
