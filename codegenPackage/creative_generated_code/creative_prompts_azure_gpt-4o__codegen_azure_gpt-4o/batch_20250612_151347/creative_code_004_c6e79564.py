"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://formebd.com.rabby.aknetworkbd.com
Prompt: Provide an example of using Python's `os` module to replicate the directory listing format shown on a LiteSpeed Web Server.
Generated: DETERMINISTIC_c6e7956463fe1bcb
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
from datetime import datetime

def list_directory(path="."):
    """
    Replicates a directory listing similar to LiteSpeed Web Server.
    
    :param path: Path of the directory to list. Defaults to current directory.
    """
    try:
        # Check if the provided path exists and is a directory
        if not os.path.exists(path) or not os.path.isdir(path):
            raise ValueError(f"Invalid path: {path} does not exist or is not a directory.")
        
        print(f"Listing directory: {path}\n")
        print("{:<40} {:>20} {:>12}".format("Name", "Last Modified", "Size"))
        print("-" * 74)

        # Iterate through items in the directory
        for item in os.listdir(path):
            item_path = os.path.join(path, item)
            # Get last modified time
            last_modified = datetime.fromtimestamp(os.path.getmtime(item_path)).strftime("%Y-%m-%d %H:%M:%S")
            # Get item size (directories have size 0)
            size = os.path.getsize(item_path) if os.path.isfile(item_path) else 0
            # Format and print each item
            print("{:<40} {:>20} {:>12}".format(item, last_modified, f"{size} bytes"))
    except Exception as e:
        # Handle exceptions and provide feedback
        print(f"Error: {e}")

if __name__ == "__main__":
    # Replace '.' with the desired directory path to list
    list_directory(".")
```
