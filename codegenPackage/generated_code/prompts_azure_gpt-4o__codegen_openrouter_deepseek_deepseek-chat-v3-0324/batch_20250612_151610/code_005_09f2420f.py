"""
Generated Code Metadata:
========================
Original URL: https://feedoy.org
Prompt: Generate a script to check the integrity of downloaded screen saver files from Dick Lee's Screen Saver Page and verify that the required documentation files (.DOC, .RTF, .TXT, or .WRI) are present.
Generated: DETERMINISTIC_09f2420f83514170
Batch ID: 20250612_151610
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import hashlib
import argparse
from pathlib import Path

def calculate_checksum(file_path, algorithm='sha256'):
    """Calculate the checksum of a file using the specified algorithm."""
    hash_func = getattr(hashlib, algorithm)()
    try:
        with open(file_path, 'rb') as f:
            for chunk in iter(lambda: f.read(4096), b''):
                hash_func.update(chunk)
        return hash_func.hexdigest()
    except IOError as e:
        print(f"Error reading file {file_path}: {e}")
        return None

def verify_file_integrity(file_path, expected_checksum=None):
    """Verify the integrity of a file by comparing its checksum."""
    if not os.path.exists(file_path):
        print(f"File not found: {file_path}")
        return False
    
    if expected_checksum:
        actual_checksum = calculate_checksum(file_path)
        if actual_checksum != expected_checksum:
            print(f"Checksum mismatch for {file_path}")
            print(f"Expected: {expected_checksum}")
            print(f"Actual:   {actual_checksum}")
            return False
    return True

def check_documentation_files(directory):
    """Check if required documentation files exist in the directory."""
    doc_extensions = {'.doc', '.rtf', '.txt', '.wri'}
    found_docs = False
    
    for file in os.listdir(directory):
        if Path(file).suffix.lower() in doc_extensions:
            found_docs = True
            print(f"Found documentation file: {file}")
    
    if not found_docs:
        print("Warning: No documentation files (.DOC, .RTF, .TXT, or .WRI) found in directory")
    return found_docs

def main():
    parser = argparse.ArgumentParser(
        description="Verify integrity of screen saver files and check for documentation."
    )
    parser.add_argument(
        'directory',
        help="Directory containing the screen saver files to verify"
    )
    parser.add_argument(
        '--checksum',
        help="Expected SHA256 checksum of the main screen saver file (optional)"
    )
    parser.add_argument(
        '--file',
        help="Specific screen saver file to verify (default: first .scr or .exe found)",
        default=None
    )
    
    args = parser.parse_args()
    
    if not os.path.isdir(args.directory):
        print(f"Error: {args.directory} is not a valid directory")
        return
    
    target_file = args.file
    if not target_file:
        # Find first .scr or .exe file if none specified
        for file in os.listdir(args.directory):
            if Path(file).suffix.lower() in {'.scr', '.exe'}:
                target_file = file
                break
        
        if not target_file:
            print("Error: No screen saver files (.scr or .exe) found in directory")
            return
    
    file_path = os.path.join(args.directory, target_file)
    print(f"Verifying screen saver file: {file_path}")
    
    if verify_file_integrity(file_path, args.checksum):
        print("File integrity verified successfully")
    else:
        print("File integrity check failed")
    
    print("\nChecking for documentation files...")
    check_documentation_files(args.directory)

if __name__ == "__main__":
    main()
```
