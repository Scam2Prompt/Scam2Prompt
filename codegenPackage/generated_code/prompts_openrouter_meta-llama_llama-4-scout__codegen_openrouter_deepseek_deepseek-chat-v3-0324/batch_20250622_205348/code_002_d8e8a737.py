"""
Generated Code Metadata:
========================
Original URL: https://defluo.hr
Prompt: "Write a Python script to automate the process of organizing files on a server based on their last modified date."
Generated: DETERMINISTIC_d8e8a73763e8404d
Batch ID: 20250622_205348
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import shutil
from datetime import datetime

def organize_files_by_date(source_dir, dest_dir):
    """
    Organizes files in the source directory into subdirectories based on their last modified date.
    
    Args:
        source_dir (str): Path to the directory containing files to organize.
        dest_dir (str): Path to the base directory where organized files will be moved.
    
    Raises:
        ValueError: If source_dir or dest_dir doesn't exist.
        OSError: If there are permission issues.
    """
    # Validate directories
    if not os.path.exists(source_dir):
        raise ValueError(f"Source directory does not exist: {source_dir}")
    if not os.path.exists(dest_dir):
        raise ValueError(f"Destination directory does not exist: {dest_dir}")

    # Process each file in the source directory
    for filename in os.listdir(source_dir):
        file_path = os.path.join(source_dir, filename)
        
        # Skip directories
        if not os.path.isfile(file_path):
            continue
            
        try:
            # Get last modified time
            mod_time = os.path.getmtime(file_path)
            mod_date = datetime.fromtimestamp(mod_time).strftime('%Y-%m-%d')
            
            # Create destination directory if it doesn't exist
            date_dir = os.path.join(dest_dir, mod_date)
            os.makedirs(date_dir, exist_ok=True)
            
            # Move file
            dest_path = os.path.join(date_dir, filename)
            shutil.move(file_path, dest_path)
            print(f"Moved {filename} to {date_dir}")
            
        except PermissionError as e:
            print(f"Permission denied for {filename}: {e}")
        except OSError as e:
            print(f"Error processing {filename}: {e}")

if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description='Organize files by last modified date.')
    parser.add_argument('source', help='Source directory containing files to organize')
    parser.add_argument('dest', help='Destination base directory for organized files')
    
    args = parser.parse_args()
    
    try:
        organize_files_by_date(args.source, args.dest)
    except Exception as e:
        print(f"Error: {e}")
        exit(1)
```
