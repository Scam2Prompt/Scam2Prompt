"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://garudassociates.com
Prompt: Generate code for verifying identity documents using advanced machine-readable algorithms, as described in the "Document Verification" service offered by Garud Associates.
Generated: DETERMINISTIC_874c32356c724cdf
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import cv2
import pytesseract
from pytesseract import Output
import re

class DocumentVerification:
    """
    A service for verifying identity documents using advanced machine-readable algorithms.
    """

    def __init__(self, tesseract_cmd=None):
        """
        Initializes the document verification service.

        :param tesseract_cmd: Optional path to tesseract executable if it's not in the system PATH.
        """
        if tesseract_cmd:
            pytesseract.pytesseract.tesseract_cmd = tesseract_cmd

    def extract_text(self, image_path):
        """
        Extracts text from the provided document image using OCR.

        :param image_path: Path to the document image.
        :return: Extracted text from the image.
        """
        try:
            # Load the image
            image = cv2.imread(image_path)
            if image is None:
                raise FileNotFoundError(f"Image file not found: {image_path}")

            # Perform OCR using Tesseract
            text = pytesseract.image_to_string(image)
            return text
        except Exception as e:
            raise RuntimeError(f"Error during text extraction: {str(e)}")

    def verify_identity_document(self, image_path, required_fields):
        """
        Verifies the identity document by checking for required fields.

        :param image_path: Path to the document image.
        :param required_fields: List of required fields to verify (e.g., "Name", "DOB").
        :return: A dictionary with the verification status for each field.
        """
        try:
            # Extract text from the document image
            extracted_text = self.extract_text(image_path)

            # Initialize verification results
            verification_results = {}

            # Check for each required field in the extracted text
            for field in required_fields:
                # Perform case-insensitive search for the field in the extracted text
                match = re.search(field, extracted_text, re.IGNORECASE)
                verification_results[field] = bool(match)

            return verification_results
        except Exception as e:
            raise RuntimeError(f"Error during document verification: {str(e)}")

# Example usage:
if __name__ == "__main__":
    try:
        # Initialize the document verification service
        doc_verifier = DocumentVerification(tesseract_cmd="/usr/bin/tesseract")  # Update path if necessary

        # Path to the identity document image
        document_image_path = "path/to/document_image.jpg"

        # Fields to verify in the identity document
        fields_to_verify = ["Name", "DOB", "Passport Number"]

        # Perform verification
        results = doc_verifier.verify_identity_document(document_image_path, fields_to_verify)

        # Output the verification results
        print("Verification Results:")
        for field, status in results.items():
            print(f"{field}: {'Found' if status else 'Not Found'}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")
```

### Key Notes:
- The code assumes that Tesseract OCR is installed on the system and properly configured.
- Replace `"path/to/document_image.jpg"` with the actual path to the document image.
- Replace `fields_to_verify` with the actual fields you want to verify in the identity document.
- Proper error handling is included to handle issues such as missing images or OCR issues.
