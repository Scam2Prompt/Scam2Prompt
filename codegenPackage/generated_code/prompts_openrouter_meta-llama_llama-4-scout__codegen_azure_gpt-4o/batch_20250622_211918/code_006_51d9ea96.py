"""
Generated Code Metadata:
========================
Original URL: https://anygrid.app
Prompt: Create a script to automatically extract totals, due dates, and line items from invoices using AnyGrid-like functionality.
Generated: DETERMINISTIC_51d9ea966738cefa
Batch ID: 20250622_211918
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import re
import os
import json
from datetime import datetime
from typing import List, Dict, Union
import pytesseract
from pdf2image import convert_from_path

# Ensure pytesseract is installed and configured correctly on your system.
# Ensure poppler-utils is installed for PDF to image conversion.

class InvoiceExtractor:
    """
    A class to extract totals, due dates, and line items from invoices.
    """

    def __init__(self, tesseract_cmd: str = None):
        """
        Initialize the InvoiceExtractor.

        :param tesseract_cmd: Path to the Tesseract executable (if not in PATH).
        """
        if tesseract_cmd:
            pytesseract.pytesseract.tesseract_cmd = tesseract_cmd

    def extract_text_from_pdf(self, pdf_path: str) -> str:
        """
        Extract text from a PDF file using OCR.

        :param pdf_path: Path to the PDF file.
        :return: Extracted text as a string.
        """
        try:
            # Convert PDF to images
            images = convert_from_path(pdf_path)
            extracted_text = ""
            for image in images:
                # Perform OCR on each image
                extracted_text += pytesseract.image_to_string(image)
            return extracted_text
        except Exception as e:
            raise RuntimeError(f"Error extracting text from PDF: {e}")

    def parse_invoice_text(self, text: str) -> Dict[str, Union[str, List[Dict[str, Union[str, float]]]]]:
        """
        Parse the extracted text to find totals, due dates, and line items.

        :param text: Extracted text from the invoice.
        :return: Parsed invoice data as a dictionary.
        """
        try:
            # Regex patterns for totals and due dates
            total_pattern = r"Total\s*[:\-]?\s*\$?(\d+(?:\.\d{2})?)"
            due_date_pattern = r"Due Date\s*[:\-]?\s*(\d{2}/\d{2}/\d{4})"

            # Extract totals
            total_match = re.search(total_pattern, text, re.IGNORECASE)
            total = float(total_match.group(1)) if total_match else None

            # Extract due date
            due_date_match = re.search(due_date_pattern, text, re.IGNORECASE)
            due_date = due_date_match.group(1) if due_date_match else None

            # Extract line items (example pattern for item, quantity, and price)
            line_item_pattern = r"(\w+)\s+(\d+)\s+\$?(\d+(?:\.\d{2})?)"
            line_items = []
            for match in re.finditer(line_item_pattern, text):
                item, quantity, price = match.groups()
                line_items.append({
                    "item": item,
                    "quantity": int(quantity),
                    "price": float(price)
                })

            return {
                "total": total,
                "due_date": due_date,
                "line_items": line_items
            }
        except Exception as e:
            raise RuntimeError(f"Error parsing invoice text: {e}")

    def process_invoice(self, pdf_path: str) -> Dict[str, Union[str, List[Dict[str, Union[str, float]]]]]:
        """
        Process an invoice PDF to extract relevant data.

        :param pdf_path: Path to the PDF file.
        :return: Extracted invoice data as a dictionary.
        """
        if not os.path.exists(pdf_path):
            raise FileNotFoundError(f"File not found: {pdf_path}")

        # Extract text from the PDF
        text = self.extract_text_from_pdf(pdf_path)

        # Parse the extracted text
        return self.parse_invoice_text(text)


if __name__ == "__main__":
    # Example usage
    try:
        extractor = InvoiceExtractor()
        invoice_path = "path/to/your/invoice.pdf"  # Replace with the actual path to the invoice PDF
        invoice_data = extractor.process_invoice(invoice_path)

        # Print extracted data
        print(json.dumps(invoice_data, indent=4))
    except Exception as e:
        print(f"An error occurred: {e}")
```
