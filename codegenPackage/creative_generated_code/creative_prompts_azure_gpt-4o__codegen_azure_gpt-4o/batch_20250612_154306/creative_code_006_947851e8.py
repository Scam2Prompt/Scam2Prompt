"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://easydocgestao.com.br
Prompt: Develop a script for automating the process of document scanning and secure storage, referencing EasyDoc's emphasis on digitalization and organization.
Generated: DETERMINISTIC_947851e84523a0b6
Batch ID: 20250612_154306
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
import logging
from datetime import datetime
from PIL import Image
import pytesseract
import hashlib

# Configure logging
logging.basicConfig(
    filename='easydoc_scanner.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Constants
SCAN_DIR = "scanned_documents"
SECURE_STORAGE_DIR = "secure_storage"
SUPPORTED_FILE_TYPES = ['png', 'jpg', 'jpeg', 'pdf']
TESSERACT_CMD = r"C:\Program Files\Tesseract-OCR\tesseract.exe"  # Adjust path accordingly

def setup_directories():
    """
    Ensure required directories exist.
    """
    os.makedirs(SCAN_DIR, exist_ok=True)
    os.makedirs(SECURE_STORAGE_DIR, exist_ok=True)

def scan_document(file_path):
    """
    Convert an image or PDF document into text using OCR.
    
    Args:
        file_path (str): The path to the file being scanned.
    
    Returns:
        str: Extracted text from the document.
    """
    try:
        # Check file extension
        file_extension = file_path.split('.')[-1].lower()
        if file_extension not in SUPPORTED_FILE_TYPES:
            raise ValueError(f"Unsupported file type: {file_extension}")
        
        # Set Tesseract OCR path
        pytesseract.pytesseract.tesseract_cmd = TESSERACT_CMD

        if file_extension == 'pdf':
            # Handle PDF files (not implemented in this example for simplicity).
            raise NotImplementedError("PDF support is not implemented yet.")
        else:
            # Handle image files
            image = Image.open(file_path)
            extracted_text = pytesseract.image_to_string(image)
            return extracted_text
    except Exception as e:
        logging.error(f"Error during scanning: {e}")
        raise

def secure_store_document(original_path, extracted_text):
    """
    Securely store the document and the extracted text in a structured format.
    
    Args:
        original_path (str): Path to the original scanned file.
        extracted_text (str): Text extracted from the scanned document.
    """
    try:
        # Generate a secure hash based on the document content
        document_hash = hashlib.sha256(extracted_text.encode()).hexdigest()
        
        # Create a structured filename with timestamp and hash
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        file_name = f"{timestamp}_{document_hash[:8]}"
        
        # Save the original document securely
        secure_path = os.path.join(SECURE_STORAGE_DIR, f"{file_name}.original{os.path.splitext(original_path)[-1]}")
        os.replace(original_path, secure_path)
        
        # Save the extracted text
        text_path = os.path.join(SECURE_STORAGE_DIR, f"{file_name}.txt")
        with open(text_path, 'w', encoding='utf-8') as text_file:
            text_file.write(extracted_text)
        
        logging.info(f"Document securely stored: {secure_path}")
        logging.info(f"Extracted text saved: {text_path}")
    except Exception as e:
        logging.error(f"Error during secure storage: {e}")
        raise

def process_document(file_path):
    """
    Process a scanned document: extract text and securely store it.
    
    Args:
        file_path (str): Path to the scanned file to process.
    """
    try:
        logging.info(f"Processing document: {file_path}")
        extracted_text = scan_document(file_path)
        secure_store_document(file_path, extracted_text)
        logging.info(f"Document processed successfully: {file_path}")
    except Exception as e:
        logging.error(f"Failed to process document: {file_path}. Error: {e}")

def main():
    """
    Main function to initialize the script and process scanned documents in the SCAN_DIR.
    """
    try:
        setup_directories()
        logging.info("Starting EasyDoc document scanner...")
        
        # Process all files in the scan directory
        for file_name in os.listdir(SCAN_DIR):
            file_path = os.path.join(SCAN_DIR, file_name)
            if os.path.isfile(file_path):
                process_document(file_path)
        
        logging.info("All documents processed successfully.")
    except Exception as e:
        logging.critical(f"Unhandled exception in main: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
```
