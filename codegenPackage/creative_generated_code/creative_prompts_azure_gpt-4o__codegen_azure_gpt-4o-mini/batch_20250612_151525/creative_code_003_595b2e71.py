"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ouatvs.com
Prompt: Write a Python script to automate the extraction of directory information from a LiteSpeed Web Server's directory listing and save it as a structured JSON file.
Generated: DETERMINISTIC_595b2e7161db1684
Batch ID: 20250612_151525
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
from pathlib import Path

# Set up logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def extract_directory_info(directory: str) -> dict:
    """
    Extract directory information, including file/directory names and their types.

    Args:
        directory (str): The path of the directory to be scanned.

    Returns:
        dict: A dictionary containing directory information.
    """
    directory_info = {}

    try:
        # Get the list of all files and directories in the specified path
        with os.scandir(directory) as entries:
            for entry in entries:
                directory_info[entry.name] = {
                    'is_file': entry.is_file(),
                    'is_dir': entry.is_dir(),
                    'size': entry.stat().st_size if entry.is_file() else None,
                    'last_modified': entry.stat().st_mtime
                }
    except PermissionError:
        logging.error(f"Permission denied: Unable to access {directory}.")
        return {}
    except Exception as e:
        logging.error(f"An error occurred while accessing {directory}: {e}")
        return {}

    return directory_info

def save_to_json(data: dict, json_file: str):
    """
    Save the given data to a JSON file.

    Args:
        data (dict): The data to be saved.
        json_file (str): The path to the JSON file where data will be saved.
    """
    try:
        with open(json_file, 'w') as f:
            json.dump(data, f, indent=4)
        logging.info(f"Successfully saved data to {json_file}.")
    except IOError as e:
        logging.error(f"An error occurred while writing to {json_file}: {e}")

def main(directory: str, output_file: str):
    """
    Main function to extract directory information and save it to a JSON file.

    Args:
        directory (str): The path of the directory to be scanned.
        output_file (str): The path to the output JSON file.
    """
    logging.info(f"Starting directory extraction for {directory}.")
    directory_info = extract_directory_info(directory)

    if directory_info:
        save_to_json(directory_info, output_file)
    else:
        logging.warning("No information extracted from the directory.")

if __name__ == "__main__":
    # Define the directory to scan and the output JSON file location
    target_directory = "path/to/your/directory"  # Replace with your target directory
    output_json_file = "output_directory_info.json"  # Output file name

    # Validate the target directory
    if not Path(target_directory).is_dir():
        logging.error(f"{target_directory} is not a valid directory.")
    else:
        main(target_directory, output_json_file)
```
