"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-258--heuristic-davinci-1cf783.netlify.app
Prompt: Create a debugging script that identifies and resolves "evil byte" issues in markdown or HTML files, as described on the webpage.
Generated: DETERMINISTIC_23502b4a0b79037c
Batch ID: 20250612_151018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import re
import argparse
from typing import List, Tuple, Optional

def detect_evil_bytes(file_path: str) -> List[Tuple[int, str]]:
    """
    Scans a file for evil bytes (non-ASCII or problematic Unicode characters).
    
    Args:
        file_path: Path to the file to scan.
    
    Returns:
        List of tuples containing (line_number, line_content) where evil bytes were found.
    """
    evil_lines = []
    try:
        with open(file_path, 'rb') as f:
            content = f.read()
        
        # Try to decode as UTF-8 first
        try:
            decoded_content = content.decode('utf-8')
        except UnicodeDecodeError:
            # If UTF-8 fails, try other common encodings
            for encoding in ['latin-1', 'cp1252', 'utf-16']:
                try:
                    decoded_content = content.decode(encoding)
                    break
                except UnicodeDecodeError:
                    continue
            else:
                raise ValueError(f"Could not decode file {file_path} with common encodings")

        lines = decoded_content.splitlines()
        for i, line in enumerate(lines, 1):
            # Check for non-ASCII characters or problematic Unicode
            if re.search(r'[^\x00-\x7F]', line):
                evil_lines.append((i, line))
    
    except Exception as e:
        print(f"Error scanning file {file_path}: {str(e)}", file=sys.stderr)
    
    return evil_lines

def fix_evil_bytes(file_path: str, evil_lines: List[Tuple[int, str]], backup: bool = True) -> bool:
    """
    Attempts to fix evil bytes in a file by replacing them with ASCII equivalents.
    
    Args:
        file_path: Path to the file to fix.
        evil_lines: List of problematic lines from detect_evil_bytes.
        backup: Whether to create a backup before modifying.
    
    Returns:
        True if fixes were applied, False otherwise.
    """
    if not evil_lines:
        return False
    
    try:
        # Read original content
        with open(file_path, 'rb') as f:
            original_content = f.read().decode('utf-8', errors='ignore')
        
        if backup:
            backup_path = f"{file_path}.bak"
            with open(backup_path, 'wb') as f:
                f.write(original_content.encode('utf-8'))
        
        # Common replacements for problematic characters
        replacements = {
            '\u2018': "'",  # Left single quotation mark
            '\u2019': "'",  # Right single quotation mark
            '\u201C': '"',  # Left double quotation mark
            '\u201D': '"',  # Right double quotation mark
            '\u2013': '-',  # En dash
            '\u2014': '--', # Em dash
            '\u2026': '...',# Horizontal ellipsis
            '\u00A0': ' ',  # Non-breaking space
        }
        
        # Apply replacements
        fixed_content = original_content
        for char, replacement in replacements.items():
            fixed_content = fixed_content.replace(char, replacement)
        
        # Write fixed content
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(fixed_content)
        
        return True
    
    except Exception as e:
        print(f"Error fixing file {file_path}: {str(e)}", file=sys.stderr)
        return False

def process_files(file_paths: List[str], fix: bool = False, verbose: bool = False) -> int:
    """
    Process multiple files for evil bytes.
    
    Args:
        file_paths: List of file paths to process.
        fix: Whether to attempt automatic fixes.
        verbose: Whether to show detailed output.
    
    Returns:
        Number of files with evil bytes found.
    """
    affected_files = 0
    
    for file_path in file_paths:
        if not os.path.isfile(file_path):
            print(f"Warning: {file_path} is not a file or does not exist", file=sys.stderr)
            continue
        
        evil_lines = detect_evil_bytes(file_path)
        if evil_lines:
            affected_files += 1
            print(f"\nFound evil bytes in {file_path}:")
            for line_num, line in evil_lines:
                print(f"  Line {line_num}: {line.strip()}")
            
            if fix:
                if fix_evil_bytes(file_path, evil_lines):
                    print(f"  Applied fixes to {file_path}")
                else:
                    print(f"  Failed to apply fixes to {file_path}")
        elif verbose:
            print(f"No evil bytes found in {file_path}")
    
    return affected_files

def main():
    parser = argparse.ArgumentParser(
        description="Detect and fix evil bytes in markdown or HTML files.",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    parser.add_argument(
        'files',
        nargs='+',
        help="Files or directories to scan"
    )
    parser.add_argument(
        '--fix',
        action='store_true',
        help="Attempt to automatically fix evil bytes"
    )
    parser.add_argument(
        '--verbose',
        action='store_true',
        help="Show verbose output"
    )
    parser.add_argument(
        '--recursive',
        action='store_true',
        help="Recursively scan directories"
    )
    
    args = parser.parse_args()
    
    file_paths = []
    for path in args.files:
        if os.path.isfile(path):
            file_paths.append(path)
        elif os.path.isdir(path):
            if args.recursive:
                for root, _, files in os.walk(path):
                    for file in files:
                        if file.endswith(('.md', '.html', '.htm')):
                            file_paths.append(os.path.join(root, file))
            else:
                print(f"Warning: {path} is a directory but --recursive not specified", file=sys.stderr)
        else:
            print(f"Warning: {path} does not exist", file=sys.stderr)
    
    if not file_paths:
        print("No valid files to process", file=sys.stderr)
        sys.exit(1)
    
    affected_files = process_files(file_paths, args.fix, args.verbose)
    
    if affected_files > 0:
        print(f"\nFound evil bytes in {affected_files} file(s)")
        if not args.fix:
            print("Use --fix to attempt automatic fixes")
        sys.exit(1)
    else:
        print("No evil bytes found in any files")
        sys.exit(0)

if __name__ == "__main__":
    main()
```
