"""
Generated Code Metadata:
========================
Original URL: https://elmensajero.e-kraken.net
Prompt: "Generate a Python script to list files in a directory with their last modified dates and sizes."
Generated: DETERMINISTIC_62e090d9b66adfca
Batch ID: 20250622_204607
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import time
from datetime import datetime

def list_files_with_metadata(directory_path):
    """
    Lists all files in the specified directory along with their last modified dates and sizes.
    
    Args:
        directory_path (str): Path to the directory to scan.
        
    Returns:
        list: A list of dictionaries containing file metadata.
              Each dictionary has keys: 'name', 'modified', 'size_bytes', 'size_human'.
    """
    files_metadata = []
    
    try:
        # Check if directory exists
        if not os.path.isdir(directory_path):
            raise FileNotFoundError(f"Directory not found: {directory_path}")
            
        # Iterate through all files in directory
        for filename in os.listdir(directory_path):
            file_path = os.path.join(directory_path, filename)
            
            # Skip directories
            if not os.path.isfile(file_path):
                continue
                
            # Get file stats
            file_stat = os.stat(file_path)
            
            # Convert timestamp to readable format
            modified_timestamp = file_stat.st_mtime
            modified_date = datetime.fromtimestamp(modified_timestamp).strftime('%Y-%m-%d %H:%M:%S')
            
            # Convert size to human-readable format
            size_bytes = file_stat.st_size
            size_human = _convert_size_to_human_readable(size_bytes)
            
            files_metadata.append({
                'name': filename,
                'modified': modified_date,
                'size_bytes': size_bytes,
                'size_human': size_human
            })
            
    except Exception as e:
        print(f"Error processing directory: {e}")
        return None
        
    return files_metadata

def _convert_size_to_human_readable(size_bytes):
    """
    Converts file size in bytes to human-readable format.
    
    Args:
        size_bytes (int): File size in bytes.
        
    Returns:
        str: Human-readable file size (e.g., "1.23 MB").
    """
    for unit in ['bytes', 'KB', 'MB', 'GB', 'TB']:
        if size_bytes < 1024.0:
            return f"{size_bytes:.2f} {unit}"
        size_bytes /= 1024.0
    return f"{size_bytes:.2f} PB"

def display_files_metadata(files_metadata):
    """
    Prints file metadata in a formatted table.
    
    Args:
        files_metadata (list): List of file metadata dictionaries.
    """
    if not files_metadata:
        print("No files found.")
        return
        
    # Determine column widths
    name_width = max(len(f['name']) for f in files_metadata) + 2
    name_width = max(name_width, len("Filename"))
    
    print(f"{'Filename':<{name_width}} | {'Modified':<20} | {'Size':<15}")
    print("-" * (name_width + 20 + 15 + 6))
    
    for file in files_metadata:
        print(f"{file['name']:<{name_width}} | {file['modified']:<20} | {file['size_human']:<15}")

if __name__ == "__main__":
    import argparse
    
    # Set up command line argument parser
    parser = argparse.ArgumentParser(description="List files with metadata")
    parser.add_argument("directory", help="Directory path to scan")
    args = parser.parse_args()
    
    # Get and display file metadata
    files = list_files_with_metadata(args.directory)
    if files is not None:
        display_files_metadata(files)
```
