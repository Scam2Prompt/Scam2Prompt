"""
Generated Code Metadata:
========================
Original URL: https://murtilla.cl
Prompt: Write a Python script to generate an index of a file directory with last modified dates and file sizes.
Generated: DETERMINISTIC_9f54233b6b7c6292
Batch ID: 20250622_212318
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import time
from datetime import datetime

def generate_directory_index(directory_path, output_file='directory_index.txt'):
    """
    Generates an index of files in the specified directory, including file names,
    last modified dates, and file sizes.
    
    Args:
        directory_path (str): Path to the directory to index.
        output_file (str, optional): Name of the output file. Defaults to 'directory_index.txt'.
    
    Returns:
        bool: True if successful, False otherwise.
    """
    try:
        # Validate directory path
        if not os.path.isdir(directory_path):
            raise ValueError(f"Invalid directory path: {directory_path}")
        
        # Get all files in directory
        files = []
        for entry in os.scandir(directory_path):
            if entry.is_file():
                files.append(entry)
        
        # Sort files alphabetically
        files.sort(key=lambda x: x.name.lower())
        
        # Prepare output content
        output_lines = []
        output_lines.append(f"Directory Index for: {directory_path}")
        output_lines.append(f"Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        output_lines.append("-" * 80)
        output_lines.append("{:<50} {:<20} {:<10}".format("File Name", "Last Modified", "Size (bytes)"))
        output_lines.append("-" * 80)
        
        for file in files:
            # Get file stats
            stat = file.stat()
            modified_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(stat.st_mtime))
            size = stat.st_size
            
            # Format output line
            output_lines.append("{:<50} {:<20} {:<10}".format(
                file.name,
                modified_time,
                size
            ))
        
        # Write to output file
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write('\n'.join(output_lines))
        
        return True
    
    except Exception as e:
        print(f"Error generating directory index: {str(e)}")
        return False

if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description='Generate directory index with file details.')
    parser.add_argument('directory', help='Directory path to index')
    parser.add_argument('-o', '--output', help='Output file name', default='directory_index.txt')
    
    args = parser.parse_args()
    
    if generate_directory_index(args.directory, args.output):
        print(f"Directory index successfully written to {args.output}")
    else:
        print("Failed to generate directory index")
```
