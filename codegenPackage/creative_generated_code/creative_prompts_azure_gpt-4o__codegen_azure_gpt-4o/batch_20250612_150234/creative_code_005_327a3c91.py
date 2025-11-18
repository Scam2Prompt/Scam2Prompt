"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fourmemebot.com
Prompt: Develop a script to manage and organize the online history of screenshots saved in Joxi's storage.
Generated: DETERMINISTIC_327a3c91aaa9182c
Batch ID: 20250612_150234
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
import shutil
from datetime import datetime

# Constants
JOXI_STORAGE_PATH = 'path_to_joxi_storage'  # Replace with the path to Joxi's storage
ORGANIZED_STORAGE_PATH = 'organized_joxi_storage'  # Directory to store organized screenshots
METADATA_FILE = 'metadata.json'  # Metadata file to save screenshot details

def organize_screenshots():
    """
    Organizes screenshots from Joxi's storage into a structured folder hierarchy
    based on their creation date and generates metadata for tracking history.
    """
    try:
        # Verify Joxi storage path exists
        if not os.path.exists(JOXI_STORAGE_PATH):
            raise FileNotFoundError(f"Joxi storage path '{JOXI_STORAGE_PATH}' does not exist.")

        # Create destination directory if it doesn't exist
        if not os.path.exists(ORGANIZED_STORAGE_PATH):
            os.makedirs(ORGANIZED_STORAGE_PATH)

        # Initialize metadata dictionary
        metadata = {}

        # Iterate through files in Joxi storage
        for filename in os.listdir(JOXI_STORAGE_PATH):
            file_path = os.path.join(JOXI_STORAGE_PATH, filename)

            # Skip directories or non-image files
            if not os.path.isfile(file_path) or not filename.lower().endswith(('.png', '.jpg', '.jpeg')):
                continue

            # Get file creation time and format it as YYYY/MM/DD
            creation_time = os.path.getctime(file_path)
            date_str = datetime.fromtimestamp(creation_time).strftime('%Y/%m/%d')

            # Create directory hierarchy based on date
            date_path = os.path.join(ORGANIZED_STORAGE_PATH, date_str.replace('/', os.sep))
            if not os.path.exists(date_path):
                os.makedirs(date_path)

            # Move file to organized folder and update metadata
            new_file_path = os.path.join(date_path, filename)
            shutil.move(file_path, new_file_path)
            metadata[filename] = {
                'original_path': file_path,
                'new_path': new_file_path,
                'creation_date': date_str
            }

        # Save metadata to JSON file
        metadata_file_path = os.path.join(ORGANIZED_STORAGE_PATH, METADATA_FILE)
        with open(metadata_file_path, 'w') as metadata_file:
            json.dump(metadata, metadata_file, indent=4)

        print(f"Screenshots organized successfully. Metadata saved to '{metadata_file_path}'.")

    except Exception as e:
        print(f"An error occurred while organizing screenshots: {str(e)}")

# Run the script
if __name__ == "__main__":
    organize_screenshots()
```
