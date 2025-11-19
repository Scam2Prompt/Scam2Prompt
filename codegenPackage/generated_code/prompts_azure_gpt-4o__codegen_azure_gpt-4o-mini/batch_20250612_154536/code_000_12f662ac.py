"""
Generated Code Metadata:
========================
Original URL: https://infrastructure.bincom.net
Prompt: Write code to programmatically list and parse the contents of a directory from a server, similar to the structure shown at https://infrastructure.bincom.net.
Generated: DETERMINISTIC_12f662ac002a668d
Batch ID: 20250612_154536
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
from typing import List, Dict

def list_directory_contents(directory_path: str) -> List[Dict[str, str]]:
    """
    List and parse the contents of a directory.

    Args:
        directory_path (str): The path to the directory to be listed.

    Returns:
        List[Dict[str, str]]: A list of dictionaries containing file and directory names with their types.
    
    Raises:
        FileNotFoundError: If the specified directory does not exist.
        NotADirectoryError: If the specified path is not a directory.
    """
    if not os.path.exists(directory_path):
        raise FileNotFoundError(f"The directory '{directory_path}' does not exist.")
    
    if not os.path.isdir(directory_path):
        raise NotADirectoryError(f"The path '{directory_path}' is not a directory.")

    contents = []
    
    # Iterate through the directory contents
    for entry in os.listdir(directory_path):
        entry_path = os.path.join(directory_path, entry)
        entry_type = 'directory' if os.path.isdir(entry_path) else 'file'
        
        # Append the entry details to the contents list
        contents.append({
            'name': entry,
            'type': entry_type
        })
    
    return contents

def save_contents_to_json(contents: List[Dict[str, str]], output_file: str) -> None:
    """
    Save the directory contents to a JSON file.

    Args:
        contents (List[Dict[str, str]]): The directory contents to save.
        output_file (str): The path to the output JSON file.
    
    Raises:
        IOError: If there is an error writing to the file.
    """
    try:
        with open(output_file, 'w') as json_file:
            json.dump(contents, json_file, indent=4)
    except IOError as e:
        raise IOError(f"An error occurred while writing to the file '{output_file}': {e}")

def main():
    """
    Main function to list directory contents and save them to a JSON file.
    """
    directory_path = '/path/to/directory'  # Change this to the target directory
    output_file = 'directory_contents.json'  # Output JSON file name

    try:
        # List the contents of the directory
        contents = list_directory_contents(directory_path)
        
        # Save the contents to a JSON file
        save_contents_to_json(contents, output_file)
        
        print(f"Directory contents saved to '{output_file}' successfully.")
    except (FileNotFoundError, NotADirectoryError, IOError) as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
