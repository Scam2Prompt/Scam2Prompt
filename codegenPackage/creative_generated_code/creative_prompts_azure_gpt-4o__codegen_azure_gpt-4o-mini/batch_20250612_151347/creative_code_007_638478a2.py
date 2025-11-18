"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://formebd.com.rabby.aknetworkbd.com
Prompt: Write a script to retrieve and display metadata (e.g., last modified date, size) of files in a directory served by LiteSpeed Web Server.
Generated: DETERMINISTIC_638478a2bf7663f4
Batch ID: 20250612_151347
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

def get_file_metadata(directory):
    """
    Retrieves and displays metadata for all files in the specified directory.
    
    :param directory: Path to the directory to scan for files.
    :raises ValueError: If the directory does not exist or is not a directory.
    """
    if not os.path.exists(directory):
        raise ValueError(f"The directory '{directory}' does not exist.")
    
    if not os.path.isdir(directory):
        raise ValueError(f"The path '{directory}' is not a directory.")
    
    try:
        # List all files in the directory
        files = os.listdir(directory)
        
        # Iterate through each file and retrieve metadata
        print(f"{'Filename':<30} {'Last Modified':<25} {'Size (Bytes)':<15}")
        print("=" * 70)
        
        for file in files:
            file_path = os.path.join(directory, file)
            
            # Only process files (ignore directories)
            if os.path.isfile(file_path):
                # Get last modified time and size of the file
                last_modified_time = os.path.getmtime(file_path)
                size = os.path.getsize(file_path)
                
                # Format last modified time
                last_modified_date = datetime.datetime.fromtimestamp(last_modified_time).strftime('%Y-%m-%d %H:%M:%S')
                
                # Display file metadata
                print(f"{file:<30} {last_modified_date:<25} {size:<15}")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Define the directory to scan for files
    dir_to_scan = "/path/to/your/directory"  # Change this to your directory path
    
    # Retrieve and display the file metadata
    get_file_metadata(dir_to_scan)
```
