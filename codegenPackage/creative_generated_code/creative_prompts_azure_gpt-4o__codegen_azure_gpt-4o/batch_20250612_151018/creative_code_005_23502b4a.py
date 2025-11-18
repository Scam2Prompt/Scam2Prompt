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

def identify_and_resolve_evil_bytes(file_path):
    """
    Scans the given markdown or HTML file for 'evil bytes' (non-printable or problematic characters)
    and replaces them with safe alternatives or removes them.
    
    :param file_path: Path to the file to be debugged.
    """
    try:
        # Read the file content
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        
        # Regular expression to match non-printable or problematic characters
        # Matches any control characters, excluding newline and tab
        evil_byte_pattern = re.compile(r'[\x00-\x08\x0B-\x0C\x0E-\x1F\x7F-\x9F]')
        
        # Identify all occurrences of evil bytes
        evil_bytes = evil_byte_pattern.findall(content)
        if evil_bytes:
            print(f"Identified {len(evil_bytes)} evil byte(s) in the file '{file_path}'.")

            # Replace evil bytes with a safe alternative (e.g., an empty string)
            cleaned_content = evil_byte_pattern.sub('', content)

            # Write the cleaned content back to the file
            with open(file_path, 'w', encoding='utf-8') as file:
                file.write(cleaned_content)
            
            print(f"Evil bytes have been successfully resolved in '{file_path}'.")
        else:
            print(f"No evil bytes found in the file '{file_path}'.")
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' does not exist.")
    except PermissionError:
        print(f"Error: Insufficient permissions to read/write the file '{file_path}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def debug_directory(directory_path, file_extensions=('.md', '.html')):
    """
    Scans all markdown and HTML files in the given directory for 'evil bytes'
    and resolves them.

    :param directory_path: Path to the directory containing the files to be debugged.
    :param file_extensions: Tuple of file extensions to process (default: .md, .html).
    """
    try:
        # Verify if the directory exists
        if not os.path.isdir(directory_path):
            print(f"Error: The directory '{directory_path}' does not exist.")
            return

        # Walk through the directory and process each file with specified extensions
        for root, _, files in os.walk(directory_path):
            for file in files:
                if file.endswith(file_extensions):
                    file_path = os.path.join(root, file)
                    print(f"Processing file: {file_path}")
                    identify_and_resolve_evil_bytes(file_path)
    except Exception as e:
        print(f"An unexpected error occurred while processing the directory: {e}")

if __name__ == "__main__":
    # Example usage: Update paths as needed
    directory_to_debug = input("Enter the directory path to scan for evil bytes: ").strip()
    debug_directory(directory_to_debug)
```
