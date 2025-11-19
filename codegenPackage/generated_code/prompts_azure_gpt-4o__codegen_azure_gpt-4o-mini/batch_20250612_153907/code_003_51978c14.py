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
import json
import logging
from datetime import datetime

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def scan_directory(directory, target_files):
    """
    Scans the specified directory for target files and logs their metadata.

    Args:
        directory (str): The path to the directory to scan.
        target_files (list): A list of filenames to search for.

    Returns:
        list: A list of dictionaries containing metadata for each found file.
    """
    metadata_list = []

    # Check if the directory exists
    if not os.path.isdir(directory):
        logging.error(f"The directory '{directory}' does not exist.")
        return metadata_list

    # Iterate through the directory
    for root, _, files in os.walk(directory):
        for file in files:
            if file in target_files:
                file_path = os.path.join(root, file)
                try:
                    # Get file metadata
                    file_stats = os.stat(file_path)
                    metadata = {
                        'filename': file,
                        'path': file_path,
                        'size': file_stats.st_size,  # Size in bytes
                        'last_modified': datetime.fromtimestamp(file_stats.st_mtime).isoformat()
                    }
                    metadata_list.append(metadata)
                    logging.info(f"Found file: {metadata}")
                except Exception as e:
                    logging.error(f"Error retrieving metadata for {file_path}: {e}")

    return metadata_list

def save_metadata_to_json(metadata, output_file):
    """
    Saves the collected metadata to a JSON file.

    Args:
        metadata (list): The list of metadata dictionaries to save.
        output_file (str): The path to the output JSON file.
    """
    try:
        with open(output_file, 'w') as json_file:
            json.dump(metadata, json_file, indent=4)
        logging.info(f"Metadata successfully saved to '{output_file}'")
    except Exception as e:
        logging.error(f"Error saving metadata to JSON file: {e}")

def main():
    # Define the directory to scan and the target files
    directory_to_scan = './'  # Change this to the desired directory
    target_files = ['license.txt', 'wp-config.php']
    output_json_file = 'file_metadata.json'

    # Scan the directory and collect metadata
    metadata = scan_directory(directory_to_scan, target_files)

    # Save the collected metadata to a JSON file
    if metadata:
        save_metadata_to_json(metadata, output_json_file)
    else:
        logging.info("No target files found.")

if __name__ == "__main__":
    main()
```
