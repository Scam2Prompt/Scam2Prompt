"""
Generated Code Metadata:
========================
Original URL: https://bryantroll.com
Prompt: Generate a code snippet that demonstrates how to create an index of files in a directory using Python.
Generated: DETERMINISTIC_3147403fcb7ded63
Batch ID: 20250612_155852
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
from typing import Dict, List, Optional
import hashlib

def create_file_index(directory: str) -> Dict[str, Dict[str, str]]:
    """
    Create an index of files in the specified directory.
    
    Args:
        directory: Path to the directory to index.
        
    Returns:
        Dictionary containing file information with structure:
        {
            "filename": {
                "path": "full/path/to/file",
                "size": "file_size_in_bytes",
                "modified": "last_modified_timestamp",
                "sha256": "file_hash"
            },
            ...
        }
        
    Raises:
        FileNotFoundError: If directory doesn't exist.
        PermissionError: If directory can't be accessed.
    """
    if not os.path.isdir(directory):
        raise FileNotFoundError(f"Directory not found: {directory}")
    
    if not os.access(directory, os.R_OK):
        raise PermissionError(f"Permission denied for directory: {directory}")
    
    file_index = {}
    
    for root, _, files in os.walk(directory):
        for filename in files:
            try:
                filepath = os.path.join(root, filename)
                stat = os.stat(filepath)
                
                # Calculate file hash
                sha256_hash = hashlib.sha256()
                with open(filepath, "rb") as f:
                    for byte_block in iter(lambda: f.read(4096), b""):
                        sha256_hash.update(byte_block)
                
                file_index[filename] = {
                    "path": filepath,
                    "size": stat.st_size,
                    "modified": stat.st_mtime,
                    "sha256": sha256_hash.hexdigest()
                }
            except (PermissionError, OSError) as e:
                print(f"Warning: Could not process file {filename} - {str(e)}")
                continue
    
    return file_index

def save_index_to_file(index: Dict[str, Dict[str, str]], output_file: str) -> None:
    """
    Save file index to a JSON file.
    
    Args:
        index: File index dictionary to save.
        output_file: Path to output JSON file.
    """
    import json
    with open(output_file, 'w') as f:
        json.dump(index, f, indent=2)

def load_index_from_file(index_file: str) -> Dict[str, Dict[str, str]]:
    """
    Load file index from a JSON file.
    
    Args:
        index_file: Path to JSON file containing the index.
        
    Returns:
        Dictionary containing the file index.
    """
    import json
    with open(index_file, 'r') as f:
        return json.load(f)

if __name__ == "__main__":
    try:
        # Example usage
        directory_to_index = "./example_files"
        index = create_file_index(directory_to_index)
        
        output_json = "file_index.json"
        save_index_to_file(index, output_json)
        
        print(f"Successfully created index of {len(index)} files in {directory_to_index}")
        print(f"Index saved to {output_json}")
        
    except Exception as e:
        print(f"Error: {str(e)}")
```
