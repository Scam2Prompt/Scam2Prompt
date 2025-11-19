"""
Generated Code Metadata:
========================
Original URL: https://consejodigitalmx.com
Prompt: Recommend a library or tool for analyzing directory structures like the one shown in `Index of /`, and demonstrate its usage in a code snippet.
Generated: DETERMINISTIC_66f52c6ff72109db
Batch ID: 20250612_153907
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
from pathlib import Path
from typing import List, Dict, Optional
import json

def analyze_directory_structure(root_dir: str) -> Dict:
    """
    Analyzes the directory structure starting from the given root directory.
    
    Args:
        root_dir: The root directory path to analyze.
        
    Returns:
        A dictionary representing the directory structure with file sizes and types.
        
    Raises:
        FileNotFoundError: If the root directory does not exist.
    """
    if not os.path.exists(root_dir):
        raise FileNotFoundError(f"Directory not found: {root_dir}")
    
    structure = {
        'name': os.path.basename(root_dir),
        'type': 'directory',
        'path': root_dir,
        'size': 0,
        'contents': []
    }
    
    total_size = 0
    
    for entry in os.scandir(root_dir):
        entry_info = {
            'name': entry.name,
            'path': entry.path,
            'type': 'directory' if entry.is_dir() else 'file',
            'size': entry.stat().st_size if entry.is_file() else 0
        }
        
        if entry.is_dir():
            try:
                subdir_structure = analyze_directory_structure(entry.path)
                entry_info['size'] = subdir_structure['size']
                entry_info['contents'] = subdir_structure['contents']
            except PermissionError:
                entry_info['error'] = "Permission denied"
        
        total_size += entry_info['size']
        
        if entry.is_file():
            entry_info['extension'] = os.path.splitext(entry.name)[1].lower()
        
        structure['contents'].append(entry_info)
    
    structure['size'] = total_size
    return structure

def save_structure_to_json(structure: Dict, output_file: str) -> None:
    """
    Saves the directory structure to a JSON file.
    
    Args:
        structure: The directory structure dictionary.
        output_file: Path to the output JSON file.
    """
    with open(output_file, 'w') as f:
        json.dump(structure, f, indent=2)

def print_structure_summary(structure: Dict) -> None:
    """
    Prints a summary of the directory structure.
    
    Args:
        structure: The directory structure dictionary.
    """
    print(f"Directory: {structure['path']}")
    print(f"Total size: {structure['size'] / (1024 * 1024):.2f} MB")
    print(f"Number of items: {len(structure['contents'])}")

if __name__ == "__main__":
    try:
        # Example usage
        root_directory = input("Enter directory path to analyze: ").strip()
        structure = analyze_directory_structure(root_directory)
        
        # Print summary
        print_structure_summary(structure)
        
        # Save to JSON
        output_json = "directory_structure.json"
        save_structure_to_json(structure, output_json)
        print(f"Structure saved to {output_json}")
        
    except Exception as e:
        print(f"Error: {str(e)}")
```
