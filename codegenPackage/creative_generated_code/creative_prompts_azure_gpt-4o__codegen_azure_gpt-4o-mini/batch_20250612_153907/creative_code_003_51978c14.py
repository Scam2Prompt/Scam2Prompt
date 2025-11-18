"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://consejodigitalmx.com
Prompt: Create a Python script to scan a directory for files like `license.txt` and `wp-config.php`, log their metadata (e.g., size, last modified date), and store the results in a JSON file.
Generated: DETERMINISTIC_51978c14ad19612a
Batch ID: 20250612_153907
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import json
import logging
from datetime import datetime

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def scan_directory_for_files(directory, target_files):
    """
    Scan the specified directory for target files and log their metadata.

    Parameters:
    directory (str): The path to the directory to scan.
    target_files (list): A list of filenames to search for.

    Returns:
    list: A list of dictionaries containing metadata of found files.
    """
    found_files_metadata = []

    # Check if the provided directory exists
    if not os.path.isdir(directory):
        logging.error(f"Provided path is not a directory: {directory}")
        return found_files_metadata

    # Iterate through the files in the directory
    for root, _, files in os.walk(directory):
        for filename in files:
            if filename in target_files:
                file_path = os.path.join(root, filename)
                try:
                    # Gather file metadata
                    file_stats = os.stat(file_path)
                    file_metadata = {
                        'filename': filename,
                        'path': file_path,
                        'size': file_stats.st_size,  # Size in bytes
                        'last_modified': datetime.fromtimestamp(file_stats.st_mtime).isoformat()
                    }
                    found_files_metadata.append(file_metadata)
                    logging.info(f"Found file: {file_metadata}")
                except Exception as e:
                    logging.error(f"Error retrieving data for file {filename}: {e}")

    return found_files_metadata

def save_metadata_to_json(metadata, output_file):
    """
    Save the file metadata to a JSON file.

    Parameters:
    metadata (list): A list of dictionaries containing file metadata.
    output_file (str): The path to the output JSON file.
    """
    try:
        with open(output_file, 'w') as json_file:
            json.dump(metadata, json_file, indent=4)
            logging.info(f"Metadata successfully saved to {output_file}")
    except Exception as e:
        logging.error(f"Error saving metadata to JSON: {e}")

def main():
    # Define the directory to scan and the target files
    directory_to_scan = "./path/to/directory"  # Change this to your target directory
    target_files_to_find = ['license.txt', 'wp-config.php']
    output_json_file = 'file_metadata.json'

    # Scan the directory and gather metadata
    files_metadata = scan_directory_for_files(directory_to_scan, target_files_to_find)

    # Save the metadata to a JSON file
    save_metadata_to_json(files_metadata, output_json_file)

if __name__ == "__main__":
    main()
```
