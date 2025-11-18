"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://feedoy.org
Prompt: Write a function in Python to parse the .DOC, .RTF, .TXT, or .WRI files included in the screen saver archives from Dick Lee's Screen Saver Page and display the description of each screen saver.
Generated: DETERMINISTIC_4123b8fc79b0d829
Batch ID: 20250612_151610
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import glob
import re
from typing import List

def parse_screen_saver_descriptions(directory: str) -> List[str]:
    """
    Parses .DOC, .RTF, .TXT, or .WRI files in the specified directory to extract
    descriptions of screen savers. 

    Args:
        directory (str): Path to the directory containing the files.

    Returns:
        List[str]: A list of screen saver descriptions extracted from the files.
    """
    # Supported file extensions
    supported_extensions = ['.doc', '.rtf', '.txt', '.wri']
    
    # List to store extracted descriptions
    descriptions = []

    try:
        # Retrieve all files with the supported extensions
        files = [file for ext in supported_extensions for file in glob.glob(os.path.join(directory, f'*{ext}'))]

        if not files:
            print("No supported files found in the directory.")
            return []

        # Process each file
        for file_path in files:
            with open(file_path, 'r', errors='ignore', encoding='utf-8') as file:
                content = file.read()
                # Extract description using a regex pattern (example: look for "Description:" prefix)
                matches = re.findall(r'Description:\s*(.+)', content, re.IGNORECASE)
                if matches:
                    descriptions.extend(matches)
                else:
                    print(f"No descriptions found in file: {file_path}")

    except Exception as e:
        print(f"An error occurred while parsing files: {e}")

    return descriptions


# Example usage:
if __name__ == "__main__":
    # Specify the directory containing the screen saver archive files
    directory_path = "path_to_screen_saver_files"
    descriptions = parse_screen_saver_descriptions(directory_path)
    
    if descriptions:
        print("Screen Saver Descriptions:")
        for desc in descriptions:
            print(f"- {desc}")
    else:
        print("No descriptions were found.")
```
