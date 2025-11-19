"""
Generated Code Metadata:
========================
Original URL: https://consejodigitalmx.com
Prompt: Develop a Python script to monitor and report on the last modified dates of files on a server, similar to the information displayed on this webpage.
Generated: DETERMINISTIC_9d2d1b9fc6433b90
Batch ID: 20250622_211206
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
import logging
import argparse
import json
from typing import List, Dict, Optional

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('file_monitor.log'),
        logging.StreamHandler()
    ]
)

def get_file_modification_info(directory: str, recursive: bool = False) -> List[Dict[str, str]]:
    """
    Retrieve modification information for files in the specified directory.
    
    Args:
        directory: Path to the directory to scan.
        recursive: Whether to scan subdirectories recursively.
    
    Returns:
        List of dictionaries containing file information (path, last_modified).
    
    Raises:
        FileNotFoundError: If directory doesn't exist.
        PermissionError: If directory access is denied.
    """
    if not os.path.exists(directory):
        raise FileNotFoundError(f"Directory not found: {directory}")
    
    if not os.path.isdir(directory):
        raise NotADirectoryError(f"Path is not a directory: {directory}")

    file_info = []
    
    try:
        if recursive:
            for root, _, files in os.walk(directory):
                for file in files:
                    file_path = os.path.join(root, file)
                    file_info.append(_get_single_file_info(file_path))
        else:
            for file in os.listdir(directory):
                file_path = os.path.join(directory, file)
                if os.path.isfile(file_path):
                    file_info.append(_get_single_file_info(file_path))
    except PermissionError as e:
        logging.error(f"Permission denied while accessing directory: {directory}")
        raise
    
    return file_info

def _get_single_file_info(file_path: str) -> Dict[str, str]:
    """
    Get modification information for a single file.
    
    Args:
        file_path: Path to the file.
    
    Returns:
        Dictionary with file path and last modified timestamp.
    """
    try:
        mod_time = os.path.getmtime(file_path)
        return {
            'file_path': file_path,
            'last_modified': datetime.fromtimestamp(mod_time).isoformat()
        }
    except OSError as e:
        logging.warning(f"Could not access file {file_path}: {str(e)}")
        return {
            'file_path': file_path,
            'last_modified': 'UNKNOWN',
            'error': str(e)
        }

def generate_report(file_info: List[Dict[str, str]], output_format: str = 'text') -> Optional[str]:
    """
    Generate a report in the specified format.
    
    Args:
        file_info: List of file information dictionaries.
        output_format: Desired output format ('text', 'json', 'csv').
    
    Returns:
        Formatted report string or None if format is invalid.
    """
    if not file_info:
        return "No files found."
    
    if output_format == 'text':
        report = []
        report.append("File Modification Report")
        report.append("=" * 40)
        for info in file_info:
            report.append(f"File: {info['file_path']}")
            report.append(f"Last Modified: {info['last_modified']}")
            report.append("-" * 40)
        return "\n".join(report)
    elif output_format == 'json':
        return json.dumps(file_info, indent=2)
    elif output_format == 'csv':
        csv_lines = ["file_path,last_modified"]
        for info in file_info:
            csv_lines.append(f"{info['file_path']},{info['last_modified']}")
        return "\n".join(csv_lines)
    else:
        logging.error(f"Invalid output format: {output_format}")
        return None

def main():
    parser = argparse.ArgumentParser(description="File Modification Monitor")
    parser.add_argument(
        'directory',
        help="Directory to monitor for file modifications"
    )
    parser.add_argument(
        '-r', '--recursive',
        action='store_true',
        help="Scan subdirectories recursively"
    )
    parser.add_argument(
        '-f', '--format',
        choices=['text', 'json', 'csv'],
        default='text',
        help="Output format (default: text)"
    )
    parser.add_argument(
        '-o', '--output',
        help="Output file path (default: stdout)"
    )
    
    args = parser.parse_args()
    
    try:
        file_info = get_file_modification_info(args.directory, args.recursive)
        report = generate_report(file_info, args.format)
        
        if report is None:
            return
        
        if args.output:
            try:
                with open(args.output, 'w') as f:
                    f.write(report)
                logging.info(f"Report written to {args.output}")
            except IOError as e:
                logging.error(f"Failed to write output file: {str(e)}")
        else:
            print(report)
            
    except Exception as e:
        logging.error(f"Error occurred: {str(e)}", exc_info=True)

if __name__ == "__main__":
    main()
```
