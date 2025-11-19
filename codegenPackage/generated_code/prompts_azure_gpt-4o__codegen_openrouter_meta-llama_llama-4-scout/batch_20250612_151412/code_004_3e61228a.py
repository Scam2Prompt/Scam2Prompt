"""
Generated Code Metadata:
========================
Original URL: https://nabberx.com
Prompt: Write code to digitize and organize business records using a document digitization solution similar to NabberX's data management services.
Generated: DETERMINISTIC_3e61228a348e3f9b
Batch ID: 20250612_151412
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**Document Digitization Solution**
=====================================

### Requirements

* Python 3.9+
* `pandas` library for data manipulation
* `PyPDF2` library for PDF handling
* `python-docx` library for Word document handling
* `openpyxl` library for Excel handling

### Code
```python
import os
import logging
import pandas as pd
from PyPDF2 import PdfReader, PdfWriter
from docx import Document
from openpyxl import load_workbook

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class DocumentDigitizationSolution:
    def __init__(self, input_folder, output_folder):
        """
        Initialize the document digitization solution.

        Args:
            input_folder (str): Path to the input folder containing documents.
            output_folder (str): Path to the output folder for digitized documents.
        """
        self.input_folder = input_folder
        self.output_folder = output_folder

    def digitize_pdf(self, file_path):
        """
        Digitize a PDF document.

        Args:
            file_path (str): Path to the PDF file.

        Returns:
            str: Path to the digitized PDF file.
        """
        try:
            # Open the PDF file
            pdf_reader = PdfReader(file_path)
            pdf_writer = PdfWriter()

            # Iterate through pages and extract text
            for page_num in range(len(pdf_reader.pages)):
                page = pdf_reader.pages[page_num]
                text = page.extract_text()
                logger.info(f"Extracted text from page {page_num+1}: {text}")

                # Add page to the writer
                pdf_writer.add_page(page)

            # Save the digitized PDF
            output_file_path = os.path.join(self.output_folder, os.path.basename(file_path))
            with open(output_file_path, 'wb') as output_pdf:
                pdf_writer.write(output_pdf)

            return output_file_path

        except Exception as e:
            logger.error(f"Error digitizing PDF: {e}")
            return None

    def digitize_word_document(self, file_path):
        """
        Digitize a Word document.

        Args:
            file_path (str): Path to the Word document file.

        Returns:
            str: Path to the digitized Word document file.
        """
        try:
            # Open the Word document
            doc = Document(file_path)

            # Extract text from paragraphs
            text = []
            for para in doc.paragraphs:
                text.append(para.text)
            logger.info(f"Extracted text: {' '.join(text)}")

            # Save the digitized Word document
            output_file_path = os.path.join(self.output_folder, os.path.basename(file_path))
            output_doc = Document()
            for para_text in text:
                output_doc.add_paragraph(para_text)
            output_doc.save(output_file_path)

            return output_file_path

        except Exception as e:
            logger.error(f"Error digitizing Word document: {e}")
            return None

    def digitize_excel_document(self, file_path):
        """
        Digitize an Excel document.

        Args:
            file_path (str): Path to the Excel file.

        Returns:
            str: Path to the digitized Excel file.
        """
        try:
            # Load the Excel workbook
            wb = load_workbook(file_path)

            # Extract data from sheets
            data = []
            for sheet_name in wb.sheetnames:
                sheet = wb[sheet_name]
                sheet_data = []
                for row in sheet.rows:
                    row_data = [cell.value for cell in row]
                    sheet_data.append(row_data)
                data.append({sheet_name: sheet_data})

            # Save the digitized Excel file
            output_file_path = os.path.join(self.output_folder, os.path.basename(file_path))
            output_wb = pd.DataFrame(data).to_excel(output_file_path, index=False)

            return output_file_path

        except Exception as e:
            logger.error(f"Error digitizing Excel document: {e}")
            return None

    def process_documents(self):
        """
        Process documents in the input folder and save digitized documents to the output folder.
        """
        for file_name in os.listdir(self.input_folder):
            file_path = os.path.join(self.input_folder, file_name)

            if file_name.endswith(".pdf"):
                digitized_file_path = self.digitize_pdf(file_path)
                if digitized_file_path:
                    logger.info(f"Digitized PDF saved to: {digitized_file_path}")

            elif file_name.endswith(".docx"):
                digitized_file_path = self.digitize_word_document(file_path)
                if digitized_file_path:
                    logger.info(f"Digitized Word document saved to: {digitized_file_path}")

            elif file_name.endswith(".xlsx") or file_name.endswith(".xls"):
                digitized_file_path = self.digitize_excel_document(file_path)
                if digitized_file_path:
                    logger.info(f"Digitized Excel document saved to: {digitized_file_path}")

if __name__ == "__main__":
    input_folder = "input_documents"
    output_folder = "digitized_documents"

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    solution = DocumentDigitizationSolution(input_folder, output_folder)
    solution.process_documents()
```
