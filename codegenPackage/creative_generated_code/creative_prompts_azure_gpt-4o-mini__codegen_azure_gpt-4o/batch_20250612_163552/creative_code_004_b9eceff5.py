"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://penguinbookspublishers.com
Prompt: How can I automate the process of formatting a manuscript for publishing, taking cues from the comprehensive services provided by Penguin Books Publishers?
Generated: DETERMINISTIC_b9eceff5e3a34629
Batch ID: 20250612_163552
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is Python code that automates the process of formatting a manuscript for publishing, inspired by publishing standards. The script performs document cleanup, title page generation, font styling, section organization, and export to a formatted file.

```python
import os
import re
from docx import Document
from docx.shared import Pt
from docx.enum.text import WD_ALIGN_PARAGRAPH

# Define constants for formatting
FONT_NAME = "Times New Roman"
FONT_SIZE_BODY = 12
FONT_SIZE_TITLE = 14
LINE_SPACING = 1.5
TITLE_PAGE_TEMPLATE = {
    "title": "Manuscript Title",
    "author": "Author Name",
    "contact": {
        "email": "author@example.com",
        "phone": "123-456-7890"
    }
}
OUTPUT_FILE = "formatted_manuscript.docx"

def format_manuscript(input_file: str):
    """
    Automates the formatting of a manuscript for publishing.
    Takes an input text file and applies professional formatting to create an output Word document.
    """
    try:
        # Step 1: Validate input file
        if not os.path.exists(input_file):
            raise FileNotFoundError(f"Input file '{input_file}' not found.")
        if not input_file.endswith(".txt"):
            raise ValueError("Input file must be a .txt file.")

        # Step 2: Read input manuscript
        with open(input_file, "r", encoding="utf-8") as file:
            manuscript_content = file.read()

        # Step 3: Create a new Word document
        doc = Document()

        # Step 4: Generate title page
        generate_title_page(doc)

        # Step 5: Format body (split into paragraphs and apply styling)
        format_body(manuscript_content, doc)

        # Step 6: Save formatted manuscript to output file
        doc.save(OUTPUT_FILE)
        print(f"Formatted manuscript saved to '{OUTPUT_FILE}'.")

    except Exception as e:
        print(f"An error occurred during formatting: {e}")

def generate_title_page(doc: Document):
    """
    Creates a title page for the manuscript using predefined template data.
    """
    title_page = doc.add_section().header
    title_page.is_linked_to_previous = False

    # Title
    title_paragraph = doc.add_paragraph()
    title_paragraph.alignment = WD_ALIGN_PARAGRAPH.CENTER
    title_run = title_paragraph.add_run(TITLE_PAGE_TEMPLATE["title"])
    title_run.font.name = FONT_NAME
    title_run.font.size = Pt(FONT_SIZE_TITLE)
    title_run.bold = True

    # Author
    author_paragraph = doc.add_paragraph()
    author_paragraph.alignment = WD_ALIGN_PARAGRAPH.CENTER
    author_run = author_paragraph.add_run("By: " + TITLE_PAGE_TEMPLATE["author"])
    author_run.font.name = FONT_NAME
    author_run.font.size = Pt(FONT_SIZE_BODY)

    # Contact Information
    contact_paragraph = doc.add_paragraph()
    contact_paragraph.alignment = WD_ALIGN_PARAGRAPH.CENTER
    contact_run = contact_paragraph.add_run(
        f"Email: {TITLE_PAGE_TEMPLATE['contact']['email']} | Phone: {TITLE_PAGE_TEMPLATE['contact']['phone']}"
    )
    contact_run.font.name = FONT_NAME
    contact_run.font.size = Pt(FONT_SIZE_BODY)

    # Add spacing
    doc.add_paragraph("\n\n")

def format_body(content: str, doc: Document):
    """
    Formats the body of the manuscript by cleaning up text and applying paragraph styles.
    """
    # Split content into paragraphs
    paragraphs = [p.strip() for p in content.split("\n") if p.strip()]

    for paragraph_text in paragraphs:
        # Remove unwanted whitespace
        paragraph_text = re.sub(r"\s+", " ", paragraph_text)

        # Add paragraph to the document
        paragraph = doc.add_paragraph()
        paragraph.alignment = WD_ALIGN_PARAGRAPH.LEFT
        run = paragraph.add_run(paragraph_text)
        run.font.name = FONT_NAME
        run.font.size = Pt(FONT_SIZE_BODY)
        paragraph.paragraph_format.line_spacing = LINE_SPACING


# Run the script (example: replace 'input.txt' with your manuscript file)
if __name__ == "__main__":
    input_file_path = "input.txt"  # Replace with the path to your manuscript file
    format_manuscript(input_file_path)
```

### Key Features:
- **Title Page Creation**: Includes title, author name, and contact information.
- **Body Formatting**: Applies font styles, removes unwanted whitespace, and organizes paragraphs.
- **Error Handling**: Ensures the input file exists and is in the correct format.

Ensure you have the `python-docx` library installed (`pip install python-docx`) before running the script.
