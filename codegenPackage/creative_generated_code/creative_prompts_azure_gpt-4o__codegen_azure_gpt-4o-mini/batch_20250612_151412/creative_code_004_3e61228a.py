"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nabberx.com
Prompt: Write code to digitize and organize business records using a document digitization solution similar to NabberX's data management services.
Generated: DETERMINISTIC_3e61228a348e3f9b
Batch ID: 20250612_151412
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import logging
from typing import List, Dict
from pathlib import Path
from pdf2image import convert_from_path
from PIL import Image
import pytesseract
import json

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class DocumentDigitizer:
    """
    A class to handle the digitization and organization of business records.
    """

    def __init__(self, input_directory: str, output_directory: str):
        """
        Initialize the DocumentDigitizer with input and output directories.

        :param input_directory: Directory containing the documents to digitize.
        :param output_directory: Directory to store the digitized documents.
        """
        self.input_directory = Path(input_directory)
        self.output_directory = Path(output_directory)
        self.output_directory.mkdir(parents=True, exist_ok=True)

    def digitize_documents(self) -> None:
        """
        Process all documents in the input directory and save the digitized text
        to the output directory.
        """
        for file_path in self.input_directory.glob('*.pdf'):
            try:
                logging.info(f"Processing file: {file_path.name}")
                images = convert_from_path(str(file_path))
                digitized_text = self.extract_text_from_images(images)
                self.save_digitized_text(file_path.stem, digitized_text)
            except Exception as e:
                logging.error(f"Failed to process {file_path.name}: {e}")

    def extract_text_from_images(self, images: List[Image.Image]) -> str:
        """
        Extract text from a list of images using OCR.

        :param images: List of images to extract text from.
        :return: Extracted text.
        """
        full_text = ""
        for image in images:
            text = pytesseract.image_to_string(image)
            full_text += text + "\n"
        return full_text

    def save_digitized_text(self, filename: str, text: str) -> None:
        """
        Save the digitized text to a JSON file.

        :param filename: Base filename to use for the output file.
        :param text: Text to save.
        """
        output_file_path = self.output_directory / f"{filename}.json"
        try:
            with open(output_file_path, 'w', encoding='utf-8') as json_file:
                json.dump({'text': text}, json_file, ensure_ascii=False, indent=4)
            logging.info(f"Saved digitized text to: {output_file_path.name}")
        except IOError as e:
            logging.error(f"Error saving file {output_file_path.name}: {e}")

if __name__ == "__main__":
    # User-defined input and output paths
    input_dir = "path/to/input/documents"
    output_dir = "path/to/output/digitized_records"

    # Create a DocumentDigitizer instance
    digitizer = DocumentDigitizer(input_directory=input_dir, output_directory=output_dir)

    # Start the digitization process
    digitizer.digitize_documents()
```
