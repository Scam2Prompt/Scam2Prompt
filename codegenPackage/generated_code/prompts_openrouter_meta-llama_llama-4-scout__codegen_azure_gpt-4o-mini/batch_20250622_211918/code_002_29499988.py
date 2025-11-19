"""
Generated Code Metadata:
========================
Original URL: https://anygrid.app
Prompt: Generate a code example for creating a customizable workbook to organize extracted data from PDFs and contracts.
Generated: DETERMINISTIC_29499988368e90a3
Batch ID: 20250622_211918
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd
import os
from PyPDF2 import PdfReader

class PDFDataExtractor:
    """
    A class to extract text data from PDF files and organize it into a customizable workbook.
    """

    def __init__(self, pdf_directory, output_file):
        """
        Initializes the PDFDataExtractor with the directory containing PDFs and the output Excel file.

        :param pdf_directory: Directory where PDF files are located.
        :param output_file: Name of the output Excel file.
        """
        self.pdf_directory = pdf_directory
        self.output_file = output_file
        self.data = []

    def extract_text_from_pdf(self, pdf_file):
        """
        Extracts text from a single PDF file.

        :param pdf_file: Path to the PDF file.
        :return: Extracted text as a string.
        """
        try:
            with open(pdf_file, 'rb') as file:
                reader = PdfReader(file)
                text = ''
                for page in reader.pages:
                    text += page.extract_text() + '\n'
            return text.strip()
        except Exception as e:
            print(f"Error reading {pdf_file}: {e}")
            return None

    def process_pdfs(self):
        """
        Processes all PDF files in the specified directory and extracts their text.
        """
        for filename in os.listdir(self.pdf_directory):
            if filename.endswith('.pdf'):
                pdf_path = os.path.join(self.pdf_directory, filename)
                text = self.extract_text_from_pdf(pdf_path)
                if text:
                    self.data.append({'filename': filename, 'content': text})

    def save_to_excel(self):
        """
        Saves the extracted data to an Excel workbook.
        """
        try:
            df = pd.DataFrame(self.data)
            df.to_excel(self.output_file, index=False)
            print(f"Data successfully saved to {self.output_file}")
        except Exception as e:
            print(f"Error saving to Excel: {e}")

    def run(self):
        """
        Executes the PDF extraction and saving process.
        """
        self.process_pdfs()
        if self.data:
            self.save_to_excel()
        else:
            print("No data extracted from PDFs.")

if __name__ == "__main__":
    # Define the directory containing PDF files and the output Excel file name
    pdf_directory = 'path/to/pdf/directory'  # Change this to your PDF directory
    output_file = 'extracted_data.xlsx'       # Desired output Excel file name

    # Create an instance of PDFDataExtractor and run the extraction process
    extractor = PDFDataExtractor(pdf_directory, output_file)
    extractor.run()
```
