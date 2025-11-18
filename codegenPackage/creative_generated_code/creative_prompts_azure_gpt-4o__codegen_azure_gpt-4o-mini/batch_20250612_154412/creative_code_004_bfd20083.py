"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://8lements.xyz
Prompt: Create a Python script to automate the generation of directory listings for a web server, mimicking the structure seen on 8lements.xyz.
Generated: DETERMINISTIC_bfd2008376edc258
Batch ID: 20250612_154412
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
import datetime
from pathlib import Path

def generate_directory_listing(root_dir):
    """
    Generate a directory listing for the specified root directory.

    Parameters:
        root_dir (str): The root directory path to generate the listing for.

    Returns:
        dict: A dictionary containing directory structure and file details.
    """
    directory_listing = {
        "root": root_dir,
        "directories": [],
        "files": []
    }

    try:
        # Walk through the directory tree
        for dirpath, dirnames, filenames in os.walk(root_dir):
            # Get relative path
            rel_path = os.path.relpath(dirpath, root_dir)

            # Add directories to the listing
            if rel_path == '.':
                directory_listing["directories"].extend(dirnames)
            else:
                directory_listing["directories"].append(rel_path)

            # Add files to the listing
            for filename in filenames:
                file_path = os.path.join(dirpath, filename)
                file_info = {
                    "name": filename,
                    "path": file_path,
                    "size": os.path.getsize(file_path),
                    "modified_time": datetime.datetime.fromtimestamp(os.path.getmtime(file_path)).isoformat()
                }
                directory_listing["files"].append(file_info)

    except Exception as e:
        print(f"An error occurred while generating directory listing: {e}")

    return directory_listing

def save_listing_to_json(listing, output_file):
    """
    Save the directory listing to a JSON file.

    Parameters:
        listing (dict): The directory listing dictionary to save.
        output_file (str): The output file path for the JSON file.
    """
    try:
        with open(output_file, 'w') as json_file:
            json.dump(listing, json_file, indent=4)
        print(f"Directory listing saved to {output_file}")
    except Exception as e:
        print(f"An error occurred while saving the listing to JSON: {e}")

def main():
    """
    Main function to execute the directory listing generation and saving.
    """
    root_directory = input("Enter the root directory to generate listing: ")
    output_file = input("Enter the output JSON file path: ")

    # Validate input directory
    if not Path(root_directory).is_dir():
        print(f"The specified root directory '{root_directory}' does not exist or is not a directory.")
        return

    # Generate the directory listing
    directory_listing = generate_directory_listing(root_directory)

    # Save the directory listing to a JSON file
    save_listing_to_json(directory_listing, output_file)

if __name__ == "__main__":
    main()
```
