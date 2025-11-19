"""
Generated Code Metadata:
========================
Original URL: https://ssdsd.netlify.app
Prompt: Generate a code snippet that extracts lesson details from the 상일미디어고 PDF files and organizes them by subject and day.
Generated: DETERMINISTIC_6f0bb6eb29ed0a68
Batch ID: 20250612_162504
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import re
import PyPDF2
from collections import defaultdict

class LessonExtractor:
    def __init__(self, pdf_directory):
        """
        Initializes the LessonExtractor with the directory containing PDF files.

        :param pdf_directory: Path to the directory containing PDF files.
        """
        self.pdf_directory = pdf_directory
        self.lesson_details = defaultdict(lambda: defaultdict(list))

    def extract_lessons(self):
        """
        Extracts lesson details from all PDF files in the specified directory.
        Organizes lessons by subject and day.
        """
        # Iterate through all PDF files in the directory
        for filename in os.listdir(self.pdf_directory):
            if filename.endswith('.pdf'):
                self._process_pdf(os.path.join(self.pdf_directory, filename))

    def _process_pdf(self, pdf_path):
        """
        Processes a single PDF file to extract lesson details.

        :param pdf_path: Path to the PDF file to be processed.
        """
        try:
            with open(pdf_path, 'rb') as file:
                reader = PyPDF2.PdfReader(file)
                for page in reader.pages:
                    text = page.extract_text()
                    self._parse_text(text)
        except Exception as e:
            print(f"Error processing {pdf_path}: {e}")

    def _parse_text(self, text):
        """
        Parses the extracted text to find lesson details.

        :param text: The text extracted from a PDF page.
        """
        # Regular expression to match lesson details
        lesson_pattern = re.compile(r'(?P<day>\w+)\s*:\s*(?P<subject>[\w\s]+)')
        for line in text.splitlines():
            match = lesson_pattern.search(line)
            if match:
                day = match.group('day').strip()
                subject = match.group('subject').strip()
                self.lesson_details[subject][day].append(line)

    def get_lessons(self):
        """
        Returns the organized lesson details.

        :return: A dictionary containing lessons organized by subject and day.
        """
        return dict(self.lesson_details)

if __name__ == "__main__":
    # Specify the directory containing the PDF files
    pdf_directory = 'path/to/pdf/files'
    
    # Create an instance of LessonExtractor
    extractor = LessonExtractor(pdf_directory)
    
    # Extract lessons from the PDF files
    extractor.extract_lessons()
    
    # Retrieve and print the organized lesson details
    lessons = extractor.get_lessons()
    for subject, days in lessons.items():
        print(f"Subject: {subject}")
        for day, details in days.items():
            print(f"  Day: {day}")
            for detail in details:
                print(f"    Detail: {detail}")
```
