"""
Generated Code Metadata:
========================
Original URL: https://app.ebookzone.club
Prompt: Create a script to analyze and categorize downloaded books based on their file format (PDF, TXT, ePub, PDB, RTF, FB2) and metadata.
Generated: DETERMINISTIC_61a8356e5c23a98b
Batch ID: 20250612_145245
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import ebook_meta
from PyPDF2 import PdfFileReader
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def get_metadata(file_path):
    """
    Retrieves metadata from a file based on its format.

    Args:
        file_path (str): The path to the file.

    Returns:
        dict: A dictionary containing the file's metadata.
    """
    metadata = {}
    file_format = os.path.splitext(file_path)[1].lower()

    try:
        if file_format == '.pdf':
            with open(file_path, 'rb') as f:
                pdf = PdfFileReader(f)
                metadata['title'] = pdf.getDocumentInfo().title
                metadata['author'] = pdf.getDocumentInfo().author
        elif file_format in ['.epub', '.fb2']:
            metadata = ebook_meta.get_metadata(file_path)
        elif file_format == '.txt':
            with open(file_path, 'r') as f:
                lines = f.readlines()
                for line in lines:
                    if line.startswith('Title:'):
                        metadata['title'] = line.strip().replace('Title:', '')
                    elif line.startswith('Author:'):
                        metadata['author'] = line.strip().replace('Author:', '')
    except Exception as e:
        logging.error(f"Error retrieving metadata for {file_path}: {str(e)}")

    return metadata

def categorize_books(directory):
    """
    Categorizes books in a directory based on their file format.

    Args:
        directory (str): The path to the directory containing the books.

    Returns:
        dict: A dictionary with file formats as keys and lists of file paths as values.
    """
    categorized_books = {
        'pdf': [],
        'txt': [],
        'epub': [],
        'pdb': [],
        'rtf': [],
        'fb2': []
    }

    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        file_format = os.path.splitext(file_path)[1].lower().replace('.', '')

        if file_format in categorized_books:
            categorized_books[file_format].append(file_path)

    return categorized_books

def analyze_books(directory):
    """
    Analyzes and categorizes books in a directory.

    Args:
        directory (str): The path to the directory containing the books.

    Returns:
        dict: A dictionary with file formats as keys and lists of dictionaries containing file metadata as values.
    """
    categorized_books = categorize_books(directory)
    analyzed_books = {}

    for file_format, file_paths in categorized_books.items():
        analyzed_books[file_format] = []

        for file_path in file_paths:
            metadata = get_metadata(file_path)
            analyzed_books[file_format].append({
                'file_path': file_path,
                'metadata': metadata
            })

    return analyzed_books

if __name__ == "__main__":
    directory = '/path/to/books'
    try:
        analyzed_books = analyze_books(directory)
        for file_format, books in analyzed_books.items():
            logging.info(f"Found {len(books)} {file_format} books:")
            for book in books:
                logging.info(f"  - {book['file_path']}: {book['metadata']}")
    except Exception as e:
        logging.error(f"Error analyzing books: {str(e)}")
```
