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
from datetime import datetime

def scan_directory(directory_path, target_files, output_file):
    """
    Scans the given directory for specific files and logs their metadata into a JSON file.

    Parameters:
        directory_path (str): Path to the directory to scan.
        target_files (list): List of filenames to search for.
        output_file (str): Path to the JSON file to store the metadata.
    """
    # Dictionary to store metadata of found files
    metadata_log = {}

    try:
        # Walk through the directory
        for root, dirs, files in os.walk(directory_path):
            for file in files:
                if file in target_files:
                    file_path = os.path.join(root, file)
                    # Get file metadata
                    file_size = os.path.getsize(file_path)  # File size in bytes
                    last_modified = datetime.fromtimestamp(
                        os.path.getmtime(file_path)
                    ).strftime('%Y-%m-%d %H:%M:%S')  # Last modified timestamp
                    
                    # Store metadata in dictionary
                    metadata_log[file] = {
                        "path": file_path,
                        "size": file_size,
                        "last_modified": last_modified
                    }
        
        # Write metadata to JSON file
        with open(output_file, 'w') as json_file:
            json.dump(metadata_log, json_file, indent=4)
        
        print(f"Metadata successfully written to {output_file}")
    
    except Exception as e:
        # Handle any unexpected errors gracefully
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Directory to scan
    directory_to_scan = "./"  # Current directory
    # Files to look for
    target_file_names = ["license.txt", "wp-config.php"]
    # Output JSON file
    output_json = "file_metadata.json"

    # Scan directory and log metadata
    scan_directory(directory_to_scan, target_file_names, output_json)
```
