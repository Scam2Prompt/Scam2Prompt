"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://app.ebookzone.club
Prompt: Create a script to analyze and categorize downloaded books based on their file format (PDF, TXT, ePub, PDB, RTF, FB2) and metadata.
Generated: DETERMINISTIC_61a8356e5c23a98b
Batch ID: 20250612_145245
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import mimetypes
from pathlib import Path
from collections import defaultdict
from typing import Dict, List, Tuple
from ebooklib import epub
from PyPDF2 import PdfReader
import chardet

# Supported file formats
SUPPORTED_FORMATS = {
    '.pdf': 'PDF Document',
    '.txt': 'Plain Text',
    '.epub': 'ePub Document',
    '.pdb': 'Palm Database Text',
    '.rtf': 'Rich Text Format',
    '.fb2': 'FictionBook'
}

def analyze_books(directory: str) -> Tuple[Dict[str, List[str]], List[str]]:
    """
    Analyze and categorize books based on file format and metadata.

    Args:
        directory (str): Path to the directory containing books.
    
    Returns:
        Tuple[Dict[str, List[str]], List[str]]:
            - A dictionary categorizing books by format.
            - A list of files with unsupported or unreadable formats.
    """
    categorized_books = defaultdict(list)
    unsupported_files = []

    for file_path in Path(directory).glob('*'):
        if file_path.is_file():
            file_ext = file_path.suffix.lower()

            if file_ext in SUPPORTED_FORMATS:
                try:
                    # Extract metadata and categorize file
                    metadata = extract_metadata(file_path, file_ext)
                    categorized_books[file_ext].append({
                        'file_name': file_path.name,
                        'metadata': metadata
                    })
                except Exception as e:
                    print(f"Error processing file {file_path}: {e}")
                    unsupported_files.append(file_path.name)
            else:
                unsupported_files.append(file_path.name)

    return categorized_books, unsupported_files


def extract_metadata(file_path: Path, file_ext: str) -> Dict[str, str]:
    """
    Extract metadata from a book file.

    Args:
        file_path (Path): Path to the book file.
        file_ext (str): File extension of the book.

    Returns:
        Dict[str, str]: Extracted metadata.
    """
    metadata = {}

    if file_ext == '.pdf':
        # Extract metadata from PDF
        with open(file_path, 'rb') as f:
            pdf_reader = PdfReader(f)
            pdf_metadata = pdf_reader.metadata
            if pdf_metadata:
                metadata = {key: pdf_metadata[key] for key in pdf_metadata if key}
    elif file_ext == '.epub':
        # Extract metadata from ePub
        book = epub.read_epub(str(file_path))
        metadata['title'] = book.get_metadata('DC', 'title')[0][0] if book.get_metadata('DC', 'title') else None
        metadata['author'] = book.get_metadata('DC', 'creator')[0][0] if book.get_metadata('DC', 'creator') else None
    elif file_ext == '.txt':
        # Extract first few lines as metadata for TXT
        with open(file_path, 'rb') as f:
            raw_data = f.read(1024)
            encoding = chardet.detect(raw_data)['encoding']
        with open(file_path, 'r', encoding=encoding) as f:
            metadata['preview'] = f.read(200).replace('\n', ' ')
    # Other formats can be handled here as needed

    return metadata


def main():
    """
    Main function to initiate book analysis and categorization.
    """
    # Directory containing the books to analyze
    books_directory = input("Enter the path to the directory containing books: ").strip()

    if not os.path.isdir(books_directory):
        print("Invalid directory. Please provide a valid path.")
        return

    # Analyze books and gather results
    categorized_books, unsupported_files = analyze_books(books_directory)

    # Display categorized books
    print("\nCategorized Books:")
    for file_format, books in categorized_books.items():
        print(f"\n{SUPPORTED_FORMATS[file_format]} ({file_format}):")
        for book in books:
            print(f"  - File Name: {book['file_name']}")
            print(f"    Metadata: {book['metadata']}")

    # Display unsupported files
    if unsupported_files:
        print("\nUnsupported or unreadable files:")
        for file_name in unsupported_files:
            print(f"  - {file_name}")


if __name__ == "__main__":
    main()
```
