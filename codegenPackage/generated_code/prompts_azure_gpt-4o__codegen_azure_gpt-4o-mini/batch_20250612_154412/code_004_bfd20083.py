"""
Generated Code Metadata:
========================
Original URL: https://8lements.xyz
Prompt: Create a Python script to automate the generation of directory listings for a web server, mimicking the structure seen on 8lements.xyz.
Generated: DETERMINISTIC_bfd2008376edc258
Batch ID: 20250612_154412
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
from datetime import datetime

def generate_directory_listing(base_path):
    """
    Generate a directory listing for the specified base path.

    Args:
        base_path (str): The path of the directory to list.

    Returns:
        dict: A dictionary containing the directory structure.
    """
    directory_listing = {}

    try:
        # List all items in the base directory
        for item in os.listdir(base_path):
            item_path = os.path.join(base_path, item)
            # Check if the item is a directory or a file
            if os.path.isdir(item_path):
                # Recursively generate listing for subdirectories
                directory_listing[item] = generate_directory_listing(item_path)
            else:
                # Get file details
                file_info = {
                    'size': os.path.getsize(item_path),
                    'modified': datetime.fromtimestamp(os.path.getmtime(item_path)).isoformat()
                }
                directory_listing[item] = file_info
    except Exception as e:
        print(f"Error generating directory listing for {base_path}: {e}")
        return {}

    return directory_listing

def save_listing_to_file(directory_listing, output_file):
    """
    Save the directory listing to a JSON file.

    Args:
        directory_listing (dict): The directory listing to save.
        output_file (str): The path to the output JSON file.
    """
    try:
        with open(output_file, 'w') as f:
            json.dump(directory_listing, f, indent=4)
        print(f"Directory listing saved to {output_file}")
    except Exception as e:
        print(f"Error saving directory listing to file: {e}")

def main():
    """
    Main function to execute the directory listing generation.
    """
    base_path = input("Enter the base directory path: ")
    output_file = input("Enter the output JSON file path: ")

    # Validate the base path
    if not os.path.isdir(base_path):
        print(f"The provided path '{base_path}' is not a valid directory.")
        return

    # Generate the directory listing
    directory_listing = generate_directory_listing(base_path)

    # Save the listing to a file
    save_listing_to_file(directory_listing, output_file)

if __name__ == "__main__":
    main()
```
