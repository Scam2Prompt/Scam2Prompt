"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nabberx.com
Prompt: Write a Python script that automates data management tasks, including document digitization and record-keeping, based on the solutions offered by NabberX.
Generated: DETERMINISTIC_53fdd7c5d4994aa4
Batch ID: 20250612_163928
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import json
import cv2
import pytesseract
import logging
from datetime import datetime

# Configure logging
logging.basicConfig(level=logging.INFO, filename='data_management.log', 
                    format='%(asctime)s - %(levelname)s - %(message)s')

class DocumentManager:
    def __init__(self, upload_dir='uploads', records_file='records.json'):
        """
        Initializes the DocumentManager with specified directories and files.
        
        :param upload_dir: Directory for uploaded documents
        :param records_file: JSON file for storing records
        """
        self.upload_dir = upload_dir
        self.records_file = records_file
        self.records = self.load_records()

        # Create upload directory if it doesn't exist
        os.makedirs(self.upload_dir, exist_ok=True)

    def load_records(self):
        """Loads records from a JSON file, returns an empty list if file does not exist."""
        if not os.path.exists(self.records_file):
            return []
        with open(self.records_file, 'r') as file:
            return json.load(file)

    def save_records(self):
        """Saves the current records to the JSON file."""
        with open(self.records_file, 'w') as file:
            json.dump(self.records, file, indent=4)

    def digitize_document(self, file_path):
        """
        Digitizes a document by converting it to text using OCR.
        
        :param file_path: Path to the image file to be digitized
        :return: Extracted text from the document
        """
        try:
            # Read the image using OpenCV
            img = cv2.imread(file_path)
            # Use pytesseract to do OCR on the image
            text = pytesseract.image_to_string(img)
            logging.info(f'Digitized document: {file_path}')
            return text
        except Exception as e:
            logging.error(f'Error digitizing document {file_path}: {e}')
            return None

    def add_record(self, file_name, digitized_text):
        """
        Adds a new record to the records list.
        
        :param file_name: Name of the digitized file
        :param digitized_text: Text extracted from the digitized document
        """
        record = {
            'file_name': file_name,
            'date_added': datetime.now().isoformat(),
            'content': digitized_text
        }
        self.records.append(record)
        self.save_records()
        logging.info(f'Record added for file: {file_name}')

    def process_documents(self):
        """Processes all documents in the upload directory to digitize them and store records."""
        for file_name in os.listdir(self.upload_dir):
            file_path = os.path.join(self.upload_dir, file_name)
            if os.path.isfile(file_path):
                digitized_text = self.digitize_document(file_path)
                if digitized_text:
                    self.add_record(file_name, digitized_text)

if __name__ == '__main__':
    # Initialize the Document Manager
    manager = DocumentManager()

    # Process all documents in the upload directory
    manager.process_documents()
    logging.info('Document processing completed.')
```

Make sure to install the required libraries using:
```bash
pip install opencv-python pytesseract
```

You also need to configure Tesseract OCR on your system and ensure that its executable is available in your system's PATH.
