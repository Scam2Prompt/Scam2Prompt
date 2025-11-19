"""
Generated Code Metadata:
========================
Original URL: https://easydocgestao.com.br
Prompt: Develop a script for automating the process of document scanning and secure storage, referencing EasyDoc's emphasis on digitalization and organization.
Generated: DETERMINISTIC_947851e84523a0b6
Batch ID: 20250612_154306
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import cv2
import numpy as np
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
        self.output_folder.mkdir(parents=True, exist_ok=True)

    def scan_documents(self):
        """
        Scans all documents in the input folder, processes them, and saves them to the output folder.
        """
        try:
            for document in self.input_folder.glob('*.jpg'):
                self.process_document(document)
        except Exception as e:
            print(f"Error scanning documents: {e}")

    def process_document(self, document_path: Path):
        """
        Processes a single document image: reads, enhances, and saves it.

        :param document_path: Path to the document image to process.
        """
        try:
            # Read the image
            image = cv2.imread(str(document_path))
            if image is None:
                raise ValueError(f"Could not read image: {document_path}")

            # Enhance the image
            enhanced_image = self.enhance_image(image)

            # Save the processed image
            self.save_document(enhanced_image, document_path.name)
        except Exception as e:
            print(f"Error processing document {document_path.name}: {e}")

    def enhance_image(self, image: np.ndarray) -> np.ndarray:
        """
        Enhances the document image for better readability.

        :param image: The original document image.
        :return: The enhanced document image.
        """
        # Convert to grayscale
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # Apply Gaussian blur
        blurred_image = cv2.GaussianBlur(gray_image, (5, 5), 0)

        # Use adaptive thresholding to enhance the document
        enhanced_image = cv2.adaptiveThreshold(blurred_image, 255,
                                                cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                                cv2.THRESH_BINARY, 11, 2)
        return enhanced_image

    def save_document(self, image: np.ndarray, original_name: str):
        """
        Saves the processed document image to the output folder with a timestamp.

        :param image: The processed document image.
        :param original_name: The original name of the document for reference.
        """
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        output_name = f"{timestamp}_{original_name}"
        output_path = self.output_folder / output_name

        cv2.imwrite(str(output_path), image)
        print(f"Document saved: {output_path}")

if __name__ == "__main__":
    # Define input and output folders
    input_folder = "path/to/input/folder"
    output_folder = "path/to/output/folder"

    # Create a DocumentScanner instance and scan documents
    scanner = DocumentScanner(input_folder, output_folder)
    scanner.scan_documents()
```
