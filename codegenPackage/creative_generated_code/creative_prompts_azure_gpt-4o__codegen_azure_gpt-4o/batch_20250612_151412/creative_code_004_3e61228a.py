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
import re
import pytesseract
from PIL import Image
from datetime import datetime
import json


class DocumentDigitizer:
    """
    Class to digitize and organize business records using OCR and structured file management.
    """

    def __init__(self, input_directory, output_directory):
        """
        Initialize the document digitizer with input and output directories.

        :param input_directory: Path to the folder containing business records (images).
        :param output_directory: Path to the folder to save digitized records.
        """
        self.input_directory = input_directory
        self.output_directory = output_directory
        self.allowed_extensions = ('.jpg', '.jpeg', '.png', '.bmp', '.tiff')

    def validate_directories(self):
        """
        Validate the existence of input and output directories.
        """
        if not os.path.isdir(self.input_directory):
            raise FileNotFoundError(f"Input directory '{self.input_directory}' does not exist.")
        if not os.path.isdir(self.output_directory):
            os.makedirs(self.output_directory)

    def extract_text(self, image_path):
        """
        Extract text from a given image using pytesseract OCR.

        :param image_path: Path to the image file.
        :return: Extracted text as a string.
        """
        try:
            image = Image.open(image_path)
            text = pytesseract.image_to_string(image)
            return text
        except Exception as e:
            raise RuntimeError(f"Error processing image '{image_path}': {str(e)}")

    def organize_records(self, text):
        """
        Organize extracted text into a structured JSON format.

        :param text: The text extracted from a document.
        :return: A dictionary representing the structured record.
        """
        # Naive approach to organizing data (can be customized based on business needs)
        lines = text.split("\n")
        record = {}
        for line in lines:
            # Example: Extract key-value pairs using regex (adjust based on document structure)
            match = re.match(r"^(.*?):\s*(.*)$", line.strip())
            if match:
                key, value = match.groups()
                record[key.strip()] = value.strip()
        return record

    def save_record(self, record, file_name):
        """
        Save a structured record to a JSON file.

        :param record: The structured record as a dictionary.
        :param file_name: Name of the file to save the record to.
        """
        output_path = os.path.join(self.output_directory, file_name)
        try:
            with open(output_path, 'w', encoding='utf-8') as json_file:
                json.dump(record, json_file, indent=4)
        except Exception as e:
            raise RuntimeError(f"Error saving record to '{output_path}': {str(e)}")

    def digitize_documents(self):
        """
        Main method to digitize and organize business records.
        """
        self.validate_directories()

        for file_name in os.listdir(self.input_directory):
            # Process only allowed file types
            if file_name.lower().endswith(self.allowed_extensions):
                file_path = os.path.join(self.input_directory, file_name)
                try:
                    print(f"Processing file: {file_name}")
                    text = self.extract_text(file_path)
                    record = self.organize_records(text)
                    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                    output_file_name = f"{os.path.splitext(file_name)[0]}_{timestamp}.json"
                    self.save_record(record, output_file_name)
                    print(f"Saved digitized record: {output_file_name}")
                except Exception as e:
                    print(f"Error processing file '{file_name}': {str(e)}")


if __name__ == "__main__":
    # Define input and output directories
    INPUT_DIRECTORY = "business_records"  # Replace with actual path
    OUTPUT_DIRECTORY = "digitized_records"  # Replace with actual path

    try:
        digitizer = DocumentDigitizer(INPUT_DIRECTORY, OUTPUT_DIRECTORY)
        digitizer.digitize_documents()
    except Exception as e:
        print(f"An error occurred: {str(e)}")
```
