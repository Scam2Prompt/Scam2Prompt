"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://thebookcompany.org
Prompt: Can you provide a code snippet for automating the formatting of a manuscript for publishing, similar to the services provided by The Book Company?
Generated: DETERMINISTIC_a9b3c51a2728fd88
Batch ID: 20250612_161039
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
from docx import Document
from docx.shared import Pt
from docx.enum.text import WD_PARAGRAPH_ALIGNMENT


class ManuscriptFormatter:
    """
    A class to automate the formatting of a manuscript for publishing.
    """

    def __init__(self, input_file: str, output_file: str):
        """
        Initializes the ManuscriptFormatter with input and output file paths.

        :param input_file: Path to the manuscript input file (in .docx format).
        :param output_file: Path where the formatted manuscript will be saved.
        """
        self.input_file = input_file
        self.output_file = output_file

    def load_document(self) -> Document:
        """
        Loads the manuscript document.

        :return: Document object representing the manuscript.
        :raises FileNotFoundError: If the input file does not exist.
        :raises Exception: For any other errors encountered during file loading.
        """
        if not os.path.exists(self.input_file):
            raise FileNotFoundError(f"The file {self.input_file} does not exist.")
        
        try:
            return Document(self.input_file)
        except Exception as e:
            raise Exception(f"An error occurred while loading the document: {e}")

    def format_document(self, document: Document):
        """
        Formats the manuscript document according to publishing standards.

        :param document: Document object to format.
        """
        # Set font size for all paragraphs
        for paragraph in document.paragraphs:
            for run in paragraph.runs:
                run.font.size = Pt(12)  # Set font size to 12pt

            # Center-align the title if it's the first paragraph
            if paragraph == document.paragraphs[0]:
                paragraph.alignment = WD_PARAGRAPH_ALIGNMENT.CENTER

    def save_document(self, document: Document):
        """
        Saves the formatted document to the specified output file.

        :param document: Document object to save.
        :raises Exception: For any errors encountered during file saving.
        """
        try:
            document.save(self.output_file)
        except Exception as e:
            raise Exception(f"An error occurred while saving the document: {e}")

    def format_manuscript(self):
        """
        Main method to format the manuscript.
        """
        document = self.load_document()
        self.format_document(document)
        self.save_document(document)
        print(f"Manuscript formatted and saved to {self.output_file}")


# Example usage
if __name__ == '__main__':
    input_path = 'input_manuscript.docx'  # Path to your input manuscript
    output_path = 'formatted_manuscript.docx'  # Path to save the formatted manuscript

    formatter = ManuscriptFormatter(input_path, output_path)
    try:
        formatter.format_manuscript()
    except Exception as e:
        print(f"An error occurred: {e}")
```
