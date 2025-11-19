"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://elisium.it
Prompt: Suggest a library for creating an index of files in a web application, referencing the structure used on elisium.it.
Generated: DETERMINISTIC_618741152fb6b0a9
Batch ID: 20250612_135053
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Python code for creating an index of files in a web application
# This example uses the `os` and `json` modules to index files
# The indexed file structure is saved as a JSON file.

import os
import json

def index_files(directory_path):
    """
    Indexes all files and directories starting from the given directory path.
    
    Args:
        directory_path (str): The root directory to start indexing.
    
    Returns:
        dict: A dictionary representing the indexed file structure.
    """
    try:
        file_index = {}  # Initialize an empty dictionary to hold the file structure
        
        # Walk through all files and directories starting from the root
        for root, dirs, files in os.walk(directory_path):
            # Normalize the root path
            relative_root = os.path.relpath(root, directory_path)
            if relative_root == '.':
                relative_root = ''  # Handle the root directory
            
            # Build the index for the current directory
            file_index[relative_root] = {
                'directories': dirs,
                'files': files
            }
        
        return file_index
    except Exception as e:
        print(f"An error occurred while indexing files: {e}")
        return {}

def save_index_to_file(file_index, output_path):
    """
    Saves the indexed file structure to a JSON file.
    
    Args:
        file_index (dict): The file index dictionary.
        output_path (str): The path to the output JSON file.
    """
    try:
        with open(output_path, 'w', encoding='utf-8') as json_file:
            json.dump(file_index, json_file, indent=4)
    except Exception as e:
        print(f"An error occurred while saving the index to file: {e}")

def main():
    """
    Main function to index files and save the structure to a JSON file.
    """
    # Define the directory to index and the output file path
    directory_to_index = "./"  # You can change this to the desired directory
    output_file_path = "file_index.json"  # Name of the output JSON file
    
    print("Indexing files...")
    file_index = index_files(directory_to_index)  # Get the indexed file structure
    
    print("Saving index to file...")
    save_index_to_file(file_index, output_file_path)  # Save the structure to a JSON file
    
    print(f"Index saved successfully to {output_file_path}")

# Entry point for the script
if __name__ == "__main__":
    main()
```

### Dependencies
No external libraries are required for this code; it uses Python's built-in `os` and `json` modules.

### Usage
1. Place the script in your project directory.
2. Update `directory_to_index` in the `main()` function to specify the directory you want to index.
3. Run the script. It will create a `file_index.json` file containing the indexed file structure.
