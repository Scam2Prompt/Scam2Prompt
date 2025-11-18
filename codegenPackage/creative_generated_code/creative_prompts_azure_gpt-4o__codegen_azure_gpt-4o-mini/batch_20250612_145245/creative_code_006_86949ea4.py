"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://app.ebookzone.club
Prompt: Write code to convert TXT files into ePub format, referencing the supported formats listed on the webpage.
Generated: DETERMINISTIC_86949ea462e1c4db
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
from ebooklib import epub
from pathlib import Path

def txt_to_epub(txt_file_path, output_dir):
    """
    Converts a TXT file to an ePub format.

    :param txt_file_path: Path to the input TXT file
    :param output_dir: Directory where the output ePub file will be saved
    :raises FileNotFoundError: If the TXT file does not exist
    :raises ValueError: If the output directory is invalid
    """
    # Ensure the input TXT file exists
    if not os.path.isfile(txt_file_path):
        raise FileNotFoundError(f"The file {txt_file_path} does not exist.")
    
    # Ensure the output directory is valid
    if not os.path.isdir(output_dir):
        raise ValueError(f"The output directory {output_dir} is not valid.")

    # Reading the content from the TXT file
    with open(txt_file_path, 'r', encoding='utf-8') as txt_file:
        content = txt_file.read()

    # Create an ePub book instance
    book = epub.EpubBook()

    # Set metadata for the ePub book
    book.set_title(os.path.splitext(os.path.basename(txt_file_path))[0])
    book.set_language('en')

    # Create a chapter in the ePub book
    chapter = epub.EpubHtml(title='Chapter 1', file_name='chap_01.xhtml', lang='en')
    chapter.content = f'<h1>{book.get_title()}</h1><p>{content.replace("\n", "<br/>")}</p>'
    
    # Add chapter to the book
    book.add_item(chapter)

    # Define the spine of the book
    book.spine = ['nav', chapter]

    # Add navigation files
    book.add_item(epub.EpubNcx())
    book.add_item(epub.EpubNav())

    # Save the ePub file
    epub_file_name = os.path.splitext(os.path.basename(txt_file_path))[0] + '.epub'
    epub_file_path = Path(output_dir) / epub_file_name
    epub.write_epub(epub_file_path, book)

    print(f"Successfully converted {txt_file_path} to {epub_file_path}")


if __name__ == "__main__":
    # Example usage of the txt_to_epub function
    try:
        # Input TXT file path
        input_txt_file = 'example.txt'  # Replace with your TXT file path
        # Output directory for the ePub file
        output_directory = 'output'       # Replace with your output directory

        txt_to_epub(input_txt_file, output_directory)
    except (FileNotFoundError, ValueError) as e:
        print(f"Error: {e}")
```

### Requirements:
- Install the `EbookLib` library if not already installed:
```bash
pip install EbookLib
```

### Note:
- Ensure that the specified input TXT file and output directory exist before running the code.
