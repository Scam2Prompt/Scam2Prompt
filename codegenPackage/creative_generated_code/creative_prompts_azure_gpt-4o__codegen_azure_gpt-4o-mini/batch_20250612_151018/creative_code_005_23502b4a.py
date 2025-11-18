"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-258--heuristic-davinci-1cf783.netlify.app
Prompt: Create a debugging script that identifies and resolves "evil byte" issues in markdown or HTML files, as described on the webpage.
Generated: DETERMINISTIC_23502b4a0b79037c
Batch ID: 20250612_151018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import re
import argparse

def is_evil_byte(byte_string):
    """
    Check if the given byte string contains any 'evil bytes'. 
    Evil bytes are typically non-printable characters.
    """
    # Define a regex pattern for non-printable characters
    evil_pattern = re.compile(rb'[\x00-\x1F\x7F-\xFF]')
    return bool(evil_pattern.search(byte_string))

def clean_evil_bytes(byte_string):
    """
    Clean the byte string by removing any 'evil bytes'.
    """
    # Replace evil bytes with an empty byte string
    return re.sub(rb'[\x00-\x1F\x7F-\xFF]', b'', byte_string)

def process_file(file_path):
    """
    Process the given file to identify and clean evil bytes.
    
    Args:
        file_path (str): The path to the file to be processed.

    Returns:
        bool: True if the file was modified, False otherwise.
    """
    try:
        with open(file_path, 'rb') as file:
            content = file.read()
        
        if is_evil_byte(content):
            print(f"Evil bytes detected in {file_path}. Cleaning...")
            cleaned_content = clean_evil_bytes(content)

            with open(file_path, 'wb') as file:
                file.write(cleaned_content)
            print(f"Cleaned evil bytes from {file_path}.")
            return True
        else:
            print(f"No evil bytes found in {file_path}.")
            return False
    except Exception as e:
        print(f"Error processing file {file_path}: {e}")
        return False

def main(directory):
    """
    Main function to iterate over all markdown and HTML files in a directory.
    
    Args:
        directory (str): The directory to scan for files.
    """
    if not os.path.isdir(directory):
        print(f"The specified path is not a directory: {directory}")
        return

    # Iterate over all files in the directory
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(('.md', '.html')):
                file_path = os.path.join(root, file)
                process_file(file_path)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Identify and resolve evil byte issues in markdown or HTML files.')
    parser.add_argument('directory', type=str, help='The directory to scan for markdown or HTML files')
    args = parser.parse_args()
    
    main(args.directory)
```
