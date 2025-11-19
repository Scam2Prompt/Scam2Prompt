"""
Generated Code Metadata:
========================
Original URL: https://feedoy.org
Prompt: Write a script that extracts and displays information from a .DOC or .TXT file included in a screen saver archive, referencing the methods used on Dick Lee's site.
Generated: DETERMINISTIC_ed4af56f0391f5c7
Batch ID: 20250612_135617
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**File Extractor Script**
=========================

```python
import os
import zipfile
import docx
import re

def extract_info_from_docx(file_path):
    """
    Extracts text from a .docx file.

    Args:
        file_path (str): Path to the .docx file.

    Returns:
        str: Extracted text.
    """
    try:
        doc = docx.Document(file_path)
        text = []
        for para in doc.paragraphs:
            text.append(para.text)
        return '\n'.join(text)
    except Exception as e:
        print(f"Error extracting text from .docx: {e}")
        return ""

def extract_info_from_txt(file_path):
    """
    Extracts text from a .txt file.

    Args:
        file_path (str): Path to the .txt file.

    Returns:
        str: Extracted text.
    """
    try:
        with open(file_path, 'r') as file:
            return file.read()
    except Exception as e:
        print(f"Error reading .txt file: {e}")
        return ""

def extract_file_from_archive(archive_path, output_path):
    """
    Extracts a .DOC or .TXT file from a screen saver archive.

    Args:
        archive_path (str): Path to the screen saver archive (.zip).
        output_path (str): Path to extract the file to.

    Returns:
        str: Path to the extracted file.
    """
    try:
        with zipfile.ZipFile(archive_path, 'r') as zip_ref:
            for file in zip_ref.namelist():
                if file.endswith(".doc") or file.endswith(".txt"):
                    zip_ref.extract(file, output_path)
                    return os.path.join(output_path, file)
    except Exception as e:
        print(f"Error extracting file from archive: {e}")
    return ""

def display_info(file_path):
    """
    Displays information from a .DOC or .TXT file.

    Args:
        file_path (str): Path to the file.
    """
    if file_path.endswith(".docx") or file_path.endswith(".doc"):
        text = extract_info_from_docx(file_path)
    elif file_path.endswith(".txt"):
        text = extract_info_from_txt(file_path)
    else:
        print("Unsupported file type")
        return

    print(text)

def main():
    archive_path = input("Enter the path to the screen saver archive (.zip): ")
    output_path = "extracted_files"

    if not os.path.exists(output_path):
        os.makedirs(output_path)

    extracted_file_path = extract_file_from_archive(archive_path, output_path)
    if extracted_file_path:
        display_info(extracted_file_path)

if __name__ == "__main__":
    main()
```
