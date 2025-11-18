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
from fpdf import FPDF

class ManuscriptFormatter(FPDF):
    """
    A class to handle the formatting and typesetting of manuscripts for publishing.
    This class inherits from FPDF to leverage its capabilities for creating PDF documents.
    """

    def __init__(self, title, author, layout_guidelines):
        """
        Initializes the ManuscriptFormatter with the title, author, and layout guidelines.
        
        :param title: Title of the manuscript
        :param author: Author of the manuscript
        :param layout_guidelines: Dictionary containing layout guidelines (font, size, margins, etc.)
        """
        super().__init__()
        self.title = title
        self.author = author
        self.layout_guidelines = layout_guidelines

        # Set up the PDF document
        self.set_auto_page_break(auto=True, margin=self.layout_guidelines['margin'])
        self.add_page()
        self.set_font(self.layout_guidelines['font'], size=self.layout_guidelines['font_size'])

    def add_text(self, text):
        """
        Add text to the PDF document with proper formatting.
        
        :param text: The text to add to the PDF
        """
        self.multi_cell(0, 10, text)

    def save_pdf(self, filename):
        """
        Save the formatted manuscript to a PDF file.
        
        :param filename: The name of the file to save the PDF as
        """
        try:
            self.output(filename)
            print(f"Manuscript saved successfully as '{filename}'.")
        except Exception as e:
            print(f"Error saving manuscript: {e}")

    def format_manuscript(self, content):
        """
        Format the manuscript by adding the title, author, and content.
        
        :param content: The main text content of the manuscript
        """
        # Add title
        self.set_font(self.layout_guidelines['font'], 'B', size=self.layout_guidelines['title_size'])
        self.cell(0, 10, self.title, ln=True, align='C')
        
        # Add author
        self.set_font(self.layout_guidelines['font'], 'I', size=self.layout_guidelines['author_size'])
        self.cell(0, 10, self.author, ln=True, align='C')
        
        # Add empty line
        self.ln(10)
        
        # Add main content
        self.set_font(self.layout_guidelines['font'], size=self.layout_guidelines['font_size'])
        self.add_text(content)

def main():
    # Define layout guidelines similar to Penguin Books Publishers
    layout_guidelines = {
        'font': 'Times',
        'font_size': 12,
        'title_size': 16,
        'author_size': 14,
        'margin': 20
    }
    
    # Example manuscript details
    title = "The Great Adventure"
    author = "John Doe"
    content = ("Once upon a time in a land far away, there lived a brave knight. "
               "His adventures took him to the highest mountains and the deepest valleys. "
               "This is a tale of courage, friendship, and the quest for glory.")
    
    # Instantiate the formatter
    formatter = ManuscriptFormatter(title, author, layout_guidelines)
    
    # Format and save the manuscript
    formatter.format_manuscript(content)
    formatter.save_pdf('manuscript.pdf')

if __name__ == "__main__":
    main()
```

Make sure to install the `fpdf` library before running the script:
```bash
pip install fpdf
```
