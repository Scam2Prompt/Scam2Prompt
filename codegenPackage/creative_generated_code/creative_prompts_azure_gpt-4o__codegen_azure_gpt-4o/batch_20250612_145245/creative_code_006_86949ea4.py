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
import sys
from ebooklib import epub

def txt_to_epub(txt_file, output_dir):
    """
    Convert a TXT file to ePub format.
    
    Args:
        txt_file (str): The path to the input TXT file.
        output_dir (str): The directory to save the generated ePub file.
        
    Returns:
        str: Path to the generated ePub file.
    """
    # Ensure the input file exists
    if not os.path.isfile(txt_file):
        raise FileNotFoundError(f"The file '{txt_file}' does not exist.")

    # Ensure the output directory exists
    if not os.path.isdir(output_dir):
        raise NotADirectoryError(f"The directory '{output_dir}' does not exist.")

    # Get the base name of the file (without extension) for the ePub title
    base_name = os.path.splitext(os.path.basename(txt_file))[0]

    # Create a new ePub book
    book = epub.EpubBook()

    # Set metadata for the ePub
    book.set_identifier(base_name)
    book.set_title(base_name)
    book.set_language('en')  # Default to English; customize as needed
    book.add_author('Unknown Author')  # Customize as needed or use metadata from TXT files

    # Read the content of the TXT file
    try:
        with open(txt_file, 'r', encoding='utf-8') as file:
            text_content = file.read()
    except Exception as e:
        raise IOError(f"Failed to read '{txt_file}': {e}")

    # Split the content into paragraphs
    paragraphs = text_content.split('\n\n')  # Using double line breaks to detect paragraphs

    # Add content as chapters
    for idx, paragraph in enumerate(paragraphs):
        chapter = epub.EpubHtml(title=f'Chapter {idx + 1}', file_name=f'chapter_{idx + 1}.xhtml', lang='en')
        chapter.content = f'<p>{paragraph.replace("\n", "<br/>")}</p>'  # Replace single line breaks with <br/>
        book.add_item(chapter)
        book.toc.append(chapter)  # Add to the table of contents
        book.spine.append(chapter)  # Add to the spine (reading order)

    # Add default navigation files
    book.add_item(epub.EpubNcx())
    book.add_item(epub.EpubNav())

    # Define the output file path
    output_file = os.path.join(output_dir, f"{base_name}.epub")

    # Write the ePub file
    try:
        epub.write_epub(output_file, book)
    except Exception as e:
        raise IOError(f"Failed to write ePub file '{output_file}': {e}")

    return output_file


if __name__ == "__main__":
    # Example usage:
    if len(sys.argv) != 3:
        print("Usage: python txt_to_epub.py <input_txt_file> <output_directory>")
        sys.exit(1)

    input_txt_file = sys.argv[1]
    output_directory = sys.argv[2]

    try:
        output_epub = txt_to_epub(input_txt_file, output_directory)
        print(f"ePub file generated successfully: {output_epub}")
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)
```
