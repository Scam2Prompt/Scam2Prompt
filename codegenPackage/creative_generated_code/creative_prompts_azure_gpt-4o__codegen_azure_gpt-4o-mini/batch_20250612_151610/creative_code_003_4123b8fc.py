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
import re
from typing import List, Tuple

try:
    from docx import Document  # For .DOCX files
except ImportError:
    Document = None  # Handle .DOCX import error if the library is not installed

def parse_text_file(file_path: str) -> str:
    """Reads a plain text file and returns its contents as a string."""
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def parse_rtf_file(file_path: str) -> str:
    """Reads an RTF file and returns its contents as a string."""
    import pyth.plugins.plaintext.reader  # RTF reader import
    from pyth.plugins.plaintext.reader import PlaintextReader
    from pyth.plugins.plaintext.writer import PlaintextWriter
    from pyth.document import Document as RTFDocument

    with open(file_path, 'r', encoding='utf-8') as file:
        rtf_content = file.read()
    
    rtf_doc = RTFDocument().from_rtf(rtf_content)
    return PlaintextWriter.write(rtf_doc).getvalue()

def parse_doc_file(file_path: str) -> str:
    """Reads a .DOC file and returns its contents as a string."""
    if Document is None:
        raise ImportError("The 'python-docx' library is required to read .DOCX files.")
    
    doc = Document(file_path)
    return '\n'.join([para.text for para in doc.paragraphs])

def extract_description(content: str) -> str:
    """Extracts the description from the content based on a simple regex."""
    # Assuming the description starts with "Description:" and continues until the end of the file
    match = re.search(r'Description:\s*(.*)', content, re.DOTALL)
    return match.group(1).strip() if match else "Description not found."

def process_screensaver_files(directory: str) -> List[Tuple[str, str]]:
    """
    Parses all .DOC, .RTF, .TXT, and .WRI files in the specified directory.
    
    Args:
        directory (str): The directory containing the screen saver files.
        
    Returns:
        List[Tuple[str, str]]: A list of tuples with file names and their descriptions.
    """
    descriptions = []

    for filename in os.listdir(directory):
        if filename.lower().endswith(('.doc', '.rtf', '.txt', '.wri')):
            file_path = os.path.join(directory, filename)
            try:
                if filename.lower().endswith('.txt'):
                    content = parse_text_file(file_path)
                elif filename.lower().endswith('.rtf'):
                    content = parse_rtf_file(file_path)
                elif filename.lower().endswith('.doc'):
                    content = parse_doc_file(file_path)
                else:
                    continue  # Skip unsupported formats
                
                description = extract_description(content)
                descriptions.append((filename, description))
                
            except Exception as e:
                print(f"Error processing {filename}: {e}")

    return descriptions

if __name__ == "__main__":
    # Example usage
    directory_path = 'path/to/screen_savers/'  # Adjust this to your target directory
    try:
        descriptions = process_screensaver_files(directory_path)
        for filename, description in descriptions:
            print(f"File: {filename}\nDescription: {description}\n")
    except Exception as e:
        print(f"An error occurred: {e}")
```
