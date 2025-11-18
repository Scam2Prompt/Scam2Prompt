"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://grasstouch.xyz
Prompt: Develop a script to replicate the structure of a LiteSpeed Web Server directory index locally, including metadata such as file names, modification dates, and sizes.
Generated: DETERMINISTIC_f5417cc3d2834f7f
Batch ID: 20250612_154029
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
import json

def get_file_metadata(file_path):
    """Retrieve metadata for a given file."""
    try:
        # Get the file size
        size = os.path.getsize(file_path)
        # Get the last modified time
        mod_time = os.path.getmtime(file_path)
        # Convert modified time to a readable format
        mod_time_str = datetime.datetime.fromtimestamp(mod_time).isoformat()
        
        return {
            'name': os.path.basename(file_path),
            'size': size,
            'modified': mod_time_str
        }
    except Exception as e:
        print(f"Error retrieving metadata for {file_path}: {e}")
        return None

def replicate_directory_structure(source_dir, dest_file):
    """Replicate the directory structure of the source directory and save metadata to a JSON file."""
    directory_structure = []

    try:
        # Walk through the source directory
        for root, _, files in os.walk(source_dir):
            for file_name in files:
                file_path = os.path.join(root, file_name)
                # Get metadata for each file
                metadata = get_file_metadata(file_path)
                if metadata:
                    # Store relative path
                    relative_path = os.path.relpath(file_path, source_dir)
                    metadata['relative_path'] = relative_path
                    directory_structure.append(metadata)

        # Write the directory structure to the output JSON file
        with open(dest_file, 'w') as json_file:
            json.dump(directory_structure, json_file, indent=4)

        print(f"Directory structure replicated successfully to {dest_file}")

    except Exception as e:
        print(f"Error while replicating directory structure: {e}")

if __name__ == "__main__":
    # Define the source directory and destination file
    source_directory = '/path/to/source/directory'  # Change to your source directory
    destination_file = 'directory_structure.json'  # Output JSON file

    # Call the function to replicate the directory structure
    replicate_directory_structure(source_directory, destination_file)
```
