"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://thephantomnetwork.net
Prompt: Develop a Python script to organize and display a chronological gallery of Photoshop edits, similar to the "Lets Begin: Photoshop" post on "The Phantom Network."
Generated: DETERMINISTIC_d5fe5bc95fc3590e
Batch ID: 20250612_153623
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import datetime
import shutil
from pathlib import Path

# Define the directory containing Photoshop edits
EDITS_DIRECTORY = 'photoshop_edits'
# Define the directory to store the organized gallery
GALLERY_DIRECTORY = 'organized_gallery'

def create_gallery_directory():
    """Create a directory for the organized gallery if it doesn't exist."""
    Path(GALLERY_DIRECTORY).mkdir(exist_ok=True)

def get_edit_timestamp(file_path):
    """Retrieve the last modified timestamp of a file."""
    try:
        timestamp = os.path.getmtime(file_path)
        return datetime.datetime.fromtimestamp(timestamp)
    except Exception as e:
        print(f"Error getting timestamp for {file_path}: {e}")
        return None

def organize_edits():
    """Organize Photoshop edits into a chronological gallery."""
    create_gallery_directory()
    
    # List all files in the edits directory
    try:
        edits = [f for f in os.listdir(EDITS_DIRECTORY) if f.endswith('.psd')]
    except FileNotFoundError:
        print(f"Directory '{EDITS_DIRECTORY}' not found.")
        return

    if not edits:
        print("No Photoshop edits found.")
        return

    # Dictionary to hold edits organized by date
    edits_by_date = {}

    for edit in edits:
        edit_path = os.path.join(EDITS_DIRECTORY, edit)
        timestamp = get_edit_timestamp(edit_path)
        
        if timestamp:
            date_str = timestamp.strftime('%Y-%m-%d')
            if date_str not in edits_by_date:
                edits_by_date[date_str] = []
            edits_by_date[date_str].append(edit)

    # Move files to the respective date directories in the gallery
    for date, files in edits_by_date.items():
        date_directory = os.path.join(GALLERY_DIRECTORY, date)
        Path(date_directory).mkdir(exist_ok=True)  # Create date directory

        for file in files:
            source_path = os.path.join(EDITS_DIRECTORY, file)
            destination_path = os.path.join(date_directory, file)

            try:
                shutil.move(source_path, destination_path)
                print(f"Moved {file} to {date_directory}")
            except Exception as e:
                print(f"Error moving {file} to {date_directory}: {e}")

def display_gallery():
    """Display the organized gallery structure."""
    try:
        for date in sorted(os.listdir(GALLERY_DIRECTORY)):
            print(f"Date: {date}")
            date_directory = os.path.join(GALLERY_DIRECTORY, date)
            for file in os.listdir(date_directory):
                print(f"  - {file}")
    except Exception as e:
        print(f"Error displaying gallery: {e}")

if __name__ == "__main__":
    organize_edits()  # Organize the Photoshop edits
    display_gallery()  # Display the organized gallery
```
