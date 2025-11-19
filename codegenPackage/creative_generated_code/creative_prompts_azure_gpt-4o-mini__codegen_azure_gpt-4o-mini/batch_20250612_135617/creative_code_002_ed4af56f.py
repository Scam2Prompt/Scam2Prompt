"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://feedoy.org
Prompt: Write a script that extracts and displays information from a .DOC or .TXT file included in a screen saver archive, referencing the methods used on Dick Lee's site.
Generated: DETERMINISTIC_ed4af56f0391f5c7
Batch ID: 20250612_135617
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import zipfile
from docx import Document
import logging

# Configure logging for better error tracking.
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def extract_files_from_zip(zip_path, extract_to):
    """
    Extracts the contents of a ZIP file to a specified directory.

    Parameters:
        zip_path (str): The path to the ZIP file.
        extract_to (str): The directory to extract files to.

    Raises:
        FileNotFoundError: If the ZIP file does not exist.
        zipfile.BadZipFile: If the file is not a zip file or is corrupted.
    """
    if not os.path.exists(zip_path):
        logging.error(f"ZIP file does not exist: {zip_path}")
        raise FileNotFoundError(f"ZIP file does not exist: {zip_path}")
    
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(extract_to)
        logging.info(f"Extracted files to: {extract_to}")

def read_txt_file(file_path):
    """
    Reads the contents of a TXT file.

    Parameters:
        file_path (str): The path to the TXT file.

    Returns:
        str: The contents of the TXT file.

    Raises:
        FileNotFoundError: If the TXT file does not exist.
    """
    if not os.path.exists(file_path):
        logging.error(f"TXT file does not exist: {file_path}")
        raise FileNotFoundError(f"TXT file does not exist: {file_path}")

    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
        logging.info(f"Read TXT file: {file_path}")
        return content

def read_docx_file(file_path):
    """
    Reads the contents of a DOCX file.

    Parameters:
        file_path (str): The path to the DOCX file.

    Returns:
        str: The contents of the DOCX file.

    Raises:
        FileNotFoundError: If the DOCX file does not exist.
    """
    if not os.path.exists(file_path):
        logging.error(f"DOCX file does not exist: {file_path}")
        raise FileNotFoundError(f"DOCX file does not exist: {file_path}")

    doc = Document(file_path)
    content = '\n'.join([para.text for para in doc.paragraphs])
    logging.info(f"Read DOCX file: {file_path}")
    return content

def display_file_content(file_path):
    """
    Displays the content of a file (TXT or DOCX).

    Parameters:
        file_path (str): The path to the file.

    Raises:
        ValueError: If the file extension is not supported.
    """
    _, ext = os.path.splitext(file_path)
    
    if ext.lower() == '.txt':
        content = read_txt_file(file_path)
    elif ext.lower() == '.docx':
        content = read_docx_file(file_path)
    else:
        logging.error(f"Unsupported file extension: {ext}")
        raise ValueError(f"Unsupported file extension: {ext}")
    
    print(content)

def main(zip_file_path, extract_directory):
    """
    Main function to extract files from a zip archive and display their content.

    Parameters:
        zip_file_path (str): The path to the ZIP file.
        extract_directory (str): The directory to extract files to.
    """
    try:
        extract_files_from_zip(zip_file_path, extract_directory)
        
        # Iterate through the extracted files and display their content
        for file_name in os.listdir(extract_directory):
            file_path = os.path.join(extract_directory, file_name)
            display_file_content(file_path)
    
    except Exception as e:
        logging.error(f"An error occurred: {e}")

# Example usage
if __name__ == "__main__":
    # Replace with the actual paths before running
    zip_file_path = 'path/to/screensaver_archive.zip'
    extract_directory = 'path/to/extract/directory'
    
    main(zip_file_path, extract_directory)
```
