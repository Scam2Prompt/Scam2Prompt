"""
Generated Code Metadata:
========================
Original URL: https://grasstouch.xyz
Prompt: Develop a script to replicate the structure of a LiteSpeed Web Server directory index locally, including metadata such as file names, modification dates, and sizes.
Generated: DETERMINISTIC_f5417cc3d2834f7f
Batch ID: 20250612_154029
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import shutil
import json
from datetime import datetime
from pathlib import Path

def get_file_metadata(file_path):
    """Extract metadata for a given file."""
    stat = os.stat(file_path)
    return {
        'name': os.path.basename(file_path),
        'size': stat.st_size,
        'modified': datetime.fromtimestamp(stat.st_mtime).isoformat(),
        'is_dir': os.path.isdir(file_path)
    }

def replicate_directory_structure(source_dir, output_dir):
    """
    Replicate the directory structure and collect metadata.
    
    Args:
        source_dir (str): Path to the source directory to replicate
        output_dir (str): Path to the output directory where structure will be created
    """
    try:
        # Create output directory if it doesn't exist
        Path(output_dir).mkdir(parents=True, exist_ok=True)
        
        metadata = []
        
        for root, dirs, files in os.walk(source_dir):
            # Get relative path from source directory
            rel_path = os.path.relpath(root, source_dir)
            
            # Create corresponding directory in output
            output_path = os.path.join(output_dir, rel_path)
            if not os.path.exists(output_path):
                os.makedirs(output_path)
            
            # Process files and directories
            for name in files + dirs:
                item_path = os.path.join(root, name)
                metadata.append(get_file_metadata(item_path))
        
        # Save metadata to JSON file
        metadata_file = os.path.join(output_dir, 'directory_metadata.json')
        with open(metadata_file, 'w') as f:
            json.dump(metadata, f, indent=2)
            
        print(f"Successfully replicated directory structure to {output_dir}")
        print(f"Metadata saved to {metadata_file}")
        
    except Exception as e:
        print(f"Error occurred: {str(e)}")
        raise

if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(
        description='Replicate LiteSpeed Web Server directory structure with metadata'
    )
    parser.add_argument('source_dir', help='Source directory to replicate')
    parser.add_argument('output_dir', help='Output directory for replicated structure')
    
    args = parser.parse_args()
    
    if not os.path.isdir(args.source_dir):
        print(f"Error: Source directory {args.source_dir} does not exist")
        exit(1)
        
    replicate_directory_structure(args.source_dir, args.output_dir)
```
