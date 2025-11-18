"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://elmensajero.e-kraken.net
Prompt: Generate code to parse and display the contents of a directory listing, including metadata like "Last modified" and "Size," as shown on the webpage.
Generated: DETERMINISTIC_42460c2115a1c55d
Batch ID: 20250612_151126
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

def get_directory_listing(directory_path):
    """
    Parse and display the contents of a directory, including metadata like:
    - File/Folder Name
    - Last Modified Date
    - Size (in bytes)
    
    Args:
        directory_path (str): Path to the directory.

    Returns:
        list[dict]: A list of dictionaries containing file metadata.
    """
    try:
        # Ensure the provided path exists and is a directory
        if not os.path.exists(directory_path):
            raise FileNotFoundError(f"The directory '{directory_path}' does not exist.")
        
        if not os.path.isdir(directory_path):
            raise NotADirectoryError(f"The path '{directory_path}' is not a directory.")
        
        # List to store file metadata
        directory_contents = []

        # Iterate through items in the directory
        for item in os.listdir(directory_path):
            item_path = os.path.join(directory_path, item)
            
            # Get file metadata
            metadata = {
                "Name": item,
                "Last Modified": datetime.fromtimestamp(os.path.getmtime(item_path)).strftime('%Y-%m-%d %H:%M:%S'),
                "Size (bytes)": os.path.getsize(item_path) if os.path.isfile(item_path) else None,  # Size is None for directories
                "Type": "File" if os.path.isfile(item_path) else "Directory"
            }

            # Append the metadata to the list
            directory_contents.append(metadata)

        return directory_contents

    except Exception as e:
        print(f"Error: {e}")
        return []

def display_directory_listing(directory_path):
    """
    Display the contents of a directory in a user-friendly format.

    Args:
        directory_path (str): Path to the directory.
    """
    directory_contents = get_directory_listing(directory_path)

    if not directory_contents:
        print("No contents to display.")
        return

    print(f"Contents of '{directory_path}':")
    print(f"{'Name':<30} {'Type':<10} {'Last Modified':<20} {'Size (bytes)':<12}")
    print("-" * 75)

    for item in directory_contents:
        print(f"{item['Name']:<30} {item['Type']:<10} {item['Last Modified']:<20} {item['Size (bytes)']:<12}")

if __name__ == "__main__":
    # Example usage: Change the path to your desired directory
    directory_path = input("Enter the directory path: ").strip()
    display_directory_listing(directory_path)
```

This code is ready to run in Python 3, and it uses standard libraries to parse and display directory contents with relevant metadata. It includes error handling and adheres to best practices.
