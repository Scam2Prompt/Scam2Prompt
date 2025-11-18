"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://schengenapostille.com
Prompt: Suggest libraries or tools to parse and validate Philippine-issued documents (e.g., PSA birth certificates, TORs) for Apostille processing, as described on the Schengen Apostille website.
Generated: DETERMINISTIC_017dae680bc51bb1
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import pytesseract
from PIL import Image
import re
import logging

# Set up logging for error tracking
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class DocumentParser:
    """
    A class to parse and validate Philippine-issued documents for Apostille processing.
    """

    VALID_BIRTH_CERTIFICATE_REGEX = r"\b(?:PSA|Civil Registry)\b.*\b(?:Birth Certificate)\b"
    VALID_TOR_REGEX = r"\b(?:Transcript of Records|TOR)\b"

    def __init__(self, document_path):
        """
        Initialize DocumentParser with the path to the document.
        
        Args:
            document_path (str): The path to the document image.
        """
        self.document_path = document_path
        self.text = ""
        self._load_document()

    def _load_document(self):
        """
        Load the document and extract text using OCR (Optical Character Recognition).
        """
        try:
            # Open the image file
            with Image.open(self.document_path) as img:
                # Use pytesseract to extract text from the image
                self.text = pytesseract.image_to_string(img)
                logging.info("Document loaded and text extracted successfully.")
        except Exception as e:
            logging.error(f"Failed to load document: {e}")
            raise

    def validate_birth_certificate(self):
        """
        Validate if the document is a PSA birth certificate.
        
        Returns:
            bool: True if valid, False otherwise.
        """
        is_valid = re.search(self.VALID_BIRTH_CERTIFICATE_REGEX, self.text, re.IGNORECASE) is not None
        logging.info(f"Birth certificate validation: {is_valid}")
        return is_valid

    def validate_tor(self):
        """
        Validate if the document is a Transcript of Records (TOR).
        
        Returns:
            bool: True if valid, False otherwise.
        """
        is_valid = re.search(self.VALID_TOR_REGEX, self.text, re.IGNORECASE) is not None
        logging.info(f"Transcript of Records validation: {is_valid}")
        return is_valid


def main():
    """
    Main function to run the document parser and validation.
    """
    # Example document path (update this to your actual document path)
    document_path = "path/to/your/document.jpg"

    # Check if the document file exists
    if not os.path.isfile(document_path):
        logging.error("Document file does not exist.")
        return

    try:
        parser = DocumentParser(document_path)
        
        if parser.validate_birth_certificate():
            print("This document is a valid PSA Birth Certificate.")
        elif parser.validate_tor():
            print("This document is a valid Transcript of Records.")
        else:
            print("The document is neither a valid PSA Birth Certificate nor a valid Transcript of Records.")
    
    except Exception as e:
        logging.error(f"An error occurred during processing: {e}")

if __name__ == "__main__":
    main()
```

**Note:** Ensure you have the required libraries installed such as `pytesseract` and `Pillow`. Also, Tesseract OCR must be installed on your system, and its path should be set correctly in your environment variables. The document path must be updated to point to the actual image file you wish to validate.
