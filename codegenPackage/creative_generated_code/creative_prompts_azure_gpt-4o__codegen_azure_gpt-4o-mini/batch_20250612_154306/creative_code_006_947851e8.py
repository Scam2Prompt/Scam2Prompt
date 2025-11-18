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
import cv2  # OpenCV for image processing
import datetime
import shutil
from pathlib import Path

class DocumentScanner:
    def __init__(self, input_folder: str, output_folder: str):
        """
        Initializes the DocumentScanner with input and output folder paths.

        :param input_folder: Path to the folder containing documents to scan.
        :param output_folder: Path to the folder where scanned documents will be stored.
        """
        self.input_folder = Path(input_folder)
        self.output_folder = Path(output_folder)
        self.ensure_output_folder_exists()

    def ensure_output_folder_exists(self):
        """Creates the output folder if it does not exist."""
        if not self.output_folder.exists():
            self.output_folder.mkdir(parents=True, exist_ok=True)

    def scan_documents(self):
        """Scans documents from the input folder and saves them in the output folder."""
        try:
            for document in self.input_folder.glob('*.jpg'):  # Adjust the extension based on requirements
                self.process_document(document)
        except Exception as e:
            print(f"Error scanning documents: {e}")

    def process_document(self, document: Path):
        """Processes a single document by scanning it and storing it securely.

        :param document: Path to the document to be processed.
        """
        try:
            image = cv2.imread(str(document))
            if image is None:
                raise ValueError(f"Could not read the image: {document}")

            # Here you can add image processing logic (e.g., deskewing, cropping, etc.)
            processed_image = self.scan_and_enhance(image)

            timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
            output_file = self.output_folder / f"{timestamp}_{document.name}"
            cv2.imwrite(str(output_file), processed_image)
            print(f"Document saved: {output_file}")
        except Exception as e:
            print(f"Error processing document {document}: {e}")

    def scan_and_enhance(self, image):
        """Enhances the image for better readability.

        :param image: The image to enhance.
        :return: Enhanced image.
        """
        # Convert image to grayscale
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        # Apply Gaussian blur
        blurred = cv2.GaussianBlur(gray, (5, 5), 0)
        # Apply thresholding
        _, thresh = cv2.threshold(blurred, 150, 255, cv2.THRESH_BINARY_INV)
        return thresh

if __name__ == "__main__":
    # Define input and output folder paths
    input_folder = './documents_to_scan'
    output_folder = './scanned_documents'

    # Create an instance of DocumentScanner
    scanner = DocumentScanner(input_folder, output_folder)
    # Start scanning documents
    scanner.scan_documents()
```
