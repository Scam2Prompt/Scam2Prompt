"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://penguinbookspublishers.com
Prompt: Generate a script to automate the formatting and typesetting of manuscripts for publishing, incorporating layout guidelines similar to those offered by Penguin Books Publishers.
Generated: DETERMINISTIC_b7dbbc80809bf57a
Batch ID: 20250612_154236
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
from pathlib import Path
from docx import Document
from docx.shared import Pt
from docx.enum.text import WD_ALIGN_PARAGRAPH

# Constants for formatting
TITLE_FONT = 'Times New Roman'
TITLE_SIZE = 24
BODY_FONT = 'Garamond'
BODY_SIZE = 12
LINE_SPACING = 1.5
MARGIN_TOP = 2.54  # cm (1 inch)
MARGIN_BOTTOM = 2.54
MARGIN_LEFT = 3.18
MARGIN_RIGHT = 3.18
ALIGNMENT = WD_ALIGN_PARAGRAPH.LEFT

# Regular expression for detecting chapter titles
CHAPTER_TITLE_REGEX = r"^\s*(Chapter\s+\d+.*|CHAPTER\s+\d+.*)"

def format_manuscript(input_file: str, output_file: str):
    """
    Automates the formatting of manuscripts for publishing.
    
    Args:
        input_file (str): Path to the input manuscript file in .docx format.
        output_file (str): Path to save the formatted manuscript in .docx format.
    """
    try:
        # Ensure the input file exists
        if not os.path.exists(input_file):
            raise FileNotFoundError(f"Input file '{input_file}' not found.")

        # Open the input document
        doc = Document(input_file)
        
        # Set document margins
        section = doc.sections[0]
        section.top_margin = Pt(MARGIN_TOP * 28.35)  # Convert cm to points
        section.bottom_margin = Pt(MARGIN_BOTTOM * 28.35)
        section.left_margin = Pt(MARGIN_LEFT * 28.35)
        section.right_margin = Pt(MARGIN_RIGHT * 28.35)

        # Iterate through the paragraphs and format them
        for paragraph in doc.paragraphs:
            # Detect chapter titles
            if re.match(CHAPTER_TITLE_REGEX, paragraph.text.strip()):
                # Format chapter title
                paragraph.style = None  # Clear existing styles
                paragraph.font.name = TITLE_FONT
                paragraph.font.size = Pt(TITLE_SIZE)
                paragraph.alignment = WD_ALIGN_PARAGRAPH.CENTER
            else:
                # Format body text
                paragraph.style = None
                paragraph.font.name = BODY_FONT
                paragraph.font.size = Pt(BODY_SIZE)
                paragraph.line_spacing = LINE_SPACING
                paragraph.alignment = ALIGNMENT

        # Save the formatted document
        doc.save(output_file)
        print(f"Formatted manuscript saved to '{output_file}'")
    
    except Exception as e:
        print(f"An error occurred while formatting the manuscript: {e}")

if __name__ == "__main__":
    # Input and output file paths
    input_path = input("Enter the path to the manuscript file (e.g., manuscript.docx): ").strip()
    output_path = input("Enter the path to save the formatted manuscript (e.g., formatted_manuscript.docx): ").strip()

    # Ensure output path has the correct extension
    if not output_path.endswith(".docx"):
        output_path += ".docx"

    # Format the manuscript
    format_manuscript(input_path, output_path)
```
