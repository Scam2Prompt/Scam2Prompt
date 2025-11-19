"""
Generated Code Metadata:
========================
Original URL: https://feedoy.org
Prompt: Write a function in Python to parse the .DOC, .RTF, .TXT, or .WRI files included in the screen saver archives from Dick Lee's Screen Saver Page and display the description of each screen saver.
Generated: DETERMINISTIC_4123b8fc79b0d829
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
import re
import tempfile
import subprocess
from pathlib import Path
from typing import Dict, List

def extract_text_from_doc(file_path: Path) -> str:
    """
    Extract text from .DOC file using antiword.
    
    Args:
    file_path (Path): Path to .DOC file.
    
    Returns:
    str: Extracted text.
    """
    try:
        # Use antiword to extract text from .DOC file
        output = subprocess.check_output(['antiword', str(file_path)])
        return output.decode('utf-8', errors='ignore')
    except Exception as e:
        print(f"Error extracting text from .DOC file: {e}")
        return ""

def extract_text_from_rtf(file_path: Path) -> str:
    """
    Extract text from .RTF file using rtf2text.
    
    Args:
    file_path (Path): Path to .RTF file.
    
    Returns:
    str: Extracted text.
    """
    try:
        # Use rtf2text to extract text from .RTF file
        output = subprocess.check_output(['rtf2text', str(file_path)])
        return output.decode('utf-8', errors='ignore')
    except Exception as e:
        print(f"Error extracting text from .RTF file: {e}")
        return ""

def extract_text_from_txt(file_path: Path) -> str:
    """
    Extract text from .TXT file.
    
    Args:
    file_path (Path): Path to .TXT file.
    
    Returns:
    str: Extracted text.
    """
    try:
        # Read text from .TXT file
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
            return file.read()
    except Exception as e:
        print(f"Error extracting text from .TXT file: {e}")
        return ""

def extract_text_from_wri(file_path: Path) -> str:
    """
    Extract text from .WRI file.
    
    Args:
    file_path (Path): Path to .WRI file.
    
    Returns:
    str: Extracted text.
    """
    try:
        # .WRI files are similar to .TXT files
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
            return file.read()
    except Exception as e:
        print(f"Error extracting text from .WRI file: {e}")
        return ""

def parse_screen_saver_description(file_path: Path) -> Dict[str, str]:
    """
    Parse the description of a screen saver from a file.
    
    Args:
    file_path (Path): Path to file.
    
    Returns:
    Dict[str, str]: Dictionary containing screen saver description.
    """
    file_extension = file_path.suffix.lower()
    descriptions: Dict[str, str] = {}
    
    if file_extension == '.doc':
        text = extract_text_from_doc(file_path)
    elif file_extension == '.rtf':
        text = extract_text_from_rtf(file_path)
    elif file_extension == '.txt':
        text = extract_text_from_txt(file_path)
    elif file_extension == '.wri':
        text = extract_text_from_wri(file_path)
    else:
        print(f"Unsupported file extension: {file_extension}")
        return descriptions
    
    # Use regular expression to find screen saver description
    pattern = re.compile(r'Description:(.*)', re.IGNORECASE)
    match = pattern.search(text)
    
    if match:
        descriptions['description'] = match.group(1).strip()
    
    return descriptions

def main(screen_saver_archive_path: Path) -> List[Dict[str, str]]:
    """
    Parse the description of each screen saver in the archive.
    
    Args:
    screen_saver_archive_path (Path): Path to screen saver archive.
    
    Returns:
    List[Dict[str, str]]: List of dictionaries containing screen saver descriptions.
    """
    screen_saver_descriptions: List[Dict[str, str]] = []
    
    # Iterate over all files in the archive
    for file_path in screen_saver_archive_path.rglob('*'):
        if file_path.is_file():
            descriptions = parse_screen_saver_description(file_path)
            if descriptions:
                screen_saver_descriptions.append(descriptions)
    
    return screen_saver_descriptions

if __name__ == "__main__":
    archive_path = Path('/path/to/screen/saver/archive')
    descriptions = main(archive_path)
    for description in descriptions:
        print(description)
```
