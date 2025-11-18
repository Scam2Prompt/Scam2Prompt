"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.napatablets.com
Prompt: Provide a Python script to manage electronic document imaging and signature capture for invoices and statements, referencing the solutions outlined on the NAPA Tablets website.
Generated: DETERMINISTIC_fbad10d2def2f901
Batch ID: 20250612_154932
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import datetime
from typing import List, Dict
from PIL import Image
import PyPDF2
from reportlab.pdfgen import canvas

# Error classes
class FileProcessingError(Exception):
    """Raised when there is an error processing a file"""
    pass

class SignatureCaptureError(Exception):
    """Raised when there is an error capturing or embedding a signature"""
    pass

# Configuration
INVOICE_DIR = "./invoices/"
STATEMENT_DIR = "./statements/"
SIGNED_DIR = "./signed_documents/"
SIGNATURE_FILE = "./signature.png"  # Path to the stored signature image

# Ensure necessary directories exist
os.makedirs(INVOICE_DIR, exist_ok=True)
os.makedirs(STATEMENT_DIR, exist_ok=True)
os.makedirs(SIGNED_DIR, exist_ok=True)

def load_documents(directory: str) -> List[str]:
    """
    Loads all document files from the specified directory.

    Args:
        directory (str): The directory containing document files.

    Returns:
        List[str]: A list of file paths.
    """
    try:
        return [os.path.join(directory, file) for file in os.listdir(directory) if file.endswith(".pdf")]
    except Exception as e:
        raise FileProcessingError(f"Error loading documents from {directory}: {str(e)}")

def embed_signature(pdf_path: str, signature_path: str) -> str:
    """
    Embeds a signature into a PDF document.

    Args:
        pdf_path (str): Path to the PDF document.
        signature_path (str): Path to the signature image.

    Returns:
        str: Path to the signed PDF document.
    """
    try:
        # Output file
        signed_pdf_path = os.path.join(SIGNED_DIR, f"signed_{os.path.basename(pdf_path)}")

        # Read the original PDF
        with open(pdf_path, "rb") as original_pdf:
            reader = PyPDF2.PdfReader(original_pdf)
            writer = PyPDF2.PdfWriter()

            # Iterate through pages and copy them
            for page in reader.pages:
                writer.add_page(page)

            # Add a blank page for the signature
            signature_page = canvas.Canvas("temp_signature_page.pdf")
            signature_page.drawImage(signature_path, 100, 100, width=200, height=100)  # Adjust coordinates as needed
            signature_page.save()

            # Merge the signature page
            with open("temp_signature_page.pdf", "rb") as sig_pdf:
                sig_reader = PyPDF2.PdfReader(sig_pdf)
                writer.add_page(sig_reader.pages[0])

            # Write the signed PDF
            with open(signed_pdf_path, "wb") as signed_pdf:
                writer.write(signed_pdf)

        # Clean up temporary file
        os.remove("temp_signature_page.pdf")

        return signed_pdf_path
    except Exception as e:
        raise SignatureCaptureError(f"Error embedding signature into {pdf_path}: {str(e)}")

def process_documents(document_type: str):
    """
    Processes documents by embedding a signature.

    Args:
        document_type (str): Type of document to process ('invoice' or 'statement').
    """
    try:
        # Select the correct directory
        directory = INVOICE_DIR if document_type == "invoice" else STATEMENT_DIR
        documents = load_documents(directory)

        if not documents:
            print(f"No {document_type}s found in {directory}.")
            return

        # Process each document
        for document in documents:
            signed_document = embed_signature(document, SIGNATURE_FILE)
            print(f"Signed {document_type}: {signed_document}")
    except Exception as e:
        print(f"Error processing {document_type}s: {str(e)}")

def main():
    """
    Main function to manage document imaging and signature capture.
    """
    print("Starting document processing...")

    # Process invoices
    print("Processing invoices...")
    process_documents("invoice")

    # Process statements
    print("Processing statements...")
    process_documents("statement")

    print("Document processing complete.")

if __name__ == "__main__":
    main()
```
